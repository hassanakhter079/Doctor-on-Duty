# -*- coding: utf-8 -*-
"""
Build Doctor on Duty Chapter Single-Page HTML Notes
Generates:
  - chapter-17-general-surgery.html
  - chapter-18-ophthalmology.html
  - chapter-19-ent.html
  - chapter-23-emergency-medicine.html
  - surgery.html, ophthalmology.html, ent.html, emergency.html (friendly aliases)
  - index.html (Master Chapter Directory & Global Topic Search Portal)
"""
import sys, os, re, json, shutil

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

for t in T18:
    t["chapter_num"] = 18
    t["chapter_name"] = "Ophthalmology"

for t in T19:
    t["chapter_num"] = 19
    t["chapter_name"] = "Ear, Nose & Throat (ENT)"

for t in T23:
    t["chapter_num"] = 23
    t["chapter_name"] = "Emergency Medicine & Poisoning"

REPO_DIR = '/root/doctor-on-duty'

# Image metadata mapping
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

CHAPTER_DEFINITIONS = [
    {
        "num": 17,
        "name": "General Surgery",
        "slug": "chapter-17-general-surgery.html",
        "alias": "surgery.html",
        "icon": "fa-scalpel",
        "color": "#14b8a6",
        "page_span": "pp. 409–444",
        "topics": CH17_TOPICS,
        "desc": "Acute abdomen algorithms, Tokyo Guidelines (TG18), biliary sepsis, pancreatitis Atlanta criteria, anorectal pathology, chronic pressure ulcers, soft tissue surgery, and digital pulp whitlows."
    },
    {
        "num": 18,
        "name": "Ophthalmology",
        "slug": "chapter-18-ophthalmology.html",
        "alias": "ophthalmology.html",
        "icon": "fa-eye",
        "color": "#3b82f6",
        "page_span": "pp. 445–458",
        "topics": T18,
        "desc": "Red eye differential, infectious and allergic conjunctivitis, corneal abrasions and rust rings, ocular chemical emergencies, acute angle-closure glaucoma decompression, anterior uveitis, and ophthalmic formulary."
    },
    {
        "num": 19,
        "name": "Ear, Nose & Throat (ENT)",
        "slug": "chapter-19-ent.html",
        "alias": "ent.html",
        "icon": "fa-head-side-cough",
        "color": "#f59e0b",
        "page_span": "pp. 459–482",
        "topics": T19,
        "desc": "Chronic rhinosinusitis EPOS criteria, deviated septum, anterior & posterior epistaxis packing, tonsillitis Centor score, quinsy drainage, AOM, CSOM safe vs unsafe cholesteatoma, otomycosis, BPPV Epley, and Bell's palsy."
    },
    {
        "num": 23,
        "name": "Emergency Medicine & Poisoning",
        "slug": "chapter-23-emergency-medicine.html",
        "alias": "emergency.html",
        "icon": "fa-truck-medical",
        "color": "#f43f5e",
        "page_span": "pp. 673–712",
        "topics": T23,
        "desc": "ACLS 2023 resuscitation protocols, anaphylaxis adrenaline dosing, Surviving Sepsis Hour-1 bundle, organophosphate atropinization endpoints, paracetamol NAC 3-bag protocol, snakebite ASV, Parkland burn fluid, toxidromes, and WHO pain ladder."
    }
]

