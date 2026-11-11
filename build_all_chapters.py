# -*- coding: utf-8 -*-
"""
Generate 62 standalone condensed clinical HTML pages for Doctor on Duty:
- Chapter 17: General Surgery (29 topics)
- Chapter 18: Ophthalmology (12 topics)
- Chapter 19: Ear, Nose & Throat (12 topics)
- Chapter 23: Emergency Medicine & Poisoning (9 topics)
And updates the master index.html portal with multi-chapter navigation,
real-time search, interactive clinical calculators, and Universal Cloud Sync.
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
from data.ch18_ophthalmology import TOPICS as T18
from data.ch19_ent import TOPICS as T19
from data.ch23_emergency import TOPICS as T23

CH17_TOPICS = T1 + T2 + T3 + T4 + T5 + T6 + T7
for t in CH17_TOPICS:
    t["chapter_num"] = 17
    t["chapter_name"] = "General Surgery"

ALL_TOPICS = CH17_TOPICS + T18 + T19 + T23

REPO_DIR = '/root/doctor-on-duty'

# Slug mapping
SLUGS = {}
# Chapter 17 (Keep existing filenames for backwards compatibility)
for i in range(1, 30):
    for t in CH17_TOPICS:
        if t["num"] == i:
            slug = t.get("slug")
            if not slug:
                # Map from existing SLUGS
                name_clean = re.sub(r'[^a-z0-9]+', '-', t["title"].lower()).strip('-')
                slug = f"{i:02d}-{name_clean}.html"
            SLUGS[i] = slug

# Specific known Chapter 17 slugs
EXISTING_CH17_SLUGS = {
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
SLUGS.update(EXISTING_CH17_SLUGS)

# Chapter 18, 19, 23
for t in T18 + T19 + T23:
    SLUGS[t["num"]] = t["slug"]

# Image Metadata
IMAGE_METADATA = {
    # Chapter 17
    1: {"img": "img/clinical_topic_01.jpg", "title": "Abdominal Topography & Quadrants", "caption": "Surface anatomy, topographical quadrants, and periumbilical reference planes for acute abdominal pain localization.", "extra_svg": "img/topic_01.svg", "extra_title": "Quadrants & Visceral vs Parietal Pain Pathways"},
    2: {"img": "img/clinical_topic_02.jpg", "title": "Visceral Pain Referred Dermatomes", "caption": "Referred pain mapping and dermatomal innervation of abdominal viscera (Gray's Anatomy / Clinical Neuroanatomy)."},
    3: {"img": "img/clinical_topic_03.jpg", "title": "Clinical Examination & Palpation", "caption": "Systematic physical examination: inspection, gentle superficial to deep palpation, peritonitis signs (guarding and rebound tenderness)."},
    4: {"img": "img/clinical_topic_04.jpg", "title": "Erect Radiograph: Pneumoperitoneum", "caption": "Erect plain abdominal and chest radiograph evaluating subdiaphragmatic crescentic free gas indicating visceral perforation."},
    5: {"img": "img/clinical_topic_05.jpg", "title": "Emergency Intravenous Resuscitation", "caption": "Immediate fluid resuscitation with wide-bore IV cannulae (16G/18G), crystalloid boluses, and hemodynamic stabilization."},
    6: {"img": "img/clinical_topic_06.jpg", "title": "Acute Appendicitis Gross Pathology", "caption": "Inflamed, hyperemic, and swollen appendix with surrounding serosal fibrinous exudate.", "extra_svg": "img/topic_06.svg", "extra_title": "McBurney Point & Alvarado Scoring System"},
    7: {"img": "img/clinical_topic_07.jpg", "title": "Acute Calculous Cholecystitis Ultrasound", "caption": "Gallbladder sonogram demonstrating thickened gallbladder wall (>4 mm), gallstones, and pericholecystic fluid halo.", "extra_svg": "img/topic_07.svg", "extra_title": "Tokyo Guidelines 2018 (TG18) Ultrasound Criteria"},
    8: {"img": "img/clinical_topic_08.jpg", "title": "Macroscopic Cholelithiasis (Gallstones)", "caption": "Multiple faceted cholesterol and mixed pigment gallstones excised during cholecystectomy."},
    9: {"img": "img/clinical_topic_09.jpg", "title": "ERCP Extraction of Choledocholithiasis", "caption": "Fluoroscopic ERCP image displaying balloon-assisted extraction of impacted common bile duct stones."},
    10: {"img": "img/clinical_topic_10.jpg", "title": "Ascending Suppurative Cholangitis", "caption": "Biliary tree obstruction presenting with Charcot's triad (RUQ pain, jaundice, fever) and Reynolds' pentad."},
    11: {"img": "img/clinical_topic_11.jpg", "title": "Acute Posterior Anal Fissure", "caption": "Linear tear in the anoderm distal to the dentate line in the posterior midline, showing exposed internal anal sphincter fibers.", "extra_svg": "img/sitz_bath_tub.png", "extra_title": "Warm Sitz Bath Hydrotherapy Setup"},
    12: {"img": "img/clinical_topic_12.jpg", "title": "Internal & External Hemorrhoids", "caption": "Vascular cushion hyperplasia and prolapsed internal hemorrhoids relative to the dentate line.", "extra_svg": "img/topic_12.svg", "extra_title": "Classification of Internal Hemorrhoids (Degrees 1 to 4)"},
    13: {"img": "img/clinical_topic_13.jpg", "title": "Anorectal Abscess Spaces & Anatomy", "caption": "Cryptoglandular infection spreading into anatomical spaces (perianal, ischiorectal, intersphincteric, pelvirectal)."},
    14: {"img": "img/clinical_topic_14.jpg", "title": "Intergluteal Pilonidal Abscess", "caption": "Infected natal cleft midline sinus tract with loose hair penetration and surrounding erythematous abscess."},
    15: {"img": "img/clinical_topic_15.jpg", "title": "Acute Necrotizing Pancreatitis Pathology", "caption": "Enzymatic auto-digestion of pancreatic parenchyma, acute interstitial edema, and retroperitoneal saponification."},
    16: {"img": "img/clinical_topic_16.jpg", "title": "Upright AXR: Small Bowel Obstruction", "caption": "Multiple centrally distributed dilated loops of small bowel with prominent air-fluid levels in a step-ladder pattern."},
    17: {"img": "img/clinical_topic_17.jpg", "title": "Massive Ascites in Cirrhotic Liver Disease", "caption": "Gross distended abdomen with shifting dullness and fluid thrill; candidate for diagnostic paracentesis (SBP check: PMN > 250/uL)."},
    18: {"img": "img/clinical_topic_18.jpg", "title": "Generalized Secondary Peritonitis", "caption": "Extensive purulent peritoneal exudate secondary to gastrointestinal perforation requiring emergent exploratory laparotomy."},
    19: {"img": "img/clinical_topic_19.jpg", "title": "Sacral Decubitus Ulcer (Stage IV)", "caption": "Full-thickness tissue loss with exposed muscle, tendon, and underlying bone, surrounded by undermined margins.", "extra_svg": "img/topic_19.svg", "extra_title": "NPUAP Pressure Ulcer Staging Classification"},
    20: {"img": "img/clinical_topic_20.jpg", "title": "Diabetic Plantar Neuropathic Ulcer", "caption": "Punched-out neuropathic plantar ulcer over the metatarsal head with surrounding hypertrophic callus."},
    21: {"img": "img/clinical_topic_21.jpg", "title": "Hypertrophic Surgical Scar", "caption": "Elevated, erythematous, pruritic fibrous scar remaining strictly confined within the boundaries of the original incision."},
    22: {"img": "img/clinical_topic_22.jpg", "title": "Severe Earlobe / Presternal Keloid", "caption": "Exuberant fibroblastic collagen deposition invading and proliferating well beyond original wound margins with high recurrence."},
    23: {"img": "img/clinical_topic_23.jpg", "title": "Subcutaneous Lobulated Lipoma", "caption": "Encapsulated, soft, mobile, lobulated adipose tumor demonstrating a positive clinical 'slip sign' on lateral palpation."},
    24: {"img": "img/clinical_topic_24.jpg", "title": "Cervical Acrochordons (Skin Tags)", "caption": "Multiple soft, flesh-colored, pedunculated papillomas in friction-prone intertriginous folds of the neck and axilla."},
    25: {"img": "img/clinical_topic_25.jpg", "title": "Dorsal Wrist Ganglion Cyst", "caption": "Transilluminating cystic nodule originating from the scapholunate ligament joint capsule containing clear gelatinous mucin."},
    26: {"img": "img/clinical_topic_26.jpg", "title": "Stage III Ingrown Toenail (Onychocryptosis)", "caption": "Lateral nail spicule piercing lateral nail fold causing marked erythema, edema, and exuberantly bleeding granulation tissue.", "extra_svg": "img/topic_26.svg", "extra_title": "Spicule Mechanism & 88% Phenol Chemical Matrixectomy"},
    27: {"img": "img/clinical_topic_27.jpg", "title": "Distal Pulp Space Whitlow / Felon", "caption": "Severe throbbing tension in the closed fibrofatty septa of the fingertip pulp risking osteomyelitis and compartment ischemia.", "extra_svg": "img/felon_finger_pulp.png", "extra_title": "Authentic Clinical Pulp Infection Presentation"},
    28: {"img": "img/clinical_topic_28.jpg", "title": "Acute Bacterial Paronychia with Abscess", "caption": "Fluctuant purulent collection tracking along the lateral and proximal eponychial nail fold requiring prompt elevator drainage."},
    29: {"img": "img/clinical_topic_29.jpg", "title": "Chronic Fungal & Irritant Paronychia", "caption": "Loss of protective cuticle, lateral fold boggy induration, secondary bacterial superinfection, and nail plate dystrophy.", "extra_svg": "img/paronychia_anatomy_clinical.png", "extra_title": "Authentic Paronychia Anatomy & Management Panel"},
    
    # Chapter 18: Ophthalmology
    101: {"img": "img/clinical_ch18_01.jpg", "title": "External Hordeolum (Stye)", "caption": "Acute focal staphylococcal micro-abscess pointing along the anterior ciliary eyelid margin."},
    102: {"img": "img/clinical_ch18_02.jpg", "title": "Anterior Blepharitis & Collarettes", "caption": "Chronic eyelid margin erythema with characteristic hard fibrinous collarettes cuffing the cilia base."},
    103: {"img": "img/clinical_ch18_03.jpg", "title": "Acute Bacterial Conjunctivitis", "caption": "Marked peripheral conjunctival injection with copious mucopurulent discharge gluing eyelashes together."},
    104: {"img": "img/clinical_ch18_04.jpg", "title": "Epidemic Keratoconjunctivitis (EKC)", "caption": "Watery serous epiphora, palpebral follicular hyperplasia, and chemosis characteristic of adenoviral infection."},
    105: {"img": "img/clinical_ch18_05.jpg", "title": "Vernal Keratoconjunctivitis (VKC)", "caption": "Everted upper eyelid displaying giant cobblestone papillae and thick ropy mucoid discharge."},
    106: {"img": "img/clinical_ch18_06.jpg", "title": "Trachomatous Follicular Inflammation", "caption": "Prominent lymphoid follicles on superior tarsal conjunctiva characteristic of WHO Trachoma Stage TF."},
    107: {"img": "img/clinical_ch18_07.jpg", "title": "Corneal Abrasion Fluorescein Staining", "caption": "Cobalt blue slit-lamp examination demonstrating brilliant green fluorescein uptake over epithelial scratch defect."},
    108: {"img": "img/clinical_ch18_08.jpg", "title": "Acute Ocular Chemical Burn", "caption": "Epithelial sloughing and dangerous limbal ischemia (ischemic porcelain blanching) after alkali chemical contact."},
    109: {"img": "img/clinical_ch18_09.jpg", "title": "Corneal Metallic Foreign Body", "caption": "Superficial metallic iron splinter embedded in corneal stroma with early surrounding orange rust ring."},
    110: {"img": "img/clinical_ch18_10.jpg", "title": "Acute Angle-Closure Glaucoma", "caption": "Steamy microcystic corneal edema, ciliary injection, and fixed vertically oval mid-dilated non-reactive pupil."},
    111: {"img": "img/clinical_ch18_11.jpg", "title": "Acute Anterior Uveitis (Iritis)", "caption": "Violaceous circumcorneal ciliary flush, sluggish constricted irregular pupil, and endothelial keratic precipitates."},
    112: {"img": "img/clinical_ch18_12.jpg", "title": "Clinical Ophthalmic Formulations", "caption": "Topical eye drops and ointments showing correct conjunctival sac pouch instillation technique."},

    # Chapter 19: ENT
    201: {"img": "img/clinical_ch19_01.jpg", "title": "CT Paranasal Sinuses: CRS", "caption": "Coronal CT PNS showing bilateral mucosal opacification and complete blockage of the osteomeatal complexes."},
    202: {"img": "img/clinical_ch19_02.jpg", "title": "Deviated Nasal Septum (DNS)", "caption": "Anterior rhinoscopy revealing marked septal cartilaginous deviation with compensatory turbinate hypertrophy."},
    203: {"img": "img/clinical_ch19_03.jpg", "title": "Acute Epistaxis Examination", "caption": "Clinical evaluation of Little's area on the anterior nasal septum for active vascular bleeding."},
    204: {"img": "img/clinical_ch19_04.jpg", "title": "Acute Follicular Tonsillitis", "caption": "Bilateral enlarged, hyperemic palatine tonsils with thick yellow follicular exudates filling tonsillar crypts."},
    205: {"img": "img/clinical_ch19_05.jpg", "title": "Peritonsillar Abscess (Quinsy)", "caption": "Unilateral bulging soft palate swelling pushing palatine tonsil medially with contralateral uvular displacement."},
    206: {"img": "img/clinical_ch19_06.jpg", "title": "Acute Otitis Media (AOM)", "caption": "Otoscopic appearance of fiery red, donut-like bulging tympanic membrane with total loss of light reflex."},
    207: {"img": "img/clinical_ch19_07.jpg", "title": "Atticoantral CSOM & Cholesteatoma", "caption": "Posterosuperior attic perforation filled with white flaky keratin debris and granulation tissue."},
    208: {"img": "img/clinical_ch19_08.jpg", "title": "Otomycosis (Aspergillus niger)", "caption": "External ear canal filled with wet blotting-paper-like fungal mycelia studded with black spores."},
    209: {"img": "img/clinical_ch19_09.jpg", "title": "Diffuse Acute Otitis Externa", "caption": "Circumferential inflammatory stenosis and maceration of external auditory canal with purulent exudate."},
    210: {"img": "img/clinical_ch19_10.jpg", "title": "Dix-Hallpike & Epley Repositioning", "caption": "Clinical positioning sequence for posterior semicircular canalithiasis particle repositioning."},
    211: {"img": "img/clinical_ch19_11.jpg", "title": "Endolymphatic Labyrinth Anatomy", "caption": "Inner ear membranous labyrinth highlighting endolymphatic hydrops distension in Ménière's disease."},
    212: {"img": "img/clinical_ch19_12.jpg", "title": "Acute Bell's Palsy (LMN VII)", "caption": "Unilateral complete facial paralysis with loss of forehead wrinkles, lagophthalmos, and drooping mouth angle."},

    # Chapter 23: Emergency Medicine
    301: {"img": "img/clinical_ch23_01.jpg", "title": "High-Quality CPR & Defibrillation", "caption": "Resuscitation team delivering continuous chest compressions (100–120/min) and early defibrillation."},
    302: {"img": "img/clinical_ch23_02.jpg", "title": "Emergency Intramuscular Epinephrine", "caption": "Immediate 0.5 mg IM adrenaline administration into the anterolateral vastus lateralis muscle of the thigh."},
    303: {"img": "img/clinical_ch23_03.jpg", "title": "ICU Sepsis Resuscitation Bundle", "caption": "Hemodynamic invasive monitoring, rapid 30 mL/kg crystalloids, and early norepinephrine vasopressor titration."},
    304: {"img": "img/clinical_ch23_04.jpg", "title": "Organophosphate Pesticide Toxicity", "caption": "Agricultural pesticide exposure leading to acute cholinergic muscarinic receptor hyper-stimulation."},
    305: {"img": "img/clinical_ch23_05.jpg", "title": "Paracetamol Hepatotoxicity", "caption": "Centrilobular Zone-III hepatic necrosis mechanism preventable by early N-acetylcysteine (NAC) infusion."},
    306: {"img": "img/clinical_ch23_06.jpg", "title": "Venomous Viperid Snakebite", "caption": "Bitten lower limb displaying severe local edema, hemorrhagic blebs, and 20-Minute Clotting Test failure."},
    307: {"img": "img/clinical_ch23_07.jpg", "title": "Major Thermal Burn Resuscitation", "caption": "Extensive partial and full-thickness burn requiring goal-directed Parkland Ringer's Lactate fluid infusion."},
    308: {"img": "img/clinical_ch23_08.jpg", "title": "Acute Poisoning Toxidrome Matrix", "caption": "Systematic clinical toxidrome differentiation based on pupil reactivity, skin moisture, and vital signs."},
    309: {"img": "img/clinical_ch23_09.jpg", "title": "Multimodal Acute Pain Management", "caption": "Emergency analgesia algorithm integrating IV paracetamol, NSAIDs, and titrated opioids based on VAS score."}
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
  max-width: 320px;
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
  font-size: 22px;
  font-weight: 800;
  letter-spacing: -0.4px;
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
  grid-template-columns: 1.15fr 0.85fr;
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
  max-height: 320px;
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
.clinical-section { margin-bottom: 16px; }
.clinical-section:last-child { margin-bottom: 0; }

.clinical-section h4 {
  font-size: 14.5px;
  font-weight: 700;
  color: var(--teal-light);
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.clinical-section p {
  font-size: 13.5px;
  color: var(--text-main);
  line-height: 1.5;
  margin-bottom: 8px;
}

.med-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 12.5px;
  margin: 8px 0 12px 0;
}

.med-table th, .med-table td {
  padding: 8px 10px;
  text-align: left;
  border: 1px solid var(--border);
}

.med-table th {
  background: var(--bg-elevated);
  color: var(--text-main);
  font-weight: 700;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.med-table td { background: var(--bg-card); }
.med-table tr:hover td { background: var(--bg-card-subtle); }

.table-responsive {
  width: 100%;
  overflow-x: auto;
  margin-bottom: 10px;
}

.steps-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 8px;
  margin: 8px 0 12px 0;
}

.step-card {
  background: var(--bg-card-subtle);
  border: 1px solid var(--border);
  border-left: 3px solid var(--teal);
  border-radius: 6px;
  padding: 8px 12px;
  font-size: 13px;
}

.step-num {
  display: inline-block;
  background: var(--teal);
  color: #fff;
  font-size: 10px;
  font-weight: 800;
  padding: 2px 6px;
  border-radius: 4px;
  margin-right: 6px;
  vertical-align: middle;
}

.alert {
  padding: 10px 14px;
  border-radius: 6px;
  font-size: 12.5px;
  line-height: 1.45;
  margin: 10px 0;
  border-left: 4px solid;
}

.alert-danger { background: rgba(244, 63, 94, 0.1); border-color: var(--rose); color: var(--rose-light); }
.alert-warning { background: rgba(245, 158, 11, 0.1); border-color: var(--amber); color: var(--amber-light); }
.alert-info { background: rgba(59, 130, 246, 0.1); border-color: var(--blue); color: var(--blue-light); }
.alert-success { background: rgba(16, 185, 129, 0.1); border-color: var(--emerald); color: var(--emerald-light); }

.bullet-list, .sub-list {
  padding-left: 18px;
  margin: 6px 0;
  font-size: 13px;
}

.bullet-list li, .sub-list li { margin-bottom: 4px; }

/* Interactive Clinical Calculators */
.calc-box {
  background: var(--bg-card-subtle);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 14px;
  margin-top: 10px;
}

.calc-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 6px 0;
  border-bottom: 1px solid var(--border-subtle);
  font-size: 13px;
}

.calc-row:last-child { border-bottom: none; }

.calc-score-display {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 8px 12px;
  margin-top: 10px;
  font-weight: 700;
}

.score-num {
  font-size: 18px;
  color: var(--teal);
  font-family: var(--font-mono);
}

.bottom-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-top: 24px;
  padding-top: 16px;
  border-top: 1px solid var(--border);
  flex-wrap: wrap;
}

@media print {
  .top-navbar, .bottom-nav, .nav-actions { display: none !important; }
  body { background: #fff !important; color: #000 !important; }
  .card, .topic-banner { border: 1px solid #ccc !important; background: #fff !important; color: #000 !important; }
}
"""

