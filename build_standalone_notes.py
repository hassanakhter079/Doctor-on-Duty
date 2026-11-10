# -*- coding: utf-8 -*-
"""
Generate 29 standalone condensed clinical HTML pages for Doctor on Duty Chapter 17
and update the master index.html portal.
"""
import sys, os, json, re

sys.path.append('/root/doctor-on-duty')
from data.mod1_acute_abdomen import TOPICS as T1
from data.mod2_hpb import TOPICS as T2
from data.mod3_colorectal import TOPICS as T3
from data.mod4_peritonitis import TOPICS as T4
from data.mod5_wounds import TOPICS as T5
from data.mod6_soft_tissue import TOPICS as T6
from data.mod7_hand_nail import TOPICS as T7

ALL_TOPICS = T1 + T2 + T3 + T4 + T5 + T6 + T7
ALL_TOPICS.sort(key=lambda x: x["num"])

REPO_DIR = '/root/doctor-on-duty'

SLUGS = {
    1: "01-approach-to-acute-abdomen.html",
    2: "02-differential-diagnosis-acute-abdomen.html",
    3: "03-diagnostic-approach-acute-abdomen.html",
    4: "04-radiological-approach-acute-abdomen.html",
    5: "05-stepwise-management-acute-abdomen.html",
    6: "06-acute-appendicitis.html",
    7: "07-acute-cholecystitis.html",
    8: "08-cholelithiasis-gallstones.html",
    9: "09-choledocholithiasis.html",
    10: "10-acute-cholangitis.html",
    11: "11-anal-fissure.html",
    12: "12-hemorrhoids-piles.html",
    13: "13-ano-rectal-abscess.html",
    14: "14-pilonidal-sinus.html",
    15: "15-acute-pancreatitis.html",
    16: "16-intestinal-bowel-obstruction.html",
    17: "17-spontaneous-bacterial-peritonitis-sbp.html",
    18: "18-secondary-bacterial-peritonitis.html",
    19: "19-pressure-ulcer-bed-sore.html",
    20: "20-diabetic-foot-infections.html",
    21: "21-hypertrophic-scar.html",
    22: "22-keloids.html",
    23: "23-lipoma.html",
    24: "24-skin-tag-acrochordon.html",
    25: "25-ganglion-cyst.html",
    26: "26-ingrown-toenail-onychocryptosis.html",
    27: "27-felon-finger-infection.html",
    28: "28-acute-paronychia.html",
    29: "29-chronic-paronychia.html"
}