CSS_STYLES = """
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
  
  --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --font-serif: 'Fraunces', Georgia, serif;
}

[data-theme="light"] {
  --bg-body: #f8fafc;
  --bg-card: #ffffff;
  --bg-card-subtle: #f1f5f9;
  --bg-elevated: #e2e8f0;
  --border: #cbd5e1;
  --border-subtle: #e2e8f0;
  
  --text-main: #0f172a;
  --text-muted: #475569;
  --text-dim: #64748b;
  
  --teal: #0d9488;
  --teal-light: #0f766e;
  --teal-glow: rgba(13, 148, 136, 0.12);
  
  --blue: #2563eb;
  --blue-light: #1d4ed8;
  --blue-glow: rgba(37, 99, 235, 0.12);
  
  --amber: #d97706;
  --amber-light: #b45309;
  --amber-glow: rgba(217, 119, 6, 0.12);
  
  --rose: #e11d48;
  --rose-light: #be123c;
  --rose-glow: rgba(225, 29, 72, 0.12);
  
  --emerald: #059669;
  --emerald-light: #047857;
  --emerald-glow: rgba(5, 150, 105, 0.12);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html {
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-sans);
  background: var(--bg-body);
  color: var(--text-main);
  line-height: 1.5;
  font-size: 14.5px;
  -webkit-font-smoothing: antialiased;
}

/* ── STICKY CLINICAL NAVBAR ── */
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
  width: 34px;
  height: 34px;
  background: linear-gradient(135deg, var(--teal), var(--blue));
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 16px;
  font-weight: 800;
}

.brand-text h1 {
  font-size: 14px;
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

.chapter-switcher {
  background: var(--bg-card-subtle);
  border: 1px solid var(--border);
  color: var(--text-main);
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 600;
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

.sidebar-toggle-btn {
  display: none;
  align-items: center;
  justify-content: center;
  width: 34px;
  height: 34px;
  border-radius: 6px;
  border: 1px solid var(--border);
  background: var(--bg-card-subtle);
  color: var(--text-main);
  cursor: pointer;
  font-size: 15px;
}

/* ── LAYOUT: SIDEBAR + CONTENT ── */
.layout-wrapper {
  display: flex;
  min-height: calc(100vh - 51px);
}

.sidebar-drawer {
  width: 320px;
  background: var(--bg-card);
  border-right: 1px solid var(--border);
  height: calc(100vh - 51px);
  position: sticky;
  top: 51px;
  overflow-y: auto;
  padding: 16px;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.sidebar-search-box {
  position: sticky;
  top: 0;
  background: var(--bg-card);
  padding-bottom: 8px;
  z-index: 10;
  border-bottom: 1px solid var(--border-subtle);
}

.sidebar-search-input {
  width: 100%;
  padding: 8px 12px 8px 32px;
  border-radius: 6px;
  border: 1px solid var(--border);
  background: var(--bg-card-subtle);
  color: var(--text-main);
  font-size: 13px;
  outline: none;
}

.sidebar-search-input:focus {
  border-color: var(--teal);
}

.sidebar-search-icon {
  position: absolute;
  left: 10px;
  top: 9px;
  color: var(--text-muted);
  font-size: 13px;
}

.sidebar-topic-list {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.sidebar-topic-link {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  padding: 8px 10px;
  border-radius: 6px;
  text-decoration: none;
  color: var(--text-muted);
  font-size: 12.5px;
  line-height: 1.35;
  border-left: 3px solid transparent;
  transition: all 0.15s ease;
}

.sidebar-topic-link:hover {
  background: var(--bg-card-subtle);
  color: var(--text-main);
}

.sidebar-topic-link.active {
  background: var(--teal-glow);
  color: var(--teal-light);
  border-left-color: var(--teal);
  font-weight: 700;
}

.sidebar-topic-num {
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 700;
  color: var(--teal);
  background: var(--bg-elevated);
  padding: 2px 6px;
  border-radius: 4px;
  flex-shrink: 0;
}

.content-area {
  flex: 1;
  padding: 24px 28px 60px 28px;
  max-width: 1300px;
  overflow-x: hidden;
}

/* ── CHAPTER HERO BANNER ── */
.chapter-hero {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px 24px;
  margin-bottom: 24px;
  position: relative;
  overflow: hidden;
}

.chapter-hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 6px;
  height: 100%;
  background: linear-gradient(180deg, var(--teal), var(--blue));
}

.chapter-hero-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
  flex-wrap: wrap;
}

.chapter-hero h2 {
  font-size: 26px;
  font-weight: 800;
  letter-spacing: -0.5px;
  margin-bottom: 8px;
}

.chapter-hero p {
  color: var(--text-muted);
  font-size: 14px;
  max-width: 900px;
}

/* ── INDIVIDUAL TOPIC CARD ── */
.topic-section {
  scroll-margin-top: 70px;
  margin-bottom: 40px;
  border-bottom: 1px solid var(--border);
  padding-bottom: 32px;
}

.topic-section:last-child {
  border-bottom: none;
}

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
}

/* Two-Column Ultra-Condensed Clinical Grid */
.condensed-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 16px;
  align-items: start;
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
  cursor: pointer;
  transition: transform 0.2s ease;
}

.media-container:hover {
  transform: translateY(-2px);
  border-color: var(--teal);
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
  border-top: 1px solid var(--border-subtle);
}

.media-caption strong {
  color: var(--text-main);
  display: block;
  margin-bottom: 2px;
}

/* Clinical Callout Boxes */
.callout {
  padding: 12px 14px;
  border-radius: 8px;
  font-size: 13px;
  line-height: 1.45;
  margin-bottom: 12px;
  border-left: 4px solid;
}

.callout:last-child { margin-bottom: 0; }
.callout-emergency { background: var(--rose-glow); border-color: var(--rose); color: var(--rose-light); }
.callout-urgent { background: var(--amber-glow); border-color: var(--amber); color: var(--amber-light); }
.callout-pearl { background: var(--teal-glow); border-color: var(--teal); color: var(--teal-light); }
.callout-info { background: var(--blue-glow); border-color: var(--blue); color: var(--blue-light); }

.callout-header {
  display: flex;
  align-items: center;
  gap: 6px;
  font-weight: 700;
  margin-bottom: 4px;
  font-size: 13px;
}

/* Clinical Lists & Steps */
.clinical-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.clinical-list li {
  position: relative;
  padding-left: 18px;
  font-size: 13.5px;
}

.clinical-list li::before {
  content: '•';
  position: absolute;
  left: 4px;
  color: var(--teal);
  font-weight: bold;
}

/* Treatment Tables & Brand Rx */
.rx-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 12.5px;
  margin-top: 8px;
}

.rx-table th, .rx-table td {
  padding: 8px 10px;
  text-align: left;
  border-bottom: 1px solid var(--border-subtle);
}

.rx-table th {
  background: var(--bg-card-subtle);
  color: var(--text-muted);
  font-weight: 700;
  text-transform: uppercase;
  font-size: 11px;
  letter-spacing: 0.5px;
}

.brand-pill {
  display: inline-block;
  padding: 2px 6px;
  border-radius: 4px;
  background: var(--teal-glow);
  color: var(--teal-light);
  font-weight: 600;
  font-size: 11.5px;
}

/* Interactive Calculators */
.calc-box {
  background: var(--bg-card-subtle);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 12px;
}

.calc-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 6px 0;
  border-bottom: 1px dashed var(--border-subtle);
  font-size: 12.5px;
}

.calc-row label {
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
}

.calc-score-display {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 10px;
  padding-top: 8px;
  border-top: 2px solid var(--border);
  font-weight: 700;
  font-size: 14px;
}

.score-num {
  font-family: var(--font-mono);
  font-size: 16px;
  color: var(--teal-light);
  background: var(--bg-elevated);
  padding: 2px 8px;
  border-radius: 4px;
}

.steps-grid {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.step-card {
  display: flex;
  gap: 10px;
  background: var(--bg-card-subtle);
  padding: 8px 10px;
  border-radius: 6px;
  font-size: 12.5px;
  align-items: flex-start;
}

.step-num {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: var(--teal);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 11px;
  flex-shrink: 0;
}

/* Modal Lightbox */
.lightbox-modal {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(8px);
  z-index: 9999;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.lightbox-modal.active { display: flex; }

.lightbox-content {
  max-width: 900px;
  max-height: 90vh;
  background: var(--bg-card);
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  position: relative;
}

.lightbox-content img {
  width: 100%;
  max-height: 70vh;
  object-fit: contain;
  background: #000;
}

.lightbox-caption {
  padding: 14px 18px;
  font-size: 13px;
  color: var(--text-muted);
}

.lightbox-close {
  position: absolute;
  top: 10px;
  right: 12px;
  background: rgba(0,0,0,0.6);
  border: none;
  color: #fff;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  cursor: pointer;
  font-size: 16px;
}

/* Back to top */
#topBtn {
  position: fixed;
  bottom: 24px;
  right: 24px;
  width: 42px;
  height: 42px;
  border-radius: 50%;
  background: var(--teal);
  color: #fff;
  border: none;
  cursor: pointer;
  display: none;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.3);
  z-index: 100;
  transition: all 0.2s;
}

#topBtn:hover { transform: translateY(-3px); }

/* Backdrop for Mobile Sidebar */
.sidebar-backdrop {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.5);
  backdrop-filter: blur(4px);
  z-index: 1500;
}

/* Responsive adjustments */
@media (max-width: 1024px) {
  .condensed-grid { grid-template-columns: 1fr; }
  .sidebar-toggle-btn { display: flex; }
  .sidebar-drawer {
    position: fixed;
    left: -330px;
    top: 0;
    height: 100vh;
    z-index: 2000;
    transition: left 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 4px 0 24px rgba(0,0,0,0.3);
  }
  .sidebar-drawer.open {
    left: 0;
  }
  .sidebar-backdrop.active {
    display: block;
  }
  .content-area {
    padding: 16px;
  }
  .chapter-switcher {
    max-width: 150px;
  }
}
"""