SHARED_JS = """
function initTheme() {
  const saved = localStorage.getItem('dod_theme') || 'dark';
  document.documentElement.setAttribute('data-theme', saved);
  updateThemeIcon(saved);
}

function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('dod_theme', next);
  updateThemeIcon(next);
}

function updateThemeIcon(theme) {
  const icon = document.getElementById('theme-icon');
  if (icon) {
    icon.className = theme === 'dark' ? 'fa-solid fa-moon' : 'fa-solid fa-sun';
  }
}

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  
  const select = document.getElementById('topic-quick-jump');
  if (select) {
    select.addEventListener('change', (e) => {
      if (e.target.value) {
        window.location.href = e.target.value;
      }
    });
  }
});
"""

def generate_page(topic):
    num = topic["num"]
    ch_num = topic["chapter_num"]
    ch_name = topic["chapter_name"]
    slug = SLUGS[num]
    
    # Navigation prev/next within ALL_TOPICS
    curr_idx = next(i for i, t in enumerate(ALL_TOPICS) if t["num"] == num)
    prev_topic = ALL_TOPICS[curr_idx - 1] if curr_idx > 0 else None
    next_topic = ALL_TOPICS[curr_idx + 1] if curr_idx < len(ALL_TOPICS) - 1 else None
    
    prev_slug = SLUGS[prev_topic["num"]] if prev_topic else None
    next_slug = SLUGS[next_topic["num"]] if next_topic else None
    
    meta = IMAGE_METADATA.get(num, {
        "img": f"img/clinical_topic_{num:02d}.jpg",
        "title": topic["title"],
        "caption": topic.get("summary", "")
    })
    
    # Build select options grouped by chapter
    options_html = []
    chapters = [
        (17, "Chapter 17: General Surgery", [t for t in ALL_TOPICS if t["chapter_num"] == 17]),
        (18, "Chapter 18: Ophthalmology", [t for t in ALL_TOPICS if t["chapter_num"] == 18]),
        (19, "Chapter 19: Ear, Nose & Throat (ENT)", [t for t in ALL_TOPICS if t["chapter_num"] == 19]),
        (23, "Chapter 23: Emergency Medicine & Poisoning", [t for t in ALL_TOPICS if t["chapter_num"] == 23])
    ]
    
    for cnum, cname, top_list in chapters:
        options_html.append(f'<optgroup label="{cname}">')
        for t in top_list:
            tnum = t["num"]
            tslug = SLUGS[tnum]
            selected = "selected" if tnum == num else ""
            options_html.append(f'<option value="{tslug}" {selected}>{tnum:02d}. {t["title"]}</option>')
        options_html.append('</optgroup>')
    
    dropdown_html = "\n".join(options_html)
    
    # Right column extra content
    right_extras = []
    
    # If topic has extra SVG diagram
    if meta.get("extra_svg"):
        right_extras.append(f"""
        <div class="card">
          <div class="card-header">
            <span class="card-title"><i class="fa-solid fa-diagram-project"></i> {meta.get('extra_title', 'Clinical Diagram')}</span>
          </div>
          <div class="media-container">
            <img src="{meta['extra_svg']}" alt="{meta.get('extra_title', 'Diagram')}" loading="lazy">
          </div>
        </div>
        """)
        
    # Interactive calculators for specific conditions
    if num == 6: # Appendicitis Alvarado
        right_extras.append("""
        <div class="card">
          <div class="card-header">
            <span class="card-title"><i class="fa-solid fa-calculator"></i> Interactive Alvarado Calculator</span>
          </div>
          <div class="calc-box">
            <div class="calc-row"><label><input type="checkbox" class="alv-cb" data-pts="1" onchange="calcAlv()"> Migration of pain to RLQ</label><span>+1</span></div>
            <div class="calc-row"><label><input type="checkbox" class="alv-cb" data-pts="1" onchange="calcAlv()"> Anorexia</label><span>+1</span></div>
            <div class="calc-row"><label><input type="checkbox" class="alv-cb" data-pts="1" onchange="calcAlv()"> Nausea / Vomiting</label><span>+1</span></div>
            <div class="calc-row"><label><input type="checkbox" class="alv-cb" data-pts="2" onchange="calcAlv()"> Tenderness in RLQ</label><span>+2</span></div>
            <div class="calc-row"><label><input type="checkbox" class="alv-cb" data-pts="1" onchange="calcAlv()"> Rebound tenderness (Blumberg)</label><span>+1</span></div>
            <div class="calc-row"><label><input type="checkbox" class="alv-cb" data-pts="1" onchange="calcAlv()"> Elevated temperature (&ge; 37.3&deg;C)</label><span>+1</span></div>
            <div class="calc-row"><label><input type="checkbox" class="alv-cb" data-pts="2" onchange="calcAlv()"> Leukocytosis (&gt; 10,000 / &mu;L)</label><span>+2</span></div>
            <div class="calc-row"><label><input type="checkbox" class="alv-cb" data-pts="1" onchange="calcAlv()"> Shift to left of neutrophils (&gt; 75%)</label><span>+1</span></div>
            <div class="calc-score-display">
              <span>Total Alvarado Score:</span>
              <span id="alv-total" class="score-num">0 / 10</span>
            </div>
            <div id="alv-risk" style="margin-top:8px; font-size:12.5px; font-weight:600; color:var(--text-muted);">Risk: Low (Discharge candidate)</div>
          </div>
        </div>
        <script>
        function calcAlv() {
          let pts = 0;
          document.querySelectorAll('.alv-cb:checked').forEach(c => pts += parseInt(c.dataset.pts));
          document.getElementById('alv-total').innerText = pts + ' / 10';
          let el = document.getElementById('alv-risk');
          if (pts <= 4) { el.innerText = 'Score 1-4: Low risk (Appendicitis unlikely). Observation/Discharge.'; el.style.color = 'var(--emerald-light)'; }
          else if (pts <= 6) { el.innerText = 'Score 5-6: Intermediate / Compatible. CT scan / Ultrasound mandatory.'; el.style.color = 'var(--amber-light)'; }
          else { el.innerText = 'Score 7-10: High probability. Surgical consult & Appendectomy indicated.'; el.style.color = 'var(--rose-light)'; }
        }
        </script>
        """)
        
    elif num == 110: # Acute Angle Closure Glaucoma
        right_extras.append("""
        <div class="card">
          <div class="card-header">
            <span class="card-title"><i class="fa-solid fa-bolt"></i> AACG Emergency Resuscitation Steps</span>
          </div>
          <div class="steps-grid">
            <div class="step-card"><span class="step-num">1</span> <strong>Acetazolamide (Diamox):</strong> 500 mg IV stat, then 250 mg PO TDS.</div>
            <div class="step-card"><span class="step-num">2</span> <strong>Topical Beta-Blocker:</strong> Timolol 0.5% 1 drop stat.</div>
            <div class="step-card"><span class="step-num">3</span> <strong>Alpha-2 Agonist:</strong> Apraclonidine 1% / Brimonidine 0.2% 1 drop.</div>
            <div class="step-card"><span class="step-num">4</span> <strong>Miotic:</strong> Pilocarpine 2% 1 drop q15min (when IOP &lt; 35 mmHg).</div>
            <div class="step-card"><span class="step-num">5</span> <strong>Mannitol 20%:</strong> 1-2 g/kg IV over 45 min if IOP refractory.</div>
            <div class="step-card"><span class="step-num">6</span> <strong>Curative:</strong> Bilateral Nd:YAG Laser Peripheral Iridotomy.</div>
          </div>
        </div>
        """)
        
    elif num == 204: # Centor Score Tonsillitis
        right_extras.append("""
        <div class="card">
          <div class="card-header">
            <span class="card-title"><i class="fa-solid fa-calculator"></i> Modified Centor (McIsaac) Calculator</span>
          </div>
          <div class="calc-box">
            <div class="calc-row"><label><input type="checkbox" class="cnt-cb" data-pts="1" onchange="calcCentor()"> Tonsillar exudates / swelling</label><span>+1</span></div>
            <div class="calc-row"><label><input type="checkbox" class="cnt-cb" data-pts="1" onchange="calcCentor()"> Tender anterior cervical adenopathy</label><span>+1</span></div>
            <div class="calc-row"><label><input type="checkbox" class="cnt-cb" data-pts="1" onchange="calcCentor()"> History of fever &gt; 38&deg;C</label><span>+1</span></div>
            <div class="calc-row"><label><input type="checkbox" class="cnt-cb" data-pts="1" onchange="calcCentor()"> Absence of cough</label><span>+1</span></div>
            <div class="calc-row">
              <label>Patient Age:</label>
              <select id="cnt-age" onchange="calcCentor()" style="background:var(--bg-elevated); color:var(--text-main); border:1px solid var(--border); border-radius:4px; padding:2px 6px;">
                <option value="1">3–14 years (+1)</option>
                <option value="0" selected>15–44 years (0)</option>
                <option value="-1">&ge; 45 years (-1)</option>
              </select>
            </div>
            <div class="calc-score-display">
              <span>Centor / McIsaac Score:</span>
              <span id="cnt-total" class="score-num">0</span>
            </div>
            <div id="cnt-plan" style="margin-top:8px; font-size:12.5px; font-weight:600; color:var(--text-muted);">Probability &lt; 10%. No antibiotics.</div>
          </div>
        </div>
        <script>
        function calcCentor() {
          let pts = parseInt(document.getElementById('cnt-age').value);
          document.querySelectorAll('.cnt-cb:checked').forEach(c => pts += parseInt(c.dataset.pts));
          document.getElementById('cnt-total').innerText = pts;
          let el = document.getElementById('cnt-plan');
          if (pts <= 1) { el.innerText = 'Score &le; 1: GABHS risk < 10%. Symptomatic analgesia only; no antibiotics.'; el.style.color = 'var(--emerald-light)'; }
          else if (pts <= 3) { el.innerText = 'Score 2-3: GABHS risk 15-30%. Throat swab / RADT; treat if positive.'; el.style.color = 'var(--amber-light)'; }
          else { el.innerText = 'Score &ge; 4: GABHS risk > 50%. Empiric Penicillin V 500mg TDS x 10 days.'; el.style.color = 'var(--rose-light)'; }
        }
        </script>
        """)
        
    elif num == 307: # Parkland Burn
        right_extras.append("""
        <div class="card">
          <div class="card-header">
            <span class="card-title"><i class="fa-solid fa-calculator"></i> Interactive Parkland Formula Calculator</span>
          </div>
          <div class="calc-box">
            <div class="calc-row">
              <label>Patient Weight (kg):</label>
              <input type="number" id="burn-wt" value="70" min="5" max="150" oninput="calcBurn()" style="width:70px; background:var(--bg-elevated); color:var(--text-main); border:1px solid var(--border); border-radius:4px; padding:2px 6px;">
            </div>
            <div class="calc-row">
              <label>% TBSA Burn (2nd/3rd Deg):</label>
              <input type="number" id="burn-tbsa" value="25" min="1" max="95" oninput="calcBurn()" style="width:70px; background:var(--bg-elevated); color:var(--text-main); border:1px solid var(--border); border-radius:4px; padding:2px 6px;">
            </div>
            <div class="calc-score-display">
              <span>Total 24-hr Fluid (RL):</span>
              <span id="burn-total" class="score-num">7,000 mL</span>
            </div>
            <div class="steps-grid" style="margin-top:10px;">
              <div class="step-card" style="font-size:12px;"><strong>First 8 hrs:</strong> <span id="burn-8h">3,500 mL</span> (approx <span id="burn-8h-rate">438 mL/hr</span>)</div>
              <div class="step-card" style="font-size:12px;"><strong>Next 16 hrs:</strong> <span id="burn-16h">3,500 mL</span> (approx <span id="burn-16h-rate">219 mL/hr</span>)</div>
            </div>
            <div style="font-size:11.5px; color:var(--text-muted); margin-top:6px;">Target urine output: 0.5–1.0 mL/kg/hr.</div>
          </div>
        </div>
        <script>
        function calcBurn() {
          let wt = parseFloat(document.getElementById('burn-wt').value) || 0;
          let tbsa = parseFloat(document.getElementById('burn-tbsa').value) || 0;
          let total = 4 * wt * tbsa;
          document.getElementById('burn-total').innerText = Math.round(total).toLocaleString() + ' mL';
          let half = total / 2;
          document.getElementById('burn-8h').innerText = Math.round(half).toLocaleString() + ' mL';
          document.getElementById('burn-8h-rate').innerText = Math.round(half / 8) + ' mL/hr';
          document.getElementById('burn-16h').innerText = Math.round(half).toLocaleString() + ' mL';
          document.getElementById('burn-16h-rate').innerText = Math.round(half / 16) + ' mL/hr';
        }
        </script>
        """)

    extras_html = "\n".join(right_extras)
    
    html_page = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Topic {num:02d}: {topic['title']} | Doctor on Duty</title>
  
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

  <!-- Sticky Top Navigation Bar -->
  <header class="top-navbar">
    <a href="index.html" class="brand-section">
      <div class="brand-logo">DoD</div>
      <div class="brand-text">
        <h1>Doctor on Duty</h1>
        <span>{ch_name}</span>
      </div>
    </a>

    <div class="nav-actions">
      <select id="topic-quick-jump" class="topic-select">
{dropdown_html}
      </select>

      {f'<a href="{prev_slug}" class="nav-btn" title="Previous Topic"><i class="fa-solid fa-chevron-left"></i> Prev</a>' if prev_slug else '<span class="nav-btn" style="opacity:0.4; cursor:default;"><i class="fa-solid fa-chevron-left"></i> Prev</span>'}
      {f'<a href="{next_slug}" class="nav-btn" title="Next Topic">Next <i class="fa-solid fa-chevron-right"></i></a>' if next_slug else '<span class="nav-btn" style="opacity:0.4; cursor:default;">Next <i class="fa-solid fa-chevron-right"></i></span>'}

      <button onclick="toggleTheme()" class="nav-btn" title="Toggle Dark/Light Mode">
        <i id="theme-icon" class="fa-solid fa-moon"></i>
      </button>

      <a href="index.html" class="nav-btn primary" title="Back to Master Portal">
        <i class="fa-solid fa-house"></i> Portal
      </a>
    </div>
  </header>

  <!-- Main Container -->
  <main class="page-container">

    <!-- Topic Header Banner -->
    <div class="topic-banner">
      <div class="banner-meta">
        <span class="badge badge-category"><i class="fa-solid fa-book-medical"></i> Ch. {ch_num}: {ch_name}</span>
        <span class="badge badge-emergency"><i class="fa-solid fa-tag"></i> {topic.get('category_name', 'Clinical')}</span>
        <span class="badge badge-page"><i class="fa-solid fa-bookmark"></i> Book {topic.get('book_page', '3rd Ed.')}</span>
        <span class="badge badge-routine"><i class="fa-solid fa-hashtag"></i> Topic #{num:02d}</span>
      </div>
      <h2 class="topic-title">{topic['title']}</h2>
      <p class="topic-summary">{topic.get('summary', '')}</p>
    </div>

    <!-- 2-Column Condensed Grid -->
    <div class="condensed-grid">
      
      <!-- Left Column: Primary Clinical Protocol & Formularies -->
      <div class="column">
        <div class="card">
          <div class="card-header">
            <span class="card-title"><i class="fa-solid fa-notes-medical"></i> Clinical Management & Pharmacotherapy</span>
            <span style="font-size:11px; color:var(--text-muted); font-weight:600;"><i class="fa-solid fa-shield-halved"></i> Pakistani Standards</span>
          </div>
          {topic['content']}
        </div>
      </div>

      <!-- Right Column: Visual Diagnostics, Real Clinical Image & Quick Scores -->
      <div class="column">
        <div class="card">
          <div class="card-header">
            <span class="card-title"><i class="fa-solid fa-image"></i> Clinical Pathology & Radiodiagnostics</span>
            <span style="font-size:11px; color:var(--teal); font-weight:600;">Verified Visual</span>
          </div>
          <div class="media-container">
            <img src="{meta['img']}" alt="{meta['title']}" loading="lazy">
            <div class="media-caption">
              <strong>{meta['title']}</strong>
              {meta['caption']}
            </div>
          </div>
        </div>

        {extras_html}
      </div>

    </div>

    <!-- Bottom Navigation Bar -->
    <nav class="bottom-nav">
      <div>
        {f'<a href="{prev_slug}" class="nav-btn"><i class="fa-solid fa-arrow-left"></i> Previous Topic</a>' if prev_slug else ''}
      </div>
      <div>
        <a href="index.html" class="nav-btn primary"><i class="fa-solid fa-book-open"></i> Full Clinical Portal (All Chapters)</a>
      </div>
      <div>
        {f'<a href="{next_slug}" class="nav-btn">Next Topic <i class="fa-solid fa-arrow-right"></i></a>' if next_slug else ''}
      </div>
    </nav>

  </main>

  <script>
{SHARED_JS}
  </script>
