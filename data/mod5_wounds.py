# -*- coding: utf-8 -*-
"""
Module 5: Chronic Wounds, Ulcers & Diabetic Surgery (Topics 19 - 20)
Doctor on Duty 3rd Edition — Chapter 17 (Book pp. 435-437)
"""

TOPICS = [
    {
        "id": "topic-19",
        "num": 19,
        "title": "Pressure Ulcer (Decubitus Ulcer / Bed Sore)",
        "category": "wounds-ulcers",
        "category_name": "Wounds & Ulcers",
        "badge": "Tissue Viability & Wound Care",
        "book_page": "pp. 435–436",
        "summary": "Pathogenesis (capillary occlusion pressure > 32 mmHg), neurological causes, anatomical predilection, NPUAP 4-stage classification, wound dressings, debridement modalities, vacuum-assisted closure (NPWT), and reconstructive flap surgery.",
        "content": """
<div class="clinical-section">
  <h4><i class="fa-solid fa-bed-pulse"></i> Definition, Incidence & Pathophysiology</h4>
  <p><strong>Definition:</strong> A localized area of cellular necrosis and ulceration of the skin and underlying soft tissues, typically over a bony prominence, resulting from prolonged unrelieved external pressure, friction, or shear forces. Also known as bed sores, decubitus ulcers, trophic ulcers, or pressure sores.</p>
  <p><strong>Incidence:</strong> Occurs in ~5% of all hospitalized patients; significantly higher in paraplegic/quadriplegic patients, ICU patients, and frail elderly individuals.</p>
  <p><strong>Mechanism:</strong> Sustained external pressure exceeds normal capillary occlusive arteriolar pressure (<strong>&gt; 30–32 mmHg</strong>) &rarr; microvascular collapse &rarr; cutaneous ischemia and tissue hypoxia &rarr; cellular death, tissue necrosis, and full-thickness ulceration.</p>
  <p><strong>Neurological & Systemic Predispositions:</strong> Paraplegia, spinal cord injury, spina bifida, syringomyelia, tabes dorsalis, peripheral neuropathy, diabetic sensory loss, leprosy, severe malnutrition (hypoalbuminemia), and fecal/urinary incontinence.</p>
  <p><strong>Most Common Anatomical Sites (in Order of Frequency):</strong></p>
  <div class="pill-cloud">
    <span class="pill-item">1. Ischial Tuberosity (Sitting)</span>
    <span class="pill-item">2. Greater Trochanter (Lateral recumbent)</span>
    <span class="pill-item">3. Sacrum (Supine)</span>
    <span class="pill-item">4. Calcaneus / Heel</span>
    <span class="pill-item">5. Lateral Malleolus</span>
    <span class="pill-item">6. Occiput</span>
  </div>

  <h4><i class="fa-solid fa-layer-group"></i> NPUAP / EPUAP Staging Classification</h4>
  <div class="table-responsive">
    <table class="med-table">
      <thead>
        <tr><th>Stage</th><th>Clinical Description</th><th>Pathological Depth</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="badge badge-info">Stage 1</span></td>
          <td><strong>Non-blanchable erythema</strong> of intact skin over a bony prominence. Area may be painful, firm, soft, warmer or cooler compared to adjacent tissue.</td>
          <td>Epidermis intact; reversible microvascular congestion.</td>
        </tr>
        <tr>
          <td><span class="badge badge-warning">Stage 2</span></td>
          <td><strong>Partial-thickness skin loss</strong> presenting as a shallow open ulcer with a red-pink wound bed, without slough. May also present as an intact or ruptured serum-filled blister.</td>
          <td>Involves epidermis and dermis.</td>
        </tr>
        <tr>
          <td><span class="badge badge-danger">Stage 3</span></td>
          <td><strong>Full-thickness skin loss.</strong> Subcutaneous fat may be visible, but bone, tendon, and muscle are NOT exposed. Slough may be present. Undermining and tunneling may occur.</td>
          <td>Extends into subcutaneous fat down to (but not through) underlying deep fascia.</td>
        </tr>
        <tr>
          <td><span class="badge badge-purple">Stage 4</span></td>
          <td><strong>Full-thickness tissue loss with exposed bone, tendon, or muscle.</strong> Slough or black eschar often present. Undermining and sinus tunneling common. Direct risk of <em>osteomyelitis</em>!</td>
          <td>Extensive tissue destruction through fascia into muscle, joint capsule, or periosteum.</td>
        </tr>
        <tr>
          <td><span class="badge badge-secondary">Unstageable</span></td>
          <td>Full-thickness tissue loss in which the actual base of the ulcer is completely covered by yellow/tan/gray slough or brown/black eschar. Depth cannot be confirmed until debrided.</td>
          <td>Obscured depth.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4><i class="fa-solid fa-hand-holding-medical"></i> Clinical Management & Wound Care Protocol (Rx)</h4>
  <div class="rx-box">
    <div class="rx-header"><span class="rx-icon">Rx</span> Pressure Ulcer Management & Nursing Protocol:</div>
    <div class="rx-body">
      <ol class="rx-ordered-list">
        <li><strong>Pressure Redistribution (The Primary Foundation of Care):</strong>
          <ul class="sub-list">
            <li>Strict <strong>repositioning schedule every 2 hours</strong> for bedbound patients; every 15–30 minutes for wheelchair-bound patients.</li>
            <li>Use dynamic alternating-pressure mattresses, high-specification foam mattresses, or air-fluidized beds.</li>
            <li>Heel offloading: Place pillows beneath the calves to suspend the heels completely off the bed ("floating heels"). Never massage erythematous bony prominences!</li>
          </ul>
        </li>
        <li><strong>Wound Cleansing & Saline Irrigation:</strong>
          <ul class="sub-list">
            <li><strong>Normal Saline (0.9% NaCl)</strong> is the optimal physiological cleaning agent.</li>
            <li><em>CRITICAL WOUND CARE RULE:</em> <strong>Limit the use of toxic antiseptic fluids (Povidone-iodine, Hydrogen peroxide, Sodium hypochlorite/Dakin's)</strong> on granulating wounds because they are cytotoxic to proliferating fibroblasts and destroy nascent capillary buds!</li>
          </ul>
        </li>
        <li><strong>Debridement of Necrotic Devitalized Tissue:</strong>
          <ul class="sub-list">
            <li>Modalities: Sharp (surgical), mechanical, enzymatic (collagenase), biological (maggot therapy), or autolytic (hydrogels).</li>
            <li>Debridement removes bacterial biofilms and promotes wound granulation. (Exception: Stable, dry, intact eschar on the heel without erythema should NOT be debrided; it acts as a natural biological cover).</li>
          </ul>
        </li>
        <li><strong>Moisture-Retentive Wound Dressings:</strong>
          <ul class="sub-list">
            <li>Stage 1: Transparent adhesive film dressing or barrier cream.</li>
            <li>Stage 2: Hydrocolloid dressing (Duoderm) to maintain a moist physiological healing environment.</li>
            <li>Stage 3 & 4 (Exudative): Calcium alginate dressings, hydrofiber dressings (Aquacel), or polyurethane foam dressings (Allevyn, Mepilex) to absorb heavy exudate.</li>
          </ul>
        </li>
        <li><strong>Negative Pressure Wound Therapy (NPWT / Vacuum-Assisted Closure - VAC):</strong>
          <ul class="sub-list">
            <li>Applies controlled subatmospheric pressure (-125 mmHg) to the wound bed.</li>
            <li>Dramatically increases local microvascular blood flow, evacuates interstitial edema, reduces bacterial colonization, and stimulates rapid granulation tissue formation.</li>
          </ul>
        </li>
        <li><strong>Nutritional Support:</strong> Optimize serum albumin (&gt; 3.5 g/dL); high-protein intake (1.25–1.5 g/kg/day), Vitamin C (500mg BD), and Zinc sulphate (220mg OD) to support collagen cross-linking.</li>
        <li><strong>Surgical Reconstruction:</strong> For clean, healing Stage 3 or 4 ulcers in fit patients: Excision of the ulcer and underlying bony prominence (ostectomy) followed by <strong>regional fasciocutaneous or musculocutaneous tissue flap closure</strong> (e.g., gluteus maximus, tensor fasciae latae, or gracilis flaps).</li>
      </ol>
    </div>
  </div>
</div>
"""
    },
    {
        "id": "topic-20",
        "num": 20,
        "title": "Diabetic Foot Infections",
        "category": "wounds-ulcers",
        "category_name": "Wounds & Ulcers",
        "badge": "Limb Preservation Protocol",
        "book_page": "p. 437",
        "summary": "Neuropathy and vasculopathy pathophysiology, IDSA/IWGDF severity grades (mild, moderate, severe), probe-to-bone test, deep tissue cultures, specialized MCR offloading footwear, empirical antibiotics, and amputation guidelines.",
        "content": """
<div class="clinical-section">
  <h4><i class="fa-solid fa-shoe-prints"></i> Pathophysiology & Etiology</h4>
  <p><strong>The Triad of Diabetic Foot Complications:</strong></p>
  <div class="cards-subgrid">
    <div class="subcard">
      <div class="subcard-header primary-header">1. Diabetic Neuropathy</div>
      <p>Sensory neuropathy (loss of protective pain sensation) leads to unrecognized repetitive pressure and thermal trauma. Motor neuropathy causes intrinsic foot muscle wasting, clawing of toes, and prominent metatarsal heads. Autonomic neuropathy leads to anhidrosis, dry cracked skin, and arteriovenous shunting.</p>
    </div>
    <div class="subcard">
      <div class="subcard-header warning-header">2. Peripheral Artery Disease (PAD)</div>
      <p>Atherosclerotic tibial and peroneal arterial occlusion impairs tissue oxygenation, impairs leukocyte migration, and delays wound healing.</p>
    </div>
    <div class="subcard">
      <div class="subcard-header danger-header">3. Polymicrobial Infection</div>
      <p>Ulcers act as portals of entry. Diabetic foot infections are characteristically <strong>polymicrobial</strong>: <em>Staphylococcus aureus</em> and <em>Streptococcus</em> spp. (early/mild), with added enteric Gram-negative bacilli (<em>E. coli</em>, <em>Klebsiella</em>, <em>Proteus</em>, <em>Pseudomonas</em>) and obligate anaerobes (<em>Bacteroides</em>) in chronic, deep, or foul-smelling necrotizing wounds.</p>
    </div>
  </div>

  <h4><i class="fa-solid fa-stethoscope"></i> Clinical Assessment & IDSA / IWGDF Infection Severity</h4>
  <div class="table-responsive">
    <table class="med-table">
      <thead>
        <tr><th>Severity Grade</th><th>Clinical Features & Extent</th><th>Management Setting</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="badge badge-success">Uninfected</span></td>
          <td>Wound without purulence or any signs of inflammation.</td>
          <td>Outpatient local wound care + offloading.</td>
        </tr>
        <tr>
          <td><span class="badge badge-info">Mild Infection</span></td>
          <td>Superficial skin/subcutaneous involvement. Presence of &ge; 2 signs of inflammation (erythema, warmth, tenderness, induration, purulent discharge). <strong>Cellulitis / erythema &le; 2 cm</strong> around ulcer. No systemic toxicity.</td>
          <td>Outpatient Oral Antibiotics (1–2 weeks).</td>
        </tr>
        <tr>
          <td><span class="badge badge-warning">Moderate Infection</span></td>
          <td><strong>Erythema &gt; 2 cm</strong> around ulcer OR infection extending into deep tissues (fascia, tendon, deep muscle, joint space, or bone). No systemic signs.</td>
          <td>Hospital Admission; Oral/IV Antibiotics (2–4 weeks).</td>
        </tr>
        <tr>
          <td><span class="badge badge-danger">Severe Infection</span></td>
          <td>Any foot infection accompanied by <strong>Systemic Inflammatory Response Syndrome (SIRS):</strong> Temp &gt; 38&deg;C or &lt; 36&deg;C, HR &gt; 90 bpm, RR &gt; 20 bpm, WBC &gt; 12,000 or &lt; 4,000/&mu;L, or hypotension/shock.</td>
          <td>Urgent Hospital Admission + IV Antibiotics + Emergency Debridement.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4><i class="fa-solid fa-bone"></i> Diagnostic Workup</h4>
  <ul class="styled-list">
    <li><strong>The Probe-to-Bone (PTB) Test:</strong> Palpation of hard, gritty bone with a sterile blunt metallic probe inserted through the base of the ulcer. A positive PTB test has &gt; 90% positive predictive value for underlying <strong>osteomyelitis</strong>!</li>
    <li><strong>Microbiological Sampling:</strong> <em>Avoid superficial wound swabs!</em> (They only reflect skin colonizers). Obtain deep tissue biopsy or curettage from the debrided ulcer base for aerobic and anaerobic culture.</li>
    <li><strong>Imaging:</strong> Plain Foot Radiographs (AP, lateral, oblique) to assess for osteomyelitis (cortical destruction, periosteal reaction, osteopenia) and subcutaneous gas. MRI foot is the gold standard when radiographs are equivocal.</li>
    <li><strong>Vascular Assessment:</strong> Palpation of dorsalis pedis and posterior tibial pulses; Ankle-Brachial Index (ABI) and Arterial Doppler ultrasound.</li>
  </ul>

  <h4><i class="fa-solid fa-prescription"></i> Comprehensive Treatment Protocol & Prescription (Rx)</h4>
  <div class="rx-box">
    <div class="rx-header"><span class="rx-icon">Rx</span> Diabetic Foot Infection Medical & Surgical Regimens:</div>
    <div class="rx-body">
      <ol class="rx-ordered-list">
        <li><strong>Strict Glycemic Control:</strong> Convert to subcutaneous insulin therapy (basal-bolus or regular insulin sliding scale) to optimize neutrophil phagocytic killing.</li>
        <li><strong>Empiric Antibiotic Therapy:</strong>
          <div class="med-item">
            <strong>A. Mild Outpatient Infection (Oral for 1–2 weeks):</strong>
            <br>&bull; <span class="drug-name">Cap. Clindamycin 300mg</span> (Brand: <span class="brand">Dalacin-C</span>) &times; 1 cap TDS/QID
            <br>&bull; <em>OR</em> <span class="drug-name">Cap. Cephalexin 500mg</span> (Brands: <span class="brand">Ceporex, Keflex</span>) &times; 1 cap BD/TDS
            <br>&bull; <em>OR</em> <span class="drug-name">Tab. Co-amoxiclav 625mg</span> (Brand: <span class="brand">Augmentin</span>) &times; 1 tab TDS
            <br>&bull; <em>OR</em> <span class="drug-name">Cap. Doxycycline 100mg</span> (Brand: <span class="brand">Vibramycin</span>) &times; 1 cap BD.
          </div>
          <div class="med-item">
            <strong>B. Moderate Infection (Add Gram-negative coverage):</strong>
            <br>&bull; Add <span class="drug-name">Tab. Levofloxacin 500mg</span> (Brands: <span class="brand">Leflox, Cravit</span>) &times; 1 tab OD OR <span class="drug-name">Tab. Moxifloxacin 400mg</span> (Brands: <span class="brand">Mofest, Moxiget</span>) &times; 1 tab OD.
          </div>
          <div class="med-item">
            <strong>C. Severe / Deep / Necrotizing Infection (Inpatient IV Therapy):</strong>
            <br>&bull; <span class="drug-name">Inj. Vancomycin 1g (15–20 mg/kg)</span> &times; IV infusion &times; BD (or <span class="drug-name">Inj. Linezolid 600mg/300ml</span> [Brands: <span class="brand">Ecasil, Nezkil</span>] &times; IV &times; BD)
            <br><strong>PLUS ONE OF:</strong>
            <br>&bull; <span class="drug-name">Inj. Piperacillin/Tazobactam 4.5g</span> (Brands: <span class="brand">Tanzo, Tazocin</span>) &times; IV &times; TDS
            <br>&bull; <em>OR</em> <span class="drug-name">Inj. Meropenem 1g to 2g</span> (Brands: <span class="brand">Meronem, Penro</span>) &times; IV &times; TDS
            <br>&bull; <em>OR</em> <span class="drug-name">Inj. Moxifloxacin 400mg/250ml</span> (Moxiget) &times; IV &times; OD.
          </div>
        </li>
        <li><strong>Surgical Debridement:</strong> Prompt, aggressive surgical removal of all non-viable tissue, infected slough, and necrotic fascia. Resection of infected bony prominences to promote healing.</li>
        <li><strong>Mechanical Offloading (Vital for Healing!):</strong>
          <ul class="sub-list">
            <li>Total Contact Casting (TCC) — the gold standard for neuropathic plantar ulcers.</li>
            <li>Fitting with <strong>Microcellular Rubber (MCR) specialized footwear</strong> or customized orthotic shoes to redistribute pressure away from ulcer sites.</li>
          </ul>
        </li>
        <li><strong>Revascularization & Amputation Guidelines:</strong>
          <ul class="sub-list">
            <li>Endovascular angioplasty or surgical bypass for patients with critical limb ischemia.</li>
            <li><strong>Minor Amputation:</strong> Toe disarticulation or ray amputation to eradicate localized osteomyelitis while preserving a functional weight-bearing foot.</li>
            <li><strong>Major Amputation (Below-Knee or Above-Knee):</strong> Performed as a life-saving measure in extensive uncorrectable tissue necrosis, wet gangrene, or overwhelming sepsis.</li>
          </ul>
        </li>
      </ol>
    </div>
  </div>
</div>
"""
    }
]