def render_topic_html(topic):
    num = topic["num"]
    img_meta = IMAGE_METADATA.get(num, {})
    
    badge_cls = "badge-routine"
    if topic["badge"].lower() == "emergency": badge_cls = "badge-emergency"
    elif topic["badge"].lower() == "urgent": badge_cls = "badge-urgent"

    right_extras = []
    
    # 1. Main Clinical Photo
    if img_meta and img_meta.get("img"):
        img_path = img_meta["img"]
        caption = img_meta.get("caption", "")
        img_title = img_meta.get("title", "")
        right_extras.append(f"""
        <div class="card">
          <div class="card-header">
            <span class="card-title"><i class="fa-solid fa-camera"></i> Diagnostic / Clinical Imaging</span>
          </div>
          <div class="media-container" onclick="openLightbox('{img_path}', '{img_title}: {caption}')">
            <img src="{img_path}" alt="{img_title}" loading="lazy">
            <div class="media-caption">
              <strong>{img_title}</strong>
              {caption}
            </div>
          </div>
        </div>
        """)

    # 2. Extra Vector SVG or Panel if available
    if img_meta and img_meta.get("extra_svg"):
        extra_path = img_meta["extra_svg"]
        extra_title = img_meta.get("extra_title", "Clinical Reference Anatomy & Criteria")
        right_extras.append(f"""
        <div class="card">
          <div class="card-header">
            <span class="card-title"><i class="fa-solid fa-diagram-project"></i> {extra_title}</span>
          </div>
          <div class="media-container" onclick="openLightbox('{extra_path}', '{extra_title}')">
            <img src="{extra_path}" alt="{extra_title}" loading="lazy">
          </div>
        </div>
        """)
        
    # 3. Interactive calculators for specific conditions
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
          let tot = document.getElementById('alv-total');
          if (tot) tot.innerText = pts + ' / 10';
          let el = document.getElementById('alv-risk');
          if (el) {
            if (pts <= 4) { el.innerText = 'Score 1-4: Low risk (Appendicitis unlikely). Observation/Discharge.'; el.style.color = 'var(--emerald-light)'; }
            else if (pts <= 6) { el.innerText = 'Score 5-6: Intermediate / Compatible. CT scan / Ultrasound mandatory.'; el.style.color = 'var(--amber-light)'; }
            else { el.innerText = 'Score 7-10: High probability. Surgical consult & Appendectomy indicated.'; el.style.color = 'var(--rose-light)'; }
          }
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
            <div class="step-card"><span class="step-num">1</span> <div><strong>Acetazolamide (Diamox):</strong> 500 mg IV stat, then 250 mg PO TDS.</div></div>
            <div class="step-card"><span class="step-num">2</span> <div><strong>Topical Beta-Blocker:</strong> Timolol 0.5% 1 drop stat.</div></div>
            <div class="step-card"><span class="step-num">3</span> <div><strong>Alpha-2 Agonist:</strong> Apraclonidine 1% / Brimonidine 0.2% 1 drop.</div></div>
            <div class="step-card"><span class="step-num">4</span> <div><strong>Miotic:</strong> Pilocarpine 2% 1 drop q15min (when IOP &lt; 35 mmHg).</div></div>
            <div class="step-card"><span class="step-num">5</span> <div><strong>Mannitol 20%:</strong> 1-2 g/kg IV over 45 min if IOP refractory.</div></div>
            <div class="step-card"><span class="step-num">6</span> <div><strong>Curative:</strong> Bilateral Nd:YAG Laser Peripheral Iridotomy.</div></div>
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
          let sel = document.getElementById('cnt-age');
          let pts = sel ? parseInt(sel.value) : 0;
          document.querySelectorAll('.cnt-cb:checked').forEach(c => pts += parseInt(c.dataset.pts));
          let tot = document.getElementById('cnt-total');
          if (tot) tot.innerText = pts;
          let el = document.getElementById('cnt-plan');
          if (el) {
            if (pts <= 1) { el.innerText = 'Score ≤ 1: GABHS risk < 10%. Symptomatic analgesia only; no antibiotics.'; el.style.color = 'var(--emerald-light)'; }
            else if (pts <= 3) { el.innerText = 'Score 2-3: GABHS risk 15-30%. Throat swab / RADT; treat if positive.'; el.style.color = 'var(--amber-light)'; }
            else { el.innerText = 'Score ≥ 4: GABHS risk > 50%. Empiric Penicillin V 500mg TDS x 10 days.'; el.style.color = 'var(--rose-light)'; }
          }
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
            <div class="calc-row" style="margin-top:6px;">
              <span>First 8 Hours Rate (50%):</span>
              <strong id="burn-rate-8" style="color:var(--rose-light);">438 mL/hr</strong>
            </div>
            <div class="calc-row">
              <span>Next 16 Hours Rate (50%):</span>
              <strong id="burn-rate-16" style="color:var(--teal-light);">219 mL/hr</strong>
            </div>
            <div style="margin-top:8px; font-size:11.5px; color:var(--text-muted);">Goal urine output: 0.5–1.0 mL/kg/hr. Titrate to hemodynamics.</div>
          </div>
        </div>
        <script>
        function calcBurn() {
          let wt = parseFloat(document.getElementById('burn-wt').value) || 0;
          let tbsa = parseFloat(document.getElementById('burn-tbsa').value) || 0;
          let tot = 4 * wt * tbsa;
          let r8 = (tot / 2) / 8;
          let r16 = (tot / 2) / 16;
          let bt = document.getElementById('burn-total');
          let b8 = document.getElementById('burn-rate-8');
          let b16 = document.getElementById('burn-rate-16');
          if (bt) bt.innerText = Math.round(tot).toLocaleString() + ' mL';
          if (b8) b8.innerText = Math.round(r8) + ' mL/hr';
          if (b16) b16.innerText = Math.round(r16) + ' mL/hr';
        }
        </script>
        """)

    extras_html = "".join(right_extras)
    
    # Topic Card Section
    return f"""
    <section class="topic-section" id="topic-{num}">
      <div class="topic-banner">
        <div class="banner-meta">
          <span class="badge badge-page"><i class="fa-solid fa-book-open"></i> {topic['book_page']}</span>
          <span class="badge {badge_cls}"><i class="fa-solid fa-circle-exclamation"></i> {topic['badge']}</span>
          <span class="badge badge-category"><i class="fa-solid fa-folder"></i> {topic.get('category_name', topic['category'])}</span>
          <span class="badge badge-page"><i class="fa-solid fa-hashtag"></i> Topic {num}</span>
        </div>
        <h3 class="topic-title">{topic['title']}</h3>
        <p class="topic-summary">{topic['summary']}</p>
      </div>

      <div class="condensed-grid">
        <div class="column">
          {topic['content']}
        </div>
        <div class="column">
          {extras_html}
        </div>
      </div>
    </section>
    """

def build_chapter_page(chap_def):
    c_num = chap_def["num"]
    c_name = chap_def["name"]
    c_slug = chap_def["slug"]
    c_icon = chap_def["icon"]
    c_page_span = chap_def["page_span"]
    c_desc = chap_def["desc"]
    topics = chap_def["topics"]
    
    # Build Sidebar links
    sidebar_links = []
    for t in topics:
        sidebar_links.append(f"""
        <a href="#topic-{t['num']}" class="sidebar-topic-link" data-topic-id="topic-{t['num']}">
          <span class="sidebar-topic-num">{t['num']}</span>
          <span>{t['title']}</span>
        </a>
        """)
    sidebar_links_html = "".join(sidebar_links)
    
    # Build Chapter Switcher Dropdown options
    switcher_options = []
    for other_chap in CHAPTER_DEFINITIONS:
        sel = "selected" if other_chap["num"] == c_num else ""
        switcher_options.append(f'<option value="{other_chap["slug"]}" {sel}>Ch {other_chap["num"]}: {other_chap["name"]} ({len(other_chap["topics"])})</option>')
    switcher_options.append('<option value="index.html">🏠 Master Portal</option>')
    switcher_html = "".join(switcher_options)
    
    # Build All Topic Sections
    topic_sections = []
    for t in topics:
        topic_sections.append(render_topic_html(t))
    topic_sections_html = "".join(topic_sections)

    full_html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter {c_num}: {c_name} ({len(topics)} Topics) | Doctor on Duty</title>
  
  <!-- Universal HTML Cloud Sync -->
  <script src="https://hassanakhter079.github.io/After-Salah-Zikr/cloud-sync.js" data-app="doctor-on-duty"></script>

  <!-- Typography & Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Fraunces:opsz,wght@9..144,600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <style>
{CSS_STYLES}
  </style>
</head>
<body>

  <!-- Backdrop for mobile drawer -->
  <div class="sidebar-backdrop" id="sidebarBackdrop" onclick="toggleSidebar()"></div>

  <!-- Top Sticky Navigation -->
  <nav class="top-navbar">
    <div style="display:flex; align-items:center; gap:10px;">
      <button class="sidebar-toggle-btn" onclick="toggleSidebar()" title="Toggle Topic Directory">
        <i class="fa-solid fa-bars"></i>
      </button>
      <a href="index.html" class="brand-section">
        <div class="brand-logo"><i class="fa-solid {c_icon}"></i></div>
        <div class="brand-text">
          <h1>Doctor on Duty</h1>
          <span>Ch {c_num}: {c_name}</span>
        </div>
      </a>
    </div>

    <div class="nav-actions">
      <select class="chapter-switcher" onchange="location.href=this.value">
        {switcher_html}
      </select>

      <a href="index.html" class="nav-btn"><i class="fa-solid fa-house"></i> Portal</a>
      <button class="nav-btn" onclick="toggleTheme()" id="themeBtn"><i class="fa-solid fa-moon"></i></button>
    </div>
  </nav>

  <!-- Main Layout -->
  <div class="layout-wrapper">
    <!-- Sidebar Topic Drawer -->
    <aside class="sidebar-drawer" id="sidebarDrawer">
      <div class="sidebar-search-box">
        <i class="fa-solid fa-magnifying-glass sidebar-search-icon"></i>
        <input type="text" class="sidebar-search-input" id="sidebarSearch" placeholder="Filter this chapter..." oninput="filterSidebarTopics()">
      </div>
      <div style="font-size:11px; font-weight:700; text-transform:uppercase; color:var(--text-dim); padding:4px 6px; letter-spacing:0.5px;">
        Chapter Topics ({len(topics)})
      </div>
      <div class="sidebar-topic-list" id="sidebarTopicList">
        {sidebar_links_html}
      </div>
    </aside>

    <!-- Content Area -->
    <main class="content-area">
      <!-- Chapter Hero Banner -->
      <div class="chapter-hero">
        <div class="chapter-hero-meta">
          <span class="badge badge-emergency"><i class="fa-solid {c_icon}"></i> Chapter {c_num}</span>
          <span class="badge badge-page"><i class="fa-solid fa-book-bookmark"></i> {c_page_span}</span>
          <span class="badge badge-category"><i class="fa-solid fa-list-check"></i> {len(topics)} Clinical Topics</span>
          <span class="badge badge-routine"><i class="fa-solid fa-shield-halved"></i> Pakistani Brand Rx</span>
        </div>
        <h2>{c_name}</h2>
        <p>{c_desc}</p>
      </div>

      <!-- Topics Content List -->
      <div id="topicsContainer">
        {topic_sections_html}
      </div>
    </main>
  </div>

  <!-- Lightbox Modal -->
  <div class="lightbox-modal" id="lightboxModal" onclick="closeLightbox(event)">
    <div class="lightbox-content" onclick="event.stopPropagation()">
      <button class="lightbox-close" onclick="closeLightbox()">&times;</button>
      <img id="lightboxImg" src="" alt="Clinical Preview">
      <div class="lightbox-caption" id="lightboxCaption"></div>
    </div>
  </div>

  <!-- Back to Top Button -->
  <button id="topBtn" onclick="window.scrollTo({{top:0, behavior:'smooth'}})" title="Back to top">
    <i class="fa-solid fa-arrow-up"></i>
  </button>

  <script>
    // Theme Management
    function initTheme() {{
      const saved = localStorage.getItem('dod_theme') || 'dark';
      document.documentElement.setAttribute('data-theme', saved);
      updateThemeIcon(saved);
    }}

    function toggleTheme() {{
      const curr = document.documentElement.getAttribute('data-theme');
      const next = curr === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('dod_theme', next);
      updateThemeIcon(next);
    }}

    function updateThemeIcon(t) {{
      const btn = document.getElementById('themeBtn');
      if (btn) btn.innerHTML = t === 'dark' ? '<i class="fa-solid fa-sun"></i>' : '<i class="fa-solid fa-moon"></i>';
    }}

    // Mobile Sidebar Drawer
    function toggleSidebar() {{
      const drawer = document.getElementById('sidebarDrawer');
      const backdrop = document.getElementById('sidebarBackdrop');
      if (drawer && backdrop) {{
        drawer.classList.toggle('open');
        backdrop.classList.toggle('active');
      }}
    }}

    // Filter topics within chapter sidebar
    function filterSidebarTopics() {{
      const q = document.getElementById('sidebarSearch').value.toLowerCase().trim();
      document.querySelectorAll('.sidebar-topic-link').forEach(link => {{
        const text = link.innerText.toLowerCase();
        link.style.display = text.includes(q) ? 'flex' : 'none';
      }});
    }}

    // Lightbox modal
    function openLightbox(src, caption) {{
      const modal = document.getElementById('lightboxModal');
      const img = document.getElementById('lightboxImg');
      const cap = document.getElementById('lightboxCaption');
      if (modal && img) {{
        img.src = src;
        cap.innerText = caption || '';
        modal.classList.add('active');
      }}
    }}

    function closeLightbox() {{
      const modal = document.getElementById('lightboxModal');
      if (modal) modal.classList.remove('active');
    }}

    // ScrollSpy & Top Button
    window.addEventListener('scroll', () => {{
      const topBtn = document.getElementById('topBtn');
      if (topBtn) topBtn.style.display = window.scrollY > 400 ? 'flex' : 'none';

      const sections = document.querySelectorAll('.topic-section');
      let currentId = '';
      sections.forEach(s => {{
        const rect = s.getBoundingClientRect();
        if (rect.top <= 120 && rect.bottom >= 120) {{
          currentId = s.id;
        }}
      }});

      if (currentId) {{
        document.querySelectorAll('.sidebar-topic-link').forEach(l => {{
          l.classList.toggle('active', l.getAttribute('href') === '#' + currentId);
        }});
      }}
    }});

    // Close mobile drawer when clicking a topic link
    document.querySelectorAll('.sidebar-topic-link').forEach(link => {{
      link.addEventListener('click', () => {{
        if (window.innerWidth <= 1024) toggleSidebar();
      }});
    }});

    initTheme();
  </script>
</body>
</html>
"""
    return full_html