</body>
</html>
"""
    dest_path = os.path.join(REPO_DIR, slug)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(html_page.strip())
    print(f"Generated standalone page: {slug} ({os.path.getsize(dest_path)} bytes)")

def build_master_portal():
    """Generates the master index.html portal linking to all 62 individual note files across all chapters."""
    
    chapter_groups = [
        (17, "Chapter 17: General Surgery", [t for t in ALL_TOPICS if t["chapter_num"] == 17], "fa-solid fa-scalpel", "var(--rose)"),
        (18, "Chapter 18: Ophthalmology", [t for t in ALL_TOPICS if t["chapter_num"] == 18], "fa-solid fa-eye", "var(--teal)"),
        (19, "Chapter 19: Ear, Nose & Throat (ENT)", [t for t in ALL_TOPICS if t["chapter_num"] == 19], "fa-solid fa-head-side-cough", "var(--amber)"),
        (23, "Chapter 23: Emergency Medicine & Poisoning", [t for t in ALL_TOPICS if t["chapter_num"] == 23], "fa-solid fa-truck-medical", "var(--blue)")
    ]

    cards_html = []
    for cnum, cname, topic_list, cicon, ccolor in chapter_groups:
        cards_html.append(f"""
        <div class="chapter-block" data-chapter="{cnum}">
          <div class="category-header" style="border-left: 4px solid {ccolor};">
            <h3><i class="{cicon}" style="color: {ccolor};"></i> {cname} ({len(topic_list)} Topics)</h3>
          </div>
          <div class="topic-cards-grid">
        """)
        
        for t in topic_list:
            num = t["num"]
            slug = SLUGS[num]
            meta = IMAGE_METADATA.get(num, {"img": f"img/clinical_topic_{num:02d}.jpg", "title": t["title"], "caption": ""})
            badge_class = f"badge-{t.get('badge', 'routine')}"
            badge_text = t.get('badge', 'CLINICAL').upper()
            
            cards_html.append(f"""
            <a href="{slug}" class="topic-card" data-title="{t['title'].lower()}" data-num="{num}" data-summary="{t.get('summary', '').lower()}" data-chapter="{cnum}">
              <div class="card-thumb">
                <img src="{meta['img']}" alt="{t['title']}" loading="lazy">
                <span class="badge {badge_class} thumb-badge">{badge_text}</span>
                <span class="thumb-page">{t.get('book_page', '3rd Ed.')}</span>
              </div>
              <div class="card-body">
                <div class="card-topic-num">Topic #{num:02d} &bull; Ch. {cnum}</div>
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
  <title>Doctor on Duty | System-Wise Clinical Notes Portal</title>
  
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
  max-width: 750px;
  font-size: 14px;
  line-height: 1.5;
}}