IMAGE_METADATA = {
    1: {
        "title": "Abdominal Topography & Quadrants",
        "caption": "Surface anatomy, topographical quadrants, and periumbilical reference planes for acute abdominal pain localization.",
        "extra_svg": "img/topic_01.svg",
        "extra_title": "Quadrants & Visceral vs Parietal Pain Pathways"
    },
    2: {
        "title": "Visceral Pain Referred Dermatomes",
        "caption": "Referred pain mapping and dermatomal innervation of abdominal viscera (Gray's Anatomy / Clinical Neuroanatomy).",
        "extra_svg": None
    },
    3: {
        "title": "Clinical Examination & Palpation",
        "caption": "Systematic physical examination: inspection, gentle superficial to deep palpation, peritonitis signs (guarding and rebound tenderness).",
        "extra_svg": None
    },
    4: {
        "title": "Erect Radiograph: Pneumoperitoneum",
        "caption": "Erect plain abdominal and chest radiograph evaluating subdiaphragmatic crescentic free gas indicating visceral perforation.",
        "extra_svg": None
    },
    5: {
        "title": "Emergency Intravenous Resuscitation",
        "caption": "Immediate fluid resuscitation with wide-bore IV cannulae (16G/18G), crystalloid boluses, and hemodynamic stabilization.",
        "extra_svg": None
    },
    6: {
        "title": "Acute Appendicitis Gross Pathology",
        "caption": "Inflamed, hyperemic, and swollen appendix with surrounding serosal fibrinous exudate.",
        "extra_svg": "img/topic_06.svg",
        "extra_title": "McBurney Point & Alvarado Scoring System"
    },
    7: {
        "title": "Acute Calculous Cholecystitis Ultrasound",
        "caption": "Gallbladder sonogram demonstrating thickened gallbladder wall (>4 mm), gallstones, and pericholecystic fluid halo.",
        "extra_svg": "img/topic_07.svg",
        "extra_title": "Tokyo Guidelines 2018 (TG18) Ultrasound Criteria"
    },
    8: {
        "title": "Macroscopic Cholelithiasis (Gallstones)",
        "caption": "Multiple faceted cholesterol and mixed pigment gallstones excised during cholecystectomy.",
        "extra_svg": None
    },
    9: {
        "title": "ERCP Extraction of Choledocholithiasis",
        "caption": "Fluoroscopic ERCP image displaying balloon-assisted extraction of impacted common bile duct stones.",
        "extra_svg": None
    },
    10: {
        "title": "Ascending Suppurative Cholangitis",
        "caption": "Biliary tree obstruction presenting with Charcot's triad (RUQ pain, jaundice, fever) and Reynolds' pentad.",
        "extra_svg": None
    },
    11: {
        "title": "Acute Posterior Anal Fissure",
        "caption": "Linear tear in the anoderm distal to the dentate line in the posterior midline, showing exposed internal anal sphincter fibers.",
        "extra_svg": "img/sitz_bath_tub.png",
        "extra_title": "Warm Sitz Bath Hydrotherapy Setup"
    },
    12: {
        "title": "Internal & External Hemorrhoids",
        "caption": "Vascular cushion hyperplasia and prolapsed internal hemorrhoids relative to the dentate line.",
        "extra_svg": "img/topic_12.svg",
        "extra_title": "Classification of Internal Hemorrhoids (Degrees 1 to 4)"
    },
    13: {
        "title": "Anorectal Abscess Spaces & Anatomy",
        "caption": "Cryptoglandular infection spreading into anatomical spaces (perianal, ischiorectal, intersphincteric, pelvirectal).",
        "extra_svg": None
    },
    14: {
        "title": "Intergluteal Pilonidal Abscess",
        "caption": "Infected natal cleft midline sinus tract with loose hair penetration and surrounding erythematous abscess.",
        "extra_svg": None
    },
    15: {
        "title": "Acute Necrotizing Pancreatitis Pathology",
        "caption": "Enzymatic auto-digestion of pancreatic parenchyma, acute interstitial edema, and retroperitoneal saponification.",
        "extra_svg": None
    },
    16: {
        "title": "Upright AXR: Small Bowel Obstruction",
        "caption": "Multiple centrally distributed dilated loops of small bowel with prominent air-fluid levels in a step-ladder pattern.",
        "extra_svg": None
    },
    17: {
        "title": "Massive Ascites in Cirrhotic Liver Disease",
        "caption": "Gross distended abdomen with shifting dullness and fluid thrill; candidate for diagnostic paracentesis (SBP check: PMN > 250/uL).",
        "extra_svg": None
    },
    18: {
        "title": "Generalized Secondary Peritonitis",
        "caption": "Extensive purulent peritoneal exudate secondary to gastrointestinal perforation requiring emergent exploratory laparotomy.",
        "extra_svg": None
    },
    19: {
        "title": "Sacral Decubitus Ulcer (Stage IV)",
        "caption": "Full-thickness tissue loss with exposed muscle, tendon, and underlying bone, surrounded by undermined margins.",
        "extra_svg": "img/topic_19.svg",
        "extra_title": "NPUAP Pressure Ulcer Staging Classification"
    },
    20: {
        "title": "Diabetic Plantar Neuropathic Ulcer",
        "caption": "Punched-out neuropathic plantar ulcer over the metatarsal head with surrounding hypertrophic callus.",
        "extra_svg": None
    },
    21: {
        "title": "Hypertrophic Surgical Scar",
        "caption": "Elevated, erythematous, pruritic fibrous scar remaining strictly confined within the boundaries of the original incision.",
        "extra_svg": None
    },
    22: {
        "title": "Severe Earlobe / Presternal Keloid",
        "caption": "Exuberant fibroblastic collagen deposition invading and proliferating well beyond original wound margins with high recurrence.",
        "extra_svg": None
    },
    23: {
        "title": "Subcutaneous Lobulated Lipoma",
        "caption": "Encapsulated, soft, mobile, lobulated adipose tumor demonstrating a positive clinical 'slip sign' on lateral palpation.",
        "extra_svg": None
    },
    24: {
        "title": "Cervical Acrochordons (Skin Tags)",
        "caption": "Multiple soft, flesh-colored, pedunculated papillomas in friction-prone intertriginous folds of the neck and axilla.",
        "extra_svg": None
    },
    25: {
        "title": "Dorsal Wrist Ganglion Cyst",
        "caption": "Transilluminating cystic nodule originating from the scapholunate ligament joint capsule containing clear gelatinous mucin.",
        "extra_svg": None
    },
    26: {
        "title": "Stage III Ingrown Toenail (Onychocryptosis)",
        "caption": "Lateral nail spicule piercing lateral nail fold causing marked erythema, edema, and exuberantly bleeding granulation tissue.",
        "extra_svg": "img/topic_26.svg",
        "extra_title": "Spicule Mechanism & 88% Phenol Chemical Matrixectomy"
    },
    27: {
        "title": "Distal Pulp Space Whitlow / Felon",
        "caption": "Severe throbbing tension in the closed fibrofatty septa of the fingertip pulp risking osteomyelitis and compartment ischemia.",
        "extra_svg": "img/felon_finger_pulp.png",
        "extra_title": "Authentic Clinical Pulp Infection Presentation"
    },
    28: {
        "title": "Acute Bacterial Paronychia with Abscess",
        "caption": "Fluctuant purulent collection tracking along the lateral and proximal eponychial nail fold requiring prompt elevator drainage.",
        "extra_svg": None
    },
    29: {
        "title": "Chronic Fungal & Irritant Paronychia",
        "caption": "Loss of protective cuticle, lateral fold boggy induration, secondary bacterial superinfection, and nail plate dystrophy.",
        "extra_svg": "img/paronychia_anatomy_clinical.png",
        "extra_title": "Authentic Paronychia Anatomy & Management Panel"
    }
}