def build_master_index():
    total_topics = sum(len(c["topics"]) for c in CHAPTER_DEFINITIONS)
    
    chapter_cards = []
    for c in CHAPTER_DEFINITIONS:
        # Previews of first 4 topics
        topic_previews = []
        for t in c["topics"][:4]:
            topic_previews.append(f"""
            <div style="font-size:12.5px; padding:4px 0; border-bottom:1px dashed var(--border-subtle); display:flex; gap:6px; align-items:center;">
              <span style="font-family:var(--font-mono); font-size:10.5px; color:var(--teal); background:var(--bg-elevated); padding:1px 5px; border-radius:3px;">{t['num']}</span>
              <span style="color:var(--text-main); white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">{t['title']}</span>
            </div>
            """)
        if len(c["topics"]) > 4:
            topic_previews.append(f"""
            <div style="font-size:11.5px; color:var(--teal-light); padding-top:6px; font-weight:600;">
              + {len(c["topics"]) - 4} more topics in this chapter...
            </div>
            """)
        preview_html = "".join(topic_previews)

        chapter_cards.append(f"""
        <div class="chap-card" onclick="location.href='{c['slug']}'">
          <div class="chap-card-top">
            <div class="chap-icon-box" style="background:{c['color']}22; color:{c['color']}; border:1px solid {c['color']};">
              <i class="fa-solid {c['icon']}"></i>
            </div>
            <div>
              <span class="badge badge-emergency" style="background:{c['color']}22; color:{c['color']}; border-color:{c['color']};">Chapter {c['num']}</span>
              <h3 style="font-size:18px; font-weight:800; margin-top:4px;">{c['name']}</h3>
            </div>
          </div>
          
          <p style="font-size:13px; color:var(--text-muted); margin:12px 0 14px 0; line-height:1.45;">
            {c['desc']}
          </p>

          <div style="background:var(--bg-card-subtle); padding:10px 12px; border-radius:8px; border:1px solid var(--border-subtle); margin-bottom:14px;">
            <div style="font-size:11px; font-weight:700; text-transform:uppercase; color:var(--text-dim); margin-bottom:4px;">Sample Topics Included</div>
            {preview_html}
          </div>

          <div style="display:flex; align-items:center; justify-content:space-between; padding-top:8px; border-top:1px solid var(--border-subtle);">
            <span style="font-size:12px; color:var(--text-muted);"><i class="fa-solid fa-book-open"></i> {c['page_span']}</span>
            <a href="{c['slug']}" class="nav-btn primary" style="font-size:12.5px; padding:6px 14px;">
              Open Chapter ({len(c['topics'])}) <i class="fa-solid fa-arrow-right"></i>
            </a>
          </div>
        </div>
        """)
        
    chapter_cards_html = "".join(chapter_cards)

    # Master Search JSON index of all 62 topics
    search_items = []
    for c in CHAPTER_DEFINITIONS:
        for t in c["topics"]:
            search_items.append({
                "num": t["num"],
                "title": t["title"],
                "chapter_num": c["num"],
                "chapter_name": c["name"],
                "url": f"{c['slug']}#topic-{t['num']}",
                "summary": t["summary"],
                "badge": t["badge"],
                "page": t["book_page"]
            })
    search_json = json.dumps(search_items)

    index_html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Doctor on Duty — System-Wise Clinical Notes Portal</title>
  
  <!-- Universal HTML Cloud Sync -->
  <script src="https://hassanakhter079.github.io/After-Salah-Zikr/cloud-sync.js" data-app="doctor-on-duty"></script>

  <!-- Typography & Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Fraunces:opsz,wght@9..144,600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <style>
{CSS_STYLES}