.stats-grid {{
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}}

.stat-chip {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 8px 14px;
  text-align: center;
}}

.stat-chip strong {{
  display: block;
  font-size: 20px;
  color: var(--teal-light);
  font-family: var(--font-mono);
}}

.stat-chip span {{
  font-size: 11px;
  color: var(--text-muted);
  text-transform: uppercase;
  font-weight: 700;
}}

/* Chapter Navigation Filter Bar */
.chapter-nav-bar {{
  display: flex;
  align-items: center;
  gap: 8px;
  overflow-x: auto;
  padding-bottom: 12px;
  margin-bottom: 20px;
  border-bottom: 1px solid var(--border);
}}

.chapter-filter-btn {{
  padding: 8px 16px;
  border-radius: 8px;
  border: 1px solid var(--border);
  background: var(--bg-card);
  color: var(--text-muted);
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  white-space: nowrap;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.15s ease;
}}

.chapter-filter-btn:hover {{
  border-color: var(--teal);
  color: var(--teal-light);
  background: var(--bg-card-subtle);
}}

.chapter-filter-btn.active {{
  background: var(--teal);
  color: #fff;
  border-color: var(--teal);
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
  color: var(--text-muted);
  font-size: 16px;
}}

/* Category Section Blocks */
.category-block, .chapter-block {{
  margin-bottom: 32px;
}}