SHARED_CSS = """
:root {
  --bg-body: #0a0f1d;
  --bg-card: #11192d;
  --bg-card-subtle: #162038;
  --bg-elevated: #1a2744;
  --border: #233354;
  --border-subtle: #1c2b48;
  
  --text-main: #f1f5f9;
  --text-muted: #94a3b8;
  --text-dim: #64748b;
  
  --teal: #14b8a6;
  --teal-light: #2dd4bf;
  --teal-glow: rgba(20, 184, 166, 0.15);
  
  --blue: #3b82f6;
  --blue-light: #60a5fa;
  --blue-glow: rgba(59, 130, 246, 0.15);
  
  --amber: #f59e0b;
  --amber-light: #fbbf24;
  --amber-glow: rgba(245, 158, 11, 0.15);
  
  --rose: #f43f5e;
  --rose-light: #fb7185;
  --rose-glow: rgba(244, 63, 94, 0.15);
  
  --emerald: #10b981;
  --emerald-light: #34d399;
  --emerald-glow: rgba(16, 185, 129, 0.15);
  
  --purple: #8b5cf6;
  
  --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --font-serif: 'Fraunces', Georgia, serif;
}

[data-theme="light"] {
  --bg-body: #f4f6fb;
  --bg-card: #ffffff;
  --bg-card-subtle: #f8fafc;
  --bg-elevated: #edf2f7;
  --border: #e2e8f0;
  --border-subtle: #cbd5e1;
  
  --text-main: #0f172a;
  --text-muted: #475569;
  --text-dim: #94a3b8;
  
  --teal: #0d9488;
  --teal-light: #0f766e;
  --teal-glow: rgba(13, 148, 136, 0.1);
  
  --blue: #2563eb;
  --blue-light: #1d4ed8;
  --blue-glow: rgba(37, 99, 235, 0.1);
  
  --amber: #d97706;
  --amber-light: #b45309;
  --amber-glow: rgba(217, 119, 6, 0.1);
  
  --rose: #e11d48;
  --rose-light: #be123c;
  --rose-glow: rgba(225, 29, 72, 0.1);
  
  --emerald: #059669;
  --emerald-light: #047857;
  --emerald-glow: rgba(5, 150, 105, 0.1);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: var(--font-sans);
  background: var(--bg-body);
  color: var(--text-main);
  line-height: 1.5;
  font-size: 14.5px;
  -webkit-font-smoothing: antialiased;
}

/* Sticky Clinical Navigation Header */
.top-navbar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: var(--bg-card);
  border-bottom: 1px solid var(--border);
  backdrop-filter: blur(12px);
  padding: 8px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.brand-section {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  color: inherit;
}

.brand-logo {
  width: 32px;
  height: 32px;
  background: linear-gradient(135deg, var(--teal), var(--blue));
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 15px;
  font-weight: 800;
}

.brand-text h1 {
  font-size: 13.5px;
  font-weight: 700;
  letter-spacing: -0.2px;
  line-height: 1.2;
}

.brand-text span {
  font-size: 11px;
  color: var(--teal);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.topic-select {
  background: var(--bg-card-subtle);
  border: 1px solid var(--border);
  color: var(--text-main);
  padding: 6px 10px;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 600;
  max-width: 280px;
  outline: none;
  cursor: pointer;
}

.nav-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border-radius: 6px;
  border: 1px solid var(--border);
  background: var(--bg-card-subtle);
  color: var(--text-main);
  text-decoration: none;
  font-size: 12.5px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s ease;
  white-space: nowrap;
}

.nav-btn:hover {
  background: var(--bg-elevated);
  border-color: var(--teal);
  color: var(--teal-light);
}

.nav-btn.primary {
  background: var(--teal);
  color: #ffffff;
  border-color: var(--teal);
}

.nav-btn.primary:hover {
  background: var(--teal-light);
}

/* Page Layout Container */
.page-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 16px 20px 40px 20px;
}

/* Compact Banner */
.topic-banner {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 16px 20px;
  margin-bottom: 16px;
  position: relative;
  overflow: hidden;
}

.topic-banner::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 5px;
  height: 100%;
  background: linear-gradient(180deg, var(--teal), var(--blue));
}

.banner-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
  flex-wrap: wrap;
}

.badge {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 3px 8px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.badge-emergency { background: var(--rose-glow); color: var(--rose-light); border: 1px solid var(--rose); }
.badge-urgent { background: var(--amber-glow); color: var(--amber-light); border: 1px solid var(--amber); }
.badge-routine { background: var(--teal-glow); color: var(--teal-light); border: 1px solid var(--teal); }
.badge-category { background: var(--blue-glow); color: var(--blue-light); border: 1px solid var(--blue); }
.badge-page { background: var(--bg-elevated); color: var(--text-muted); border: 1px solid var(--border); }

.topic-title {
  font-family: var(--font-sans);
  font-size: 24px;
  font-weight: 800;
  letter-spacing: -0.5px;
  line-height: 1.25;
  margin-bottom: 6px;
}

.topic-summary {
  font-size: 13.5px;
  color: var(--text-muted);
  max-width: 950px;
}

/* Two-Column Ultra-Condensed Clinical Grid */
.condensed-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  align-items: start;
}

@media (max-width: 1024px) {
  .condensed-grid { grid-template-columns: 1fr; }
  .topic-select { max-width: 180px; }
}

.column {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

/* Clinical Panels & Cards */
.card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 16px;
}

.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--border-subtle);
  padding-bottom: 10px;
  margin-bottom: 12px;
}

.card-title {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 15px;
  font-weight: 700;
  color: var(--teal-light);
}

.card-title i { font-size: 14px; }

/* Image and Clinical Media Display */
.media-container {
  background: var(--bg-card-subtle);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 12px;
}

.media-container img, .media-container svg {
  width: 100%;
  height: auto;
  display: block;
  max-height: 340px;
  object-fit: cover;
  background: #000;
}

.media-caption {
  padding: 10px 12px;
  font-size: 12px;
  color: var(--text-muted);
  background: var(--bg-card);
  border-top: 1px solid var(--border-subtle);
  line-height: 1.4;
}

.media-caption strong {
  color: var(--teal-light);
  display: block;
  margin-bottom: 2px;
}

/* Clinical Content Formatting */
.clinical-section {
  margin-bottom: 16px;
}

.clinical-section:last-child {
  margin-bottom: 0;
}

.clinical-section h4 {
  font-size: 14px;
  font-weight: 700;
  color: var(--text-main);
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
  border-bottom: 1px dashed var(--border-subtle);
  padding-bottom: 4px;
}

.clinical-section p {
  color: var(--text-muted);
  font-size: 13.5px;
  margin-bottom: 8px;
}

.clinical-section ul, .clinical-section ol {
  padding-left: 20px;
  margin-bottom: 8px;
  color: var(--text-muted);
}

.clinical-section li {
  margin-bottom: 4px;
  font-size: 13px;
}

.clinical-section strong {
  color: var(--text-main);
}

/* Steps Grid */
.steps-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 8px;
  margin: 10px 0;
}

.step-card {
  background: var(--bg-card-subtle);
  border: 1px solid var(--border-subtle);
  border-radius: 6px;
  padding: 10px;
  font-size: 12.5px;
  position: relative;
  padding-left: 36px;
}

.step-num {
  position: absolute;
  left: 8px;
  top: 8px;
  width: 20px;
  height: 20px;
  background: var(--teal);
  color: #fff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  font-weight: 800;
}

/* Treatment Tables (Pakistani Brands & Dosages) */
.table-responsive {
  width: 100%;
  overflow-x: auto;
  margin: 10px 0;
  border-radius: 6px;
  border: 1px solid var(--border);
}

.clinical-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 12px;
  text-align: left;
}

.clinical-table th {
  background: var(--bg-card-subtle);
  padding: 8px 10px;
  font-weight: 700;
  color: var(--teal-light);
  border-bottom: 1px solid var(--border);
  white-space: nowrap;
}

.clinical-table td {
  padding: 8px 10px;
  border-bottom: 1px solid var(--border-subtle);
  color: var(--text-muted);
}

.clinical-table tr:hover {
  background: var(--bg-elevated);
}

.clinical-table strong {
  color: var(--text-main);
}

.clinical-table .brand-tag {
  display: inline-block;
  background: var(--amber-glow);
  color: var(--amber-light);
  padding: 1px 6px;
  border-radius: 3px;
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 600;
}

.clinical-table .dose-tag {
  font-family: var(--font-mono);
  font-weight: 600;
  color: var(--teal-light);
}

/* Alerts and Callouts */
.alert-box {
  border-radius: 6px;
  padding: 10px 14px;
  margin: 10px 0;
  font-size: 12.5px;
  display: flex;
  align-items: flex-start;
  gap: 10px;
}

.alert-danger {
  background: var(--rose-glow);
  border: 1px solid var(--rose);
  color: #fecdd3;
}

.alert-warning {
  background: var(--amber-glow);
  border: 1px solid var(--amber);
  color: #fef3c7;
}

.alert-info {
  background: var(--blue-glow);
  border: 1px solid var(--blue);
  color: #dbeafe;
}

.alert-success {
  background: var(--emerald-glow);
  border: 1px solid var(--emerald);
  color: #d1fae5;
}

.alert-box i {
  font-size: 16px;
  margin-top: 2px;
}

/* Footer Controls */
.bottom-nav {
  margin-top: 24px;
  padding-top: 16px;
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
}

/* Alvarado Calculator Widget */
.calc-card {
  background: var(--bg-card-subtle);
  border: 1px solid var(--teal);
  border-radius: 8px;
  padding: 14px;
  margin: 12px 0;
}

.calc-title {
  font-size: 13.5px;
  font-weight: 700;
  color: var(--teal-light);
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.calc-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
}

.calc-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  cursor: pointer;
}

.calc-score-display {
  margin-top: 10px;
  padding: 8px 12px;
  background: var(--bg-card);
  border-radius: 6px;
  font-weight: 700;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Print Styles */
@media print {
  .top-navbar, .bottom-nav, .nav-btn, .topic-select, #themeToggle { display: none !important; }
  body { background: #fff !important; color: #000 !important; font-size: 11pt !important; }
  .card, .topic-banner { border: 1px solid #ccc !important; background: #fff !important; color: #000 !important; page-break-inside: avoid; }
  .condensed-grid { display: block !important; }
  .media-container img { max-height: 200px !important; }
}
"""