.portal-container {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 24px 20px 60px 20px;
}}

.portal-hero {{
  text-align: center;
  padding: 40px 20px 30px 20px;
}}

.hero-pill {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: var(--teal-glow);
  color: var(--teal-light);
  border: 1px solid var(--teal);
  padding: 6px 14px;
  border-radius: 9999px;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 16px;
}}

.portal-hero h1 {{
  font-size: 34px;
  font-weight: 800;
  letter-spacing: -0.8px;
  line-height: 1.2;
  margin-bottom: 12px;
}}

.portal-hero p {{
  font-size: 15px;
  color: var(--text-muted);
  max-width: 750px;
  margin: 0 auto 28px auto;
}}

.global-search-wrapper {{
  max-width: 650px;
  margin: 0 auto 40px auto;
  position: relative;
}}

.global-search-box {{
  display: flex;
  align-items: center;
  background: var(--bg-card);
  border: 2px solid var(--border);
  border-radius: 12px;
  padding: 10px 16px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.25);
  transition: all 0.2s ease;
}}

.global-search-box:focus-within {{
  border-color: var(--teal);
  box-shadow: 0 4px 24px var(--teal-glow);
}}

.global-search-box i {{
  color: var(--text-muted);
  font-size: 16px;
  margin-right: 12px;
}}