.category-header {{
  padding: 6px 12px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 8px;
  margin-bottom: 16px;
}}

.category-header h3 {{
  font-size: 17px;
  font-weight: 800;
  display: flex;
  align-items: center;
  gap: 8px;
}}

/* Cards Grid */
.topic-cards-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
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
  transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
}}

.topic-card:hover {{
  transform: translateY(-3px);
  border-color: var(--teal);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
}}

.card-thumb {{
  position: relative;
  width: 100%;
  height: 150px;
  background: #000;
  overflow: hidden;
}}

.card-thumb img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}}

.topic-card:hover .card-thumb img {{
  transform: scale(1.05);
}}

.thumb-badge {{
  position: absolute;
  top: 8px;
  left: 8px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.4);
}}

.thumb-page {{
  position: absolute;
  bottom: 8px;
  right: 8px;
  background: rgba(0, 0, 0, 0.75);
  color: #fff;
  font-size: 10.5px;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 4px;
  backdrop-filter: blur(4px);
}}

.card-body {{
  padding: 14px;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}}

.card-topic-num {{
  font-size: 11px;
  color: var(--teal-light);
  font-weight: 800;
  text-transform: uppercase;
  margin-bottom: 4px;
  letter-spacing: 0.5px;
}}

.card-topic-title {{
  font-size: 15px;
  font-weight: 700;
  margin-bottom: 8px;
  line-height: 1.3;
  color: var(--text-main);
}}