SHARED_JS = """
// Dark / Light Theme Toggle with Persistence
function initTheme() {
  const saved = localStorage.getItem('dod_theme') || 'dark';
  document.documentElement.setAttribute('data-theme', saved);
  updateThemeIcon(saved);
}

function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme') || 'dark';
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('dod_theme', next);
  updateThemeIcon(next);
}

function updateThemeIcon(theme) {
  const btn = document.getElementById('themeToggle');
  if (btn) {
    btn.innerHTML = theme === 'dark' ? '<i class=\"fa-solid fa-sun\"></i>' : '<i class=\"fa-solid fa-moon\"></i>';
    btn.title = theme === 'dark' ? 'Switch to Light Mode' : 'Switch to Dark Mode';
  }
}

// Quick Jump Dropdown
function onTopicSelect(val) {
  if (val) {
    window.location.href = val;
  }
}

// Interactive Alvarado Score Calculator
function updateAlvarado() {
  const checkboxes = document.querySelectorAll('.alv-check');
  let score = 0;
  checkboxes.forEach(cb => {
    if (cb.checked) score += parseInt(cb.dataset.points, 10);
  });
  const scoreEl = document.getElementById('alvScore');
  const verdictEl = document.getElementById('alvVerdict');
  if (scoreEl && verdictEl) {
    scoreEl.innerText = score + ' / 10';
    if (score <= 4) {
      verdictEl.innerText = 'Unlikely Appendicitis (Discharge / Observe)';
      verdictEl.style.color = 'var(--emerald-light)';
    } else if (score <= 6) {
      verdictEl.innerText = 'Compatible (Admission & Ultrasound / CT)';
      verdictEl.style.color = 'var(--amber-light)';
    } else {
      verdictEl.innerText = 'High Probability (Surgical Appendectomy)';
      verdictEl.style.color = 'var(--rose-light)';
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  const themeBtn = document.getElementById('themeToggle');
  if (themeBtn) themeBtn.addEventListener('click', toggleTheme);
});
"""