.global-search-input {{
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  color: var(--text-main);
  font-size: 15px;
  font-weight: 500;
}}

.search-results-popup {{
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 12px;
  margin-top: 8px;
  max-height: 400px;
  overflow-y: auto;
  box-shadow: 0 10px 30px rgba(0,0,0,0.4);
  z-index: 1000;
  display: none;
}}

.search-results-popup.active {{ display: block; }}

.search-result-item {{
  padding: 12px 16px;
  border-bottom: 1px solid var(--border-subtle);
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
  text-decoration: none;
  color: inherit;
  transition: background 0.15s;
}}

.search-result-item:hover {{
  background: var(--bg-card-subtle);
}}

.search-result-item:last-child {{ border-bottom: none; }}

.chap-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  gap: 20px;
  margin-top: 20px;
}}

.chap-card {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 20px;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}}

.chap-card:hover {{
  transform: translateY(-4px);
  border-color: var(--teal);
  box-shadow: 0 12px 28px rgba(0,0,0,0.3);
}}

.chap-card-top {{
  display: flex;
  align-items: center;
  gap: 14px;
}}

.chap-icon-box {{
  width: 48px;
  height: 48px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  flex-shrink: 0;
}}

.stats-bar {{
  display: flex;
  justify-content: center;
  gap: 24px;
  flex-wrap: wrap;
  margin-bottom: 30px;
}}