.card-topic-summary {{
  font-size: 12.5px;
  color: var(--text-muted);
  line-height: 1.45;
  margin-bottom: 14px;
  flex-grow: 1;
}}

.card-footer-cta {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid var(--border-subtle);
  padding-top: 10px;
  font-size: 12px;
  font-weight: 700;
  color: var(--teal);
}}

.topic-card:hover .card-footer-cta {{
  color: var(--teal-light);
}}

/* Upcoming Chapters Roadmap Section */
.roadmap-section {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px;
  margin-top: 40px;
}}

.roadmap-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 12px;
  margin-top: 14px;
}}

.roadmap-item {{
  background: var(--bg-card-subtle);
  border: 1px solid var(--border-subtle);
  border-radius: 8px;
  padding: 10px 12px;
  font-size: 12.5px;
}}

.roadmap-item strong {{
  color: var(--teal-light);
  display: block;
  margin-bottom: 2px;
}}

.roadmap-item span {{
  color: var(--text-muted);
  font-size: 11px;
}}
</style>
</head>
<body>

  <!-- Top Header Navigation -->
  <header class="top-navbar">
    <a href="index.html" class="brand-section">
      <div class="brand-logo">DoD</div>
      <div class="brand-text">
        <h1>Doctor on Duty</h1>
        <span>System-Wise Clinical Reference Guide</span>
      </div>
    </a>

    <div class="nav-actions">
      <button onclick="toggleTheme()" class="nav-btn" title="Toggle Dark/Light Mode">
        <i id="theme-icon" class="fa-solid fa-moon"></i>
      </button>
      <a href="https://github.com/hassanakhter079/Doctor-on-Duty" target="_blank" class="nav-btn">
        <i class="fa-brands fa-github"></i> Repository
      </a>
    </div>
  </header>

  <!-- Main Portal Body -->
  <main class="page-container">

    <!-- Hero Portal Banner -->
    <div class="portal-hero">
      <div>
        <h2>Doctor on Duty (3rd Edition)</h2>
        <p>Condensed system-by-system clinical reference guide. Complete with evidence-based diagnostics, stepwise emergency/inpatient management protocols, authentic Pakistani brand formularies, and clinical images for every single topic.</p>
      </div>
      <div class="stats-grid">
        <div class="stat-chip">
          <strong>62</strong>
          <span>Live Notes</span>
        </div>
        <div class="stat-chip">
          <strong>4</strong>
          <span>Active Systems</span>
        </div>
        <div class="stat-chip">
          <strong>100%</strong>
          <span>Data Density</span>
        </div>
      </div>
    </div>

    <!-- Chapter Navigation Filter Bar -->
    <div class="chapter-nav-bar">
      <button class="chapter-filter-btn active" onclick="filterChapter('all', this)"><i class="fa-solid fa-layer-group"></i> All Chapters (62)</button>
      <button class="chapter-filter-btn" onclick="filterChapter('17', this)"><i class="fa-solid fa-scalpel"></i> Ch 17: Surgery (29)</button>
      <button class="chapter-filter-btn" onclick="filterChapter('18', this)"><i class="fa-solid fa-eye"></i> Ch 18: Ophthalmology (12)</button>
      <button class="chapter-filter-btn" onclick="filterChapter('19', this)"><i class="fa-solid fa-head-side-cough"></i> Ch 19: ENT (12)</button>
      <button class="chapter-filter-btn" onclick="filterChapter('23', this)"><i class="fa-solid fa-truck-medical"></i> Ch 23: Emergency (9)</button>
    </div>

    <!-- Live Search Input -->
    <div class="search-box-wrapper">
      <i class="fa-solid fa-magnifying-glass search-icon"></i>
      <input type="text" id="live-search" class="search-input" placeholder="Search across all 62 clinical notes by topic, symptom, sign, drug (Rocephin, Flagyl, Diamox...), or guideline...">
    </div>

    <!-- Cards Section -->
    <div id="cards-container">
{all_cards_str}
    </div>

    <!-- Roadmap of Full Book Chapters -->
    <div class="roadmap-section">
      <h3 style="font-size:16px; font-weight:800; display:flex; align-items:center; gap:8px;">
        <i class="fa-solid fa-map-location-dot" style="color:var(--teal);"></i> Doctor on Duty Master System Roadmap
      </h3>
      <p style="font-size:13px; color:var(--text-muted); margin-top:4px;">
        Full system-by-system chapters of Doctor on Duty (3rd Edition, 695 pages):
      </p>
      <div class="roadmap-grid">
        <div class="roadmap-item" style="border-left:3px solid var(--emerald);">
          <strong>Ch 17: General Surgery</strong>
          <span>29 Notes &bull; Complete &bull; pp. 409–444</span>
        </div>
        <div class="roadmap-item" style="border-left:3px solid var(--emerald);">
          <strong>Ch 18: Ophthalmology</strong>
          <span>12 Notes &bull; Complete &bull; pp. 445–458</span>
        </div>
        <div class="roadmap-item" style="border-left:3px solid var(--emerald);">
          <strong>Ch 19: ENT (Otolaryngology)</strong>
          <span>12 Notes &bull; Complete &bull; pp. 459–482</span>
        </div>
        <div class="roadmap-item" style="border-left:3px solid var(--emerald);">
          <strong>Ch 23: Emergency & Poisoning</strong>
          <span>9 Notes &bull; Complete &bull; pp. 673–712</span>
        </div>
        <div class="roadmap-item">
          <strong>Ch 05: Infectious Diseases</strong>
          <span>Malaria, Dengue, Typhoid &bull; pp. 64–96</span>
        </div>
        <div class="roadmap-item">
          <strong>Ch 06: Pulmonology</strong>
          <span>Pneumonia, Asthma, COPD &bull; pp. 97–127</span>
        </div>
        <div class="roadmap-item">
          <strong>Ch 07: Cardiology (CVS)</strong>
          <span>HTN, ACS, Heart Failure &bull; pp. 128–174</span>
        </div>
        <div class="roadmap-item">
          <strong>Ch 08: Gastroenterology</strong>
          <span>PUD, IBD, Cirrhosis &bull; pp. 175–224</span>
        </div>
        <div class="roadmap-item">
          <strong>Ch 10: Endocrinology</strong>
          <span>DKA, HHS, Diabetes OPD &bull; pp. 225–259</span>
        </div>
        <div class="roadmap-item">
          <strong>Ch 11: Nephrology & Urology</strong>
          <span>AKI, CKD, Stones, BPH &bull; pp. 260–303</span>
        </div>
        <div class="roadmap-item">
          <strong>Ch 13: Rheumatology</strong>
          <span>RA, SLE, Gout &bull; pp. 304–338</span>
        </div>
        <div class="roadmap-item">
          <strong>Ch 14: Neurology</strong>
          <span>Stroke, Meningitis, Epilepsy &bull; pp. 339–363</span>
        </div>
        <div class="roadmap-item">
          <strong>Ch 15: Psychiatry</strong>
          <span>Depression, Psychosis &bull; pp. 364–384</span>
        </div>
        <div class="roadmap-item">
          <strong>Ch 16: Dermatology</strong>
          <span>Eczema, Psoriasis, Scabies &bull; pp. 385–408</span>
        </div>
        <div class="roadmap-item">
          <strong>Ch 20: Spine & Orthopedics</strong>
          <span>Radiculopathy, Fractures &bull; pp. 483–515</span>
        </div>
        <div class="roadmap-item">
          <strong>Ch 21: Gynaecology & Obs</strong>
          <span>Ectopic, PPH, Eclampsia &bull; pp. 516–593</span>
        </div>
        <div class="roadmap-item">
          <strong>Ch 22: Pediatrics</strong>
          <span>APGAR, WHO Fluids, Croup &bull; pp. 594–672</span>
        </div>
        <div class="roadmap-item">
          <strong>Ch 24: Drug Formularies</strong>
          <span>Pakistani Adult Dosages &bull; pp. 752–767</span>
        </div>
      </div>
    </div>

  </main>

  <script>
{SHARED_JS}