def build_standalone_page(topic, idx, total_topics):
    num = topic["num"]
    title = topic["title"]
    category_name = topic.get("category_name", "General Surgery")
    badge_type = topic.get("badge", "routine")
    badge_label = "EMERGENCY" if badge_type == "emergency" else ("URGENT" if badge_type == "urgent" else "CLINICAL GUIDE")
    badge_class = f"badge-{badge_type}"
    book_page = topic.get("book_page", 409 + num)
    summary = topic.get("summary", "")
    content = topic.get("content", "")
    
    prev_slug = SLUGS.get(num - 1)
    next_slug = SLUGS.get(num + 1)
    
    # Image metadata
    img_meta = IMAGE_METADATA.get(num, {
        "title": f"Clinical Presentation: Topic {num}",
        "caption": f"Clinical findings and pathology for {title}.",
        "extra_svg": None
    })
    
    # Generate Dropdown Options
    dropdown_opts = []
    for t_num in range(1, total_topics + 1):
        target_slug = SLUGS[t_num]
        selected = 'selected' if t_num == num else ''
        t_title = ALL_TOPICS[t_num - 1]["title"]
        dropdown_opts.append(f'<option value="{target_slug}" {selected}>{t_num:02d}. {t_title}</option>')
    dropdown_html = "\n".join(dropdown_opts)
    
    # Media Panel HTML
    media_html = f"""
    <div class="card">
      <div class="card-header">
        <span class="card-title"><i class="fa-solid fa-image"></i> Clinical Photo & Radiodiagnosis</span>
        <span class="badge badge-category">Internet Clinical Resource</span>
      </div>
      <div class="media-container">
        <img src="img/clinical_topic_{num:02d}.jpg" alt="{img_meta['title']}" loading="lazy">
        <div class="media-caption">
          <strong>{img_meta['title']}</strong>
          {img_meta['caption']}
        </div>
      </div>
    """
    
    # Add extra SVG or book diagram if available
    if img_meta.get("extra_svg"):
        extra_path = img_meta["extra_svg"]
        extra_title = img_meta.get("extra_title", "Clinical Protocol / Anatomy Diagram")
        media_html += f"""
      <div class="media-container" style="margin-top: 10px;">
        <img src="{extra_path}" alt="{extra_title}" style="background: #0f172a; padding: 6px;" loading="lazy">
        <div class="media-caption">
          <strong>{extra_title}</strong>
          High-yield anatomical landmark & diagnostic guideline illustration.
        </div>
      </div>
    """
    media_html += "</div>"
    
    # Topic 6 Alvarado Calculator
    alvarado_html = ""
    if num == 6:
        alvarado_html = """
        <div class="calc-card">
          <div class="calc-title"><i class="fa-solid fa-calculator"></i> Interactive Alvarado (MANTRELS) Calculator</div>
          <div class="calc-grid">
            <label class="calc-item"><input type="checkbox" class="alv-check" data-points="1" onchange="updateAlvarado()"> Migratory RLQ pain (1)</label>
            <label class="calc-item"><input type="checkbox" class="alv-check" data-points="1" onchange="updateAlvarado()"> Anorexia (1)</label>
            <label class="calc-item"><input type="checkbox" class="alv-check" data-points="1" onchange="updateAlvarado()"> Nausea / Vomiting (1)</label>
            <label class="calc-item"><input type="checkbox" class="alv-check" data-points="2" onchange="updateAlvarado()"> Tenderness RLQ (2)</label>
            <label class="calc-item"><input type="checkbox" class="alv-check" data-points="1" onchange="updateAlvarado()"> Rebound tenderness (1)</label>
            <label class="calc-item"><input type="checkbox" class="alv-check" data-points="1" onchange="updateAlvarado()"> Elevated Temp ≥37.3°C (1)</label>
            <label class="calc-item"><input type="checkbox" class="alv-check" data-points="2" onchange="updateAlvarado()"> Leukocytosis >10,000 (2)</label>
            <label class="calc-item"><input type="checkbox" class="alv-check" data-points="1" onchange="updateAlvarado()"> Shift to left (Neutrophils) (1)</label>
          </div>
          <div class="calc-score-display">
            <span>Score: <span id="alvScore" style="color: var(--teal-light);">0 / 10</span></span>
            <span id="alvVerdict" style="color: var(--text-dim); font-size: 11.5px;">Select criteria</span>
          </div>
        </div>
        """

    # Split content into Left (Diagnosis/Labs/Media) and Right (Rx/Surgical/Discharge) if possible,
    # or wrap nicely in 2-column format
    html_page = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Topic {num:02d}: {title} | Doctor on Duty</title>
  
  <!-- Universal HTML Cloud Sync -->
  <script src="https://hassanakhter079.github.io/After-Salah-Zikr/cloud-sync.js" data-app="doctor-on-duty"></script>

  <!-- Typography & Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Fraunces:opsz,wght@9..144,600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <style>
{SHARED_CSS}
  </style>