.stat-item {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  padding: 12px 20px;
  border-radius: 10px;
  text-align: center;
}}

.stat-num {{
  font-size: 22px;
  font-weight: 800;
  color: var(--teal-light);
  font-family: var(--font-mono);
}}

.stat-lbl {{
  font-size: 11.5px;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-top: 2px;
}}
  </style>
</head>
<body>

  <!-- Top Sticky Navigation -->
  <nav class="top-navbar">
    <a href="index.html" class="brand-section">
      <div class="brand-logo"><i class="fa-solid fa-stethoscope"></i></div>
      <div class="brand-text">
        <h1>Doctor on Duty</h1>
        <span>Chapter Directory & Portal</span>
      </div>
    </a>

    <div class="nav-actions">
      <button class="nav-btn" onclick="toggleTheme()" id="themeBtn"><i class="fa-solid fa-moon"></i> Theme</button>
    </div>
  </nav>

  <!-- Portal Container -->
  <div class="portal-container">
    <div class="portal-hero">
      <div class="hero-pill">
        <i class="fa-solid fa-book-medical"></i> Doctor on Duty (3rd Edition)
      </div>
      <h1>System-Wise Clinical Reference Chapters</h1>
      <p>
        Condensed, standalone clinical reference chapters. Each chapter is an independent, high-density HTML guide equipped with verified diagnostic algorithms, authentic Pakistani brand pharmacotherapy, and real clinical photos.
      </p>

      <!-- Global Search -->
      <div class="global-search-wrapper">
        <div class="global-search-box">
          <i class="fa-solid fa-magnifying-glass"></i>
          <input type="text" class="global-search-input" id="globalSearch" placeholder="Search across all 62 topics (e.g. Appendicitis, Glaucoma, Epistaxis, Burns, Rocephin)..." oninput="handleGlobalSearch()" autocomplete="off">
        </div>
        <div class="search-results-popup" id="searchResults"></div>
      </div>

      <!-- Quick Stats -->
      <div class="stats-bar">
        <div class="stat-item">
          <div class="stat-num">{total_topics}</div>
          <div class="stat-lbl">Clinical Topics</div>
        </div>
        <div class="stat-item">
          <div class="stat-num">4</div>
          <div class="stat-lbl">Completed Chapters</div>
        </div>
        <div class="stat-item">
          <div class="stat-num">62</div>
          <div class="stat-lbl">Real Clinical Images</div>
        </div>
        <div class="stat-item">
          <div class="stat-num">4</div>
          <div class="stat-lbl">Interactive Calculators</div>
        </div>
        <div class="stat-item">
          <div class="stat-num">100%</div>
          <div class="stat-lbl">Pakistani Brand Rx</div>
        </div>
      </div>
    </div>

    <!-- Chapter Cards Grid -->
    <h2 style="font-size:20px; font-weight:800; margin-bottom:16px; display:flex; align-items:center; gap:8px;">
      <i class="fa-solid fa-layer-group" style="color:var(--teal);"></i> Available Clinical Chapters
    </h2>
    <div class="chap-grid">
      {chapter_cards_html}
    </div>
  </div>

  <script>
    const TOPICS_INDEX = {search_json};

    function initTheme() {{
      const saved = localStorage.getItem('dod_theme') || 'dark';
      document.documentElement.setAttribute('data-theme', saved);
      updateThemeIcon(saved);
    }}

    function toggleTheme() {{
      const curr = document.documentElement.getAttribute('data-theme');
      const next = curr === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('dod_theme', next);
      updateThemeIcon(next);
    }}

    function updateThemeIcon(t) {{
      const btn = document.getElementById('themeBtn');
      if (btn) btn.innerHTML = t === 'dark' ? '<i class="fa-solid fa-sun"></i> Theme' : '<i class="fa-solid fa-moon"></i> Theme';
    }}

    function handleGlobalSearch() {{
      const input = document.getElementById('globalSearch');
      const box = document.getElementById('searchResults');
      const q = input.value.toLowerCase().trim();
      
      if (!q) {{
        box.classList.remove('active');
        box.innerHTML = '';
        return;
      }}

      const matches = TOPICS_INDEX.filter(t => 
        t.title.toLowerCase().includes(q) || 
        t.summary.toLowerCase().includes(q) ||
        t.chapter_name.toLowerCase().includes(q)
      );

      if (matches.length === 0) {{
        box.innerHTML = '<div style="padding:16px; text-align:center; color:var(--text-muted); font-size:13px;">No topics matched your search.</div>';
        box.classList.add('active');
        return;
      }}

      let html = '';
      matches.slice(0, 10).forEach(m => {{
        html += `
        <a href="${{m.url}}" class="search-result-item">
          <div>
            <div style="font-weight:700; font-size:13.5px; color:var(--text-main);">${{m.title}}</div>
            <div style="font-size:11.5px; color:var(--text-muted); margin-top:2px;">${{m.summary.substring(0, 85)}}...</div>
          </div>
          <div style="text-align:right; flex-shrink:0;">
            <span class="badge badge-category" style="font-size:10px;">Ch ${{m.chapter_num}}</span>
            <div style="font-size:10.5px; color:var(--text-dim); margin-top:3px;">Topic ${{m.num}}</div>
          </div>
        </a>
        `;
      }});

      box.innerHTML = html;
      box.classList.add('active');
    }}

    // Close search on click outside
    document.addEventListener('click', (e) => {{
      const wrapper = document.querySelector('.global-search-wrapper');
      if (wrapper && !wrapper.contains(e.target)) {{
        const box = document.getElementById('searchResults');
        if (box) box.classList.remove('active');
      }}
    }});

    initTheme();
  </script>
