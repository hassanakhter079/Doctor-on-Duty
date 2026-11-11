# -*- coding: utf-8 -*-
"""
Chapter 23: Emergency Medicine, Toxicology & Resuscitation — 9 Complete Topics
Doctor on Duty 3rd Edition (Book pp. 673–712)
Life-saving resuscitation algorithms, toxidromes, organophosphate atropinization,
anaphylaxis adrenaline protocols, Parkland burn fluid formula, paracetamol NAC nomogram,
and authentic Pakistani emergency hospital formularies (Adrenaline, Atropine, PAM, NAC, ASV, Rocephin, Norad, Kinz, Toradol).
"""

TOPICS = [
    {
        "id": "ch23-topic-1",
        "num": 301,
        "chapter_num": 23,
        "chapter_name": "Emergency Medicine & Poisoning",
        "slug": "ch23-01-acls-cardiac-arrest.html",
        "title": "ACLS Cardiac Arrest Algorithm & Resuscitation",
        "category": "resuscitation",
        "category_name": "Emergency Resuscitation",
        "badge": "Life Support",
        "book_page": "pp. 673–676",
        "summary": "Advanced Cardiovascular Life Support (ACLS) algorithmic management of adult cardiac arrest; shockable (VF / pVT) vs non-shockable (PEA / Asystole) pathways, high-quality chest compressions, early defibrillation, adrenaline & amiodarone protocols, and reversing the 5Hs and 5Ts.",
        "content": """
<div class="clinical-section">
  <h4><i class="fa-solid fa-heart-pulse"></i> 1. The Core Resuscitation Pathways</h4>
  <p>Survival in sudden cardiac arrest hinges upon immediate recognition, high-quality cardiopulmonary resuscitation (CPR), and rapid rhythm differentiation into shockable vs non-shockable rhythms:</p>
  <div class="table-responsive">
    <table class="med-table">
      <thead>
        <tr><th>Rhythm Category</th><th>ECG Rhythms</th><th>Immediate Energy & Defibrillation</th><th>Drug Therapy Pipeline</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Shockable (VF / pVT)</strong></td>
          <td><strong>Ventricular Fibrillation (VF)</strong> or <strong>Pulseless Ventricular Tachycardia (pVT)</strong>.</td>
          <td><strong>Immediate unsynchronized shock:</strong> Biphasic: <strong>120–200 Joules</strong> (or maximum device output); Monophasic: <strong>360 Joules</strong>. Resume CPR immediately for 2 minutes without checking pulse!</td>
          <td>&bull; <strong>Adrenaline (Epinephrine 1:10,000):</strong> 1 mg IV/IO after 2nd shock, repeat every 3 to 5 minutes.<br>&bull; <strong>Amiodarone:</strong> First dose <strong>300 mg IV/IO bolus</strong> after 3rd shock; second dose <strong>150 mg IV/IO</strong> after 5th shock.<br>(Alternative: Lidocaine 1–1.5 mg/kg IV).</td>
        </tr>
        <tr>
          <td><strong>Non-Shockable (PEA / Asystole)</strong></td>
          <td><strong>Asystole</strong> (flatline confirmed in &ge; 2 leads) or <strong>Pulseless Electrical Activity (PEA)</strong> (organized rhythm without palpable pulse).</td>
          <td><strong>DO NOT SHOCK!</strong> Defibrillation is completely futile and causes myocardial damage. Focus 100% on uninterrupted CPR and reversible causes.</td>
          <td>&bull; <strong>Adrenaline (Epinephrine):</strong> 1 mg IV/IO <strong>as early as possible</strong>, then repeat every 3 to 5 minutes.<br>&bull; Identify and treat underlying <strong>5Hs and 5Ts</strong> aggressively.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4><i class="fa-solid fa-hand-holding-heart"></i> 2. High-Quality CPR Metrics</h4>
  <div class="steps-grid">
    <div class="step-card">
      <span class="step-num">Rate</span>
      <strong>100 to 120 Compressions/Minute:</strong> Fast, rhythmic compression on lower half of sternum.
    </div>
    <div class="step-card">
      <span class="step-num">Depth</span>
      <strong>At Least 5 to 6 cm (2 to 2.4 inches):</strong> In adults, avoiding excessive depths (&gt; 6 cm).
    </div>
    <div class="step-card">
      <span class="step-num">Recoil</span>
      <strong>Full Chest Recoil:</strong> Allow the chest to re-expand completely between compressions to allow ventricular filling. Do not lean on the chest!
    </div>
    <div class="step-card">
      <span class="step-num">Min. Pauses</span>
      <strong>Minimize Interruptions:</strong> Keep pauses for rhythm checks and shock delivery strictly &lt; 10 seconds. Switch compressors every 2 minutes to prevent fatigue.
    </div>
  </div>

  <h4><i class="fa-solid fa-list-check"></i> 3. Reversible Etiologies: The 5Hs and 5Ts</h4>
  <div class="table-responsive">
    <table class="med-table">
      <thead>
        <tr><th>The 5 H's (Metabolic / Fluid)</th><th>Targeted Emergency Interventions</th><th>The 5 T's (Mechanical / Vascular)</th><th>Targeted Emergency Interventions</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Hypovolemia</strong></td>
          <td>Rapid IV crystalloid boluses (Ringer's lactate) or O-negative uncrossed blood.</td>
          <td><strong>Tension Pneumothorax</strong></td>
          <td>Immediate needle thoracocentesis (2nd ICS MCL or 5th ICS AAL) followed by chest tube.</td>
        </tr>
        <tr>
          <td><strong>Hypoxia</strong></td>
          <td>100% FiO2 via bag-valve-mask, secure endotracheal airway.</td>
          <td><strong>Tamponade (Cardiac)</strong></td>
          <td>Emergent ultrasound-guided pericardiocentesis.</td>
        </tr>
        <tr>
          <td><strong>Hydrogen Ion (Acidosis)</strong></td>
          <td>Adequate ventilation; IV Sodium Bicarbonate (8.4% 50–100 mmol) in prolonged arrest.</td>
          <td><strong>Toxins (Poisoning)</strong></td>
          <td>Specific antidotes (Naloxone for opioids, Atropine for organophosphates, Calcium/DigiFab).</td>
        </tr>
        <tr>
          <td><strong>Hypo- / Hyperkalemia</strong></td>
          <td>Hyperkalemia: IV 10% Calcium Gluconate (10 mL) + Insulin/Dextrose + Sodium Bicarb.</td>
          <td><strong>Thrombosis (Pulmonary PE)</strong></td>
          <td>Emergency systemic thrombolysis (Alteplase 50mg IV bolus) during CPR.</td>
        </tr>
        <tr>
          <td><strong>Hypothermia</strong></td>
          <td>Active internal core rewarming (warmed IV fluids, warm humidified oxygen).</td>
          <td><strong>Thrombosis (Coronary ACS)</strong></td>
          <td>Immediate transfer for emergency primary PCI / cath lab upon ROSC.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""
    },
    {
        "id": "ch23-topic-2",
        "num": 302,
        "chapter_num": 23,
        "chapter_name": "Emergency Medicine & Poisoning",
        "slug": "ch23-02-anaphylaxis-emergency.html",
        "title": "Anaphylaxis Emergency Management & Adrenaline Protocol",
        "category": "resuscitation",
        "category_name": "Emergency Resuscitation",
        "badge": "Life-Threatening Emergency",
        "book_page": "pp. 677–680",
        "summary": "Severe, sudden-onset multi-system type-I hypersensitivity reaction; airway compromise, bronchospasm, distributive shock, universal first-line Intramuscular Adrenaline (Epinephrine 1:1,000) 0.5 mg anterolateral thigh dosing, aggressive IV fluid resuscitation, and biphasic reaction prevention.",
        "content": """
<div class="clinical-section">
  <h4><i class="fa-solid fa-triangle-exclamation"></i> 1. Diagnostic Criteria & Triggers</h4>
  <p>Anaphylaxis is a clinical diagnosis. <strong>Treatment must NEVER be delayed for laboratory tests or extensive history:</strong></p>
  <div class="steps-grid">
    <div class="step-card">
      <span class="step-num">Trigger</span>
      <strong>Common Triggers:</strong> Drugs (Penicillins, Cephalosporins, NSAIDs, IV radiocontrast), food (peanuts, seafood, eggs, milk), insect venoms (wasp/bee stings), latex.
    </div>
    <div class="step-card">
      <span class="step-num">Airway / Resp</span>
      <strong>Respiratory Compromise:</strong> Laryngeal edema, stridor, hoarseness, globus sensation, severe bronchospasm, diffuse wheezing, intercostal retraction, SpO2 &lt; 92%.
    </div>
    <div class="step-card">
      <span class="step-num">Cardiovascular</span>
      <strong>Hypotension / Collapse:</strong> Systolic BP &lt; 90 mmHg or &gt; 30% drop from baseline, reflex tachycardia, diaphoresis, syncope, cardiac arrest.
    </div>
    <div class="step-card">
      <span class="step-num">Cutaneous</span>
      <strong>Skin / Mucosal Signs:</strong> Generalized pruritic urticaria (hives), widespread erythema, angioedema (swollen lips, tongue, uvula, periorbital tissues). <em>Note: Up to 20% of fatal cases lack cutaneous signs due to sudden vascular collapse!</em>
    </div>
  </div>

  <h4><i class="fa-solid fa-syringe"></i> 2. The Life-Saving Golden Drug: Intramuscular Adrenaline</h4>
  <div class="alert alert-danger">
    <strong><i class="fa-solid fa-bell"></i> ADRENALINE (EPINEPHRINE) IS THE FIRST AND ONLY LIFE-SAVING DRUG:</strong>
    <p>Antihistamines and steroids do NOT save lives in acute anaphylaxis; they do not reverse bronchospasm or distributive shock. Intramuscular injection into the <strong>anterolateral aspect of the middle third of the thigh (vastus lateralis)</strong> achieves peak plasma concentrations within 8 minutes (vastly superior to deltoid or subcutaneous routes):</p>
    <div class="steps-grid">
      <div class="step-card">
        <span class="step-num">Adult Dose</span>
        <strong>Adults (&gt; 12 years):</strong><br>
        <strong>0.5 mg IM (0.5 mL of 1:1,000 [1 mg/mL] solution)</strong> stat into mid-outer thigh. Repeat every 5 to 15 minutes if symptoms persist or deteriorate!
      </div>
      <div class="step-card">
        <span class="step-num">Child 6–12y</span>
        <strong>Children 6 to 12 years:</strong><br>
        <strong>0.3 mg IM (0.3 mL of 1:1,000 solution)</strong> stat into mid-outer thigh.
      </div>
      <div class="step-card">
        <span class="step-num">Child &lt;6y</span>
        <strong>Children &lt; 6 years:</strong><br>
        <strong>0.15 mg IM (0.15 mL of 1:1,000 solution)</strong> stat into mid-outer thigh.
      </div>
    </div>
  </div>

  <h4><i class="fa-solid fa-prescription-bottle-medical"></i> 3. Immediate Resuscitation & Secondary Therapies</h4>
  <div class="table-responsive">
    <table class="med-table">
      <thead>
        <tr><th>Priority</th><th>Intervention & Drug Molecule</th><th>Brand Names (Pakistan)</th><th>Dosage & Clinical Pearls</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>1. Positioning</strong></td>
          <td>Lie patient flat; elevate legs (Trendelenburg).</td>
          <td><em>Patient Position</em></td>
          <td>Prevents the "empty heart syndrome" (sudden death upon standing due to massive venodilation and lack of venous return). If breathing is labored, allow sitting up slightly.</td>
        </tr>
        <tr>
          <td><strong>2. High-Flow Oxygen</strong></td>
          <td>Oxygen via non-rebreather mask at 15 L/min.</td>
          <td><em>Medical Oxygen</em></td>
          <td>Maintain SpO2 &gt; 94–98%. Prepare for emergency endotracheal intubation or surgical cricothyroidotomy if progressive laryngeal stridor occurs.</td>
        </tr>
        <tr>
          <td><strong>3. Aggressive IV Fluid Resuscitation</strong></td>
          <td>Crystalloids: Normal Saline 0.9% or Ringer's Lactate.</td>
          <td><em>Infusion 0.9% Normal Saline</em></td>
          <td><strong>1 to 2 Liters rapid IV pressure bolus in adults</strong> (20 mL/kg in children) via 2 wide-bore 16G cannulae. Up to 35% of circulating blood volume shifts into extravascular tissues within 10 minutes!</td>
        </tr>
        <tr>
          <td><strong>4. Secondary Steroid (Prevents Biphasic)</strong></td>
          <td>Hydrocortisone sodium succinate</td>
          <td><em>Inj Solu-Cortef 100mg / 250mg</em></td>
          <td><strong>200 mg IV slow bolus</strong> (Children: 4 mg/kg). Slow onset (takes 4–6 hrs); primarily indicated to prevent late <strong>biphasic anaphylactic recurrence</strong> (occurs in up to 20% within 8–72 hours).</td>
        </tr>
        <tr>
          <td><strong>5. Secondary Antihistamine</strong></td>
          <td>Chlorpheniramine maleate</td>
          <td><em>Inj Piriton 10mg</em></td>
          <td><strong>10 mg slow IV/IM</strong>. Relieves cutaneous itching and hives; does NOT reverse airway obstruction.</td>
        </tr>
        <tr>
          <td><strong>6. Bronchospasm Adjuvant</strong></td>
          <td>Salbutamol nebulization 5mg</td>
          <td><em>Nebulizing Sol Ventolin</em></td>
          <td>5mg nebulized with oxygen for persistent wheezing after adrenaline.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""
    },
    {
        "id": "ch23-topic-3",
        "num": 303,
        "chapter_num": 23,
        "chapter_name": "Emergency Medicine & Poisoning",
        "slug": "ch23-03-sepsis-septic-shock.html",
        "title": "Sepsis & Septic Shock (Surviving Sepsis Hour-1 Bundle)",
        "category": "resuscitation",
        "category_name": "Emergency Resuscitation",
        "badge": "Critical Care",
        "book_page": "pp. 681–685",
        "summary": "Life-threatening organ dysfunction caused by a dysregulated host response to infection (Sepsis-3); bedside qSOFA screening, Surviving Sepsis Campaign Hour-1 Bundle, blood cultures, 30 mL/kg crystalloid bolus, early Norepinephrine vasopressor support (MAP >= 65 mmHg), and empiric broad-spectrum IV antimicrobials.",
        "content": """
<div class="clinical-section">
  <h4><i class="fa-solid fa-viruses"></i> 1. Sepsis-3 Definitions & Bedside qSOFA Score</h4>
  <p>According to international consensus (Sepsis-3), <strong>Sepsis</strong> is defined as life-threatening organ dysfunction caused by a dysregulated host response to infection (quantified by an acute increase in SOFA score &ge; 2). <strong>Septic Shock</strong> is a subset with persistent hypotension requiring vasopressors to maintain MAP &ge; 65 mmHg AND serum lactate &gt; 2 mmol/L despite adequate fluid resuscitation (hospital mortality &gt; 40%):</p>
  <div class="steps-grid">
    <div class="step-card">
      <span class="step-num">qSOFA Criteria</span>
      <strong>Quick SOFA Bedside Screen (&ge; 2 of 3 indicates high mortality risk):</strong><br>
      &bull; <strong>Respiratory Rate:</strong> &ge; 22 breaths/min.<br>
      &bull; <strong>Altered Mentation:</strong> Glasgow Coma Scale (GCS) &lt; 15.<br>
      &bull; <strong>Systolic Blood Pressure:</strong> &le; 100 mmHg.
    </div>
    <div class="step-card">
      <span class="step-num">Septic Shock Signs</span>
      <strong>Clinical Shock Markers:</strong> Mottled skin, capillary refill time &gt; 3 seconds, oliguria (&lt; 0.5 mL/kg/hr), bounding pulses progressing to thready tachycardia, cool extremities, hyperlactatemia.
    </div>
  </div>

  <h4><i class="fa-solid fa-clock-rotate-left"></i> 2. The Surviving Sepsis Campaign "Hour-1 Bundle"</h4>
  <div class="alert alert-danger">
    <strong><i class="fa-solid fa-stopwatch"></i> EMERGENCY ACTIONS TO INITIATE WITHIN THE FIRST 60 MINUTES:</strong>
    <div class="steps-grid">
      <div class="step-card">
        <span class="step-num">Element 1</span>
        <strong>Measure Serum Lactate:</strong> Immediate point-of-care venous/arterial lactate. Re-measure within 2–4 hours if initial lactate is &gt; 2.0 mmol/L to guide resuscitation.
      </div>
      <div class="step-card">
        <span class="step-num">Element 2</span>
        <strong>Obtain Blood Cultures:</strong> Draw 2 sets of peripheral blood cultures (aerobic & anaerobic) from separate venipuncture sites <em>prior to starting antibiotics</em> (without delaying antibiotic initiation &gt; 45 minutes).
      </div>
      <div class="step-card">
        <span class="step-num">Element 3</span>
        <strong>Administer Broad-Spectrum IV Antimicrobials:</strong> Infuse empiric IV antibiotics targeting likely source within the first hour. Mortality increases by 7.6% for every single hour of delay in septic shock!
      </div>
      <div class="step-card">
        <span class="step-num">Element 4</span>
        <strong>Rapid IV Crystalloid Bolus (30 mL/kg):</strong> Administer <strong>30 mL/kg of balanced crystalloid (Ringer's Lactate / Plasmalyte)</strong> IV within the first 3 hours for hypotension (MAP &lt; 65) or lactate &ge; 4.0 mmol/L. (Average 70 kg adult = 2,100 mL).
      </div>
      <div class="step-card">
        <span class="step-num">Element 5</span>
        <strong>Apply Vasopressors to Maintain MAP &ge; 65 mmHg:</strong> If blood pressure does not respond during or after fluid loading, start vasopressors immediately to restore perfusion.
      </div>
    </div>
  </div>

  <h4><i class="fa-solid fa-prescription-bottle-medical"></i> 3. Pharmacotherapy & Critical Care Formularies</h4>
  <div class="table-responsive">
    <table class="med-table">
      <thead>
        <tr><th>Role</th><th>Drug & Strength</th><th>Brand Names (Pakistan)</th><th>Regimen & Clinical Pearls</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>First-Line Vasopressor</strong></td>
          <td><strong>Norepinephrine</strong> (Noradrenaline)</td>
          <td><em>Inj Norad 4mg / 4mL</em><br><em>Inj Levophed</em></td>
          <td><strong>Drug of Choice.</strong> Potent alpha-1 vasoconstrictor with modest beta-1 inotropy. Start at <strong>2 to 12 mcg/min</strong> via central line (or peripheral 18G while central access is prepared), titrated to maintain <strong>MAP &ge; 65 mmHg</strong>. Vastly superior to Dopamine (lower arrhythmia rate and lower mortality).</td>
        </tr>
        <tr>
          <td><strong>Second-Line Vasopressor</strong></td>
          <td>Vasopressin (ADH)</td>
          <td><em>Inj Vasopressin 20 units</em></td>
          <td>Fixed dose <strong>0.03 units/min</strong> IV infusion added to Norepinephrine to reduce catecholamine requirements.</td>
        </tr>
        <tr>
          <td><strong>Empiric Antimicrobial Combination (Abdominal / Sepsis of Unknown Origin)</strong></td>
          <td>Ceftriaxone 2g IV + Metronidazole 500mg IV<br>OR Piperacillin-Tazobactam 4.5g IV</td>
          <td><em>Vial Rocephin 2g</em><br><em>Infusion Flagyl 500mg</em><br><em>Vial Tazocin 4.5g</em></td>
          <td>Rocephin 2g IV OD + Flagyl 500mg IV TDS. For hospital-acquired sepsis / ICU: Tazocin 4.5g IV QDS or Meropenem (<em>Meronem 1g</em>) TDS + Vancomycin (<em>Vancocin 1g</em>) BD.</td>
        </tr>
        <tr>
          <td><strong>Refractory Shock Corticosteroid</strong></td>
          <td>Hydrocortisone</td>
          <td><em>Inj Solu-Cortef 100mg</em></td>
          <td><strong>200 mg/day IV</strong> (given as 50 mg IV q6h or continuous infusion). Indicated only if shock remains refractory despite escalating doses of Norepinephrine and adequate fluids.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""
    },
    {
        "id": "ch23-topic-4",
        "num": 304,
        "chapter_num": 23,
        "chapter_name": "Emergency Medicine & Poisoning",
        "slug": "ch23-04-organophosphate-poisoning.html",
        "title": "Organophosphate & Carbamate Poisoning (Atropinization)",
        "category": "toxicology",
        "category_name": "Toxicology & Poisoning",
        "badge": "Agricultural Poisoning",
        "book_page": "pp. 686–690",
        "summary": "Irreversible acetylcholinesterase inhibition leading to massive acetylcholine storm; DUMBELS / SLUDGEM cholinergic toxidrome, lethal bronchorrhea and bronchospasm, aggressive emergency Atropine titration until target atropinization endpoints, Pralidoxime (PAM) enzyme reactivator, and decontamination.",
        "content": """
<div class="clinical-section">
  <h4><i class="fa-solid fa-skull"></i> 1. Mechanism & The DUMBELS Cholinergic Toxidrome</h4>
  <p>Organophosphates (OP: Chlorpyrifos, Malathion, Diazinon, Parathion) and Carbamates are agricultural pesticides widely accessible in Pakistan, frequently ingested for intentional self-harm or absorbed transcutaneously during spraying. They phosphorylate and inactivate <strong>acetylcholinesterase (AChE)</strong>, causing uncontrolled accumulation of acetylcholine at muscarinic, nicotinic, and CNS synapses:</p>
  <div class="table-responsive">
    <table class="med-table">
      <thead>
        <tr><th>Synaptic Receptor</th><th>Clinical Manifestations (Toxidrome)</th><th>Immediate Cause of Death</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Muscarinic Receptors (Parasympathetic Overdrive)</strong></td>
          <td>Mnemonic <strong>DUMBELS</strong>:<br>
          &bull; <strong>D</strong>iarrhea & Abdominal Cramps<br>
          &bull; <strong>U</strong>rination (Incontinence)<br>
          &bull; <strong>M</strong>iosis (Pinpoint non-reactive pupils)<br>
          &bull; <strong>B</strong>radycardia, <strong>B</strong>ronchospasm, <strong>B</strong>ronchorrhea (Copious frothy pulmonary secretions)<br>
          &bull; <strong>E</strong>mesis (Vomiting)<br>
          &bull; <strong>L</strong>acrimation<br>
          &bull; <strong>S</strong>alivation & Sweating (Diaphoresis)</td>
          <td rowspan="3"><strong>"Drowning in secretions":</strong> Massive pulmonary bronchorrhea, intense bronchospasm, and central respiratory drive depression cause fatal asphyxia within hours!</td>
        </tr>
        <tr>
          <td><strong>Nicotinic Receptors (Neuromuscular Junction)</strong></td>
          <td>Mnemonic <strong>MTWTF</strong>:<br>
          &bull; <strong>M</strong>ydriasis (early paradoxical)<br>
          &bull; <strong>T</strong>achycardia<br>
          &bull; <strong>W</strong>eakness & Flaccid paralysis<br>
          &bull; <strong>T</strong>remors<br>
          &bull; <strong>F</strong>asciculations (Tongue, facial, and diffuse muscle twitches; pathognomonic). Respiratory muscle diaphragm paralysis.</td>
        </tr>
        <tr>
          <td><strong>Central Nervous System (CNS)</strong></td>
          <td>Agitation, confusion, coma, seizures, central respiratory arrest.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4><i class="fa-solid fa-syringe"></i> 2. The Emergency Atropine Titration Protocol</h4>
  <div class="alert alert-danger">
    <strong><i class="fa-solid fa-capsules"></i> ATROPINE IS THE PHYSIOLOGICAL ANTIDOTE:</strong>
    <p>Atropine competitively blocks muscarinic receptors, clearing fatal bronchorrhea and reversing bronchospasm. <em>Pupil size and heart rate alone are unreliable markers; the primary goal is drying lung secretions:</em></p>
    <div class="steps-grid">
      <div class="step-card">
        <span class="step-num">Step 1</span>
        <strong>Initial Bolus:</strong> Administer <strong>Atropine 1.8 to 3.0 mg IV stat</strong> (3 to 5 ampoules of 0.6 mg).
      </div>
      <div class="step-card">
        <span class="step-num">Step 2</span>
        <strong>The Doubling Rule (Every 5 Minutes):</strong> If secretions remain moist and lungs rattling after 5 minutes, <strong>double the previous dose</strong> (e.g. 3 mg &rarr; 6 mg &rarr; 12 mg &rarr; 24 mg IV) every 5 minutes until complete atropinization is achieved!
      </div>
      <div class="step-card">
        <span class="step-num">Endpoints</span>
        <strong>Target Endpoints of Atropinization:</strong><br>
        (1) <strong>Lungs completely clear on auscultation (no crackles/bronchorrhea)</strong><br>
        (2) <strong>Dry mouth and axillae</strong><br>
        (3) <strong>Heart Rate &gt; 80 beats/min</strong><br>
        (4) <strong>Systolic BP &gt; 90 mmHg</strong><br>
        (5) <strong>Pupils dilated &ge; 4mm</strong> (pupils may remain small; do not wait for mydriasis if lungs are dry!).
      </div>
      <div class="step-card">
        <span class="step-num">Maintenance</span>
        <strong>Continuous Atropine Infusion:</strong> Once atropinized, calculate <strong>10% to 20% of the total loading dose per hour</strong> as a continuous IV infusion in normal saline. Taper cautiously over 24 to 72 hours.
      </div>
    </div>
  </div>

  <h4><i class="fa-solid fa-pills"></i> 3. Cholinesterase Reactivator & Decontamination</h4>
  <div class="table-responsive">
    <table class="med-table">
      <thead>
        <tr><th>Intervention</th><th>Agent & Regimen</th><th>Clinical Rationale</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Cholinesterase Reactivator (Oxime)</strong></td>
          <td><strong>Pralidoxime (PAM / 2-PAM)</strong>: 1 to 2 g IV in 100 mL Normal Saline over 30 minutes, followed by 500 mg/hr infusion (or 1g q6h).</td>
          <td>Cleaves the organophosphate-enzyme bond, regenerating active AChE at nicotinic neuromuscular junctions (reverses muscle weakness and fasciculations). <em>Must be given before "aging" (irreversible covalent bonding, occurs within 24–48 hours).</em></td>
        </tr>
        <tr>
          <td><strong>Seizure Control</strong></td>
          <td><strong>Diazepam (Valium)</strong>: 5 to 10 mg slow IV bolus, repeat q10-15min.</td>
          <td>Suppresses central cholinergic seizures and mitigates excitotoxic neuronal injury.</td>
        </tr>
        <tr>
          <td><strong>Dermal Decontamination</strong></td>
          <td>Strip all clothes, place in sealed bag, wash body with soap and water twice.</td>
          <td>Prevents continuous transdermal absorption. Healthcare providers must wear nitrile gloves and aprons (secondary poisoning risk).</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""
    },
    {
        "id": "ch23-topic-5",
        "num": 305,
        "chapter_num": 23,
        "chapter_name": "Emergency Medicine & Poisoning",
        "slug": "ch23-05-paracetamol-toxicity.html",
        "title": "Paracetamol Toxicity & N-Acetylcysteine (NAC Protocol)",
        "category": "toxicology",
        "category_name": "Toxicology & Poisoning",
        "badge": "Hepatotoxicity",
        "book_page": "pp. 691–694",
        "summary": "Dose-dependent toxic metabolite (NAPQI) accumulation depleting hepatic glutathione; Rumack-Matthew treatment nomogram, 4 clinical stages, and the definitive intravenous N-Acetylcysteine (NAC / Parvolex) 3-bag protocol preventing fulminant hepatic necrosis.",
        "content": """
<div class="clinical-section">
  <h4><i class="fa-solid fa-liver"></i> 1. Pathophysiology & Toxic Ingestion Thresholds</h4>
  <p>Paracetamol (Acetaminophen) is safe at therapeutic doses (max 4 g/day in adults). Metabolism occurs primarily via glucuronidation and sulfation. A small fraction (5–10%) is metabolized by CYP2E1 into the highly reactive, electrophilic, toxic intermediate <strong>N-acetyl-p-benzoquinone imine (NAPQI)</strong>, normally neutralized by hepatic <strong>glutathione</strong>:</p>
  <div class="steps-grid">
    <div class="step-card">
      <span class="step-num">Toxicity</span>
      <strong>Threshold Doses:</strong><br>
      &bull; Acute single ingestion <strong>&ge; 150 mg/kg</strong> in children or <strong>&ge; 7.5 g (15 tablets of 500mg)</strong> in adults causes severe hepatic necrosis.<br>
      &bull; Ingestion &gt; 250 mg/kg (or &gt; 12 g) carries a high risk of fatal fulminant hepatic failure.
    </div>
    <div class="step-card">
      <span class="step-num">Glutathione</span>
      <strong>Glutathione Depletion:</strong> Once hepatic glutathione stores are depleted by &gt; 70%, free uncapped NAPQI binds covalently to cysteinyl sulfhydryl groups of hepatocyte proteins, causing centrilobular (Zone III) hepatic necrosis.
    </div>
  </div>

  <h4><i class="fa-solid fa-clock"></i> 2. The Four Clinical Stages of Poisoning</h4>
  <div class="table-responsive">
    <table class="med-table">
      <thead>
        <tr><th>Stage</th><th>Time Post-Ingestion</th><th>Clinical Features & Laboratory Markers</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Stage I (Pre-injury)</strong></td>
          <td>0.5 to 24 hours</td>
          <td>Asymptomatic or mild non-specific symptoms: anorexia, nausea, vomiting, malaise, diaphoresis. Normal LFTs.</td>
        </tr>
        <tr>
          <td><strong>Stage II (Hepatic Injury)</strong></td>
          <td>24 to 72 hours</td>
          <td>"Quiescent period": Subjective gastrointestinal symptoms improve, but right upper quadrant (RUQ) abdominal pain and liver tenderness appear. <strong>AST/ALT and Bilirubin begin to rise sharply; INR/PT prolongs.</strong></td>
        </tr>
        <tr>
          <td><strong>Stage III (Peak Toxicity)</strong></td>
          <td>72 to 96 hours</td>
          <td><strong>Peak fulminant hepatic failure:</strong> Jaundice, coagulopathy (INR &gt; 5.0), hypoglycemia, hepatic encephalopathy (asterixis, coma), metabolic lactic acidosis, acute renal failure (hepatorenal syndrome / tubular necrosis). AST/ALT frequently &gt; 10,000 U/L. Highest mortality.</td>
        </tr>
        <tr>
          <td><strong>Stage IV (Recovery)</strong></td>
          <td>4 days to 2 weeks</td>
          <td>Survivors experience complete histological liver regeneration without permanent cirrhosis or fibrosis.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4><i class="fa-solid fa-prescription-bottle-medical"></i> 3. N-Acetylcysteine (NAC) 3-Bag IV Infusion Protocol</h4>
  <div class="alert alert-success">
    <strong><i class="fa-solid fa-shield-virus"></i> N-ACETYLCYSTEINE (NAC / PARVOLEX) IS 100% PROTECTIVE WITHIN 8 HOURS:</strong>
    <p>NAC replenishes hepatic glutathione and acts as an alternative substrate directly binding NAPQI. If initiated within 8 hours of ingestion, hepatotoxicity risk drops to &lt; 2%:</p>
    <div class="table-responsive">
      <table class="med-table">
        <thead>
          <tr><th>Infusion Bag</th><th>NAC Dosage</th><th>Diluent Volume (5% Dextrose)</th><th>Infusion Duration</th></tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Bag 1 (Loading Dose)</strong></td>
            <td><strong>150 mg/kg</strong></td>
            <td>200 mL 5% Dextrose (or 0.9% Saline)</td>
            <td>Over <strong>1 Hour</strong></td>
          </tr>
          <tr>
            <td><strong>Bag 2 (Second Dose)</strong></td>
            <td><strong>50 mg/kg</strong></td>
            <td>500 mL 5% Dextrose</td>
            <td>Over <strong>4 Hours</strong></td>
          </tr>
          <tr>
            <td><strong>Bag 3 (Third Dose)</strong></td>
            <td><strong>100 mg/kg</strong></td>
            <td>1,000 mL 5% Dextrose</td>
            <td>Over <strong>16 Hours</strong></td>
          </tr>
        </tbody>
      </table>
    </div>
    <p><em>Total Dose: 300 mg/kg IV over 21 hours. (If AST/ALT remains elevated or INR &gt; 1.3 at end of Bag 3, continue Bag 3 rate continuously until LFTs improve).</em></p>
  </div>
</div>
"""
    },
    {
        "id": "ch23-topic-6",
        "num": 306,
        "chapter_num": 23,
        "chapter_name": "Emergency Medicine & Poisoning",
        "slug": "ch23-06-snake-bite-envenomation.html",
        "title": "Snake Bite Envenomation (ASV & 20WBCT Protocol)",
        "category": "toxicology",
        "category_name": "Toxicology & Poisoning",
        "badge": "Envenomation Protocol",
        "book_page": "pp. 695–698",
        "summary": "Emergency management of venomous snakebites in Pakistan; distinguishing Vasculotoxic/Hemotoxic (Viperidae: Russell's & Saw-scaled viper) from Neurotoxic (Elapidae: Cobra & Krait); the 20-Minute Whole Blood Clotting Test (20WBCT), prohibition of tourniquets, and Polyvalent Anti-Snake Venom (ASV) titration.",
        "content": """
<div class="clinical-section">
  <h4><i class="fa-solid fa-staff-snake"></i> 1. Venomous Families in Pakistan</h4>
  <p>Over 20,000 venomous snakebite envenomations occur annually in Pakistan (especially during monsoons and harvest seasons in Punjab and Sindh):</p>
  <div class="table-responsive">
    <table class="med-table">
      <thead>
        <tr><th>Venomous Family</th><th>Common Pakistani Species</th><th>Pathophysiology & Hallmark Signs</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Viperidae (Vipers - Vasculotoxic / Hemotoxic)</strong></td>
          <td>&bull; <strong>Russell's Viper</strong> (<em>Daboia russelii</em>)<br>&bull; <strong>Saw-scaled Viper</strong> (<em>Echis carinatus / لونڈی سانپ</em>)</td>
          <td>Procoagulant venom activates Factor X/prothrombin &rarr; Consumption Coagulopathy (DIC), severe local swelling, bleeding from puncture fang marks, spontaneous gum bleeding, hematuria, hemoptysis, and acute renal failure (AKI).</td>
        </tr>
        <tr>
          <td><strong>Elapidae (Elapids - Neurotoxic)</strong></td>
          <td>&bull; <strong>Common Krait</strong> (<em>Bungarus caeruleus / سنگچور</em>)<br>&bull; <strong>Black Cobra</strong> (<em>Naja naja / ناگ</em>)</td>
          <td>Post-synaptic/pre-synaptic neurotoxins block ACh receptors: <strong>Bilateral ptosis</strong> (earliest sign), ophthalmoplegia, diplopia, bulbar palsy (dysphagia, pooling of secretions), respiratory muscle paralysis. Krait bites frequently occur at night while sleeping with minimal local swelling!</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4><i class="fa-solid fa-vial"></i> 2. The 20-Minute Whole Blood Clotting Test (20WBCT)</h4>
  <div class="steps-grid">
    <div class="step-card">
      <span class="step-num">Step 1</span>
      Draw <strong>2 mL of fresh venous blood</strong> into a clean, dry, new glass test tube (never use plastic or tube with anticoagulant/heparin).
    </div>
    <div class="step-card">
      <span class="step-num">Step 2</span>
      Leave the tube standing undisturbed at room temperature for <strong>exactly 20 minutes</strong>.
    </div>
    <div class="step-card">
      <span class="step-num">Result</span>
      Gently tip the tube to 90°. If blood is still liquid and flows out, <strong>20WBCT is POSITIVE (incoagulable blood)</strong>, confirming systemic viperid envenomation. Repeat q4h.
    </div>
  </div>

  <h4><i class="fa-solid fa-ban"></i> 3. Dangerous Harmful Practices to Strictly Avoid</h4>
  <div class="alert alert-danger">
    <ul class="bullet-list">
      <li><strong>NO Tourniquets or Tight Bands:</strong> Causes ischemic gangrene, limb amputation, and massive toxin surge upon release.</li>
      <li><strong>NO Incision, Slashing, or Sucking:</strong> Causes severe hemorrhage, tendon laceration, and introduces oral bacterial infection.</li>
      <li><strong>NO Potassium Permanganate, Herbs, or Electric Shocks.</strong></li>
      <li><strong>Correct First Aid:</strong> Reassure patient, immobilize entire bitten limb with a splint/crepe bandage at heart level, and transport immediately to hospital.</li>
    </ul>
  </div>

  <h4><i class="fa-solid fa-syringe"></i> 4. Polyvalent Anti-Snake Venom (ASV) Protocol</h4>
  <div class="steps-grid">
    <div class="step-card">
      <span class="step-num">Initial Dose</span>
      <strong>Standard Loading Dose (Adults & Children receive SAME dose):</strong><br>
      Dilute <strong>10 vials of Polyvalent ASV (NIH Islamabad)</strong> in <strong>500 mL of 0.9% Normal Saline</strong> (100 mL in children). Infuse slowly at 2 mL/min for first 10 minutes (watch for anaphylaxis), then complete over <strong>1 hour</strong>.
    </div>
    <div class="step-card">
      <span class="step-num">Monitoring</span>
      <strong>Response Criteria:</strong><br>
      &bull; Systemic bleeding stops within 15–30 minutes.<br>
      &bull; <strong>20WBCT normalizes (blood clots) within 6 hours.</strong> If blood remains incoagulable after 6 hours, repeat full dose of 10 vials of ASV.
    </div>
    <div class="step-card">
      <span class="step-num">Neurotoxic Trial</span>
      <strong>Neostigmine Test (For Cobra/Krait Neurotoxicity):</strong><br>
      Give <strong>Inj Atropine 0.6mg IV</strong>, followed immediately by <strong>Inj Neostigmine 1.5mg to 2.5mg IV/IM</strong>. If ptosis and respiratory effort improve within 30 minutes, maintain Neostigmine 0.5mg q30min with atropine until recovery.
    </div>
  </div>
</div>
"""
    },
    {
        "id": "ch23-topic-7",
        "num": 307,
        "chapter_num": 23,
        "chapter_name": "Emergency Medicine & Poisoning",
        "slug": "ch23-07-burn-injury-parkland.html",
        "title": "Thermal Burn Injury & Parkland Fluid Resuscitation",
        "category": "resuscitation",
        "category_name": "Emergency Resuscitation",
        "badge": "Burn Resuscitation",
        "book_page": "pp. 699–702",
        "summary": "Acute major burn resuscitation; Wallace Rule of Nines Total Body Surface Area (TBSA) calculation, Parkland crystalloid formula (4 mL x kg x %TBSA), fluid titration targeting urine output (0.5–1 mL/kg/hr), inhalation injury airway alert, and silver sulfadiazine wound care.",
        "content": """
<div class="clinical-section">
  <h4><i class="fa-solid fa-fire"></i> 1. TBSA Estimation: The Wallace Rule of Nines</h4>
  <p>In thermal, flame, and scald burns, accurate calculation of % Total Body Surface Area (% TBSA) of partial-thickness (2nd degree) and full-thickness (3rd degree) burns guides fluid therapy. (<em>Superficial 1st degree erythema is excluded from TBSA calculations!</em>):</p>
  <div class="table-responsive">
    <table class="med-table">
      <thead>
        <tr><th>Anatomical Body Region</th><th>Adult % TBSA (Rule of Nines)</th><th>Infant / Child &lt; 1 Year</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Head & Neck</strong></td>
          <td><strong>9%</strong> (4.5% anterior, 4.5% posterior)</td>
          <td><strong>18%</strong> (Head is disproportionately larger)</td>
        </tr>
        <tr>
          <td><strong>Anterior Torso (Chest & Abdomen)</strong></td>
          <td><strong>18%</strong> (9% chest, 9% abdomen)</td>
          <td><strong>18%</strong></td>
        </tr>
        <tr>
          <td><strong>Posterior Torso (Upper & Lower Back)</strong></td>
          <td><strong>18%</strong> (9% upper back, 9% buttocks/lower back)</td>
          <td><strong>18%</strong></td>
        </tr>
        <tr>
          <td><strong>Each Upper Extremity (Right & Left)</strong></td>
          <td><strong>9% each</strong> (4.5% front, 4.5% back) = 18% total</td>
          <td><strong>9% each</strong> = 18% total</td>
        </tr>
        <tr>
          <td><strong>Each Lower Extremity (Right & Left)</strong></td>
          <td><strong>18% each</strong> (9% front, 9% back) = 36% total</td>
          <td><strong>14% each</strong> = 28% total</td>
        </tr>
        <tr>
          <td><strong>Perineum & Genitalia</strong></td>
          <td><strong>1%</strong></td>
          <td><strong>1%</strong></td>
        </tr>
        <tr>
          <td><strong>Palmar Surface Rule</strong></td>
          <td colspan="2">Patient's entire palm (including fingers) equals <strong>approximately 1% TBSA</strong> (ideal for patchy scattered burns).</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4><i class="fa-solid fa-faucet-drip"></i> 2. The Parkland Fluid Resuscitation Formula</h4>
  <div class="alert alert-info">
    <strong><i class="fa-solid fa-calculator"></i> THE PARKLAND (BAXTER) CRYSTALLOID FORMULA:</strong>
    <p>Indicated for all burns &ge; 15% TBSA in adults (&ge; 10% TBSA in children):</p>
    <p style="font-size:16px; font-weight:700; color:var(--teal);">Total 24-Hour Fluid (Ringer's Lactate) = 4 mL &times; Weight (kg) &times; % TBSA Burn</p>
    <div class="steps-grid">
      <div class="step-card">
        <span class="step-num">First 8 Hours</span>
        <strong>Give 50% of Total Volume in First 8 Hours:</strong><br>
        <em>Calculated from the exact TIME OF BURN INJURY, NOT the time of hospital arrival!</em>
      </div>
      <div class="step-card">
        <span class="step-num">Next 16 Hours</span>
        <strong>Give Remaining 50% Volume over Next 16 Hours:</strong><br>
        Infused at a steady rate over the remaining 16 hours of the first day.
      </div>
    </div>
  </div>

  <h4><i class="fa-solid fa-gauge"></i> 3. Clinical Titration Target: Hourly Urine Output</h4>
  <p>The Parkland formula is an initial starting estimate. <strong>The rate of fluid infusion must be adjusted hourly based on Foley catheter urine output:</strong></p>
  <ul class="bullet-list">
    <li><strong>Adult Target:</strong> <strong>0.5 to 1.0 mL/kg/hour</strong> (approx 30 to 50 mL/hr).</li>
    <li><strong>Pediatric Target (&lt; 30 kg):</strong> <strong>1.0 to 1.5 mL/kg/hour</strong>.</li>
    <li><strong>Electrical Burns / Rhabdomyolysis / Hemochromogenuria:</strong> Target <strong>1.5 to 2.0 mL/kg/hour</strong> (75–100 mL/hr) until urine clears to prevent myoglobinuric acute renal tubular necrosis.</li>
  </ul>

  <h4><i class="fa-solid fa-wind"></i> 4. Inhalation Injury & Topical Wound Care</h4>
  <div class="steps-grid">
    <div class="step-card">
      <span class="step-num">Inhalation</span>
      <strong>Airway Red Flags (Early Intubation):</strong> Singed facial hair/eyebrows, carbonaceous sputum, soot in oropharynx, stridor, voice hoarseness, closed-space fire exposure. Prophylactic endotracheal intubation before laryngeal edema prevents intubation failure!
    </div>
    <div class="step-card">
      <span class="step-num">Wound Care</span>
      <strong>Topical Antimicrobial Dressings:</strong>
      <ul class="sub-list">
        <li><strong>Silver Sulfadiazine 1% cream</strong> (<em>Flamazine / Silvadene</em>): Broad-spectrum against Pseudomonas and MRSA. Apply 2–3 mm layer BD. (Avoid near eyes or in sulfa allergy).</li>
        <li><strong>Polymyxin-Bacitracin Ointment</strong> (<em>Polyfax</em>): Preferred for facial burns.</li>
      </ul>
    </div>
  </div>
</div>
"""
    },
    {
        "id": "ch23-topic-8",
        "num": 308,
        "chapter_num": 23,
        "chapter_name": "Emergency Medicine & Poisoning",
        "slug": "ch23-08-acute-poisoning-approach.html",
        "title": "General Approach to the Poisoned Patient (Toxidromes)",
        "category": "toxicology",
        "category_name": "Toxicology & Poisoning",
        "badge": "Toxidrome Matrix",
        "book_page": "pp. 703–707",
        "summary": "Master diagnostic matrix of acute clinical toxidromes (Anticholinergic, Cholinergic, Sympathomimetic, Sedative-Hypnotic, Opioid); emergency decontamination principles, activated charcoal indications, urine alkalinization, and definitive targeted antidotes.",
        "content": """
<div class="clinical-section">
  <h4><i class="fa-solid fa-table-cells"></i> 1. The 5 Major Clinical Toxidromes</h4>
  <p>A "toxidrome" is a constellation of clinical signs and symptoms that points to a specific toxic class of drug or chemical, allowing immediate emergency recognition prior to toxicological lab confirmation:</p>
  <div class="table-responsive">
    <table class="med-table">
      <thead>
        <tr><th>Toxidrome</th><th>Pupils</th><th>Vitals (HR, BP, Temp)</th><th>Skin & Mucosa</th><th>CNS & Hallmarks</th><th>Common Agents</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Anticholinergic</strong></td>
          <td><strong>Mydriasis</strong> (Large dilated, sluggish)</td>
          <td>Tachycardia, Hypertension, Hyperthermia</td>
          <td><strong>Dry, hot, flushed skin</strong>, dry mouth, urinary retention</td>
          <td>Agitation, delirium, hallucinations ("mad as a hatter, red as a beet, dry as a bone, hot as a hare, blind as a bat")</td>
          <td>Atropine, Tricyclic antidepressants (Amitriptyline), Antihistamines, Scopolamine, Datura.</td>
        </tr>
        <tr>
          <td><strong>Cholinergic</strong></td>
          <td><strong>Miosis</strong> (Pinpoint pupils)</td>
          <td>Bradycardia, Variable BP, Hypothermia</td>
          <td><strong>Diaphoresis (Profuse sweating)</strong>, salivation, lacrimation</td>
          <td>Fasciculations, muscle flaccidity, confusion, coma, bronchorrhea</td>
          <td>Organophosphates, Carbamates, Nerve agents, Pilocarpine, Neostigmine.</td>
        </tr>
        <tr>
          <td><strong>Sympathomimetic</strong></td>
          <td><strong>Mydriasis</strong> (Large dilated)</td>
          <td>Severe Tachycardia, Severe Hypertension, Hyperthermia</td>
          <td><strong>Diaphoresis (Sweaty, wet skin)</strong> &rarr; Distinguishes from anticholinergic!</td>
          <td>Extreme agitation, paranoia, tremors, seizures, cardiac arrhythmias</td>
          <td>Cocaine, Amphetamines, Methamphetamine ("Ice"), MDMA/Ecstasy, Pseudoephedrine.</td>
        </tr>
        <tr>
          <td><strong>Sedative-Hypnotic</strong></td>
          <td>Normal / Mid-dilated</td>
          <td>Bradycardia, Hypotension, Hypothermia, Bradypnea</td>
          <td>Dry or normal, cool extremities</td>
          <td>Stupor, coma, ataxia, slurred speech, hyporeflexia. Minimal respiratory depression alone.</td>
          <td>Benzodiazepines (Valium, Xanax), Barbiturates, Alcohol, Zolpidem.</td>
        </tr>
        <tr>
          <td><strong>Opioid</strong></td>
          <td><strong>Pinpoint (Miosis)</strong></td>
          <td>Severe Bradypnea, Bradycardia, Hypotension, Hypothermia</td>
          <td>Cool, clammy, cyanotic skin</td>
          <td><strong>The Opioid Triad:</strong> Coma, Pinpoint pupils, and severe <strong>Respiratory Depression (&lt; 8 breaths/min)</strong>.</td>
          <td>Heroin, Morphine, Methadone, Fentanyl, Tramadol, Codeine.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4><i class="fa-solid fa-pills"></i> 2. Master Specific Antidote Reference Directory</h4>
  <div class="table-responsive">
    <table class="med-table">
      <thead>
        <tr><th>Toxic Agent / Poison</th><th>Specific Antidote</th><th>Emergency Dosing Regimen</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Opioids (Heroin, Morphine, Fentanyl)</strong></td>
          <td><strong>Naloxone (Narcan)</strong></td>
          <td>0.4 mg to 2.0 mg IV/IM/SC/Intranasal. Repeat q2-3min until spontaneous breathing &ge; 10/min. (Caution: Shorter half-life than opioids; observe for rebound sedation).</td>
        </tr>
        <tr>
          <td><strong>Benzodiazepines (Valium, Lexotanil)</strong></td>
          <td><strong>Flumazenil (Anexate)</strong></td>
          <td>0.2 mg IV over 30 sec, then 0.3 mg q1min (max 3 mg). <em>(Caution: Contraindicated in chronic benzo dependence or co-ingestion of TCAs due to lethal refractory seizures!).</em></td>
        </tr>
        <tr>
          <td><strong>Paracetamol (Panadol)</strong></td>
          <td><strong>N-Acetylcysteine (NAC)</strong></td>
          <td>150 mg/kg loading dose over 1h &rarr; 50 mg/kg over 4h &rarr; 100 mg/kg over 16h IV.</td>
        </tr>
        <tr>
          <td><strong>Organophosphates / Carbamates</strong></td>
          <td><strong>Atropine + Pralidoxime</strong></td>
          <td>Atropine 2–3 mg IV doubled q5min until dry lungs + PAM 1–2g IV over 30 min.</td>
        </tr>
        <tr>
          <td><strong>Beta-Blockers (Propranolol, Atenolol)</strong></td>
          <td><strong>Glucagon + High-Dose Insulin</strong></td>
          <td>Glucagon 5–10 mg IV bolus + High-dose Insulin Euglycemia (1 unit/kg bolus + 1 unit/kg/hr infusion with 10% Dextrose).</td>
        </tr>
        <tr>
          <td><strong>Tricyclic Antidepressants (TCAs)</strong></td>
          <td><strong>Sodium Bicarbonate 8.4%</strong></td>
          <td>1 to 2 mmol/kg (approx 50–100 mL of 8.4% NaHCO3) IV push for wide QRS &gt; 100 ms or ventricular dysrhythmias.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""
    },
    {
        "id": "ch23-topic-9",
        "num": 309,
        "chapter_num": 23,
        "chapter_name": "Emergency Medicine & Poisoning",
        "slug": "ch23-09-acute-pain-management.html",
        "title": "Emergency Acute Pain Management & WHO Ladder",
        "category": "resuscitation",
        "category_name": "Emergency Resuscitation",
        "badge": "Analgesia Protocol",
        "book_page": "pp. 708–712",
        "summary": "Systematic acute pain assessment using Visual Analog Scale (VAS); WHO 3-step analgesic ladder adapted for acute emergency care, multimodal opioid-sparing analgesia, IV paracetamol/ketorolac protocols, and localized Pakistani analgesics (Provas, Toradol, Tramal, Kinz, Synflex).",
        "content": """
<div class="clinical-section">
  <h4><i class="fa-solid fa-chart-simple"></i> 1. Pain Assessment & The Visual Analog Scale (VAS)</h4>
  <p>Pain is the "5th Vital Sign". Rapid, objective pain assessment dictates the immediate analgesic tier:</p>
  <div class="steps-grid">
    <div class="step-card">
      <span class="step-num">Mild (1–3)</span>
      <strong>VAS 1 to 3:</strong> Mild discomfort, pain is tolerable, does not disrupt conversation or sleep.
    </div>
    <div class="step-card">
      <span class="step-num">Moderate (4–6)</span>
      <strong>VAS 4 to 6:</strong> Moderate pain, interferes with movement, concentration, and respiration. Patient is grimacing.
    </div>
    <div class="step-card">
      <span class="step-num">Severe (7–10)</span>
      <strong>VAS 7 to 10:</strong> Severe, excruciating, overwhelming pain. Inability to lie still, crying, writhing in agony, tachycardia, diaphoresis.
    </div>
  </div>

  <h4><i class="fa-solid fa-stairs"></i> 2. The Emergency WHO Analgesic Ladder (Pakistani Brands)</h4>
  <div class="table-responsive">
    <table class="med-table">
      <thead>
        <tr><th>Pain Tier (VAS)</th><th>Analgesic Class & Drug</th><th>Pakistani Brand Names</th><th>Dosage & Route</th><th>Clinical Pearls</th></tr>
      </thead>
      <tbody>
        <tr>
          <td rowspan="2"><strong>Step 1: Mild Pain (VAS 1–3)</strong></td>
          <td><strong>Paracetamol</strong></td>
          <td><em>Infusion Provas 1g / 100mL</em><br><em>Tab Panadol 500mg</em></td>
          <td>1 g IV infusion over 15 min or 1 g PO QDS (max 4 g/day).</td>
          <td>Non-opioid foundation; excellent safety profile, zero gastrointestinal/renal toxicity.</td>
        </tr>
        <tr>
          <td><strong>NSAIDs</strong></td>
          <td><em>Tab Synflex 550mg (Naproxen)</em><br><em>Tab Brufen 400mg (Ibuprofen)</em></td>
          <td>Synflex 550mg PO BD or Brufen 400mg TDS with meals.</td>
          <td>Inhibits peripheral COX-1/COX-2. (Contraindicated in active peptic ulcer, CKD, or third-trimester pregnancy).</td>
        </tr>
        <tr>
          <td rowspan="2"><strong>Step 2: Moderate Pain (VAS 4–6)</strong></td>
          <td><strong>Weak Opioid + Non-Opioid</strong></td>
          <td><em>Cap/Inj Tramal 50mg / 100mg</em> (Tramadol)</td>
          <td>50 mg to 100 mg IV slow push / PO TDS (max 400 mg/day).</td>
          <td>Dual action: mu-opioid agonist + SNRI reuptake inhibitor. Co-prescribe antiemetic (<em>Inj Maxolon 10mg</em>) due to nausea.</td>
        </tr>
        <tr>
          <td><strong>IV NSAID (Short Course)</strong></td>
          <td><em>Inj Toradol 30mg / 1mL</em> (Ketorolac)</td>
          <td>30 mg IV/IM stat, then 15–30 mg q6h PRN (max 5 consecutive days).</td>
          <td>Potent parenteral analgesia comparable to morphine in renal colic and musculoskeletal trauma.</td>
        </tr>
        <tr>
          <td rowspan="2"><strong>Step 3: Severe Pain (VAS 7–10)</strong></td>
          <td><strong>Strong Opioid (Nalbuphine)</strong></td>
          <td><em>Inj Kinz 10mg / 20mg</em> (Nalbuphine HCl)</td>
          <td><strong>10 mg to 20 mg IV slow push or deep IM</strong> q3-6h PRN.</td>
          <td>Mixed kappa-agonist / mu-antagonist. <strong>Widely used in Pakistani emergency rooms</strong> because it produces potent analgesia with a plateau "ceiling effect" on respiratory depression.</td>
        </tr>
        <tr>
          <td><strong>Pure Strong Opioid (Morphine)</strong></td>
          <td><em>Inj Morphine 10mg / 1mL</em></td>
          <td><strong>0.1 mg/kg IV titrated in 2–4 mg boluses q5-10min</strong> until pain score &lt; 4.</td>
          <td>Gold standard for polytrauma and STEMI cardiac chest pain. Ensure Naloxone is immediately available at bedside.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""
    }
]