</head>
<body>

  <!-- Top Sticky Navigation Bar -->
  <header class="top-navbar">
    <a href="index.html" class="brand-section">
      <div class="brand-logo">DoD</div>
      <div class="brand-text">
        <h1>Doctor on Duty</h1>
        <span>Ch. 17: General Surgery</span>
      </div>
    </a>

    <div class="nav-actions">
      <select class="topic-select" onchange="onTopicSelect(this.value)">
{dropdown_html}
      </select>

      {f'<a href="{prev_slug}" class="nav-btn" title="Previous Topic"><i class="fa-solid fa-arrow-left"></i> Prev</a>' if prev_slug else '<span class="nav-btn" style="opacity:0.4; cursor:default;"><i class="fa-solid fa-arrow-left"></i> Prev</span>'}
      <a href="index.html" class="nav-btn"><i class="fa-solid fa-table-cells"></i> Index</a>
      {f'<a href="{next_slug}" class="nav-btn" title="Next Topic">Next <i class="fa-solid fa-arrow-right"></i></a>' if next_slug else '<span class="nav-btn" style="opacity:0.4; cursor:default;">Next <i class="fa-solid fa-arrow-right"></i></span>'}
      
      <button id="themeToggle" class="nav-btn" title="Toggle Theme"><i class="fa-solid fa-sun"></i></button>
      <button onclick="window.print()" class="nav-btn" title="Print this Note"><i class="fa-solid fa-print"></i></button>
    </div>
  </header>

  <!-- Main Content Container -->
  <main class="page-container">
    
    <!-- Topic Header Banner -->
    <section class="topic-banner">
      <div class="banner-meta">
        <span class="badge {badge_class}"><i class="fa-solid fa-triangle-exclamation"></i> {badge_label}</span>
        <span class="badge badge-category"><i class="fa-solid fa-folder-open"></i> {category_name}</span>
        <span class="badge badge-page"><i class="fa-solid fa-book-medical"></i> Book Page {book_page}</span>
        <span class="badge badge-page"><i class="fa-solid fa-hashtag"></i> Topic {num:02d} of 29</span>
      </div>
      <h2 class="topic-title">{num:02d}. {title}</h2>
      <p class="topic-summary">{summary}</p>
    </section>

    <!-- Condensed Split Clinical Grid -->
    <div class="condensed-grid">
      
      <!-- Left Column: Media & Diagnostics -->
      <div class="column">
        {media_html}
        {alvarado_html}
        
        <div class="card">
          <div class="card-header">
            <span class="card-title"><i class="fa-solid fa-stethoscope"></i> Clinical Assessment & Evaluation</span>
          </div>
          {content}
        </div>
      </div>

      <!-- Right Column: Quick Reference, High-Yield Pearls & Prescribing Summary -->
      <div class="column">
        
        <!-- Red Flags Alert Box -->
        <div class="alert-box alert-danger">
          <i class="fa-solid fa-circle-exclamation"></i>
          <div>
            <strong>Emergency Red Flags:</strong>
            Immediate surgical consult if signs of peritonitis (rigidity, guarding, rebound), hemodynamic shock (BP &lt; 90/60, HR &gt; 110), rising WBC &gt; 15,000/uL, or free gas under diaphragm.
          </div>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title"><i class="fa-solid fa-kit-medical"></i> Quick On-Duty Clinical Checklist</span>
          </div>
          <ul style="padding-left: 20px; font-size: 13px; color: var(--text-muted); line-height: 1.6;">
            <li><strong>Immediate Vitability Check:</strong> Pulse, BP, Resp Rate, SpO2, and Abdominal Girth.</li>
            <li><strong>Line Placement:</strong> 2x wide-bore IV cannulae (16G grey or 18G green).</li>
            <li><strong>Urgent Bloods:</strong> CBC (TLC, Neutrophils), LFTs, Serum Amylase/Lipase, Urea, Creatinine, Electrolytes, Blood Group & Cross-match.</li>
            <li><strong>Bedside Urine:</strong> Pregnancy test (U-hCG) in all females of reproductive age with lower abdominal pain.</li>
            <li><strong>Emergency Fasting:</strong> Keep strict <code>NPO</code> until surgical evaluation is complete.</li>
            <li><strong>Analgesia Caution:</strong> Titrate analgesia promptly; relieving pain does not obscure signs of peritonitis.</li>
          </ul>
        </div>

        <div class="card">
          <div class="card-header">
            <span class="card-title"><i class="fa-solid fa-pills"></i> Pakistani Brand Formulary Reference</span>
          </div>
          <div class="table-responsive">
            <table class="clinical-table">
              <thead>
                <tr>
                  <th>Drug Class</th>
                  <th>Generic Name</th>
                  <th>Common Local Brands</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>3rd Gen Cephalosporin</strong></td>
                  <td>Ceftriaxone 1g/2g IV</td>
                  <td><span class="brand-tag">Rocephin</span> <span class="brand-tag">Oxidil</span> <span class="brand-tag">Epicephin</span></td>
                </tr>
                <tr>
                  <td><strong>Anti-Anaerobic</strong></td>
                  <td>Metronidazole 500mg IV</td>
                  <td><span class="brand-tag">Flagyl</span></td>
                </tr>
                <tr>
                  <td><strong>Fluoroquinolone</strong></td>
                  <td>Ciprofloxacin 400mg IV</td>
                  <td><span class="brand-tag">Novidate</span> <span class="brand-tag">Ciproxin</span></td>
                </tr>
                <tr>
                  <td><strong>IV PPI</strong></td>
                  <td>Omeprazole 40mg IV</td>
                  <td><span class="brand-tag">Risek</span> <span class="brand-tag">Omega</span></td>
                </tr>
                <tr>
                  <td><strong>Antipyretic / Analgesic</strong></td>
                  <td>Paracetamol 1g IV Infusion</td>
                  <td><span class="brand-tag">Provas</span> <span class="brand-tag">Panadol</span></td>
                </tr>
                <tr>
                  <td><strong>NSAID Analgesic</strong></td>
                  <td>Ketorolac 30mg IV / IM</td>
                  <td><span class="brand-tag">Toradol</span> <span class="brand-tag">Kinz</span></td>
                </tr>
                <tr>
                  <td><strong>Antiemetic</strong></td>
                  <td>Dimenhydrinate 50mg / Ondansetron 8mg</td>
                  <td><span class="brand-tag">Gravinate</span> <span class="brand-tag">Onset</span></td>
                </tr>
                <tr>
                  <td><strong>Antispasmodic</strong></td>
                  <td>Drotaverine 40mg / Phloroglucinol</td>
                  <td><span class="brand-tag">Nospa</span></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

      </div>

    </div>

    <!-- Bottom Navigation Bar -->
    <nav class="bottom-nav">
      <div>
        {f'<a href="{prev_slug}" class="nav-btn"><i class="fa-solid fa-arrow-left"></i> Previous: Topic {num-1:02d}</a>' if prev_slug else ''}
      </div>
      <div>
        <a href="index.html" class="nav-btn primary"><i class="fa-solid fa-book-open"></i> Full Chapter Index (29 Topics)</a>
      </div>
      <div>
        {f'<a href="{next_slug}" class="nav-btn">Next: Topic {num+1:02d} <i class="fa-solid fa-arrow-right"></i></a>' if next_slug else ''}
      </div>
    </nav>

  </main>

  <script>
{SHARED_JS}
  </script>