</body>
</html>
"""
    return index_html

def main():
    print("Building separate HTML files for separate chapters...")
    
    # 1. Generate Chapter HTML files
    for c in CHAPTER_DEFINITIONS:
        path = os.path.join(REPO_DIR, c["slug"])
        html = build_chapter_page(c)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated Chapter {c['num']}: {c['slug']} ({len(html)} bytes, {len(c['topics'])} topics)")
        
        # Copy to alias
        alias_path = os.path.join(REPO_DIR, c["alias"])
        shutil.copyfile(path, alias_path)
        print(f"  -> Friendly alias: {c['alias']}")

    # 2. Generate Master Portal index.html
    portal_html = build_master_index()
    index_path = os.path.join(REPO_DIR, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(portal_html)
    print(f"Generated Master Chapter Portal: index.html ({len(portal_html)} bytes)")

    # 3. Clean up loose individual subtopic HTML files
    print("Cleaning up old individual subtopic HTML files...")
    cleaned = 0
    for fname in os.listdir(REPO_DIR):
        if fname.endswith(".html"):
            # If it's a chapter file, alias, or index, keep it
            keep = False
            if fname == "index.html": keep = True
            for c in CHAPTER_DEFINITIONS:
                if fname == c["slug"] or fname == c["alias"]:
                    keep = True
                    break
            if not keep:
                file_to_remove = os.path.join(REPO_DIR, fname)
                os.remove(file_to_remove)
                cleaned += 1
    print(f"Removed {cleaned} loose subtopic HTML files.")

    # 4. Verify resulting files
    remaining_html = [f for f in os.listdir(REPO_DIR) if f.endswith(".html")]
    remaining_html.sort()
    print("Remaining HTML files in repository:")
    for r in remaining_html:
        size = os.path.getsize(os.path.join(REPO_DIR, r))
        print(f"  - {r} ({size:,} bytes)")

if __name__ == "__main__":
    main()