// Chapter Filtering
function filterChapter(ch, btn) {{
  document.querySelectorAll('.chapter-filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  
  const blocks = document.querySelectorAll('.chapter-block');
  blocks.forEach(block => {{
    if (ch === 'all' || block.dataset.chapter === ch) {{
      block.style.display = 'block';
    }} else {{
      block.style.display = 'none';
    }}
  }});
}}

// Live Real-Time Search
document.getElementById('live-search').addEventListener('input', (e) => {{
  const query = e.target.value.toLowerCase().trim();
  const cards = document.querySelectorAll('.topic-card');
  const blocks = document.querySelectorAll('.chapter-block');
  
  if (!query) {{
    cards.forEach(c => c.style.display = 'flex');
    blocks.forEach(b => b.style.display = 'block');
    return;
  }}
  
  blocks.forEach(block => {{
    let visibleInBlock = 0;
    const blockCards = block.querySelectorAll('.topic-card');
    blockCards.forEach(card => {{
      const title = card.dataset.title || '';
      const summary = card.dataset.summary || '';
      if (title.includes(query) || summary.includes(query)) {{
        card.style.display = 'flex';
        visibleInBlock++;
      }} else {{
        card.style.display = 'none';
      }}
    }});
    block.style.display = visibleInBlock > 0 ? 'block' : 'none';
  }});
}});
  </script>
</body>
</html>
"""
    dest_path = os.path.join(REPO_DIR, "index.html")
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(portal_html.strip())
    print(f"Generated Master Portal: index.html ({os.path.getsize(dest_path)} bytes)")

if __name__ == '__main__':
    print(f"Building {len(ALL_TOPICS)} standalone notes across 4 major chapters...")
    for t in ALL_TOPICS:
        generate_page(t)
    print("\nBuilding Master Index Portal...")
    build_master_portal()
    print("\nComplete! All 62 topics and portal generated successfully.")