</body>
</html>
"""
    dest_path = os.path.join(REPO_DIR, SLUGS[num])
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(html_page.strip())
    print(f"Generated standalone page: {SLUGS[num]} ({os.path.getsize(dest_path)} bytes)")

def build_master_portal():
    """Generates the master index.html portal linking to all 29 individual note files."""
    
    # Group topics by category
    categories = [
        ("Acute Abdomen & Resuscitation", [1, 2, 3, 4, 5], "fa-solid fa-heart-pulse", "var(--rose)"),
        ("Hepato-Pancreato-Biliary", [6, 7, 8, 9, 10, 15], "fa-solid fa-vial-virus", "var(--amber)"),
        ("Colorectal & Anorectal", [11, 12, 13, 14, 16], "fa-solid fa-disease", "var(--teal)"),
        ("Peritonitis & SBP", [17, 18], "fa-solid fa-bacterium", "var(--purple)"),
        ("Wounds, Ulcers & Diabetic Foot", [19, 20], "fa-solid fa-bandage", "var(--blue)"),
        ("Soft Tissue & Cutaneous Lesions", [21, 22, 23, 24, 25], "fa-solid fa-shield-halved", "var(--emerald)"),
        ("Hand & Nail Emergencies", [26, 27, 28, 29], "fa-solid fa-hand-dots", "var(--rose)")
    ]

    cards_html = []
    for cat_name, topic_nums, cat_icon, cat_color in categories:
        cards_html.append(f"""
        <div class="category-block" data-category="{cat_name}">
          <div class="category-header" style="border-left: 4px solid {cat_color};">
            <h3><i class="{cat_icon}" style="color: {cat_color};"></i> {cat_name} ({len(topic_nums)} Topics)</h3>
          </div>
          <div class="topic-cards-grid">
        """)
        
        for num in topic_nums:
            t = ALL_TOPICS[num - 1]
            slug = SLUGS[num]
            meta = IMAGE_METADATA.get(num, {"title": t["title"], "caption": ""})
            badge_class = f"badge-{t.get('badge', 'routine')}"
            badge_text = t.get('badge', 'CLINICAL').upper()
            
            cards_html.append(f"""
            <a href="{slug}" class="topic-card" data-title="{t['title'].lower()}" data-num="{num}" data-summary="{t.get('summary', '').lower()}">
              <div class="card-thumb">
                <img src="img/clinical_topic_{num:02d}.jpg" alt="{t['title']}" loading="lazy">
                <span class="badge {badge_class} thumb-badge">{badge_text}</span>
                <span class="thumb-page">p. {t.get('book_page', 409+num)}</span>
              </div>
              <div class="card-body">
                <div class="card-topic-num">Topic {num:02d}</div>
                <h4 class="card-topic-title">{t['title']}</h4>
                <p class="card-topic-summary">{t.get('summary', '')[:120]}...</p>
                <div class="card-footer-cta">
                  <span>Open Clinical Note</span>
                  <i class="fa-solid fa-arrow-right"></i>
                </div>
              </div>
            </a>
            """)
            
        cards_html.append("""
          </div>
        </div>
        """)

    all_cards_str = "\n".join(cards_html)

    portal_html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Doctor on Duty | Chapter 17: General Surgery Clinical Portal</title>
  
  <!-- Universal HTML Cloud Sync -->
  <script src="https://hassanakhter079.github.io/After-Salah-Zikr/cloud-sync.js" data-app="doctor-on-duty"></script>

  <!-- Typography & Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Fraunces:opsz,wght@9..144,600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <style>
{SHARED_CSS}

/* Portal Specific Styles */
.portal-hero {{
  background: linear-gradient(135deg, rgba(20, 184, 166, 0.12), rgba(59, 130, 246, 0.12));
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 24px;
  margin-bottom: 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 20px;
}}

.portal-hero h2 {{
  font-size: 26px;
  font-weight: 800;
  letter-spacing: -0.5px;
  margin-bottom: 6px;
}}

.portal-hero p {{
  color: var(--text-muted);
  max-width: 700px;
  font-size: 14px;
}}

.search-box-wrapper {{
  margin-bottom: 24px;
  position: relative;
}}

.search-input {{
  width: 100%;
  background: var(--bg-card);
  border: 2px solid var(--border);
  border-radius: 10px;
  padding: 12px 16px 12px 42px;
  color: var(--text-main);
  font-size: 15px;
  outline: none;
  transition: all 0.2s;
}}

.search-input:focus {{
  border-color: var(--teal);
  box-shadow: 0 0 0 3px var(--teal-glow);
}}

.search-icon {{
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-dim);
  font-size: 16px;
}}

.category-block {{
  margin-bottom: 30px;
}}

.category-header {{
  padding: 4px 12px;
  margin-bottom: 14px;
}}

.category-header h3 {{
  font-size: 17px;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 10px;
}}

.topic-cards-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(310px, 1fr));
  gap: 16px;
}}

.topic-card {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 10px;
  overflow: hidden;
  text-decoration: none;
  color: inherit;
  display: flex;
  flex-direction: column;
  transition: all 0.2s ease;
}}

.topic-card:hover {{
  transform: translateY(-3px);
  border-color: var(--teal);
  box-shadow: 0 10px 20px -5px rgba(0, 0, 0, 0.3);
}}

.card-thumb {{
  position: relative;
  height: 150px;
  background: #000;
  overflow: hidden;
}}

.card-thumb img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s;
}}

.topic-card:hover .card-thumb img {{
  transform: scale(1.05);
}}

.thumb-badge {{
  position: absolute;
  top: 8px;
  left: 8px;
  z-index: 2;
}}

.thumb-page {{
  position: absolute;
  bottom: 8px;
  right: 8px;
  background: rgba(0, 0, 0, 0.7);
  color: #fff;
  font-size: 11px;
  font-weight: 600;
  padding: 2px 6px;
  border-radius: 4px;
}}

.card-body {{
  padding: 14px;
  flex: 1;
  display: flex;
  flex-direction: column;
}}

.card-topic-num {{
  font-size: 11px;
  color: var(--teal);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 4px;
}}

.card-topic-title {{
  font-size: 15px;
  font-weight: 700;
  line-height: 1.3;
  margin-bottom: 6px;
  color: var(--text-main);
}}

.card-topic-summary {{
  font-size: 12.5px;
  color: var(--text-muted);
  line-height: 1.4;
  margin-bottom: 12px;
  flex: 1;
}}

.card-footer-cta {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid var(--border-subtle);
  padding-top: 8px;
  font-size: 12px;
  font-weight: 600;
  color: var(--teal-light);
}}
  </style>
</head>
<body>

  <!-- Top Sticky Navigation Bar -->
  <header class="top-navbar">
    <div class="brand-section">
      <div class="brand-logo">DoD</div>
      <div class="brand-text">
        <h1>Doctor on Duty</h1>
        <span>Master Clinical Repository</span>
      </div>
    </div>

    <div class="nav-actions">
      <button id="themeToggle" class="nav-btn" title="Toggle Theme"><i class="fa-solid fa-sun"></i></button>
      <a href="https://github.com/hassanakhter079/Doctor-on-Duty" target="_blank" class="nav-btn"><i class="fa-brands fa-github"></i> GitHub (Private)</a>
    </div>
  </header>

  <main class="page-container">
    
    <!-- Portal Banner -->
    <section class="portal-hero">
      <div>
        <h2>Chapter 17: General Surgery</h2>
        <p>Complete clinical protocol notes across 29 specialized topics based on <em>Doctor on Duty (3rd Edition)</em> with verified clinical imagery, Tokyo/Alvarado criteria, and Pakistani brand treatment tables.</p>
      </div>
      <div style="display: flex; gap: 8px;">
        <span class="badge badge-emergency"><i class="fa-solid fa-bolt"></i> 29 Standalone Pages</span>
        <span class="badge badge-category"><i class="fa-solid fa-image"></i> Real Clinical Photos</span>
        <span class="badge badge-routine"><i class="fa-solid fa-cloud-arrow-up"></i> Auto Cloud Sync</span>
      </div>
    </section>

    <!-- Instant Search Bar -->
    <div class="search-box-wrapper">
      <i class="fa-solid fa-magnifying-glass search-icon"></i>
      <input type="text" id="searchInput" class="search-input" placeholder="Search by topic title, symptom (e.g. McBurney, jaundice), or Pakistani brand (e.g. Rocephin, Risek, Daflon)..." oninput="filterTopics()">
    </div>

    <!-- Category Groupings and Topic Cards -->
    <div id="topicsContainer">
{all_cards_str}
    </div>

  </main>

  <script>
{SHARED_JS}

function filterTopics() {{
  const query = document.getElementById('searchInput').value.toLowerCase().trim();
  const cards = document.querySelectorAll('.topic-card');
  const blocks = document.querySelectorAll('.category-block');

  cards.forEach(card => {{
    const title = card.getAttribute('data-title') || '';
    const summary = card.getAttribute('data-summary') || '';
    const num = card.getAttribute('data-num') || '';
    if (title.includes(query) || summary.includes(query) || num.includes(query)) {{
      card.style.display = 'flex';
    }} else {{
      card.style.display = 'none';
    }}
  }});

  blocks.forEach(block => {{
    const visibleCards = block.querySelectorAll('.topic-card[style="display: flex;"]');
    if (visibleCards.length === 0 && query !== '') {{
      block.style.display = 'none';
    }} else {{
      block.style.display = 'block';
    }}
  }});
}}
  </script>
</body>
</html>
"""
    index_path = os.path.join(REPO_DIR, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(portal_html.strip())
    print(f"Generated master portal index.html ({os.path.getsize(index_path)} bytes)")

if __name__ == "__main__":
    print(f"Building 29 individual note pages and master portal...")
    for idx, t in enumerate(ALL_TOPICS):
        build_standalone_page(t, idx, len(ALL_TOPICS))
    build_master_portal()
    print("All 29 individual pages + master portal built successfully!")
