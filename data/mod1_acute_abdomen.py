# -*- coding: utf-8 -*-
"""
Module 1: Acute Abdomen Core Approach (Topics 1 - 5)
Doctor on Duty 3rd Edition — Chapter 17 (Book pp. 409-418)
"""

TOPICS = [
    {
        "id": "topic-1",
        "num": 1,
        "title": "Approach to the Management of Acute Abdomen",
        "category": "acute-abdomen",
        "category_name": "Acute Abdomen",
        "badge": "Clinical Approach",
        "book_page": "pp. 409–414",
        "summary": "Systematic bedside evaluation of acute abdominal pain: SOCRATES history, review of systems, pain character, diagnostic gestures, physical exam, and ruling out the 8 critical life-threatening etiologies.",
        "content": """
<div class="clinical-section">
  <h4><i class="fa-solid fa-clipboard-list"></i> 1. Presenting Complaint & History of Presenting Complaint</h4>
  <p>Make your clinical approach in a case of acute abdomen using the structured <strong>SOCRATES / OPQRST</strong> framework:</p>
  <div class="steps-grid">
    <div class="step-card">
      <span class="step-num">1</span>
      <strong>Onset:</strong> When did the chief complaint occur? Gradual, rapid, or sudden? Intermittent or constant?
    </div>
    <div class="step-card">
      <span class="step-num">2</span>
      <strong>Duration:</strong> When do symptoms occur? At night, constant, in the mornings, or postprandial?
    </div>
    <div class="step-card">
      <span class="step-num">3</span>
      <strong>Progression:</strong> Is the problem getting worse or better? Any specific activities or interventions that modify it?
    </div>
    <div class="step-card">
      <span class="step-num">4</span>
      <strong>Aggravating Factors:</strong> Movement, deep breathing, coughing, food intake, defecation.
    </div>
    <div class="step-card">
      <span class="step-num">5</span>
      <strong>Radiation:</strong> Where does pain radiate?
      <ul class="sub-list">
        <li>Left chest &rarr; left arm/jaw: Suggestive of Ischemic Heart Disease (ACS).</li>
        <li>Flank &rarr; groin/scrotum: Feature of ureteric calculus (stone colic).</li>
        <li>Epigastrium &rarr; right scapula/shoulder: Biliary pathology (phrenic nerve/C3-C5 dermatome).</li>
        <li>Epigastrium &rarr; mid-back: Acute pancreatitis or penetrating posterior ulcer.</li>
      </ul>
    </div>
    <div class="step-card">
      <span class="step-num">6</span>
      <strong>Relieving Factors:</strong> Relief with food, antacids, vomiting, sitting upright, or leaning forward.
    </div>
    <div class="step-card">
      <span class="step-num">7</span>
      <strong>Scale (Severity):</strong> Numerical rating scale of 1 to 10 (1 = mild, 10 = worst imaginable pain).
    </div>
    <div class="step-card">
      <span class="step-num">8</span>
      <strong>Site:</strong> Anatomical quadrant or region (RUQ, Epigastrium, LUQ, RLQ, LLQ, Suprapubic, Umbilical).
    </div>
    <div class="step-card">
      <span class="step-num">9</span>
      <strong>Associated Symptoms:</strong> Nausea, vomiting (early in high small bowel obstruction; late/persistent in distal obstruction). Ask if there is anything else the patient has noticed.
    </div>
  </div>

  <h4><i class="fa-solid fa-stethoscope"></i> 2. Review of Systems (ROS) Checklist</h4>
  <div class="table-responsive">
    <table class="med-table">
      <thead>
        <tr><th>System</th><th>Key Symptoms & Clinical Significance</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="badge badge-info">Systemic</span></td>
          <td>Fever, chills, rigors, jaundice, unexplained weight loss, anorexia, malaise, functional disability.</td>
        </tr>
        <tr>
          <td><span class="badge badge-warning">Upper GI</span></td>
          <td>Dysphagia, odynophagia, indigestion, heartburn/pyrosis, nausea, vomiting, haematemesis, waterbrash.</td>
        </tr>
        <tr>
          <td><span class="badge badge-danger">Lower GI</span></td>
          <td>Diarrhoea, absolute constipation (obstipation), melaena (black tarry stool), hematochezia (fresh rectal bleeding), steatorrhoea.</td>
        </tr>
        <tr>
          <td><span class="badge badge-primary">Genitourinary</span></td>
          <td>Increased frequency, dysuria, urgency, gross or microscopic haematuria, loin pain.</td>
        </tr>
        <tr>
          <td><span class="badge badge-purple">Gynaecological</span></td>
          <td>Length of menstrual cycle, amount of bleeding, dysmenorrhoea, intermenstrual bleeding, Last Menstrual Period (LMP mandatory to exclude ectopic).</td>
        </tr>
        <tr>
          <td><span class="badge badge-secondary">Background</span></td>
          <td>Complete detail of Past Medical History, Surgical History, Drug History (NSAIDs, anticoagulants, steroids), Family History, Social History (alcohol, smoking).</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4><i class="fa-solid fa-bolt"></i> 3. Character of Pain</h4>
  <div class="pill-cloud">
    <span class="pill-item"><i class="fa-solid fa-fire"></i> <strong>Burning:</strong> Peptic ulcer disease, severe reflux, gastritis</span>
    <span class="pill-item"><i class="fa-solid fa-hand-fist"></i> <strong>Gripping Heaviness:</strong> Cardiac ischemia / mesenteric ischemia</span>
    <span class="pill-item"><i class="fa-solid fa-weight-hanging"></i> <strong>Dull Ache:</strong> Visceral organ distension, early appendicitis, hepatitis</span>
    <span class="pill-item"><i class="fa-solid fa-heart-pulse"></i> <strong>Throbbing:</strong> Abscess formation (anorectal, hepatic, retroperitoneal)</span>
    <span class="pill-item"><i class="fa-solid fa-burst"></i> <strong>Stabbing / Crushing:</strong> Perforation of hollow viscus, ruptured aneurysm, dissection</span>
    <span class="pill-item"><i class="fa-solid fa-wave-square"></i> <strong>Colicky (Spasmodic):</strong> Bowel obstruction, ureteric colic, biliary colic</span>
  </div>

  <h4><i class="fa-solid fa-user-doctor"></i> 4. Patient Gestures in Pain Analysis</h4>
  <div class="callout callout-info">
    <ul class="styled-list">
      <li><strong>Squeezing gesture over chest/epigastrium:</strong> Describes ischemic cardiac pain (Levine sign).</li>
      <li><strong>Hand on flank gripping toward groin:</strong> Describes acute renal / ureteric colic.</li>
      <li><strong>Rubbing retrosternal area up and down:</strong> Heartburn / severe reflux esophagitis.</li>
      <li><strong>Rubbing buttock and lateral thigh:</strong> Sciatica / nerve root compression.</li>
      <li><strong>Arms clenched tightly around mid-abdomen & rocking:</strong> Midgut colic / early bowel obstruction.</li>
      <li><strong>Lying motionless with knees flexed, afraid to breathe or move:</strong> Generalized peritonitis (perforated viscus).</li>
    </ul>
  </div>

  <h4><i class="fa-solid fa-triangle-exclamation"></i> 5. First Rule Out Critical Life-Threatening Etiologies</h4>
  <div class="cards-subgrid">
    <div class="subcard">
      <div class="subcard-header danger-header"><i class="fa-solid fa-heart-pulse"></i> 1. Acute Coronary Syndrome (ACS)</div>
      <p>Heavy, dull, pressure/squeezing substernal or epigastric pain radiating to left shoulder/arm/jaw. Nausea, diaphoresis, syncope, anxiety.</p>
      <div class="diag-tags"><strong>Dx:</strong> ECG (ST elevation/depression, T-inversions), Troponin, TTE (wall motion abnormalities).</div>
    </div>
    <div class="subcard">
      <div class="subcard-header danger-header"><i class="fa-solid fa-lungs"></i> 2. Acute Mesenteric Ischemia</div>
      <p>Age &gt; 60 yrs, atrial fibrillation, thrombophilia, vascular disease. <em>Hallmark: Pain out of proportion to physical exam findings!</em> Severe diffuse distension, vomiting, hematochezia.</p>
      <div class="diag-tags"><strong>Dx:</strong> Marked Lactic acidosis, hyperkalemia, leukocytosis; CT Angiography (arterial occlusion, pneumatosis intestinalis).</div>
    </div>
    <div class="subcard">
      <div class="subcard-header danger-header"><i class="fa-solid fa-droplet"></i> 3. Ruptured / Impending Abdominal Aortic Aneurysm (AAA)</div>
      <p>Age &gt; 50 yrs, sudden severe central abdominal/back pain, shock, hypotension, pulsatile midline mass, Grey Turner / Cullen signs.</p>
      <div class="diag-tags"><strong>Dx:</strong> Bedside Ultrasound (aortic diameter &gt; 3cm, retroperitoneal fluid); CT/MR Angiography in stable patients.</div>
    </div>
    <div class="subcard">
      <div class="subcard-header danger-header"><i class="fa-solid fa-radiation"></i> 4. GI Perforation & Peritonitis</div>
      <p>Sudden severe diffuse pain, board-like rigidity, involuntary guarding, rebound tenderness, absent bowel sounds, loss of liver dullness on percussion.</p>
      <div class="diag-tags"><strong>Dx:</strong> Erect Chest X-ray / Abdominal X-ray showing free air under diaphragm (pneumoperitoneum).</div>
    </div>
    <div class="subcard">
      <div class="subcard-header danger-header"><i class="fa-solid fa-shield-virus"></i> 5. Aortic Dissection</div>
      <p>Sudden severe, sharp, tearing chest or abdominal pain radiating to the back. Asymmetrical pulses / blood pressure deficit, syncope, new aortic regurgitation murmur.</p>
      <div class="diag-tags"><strong>Dx:</strong> D-dimer, CXR widening of mediastinum, CT Angiography chest/abdomen (intimal flap with true & false lumen).</div>
    </div>
    <div class="subcard">
      <div class="subcard-header warning-header"><i class="fa-solid fa-bacterium"></i> 6. Acute Appendicitis</div>
      <p>Periumbilical pain migrating to right iliac fossa (RLQ), anorexia, low-grade fever, McBurney tenderness, Rovsing/Psoas/Obturator signs.</p>
      <div class="diag-tags"><strong>Dx:</strong> CBC (neutrophilic leukocytosis), USG abdomen/pelvis, CT abdomen with contrast.</div>
    </div>
    <div class="subcard">
      <div class="subcard-header warning-header"><i class="fa-solid fa-arrows-split-up-and-left"></i> 7. Mechanical Bowel Obstruction</div>
      <p>Colicky pain, obstipation (no flatus/feces), bilious/feculent vomiting, tympanic distension, high-pitched tinkling sounds or absent sounds, empty collapsed rectum.</p>
      <div class="diag-tags"><strong>Dx:</strong> Plain X-ray erect/supine (dilated loops &gt; 3cm, multiple air-fluid levels), CT abdomen transition point.</div>
    </div>
    <div class="subcard">
      <div class="subcard-header warning-header"><i class="fa-solid fa-capsules"></i> 8. Peptic Ulcer Disease (PUD)</div>
      <p>Epigastric gnawing pain; Duodenal ulcer relieved by food; Gastric ulcer exacerbated by food. NSAID use history, anemia, occult bleeding.</p>
      <div class="diag-tags"><strong>Dx:</strong> CBC, FOBT, H. pylori urea breath test, EGD (esophagogastroduodenoscopy).</div>
    </div>
  </div>
</div>
"""
    },
    {
        "id": "topic-2",
        "num": 2,
        "title": "Differential Diagnosis and Causes of Acute Abdomen",
        "category": "acute-abdomen",
        "category_name": "Acute Abdomen",
        "badge": "Anatomical Matrix",
        "book_page": "p. 415",
        "summary": "Master diagnostic differential matrix categorizing acute abdomen into gastrointestinal vs non-gastrointestinal causes across all anatomical abdominal quadrants.",
        "content": """
<div class="clinical-section">
  <p class="lead-text">Accurate anatomical localization is the single most valuable initial discriminator in acute abdomen. Below is the systematic Gastrointestinal vs Non-Gastrointestinal etiology matrix:</p>

  <div class="table-responsive">
    <table class="med-table diff-table">
      <thead>
        <tr>
          <th style="width: 22%;">Anatomical Quadrant</th>
          <th style="width: 39%;">Gastrointestinal Causes</th>
          <th style="width: 39%;">Non-Gastrointestinal Causes</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong class="text-primary"><i class="fa-solid fa-compass"></i> Right Upper Quadrant (RUQ)</strong></td>
          <td>
            <ul class="compact-list">
              <li>Acute cholecystitis & biliary colic</li>
              <li>Cholelithiasis & Choledocholithiasis</li>
              <li>Acute ascending cholangitis</li>
              <li>Hepatitis & Acute hepatic congestion</li>
              <li>Pyogenic / Amoebic liver abscess</li>
              <li>Duodenal ulcer / Perforated ulcer</li>
            </ul>
          </td>
          <td>
            <ul class="compact-list">
              <li>Right lower lobe pneumonia / pleurisy</li>
              <li>Pulmonary embolism (RLL)</li>
              <li>Subphrenic abscess</li>
              <li>Right pyelonephritis / Renal calculus</li>
              <li>Fitz-Hugh-Curtis syndrome (perihepatitis)</li>
              <li>Herpes zoster (thoracic dermatome)</li>
            </ul>
          </td>
        </tr>
        <tr>
          <td><strong class="text-primary"><i class="fa-solid fa-compass"></i> Epigastrium</strong></td>
          <td>
            <ul class="compact-list">
              <li>Peptic ulcer disease (Gastric / Duodenal)</li>
              <li>Acute pancreatitis</li>
              <li>GERD / Severe gastritis</li>
              <li>Early acute appendicitis (visceral pain phase)</li>
              <li>Mallory-Weiss tear / Boerhaave syndrome</li>
              <li>Gastric outlet obstruction</li>
            </ul>
          </td>
          <td>
            <ul class="compact-list">
              <li>Acute Coronary Syndrome (Inferior MI)</li>
              <li>Acute pericarditis</li>
              <li>Aortic dissection (thoracoabdominal)</li>
              <li>Rupturing Abdominal Aortic Aneurysm (AAA)</li>
              <li>Pneumonia / Pleurisy</li>
            </ul>
          </td>
        </tr>
        <tr>
          <td><strong class="text-primary"><i class="fa-solid fa-compass"></i> Left Upper Quadrant (LUQ)</strong></td>
          <td>
            <ul class="compact-list">
              <li>Acute gastritis & gastric ulcer</li>
              <li>Acute pancreatitis (tail pathology)</li>
              <li>Splenic flexure colitis / diverticulitis</li>
            </ul>
          </td>
          <td>
            <ul class="compact-list">
              <li>Splenic infarction or rupture / hematoma</li>
              <li>Splenic abscess</li>
              <li>Left lower lobe pneumonia / pleurisy</li>
              <li>Left pyelonephritis / Renal colic</li>
              <li>Myocardial infarction</li>
            </ul>
          </td>
        </tr>
        <tr>
          <td><strong class="text-primary"><i class="fa-solid fa-compass"></i> Right Lower Quadrant (RLQ)</strong></td>
          <td>
            <ul class="compact-list">
              <li><strong>Acute appendicitis</strong> (most common)</li>
              <li>Cecal diverticulitis</li>
              <li>Meckel's diverticulitis</li>
              <li>Terminal ileitis (Crohn's disease, Yersinia)</li>
              <li>Mesenteric adenitis (especially children)</li>
              <li>Incarcerated / strangulated right hernia</li>
            </ul>
          </td>
          <td>
            <ul class="compact-list">
              <li>Right ureteric colic / Pyelonephritis</li>
              <li>Ruptured ectopic pregnancy (life-threatening!)</li>
              <li>Right ovarian torsion / Ruptured ovarian cyst</li>
              <li>Pelvic Inflammatory Disease (PID) / Salpingitis</li>
              <li>Endometriosis</li>
              <li>Testicular torsion / Epididymo-orchitis</li>
            </ul>
          </td>
        </tr>
        <tr>
          <td><strong class="text-primary"><i class="fa-solid fa-compass"></i> Left Lower Quadrant (LLQ)</strong></td>
          <td>
            <ul class="compact-list">
              <li><strong>Acute diverticulitis</strong> (sigmoid colon)</li>
              <li>Sigmoid volvulus</li>
              <li>Ulcerative colitis / Infectious colitis</li>
              <li>Ischemic colitis</li>
              <li>Incarcerated / strangulated left hernia</li>
            </ul>
          </td>
          <td>
            <ul class="compact-list">
              <li>Left ureteric colic / Pyelonephritis</li>
              <li>Ruptured ectopic pregnancy</li>
              <li>Left ovarian torsion / Ruptured cyst</li>
              <li>Pelvic Inflammatory Disease (PID)</li>
              <li>Endometriosis</li>
              <li>Testicular torsion / Epididymo-orchitis</li>
            </ul>
          </td>
        </tr>
        <tr>
          <td><strong class="text-primary"><i class="fa-solid fa-compass"></i> Suprapubic / Pelvic</strong></td>
          <td>
            <ul class="compact-list">
              <li>Acute appendicitis (pelvic anatomical position)</li>
              <li>Diverticulitis</li>
              <li>Distal bowel obstruction</li>
            </ul>
          </td>
          <td>
            <ul class="compact-list">
              <li>Acute urinary retention (distended bladder)</li>
              <li>Acute cystitis / Prostatitis</li>
              <li>Pelvic Inflammatory Disease / Endometritis</li>
              <li>Pregnancy complications / Dysmenorrhea</li>
            </ul>
          </td>
        </tr>
        <tr>
          <td><strong class="text-primary"><i class="fa-solid fa-compass"></i> Diffuse / Generalized</strong></td>
          <td>
            <ul class="compact-list">
              <li>Generalized secondary peritonitis (perforated viscus)</li>
              <li>Acute mesenteric ischemia</li>
              <li>Mechanical bowel obstruction (advanced)</li>
              <li>Gastroenteritis</li>
              <li>Paralytic ileus</li>
            </ul>
          </td>
          <td>
            <ul class="compact-list">
              <li>Diabetic Ketoacidosis (DKA)</li>
              <li>Acute intermittent porphyria</li>
              <li>Addisonian crisis / Adrenal insufficiency</li>
              <li>Uremia</li>
              <li>Familial Mediterranean Fever (FMF)</li>
              <li>Ruptured Abdominal Aortic Aneurysm (AAA)</li>
            </ul>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""
    },
    {
        "id": "topic-3",
        "num": 3,
        "title": "Diagnostic Approach of Acute Abdomen",
        "category": "acute-abdomen",
        "category_name": "Acute Abdomen",
        "badge": "Laboratory Workup",
        "book_page": "p. 416",
        "summary": "Evidence-guided laboratory investigations for acute abdomen, test interpretations, sensitivity/specificity, and pre-test probability management.",
        "content": """
<div class="clinical-section">
  <p class="lead-text">The diagnostic laboratory workup must be guided by pre-test probability, vital signs stability, and specific diagnostic hypotheses:</p>

  <div class="lab-grid">
    <div class="lab-card">
      <div class="lab-card-title"><i class="fa-solid fa-vial"></i> Complete Blood Count (CBC)</div>
      <ul>
        <li><strong>Leukocytosis (WBC &gt; 11,000/&mu;L) with left shift (&ge; 75% neutrophils):</strong> Highly suggestive of acute bacterial inflammation (appendicitis, cholecystitis, diverticulitis, abscess).</li>
        <li><strong>Hematocrit (Hct):</strong> Elevated Hct (hemoconcentration) signifies intravascular volume depletion (severe dehydration, bowel obstruction, pancreatitis third-spacing). Low Hct signifies acute occult hemorrhage (ruptured AAA, ectopic pregnancy, splenic rupture, hemorrhagic pancreatitis).</li>
      </ul>
    </div>

    <div class="lab-card">
      <div class="lab-card-title"><i class="fa-solid fa-kidneys"></i> Renal Profile & Electrolytes (UCE)</div>
      <ul>
        <li><strong>Blood Urea Nitrogen (BUN) & Serum Creatinine:</strong> Evaluates dehydration, prerenal azotemia, acute kidney injury (AKI), or hepatorenal syndrome.</li>
        <li><strong>Serum Electrolytes (Na+, K+, Cl-, HCO3-):</strong> Detects severe hypokalemia/hypochloremic metabolic alkalosis from persistent vomiting, or hyperkalemia from bowel necrosis and tissue breakdown.</li>
      </ul>
    </div>

    <div class="lab-card">
      <div class="lab-card-title"><i class="fa-solid fa-liver"></i> Liver Function Tests (LFTs)</div>
      <ul>
        <li><strong>Cholestatic Markers:</strong> Elevated Total & Direct Bilirubin, Alkaline Phosphatase (ALP), and Gamma-Glutamyl Transferase (GGT) strongly indicate biliary obstruction (choledocholithiasis, cholangitis, extrinsic compression).</li>
        <li><strong>Aminotransferases (ALT, AST):</strong> Extreme elevations (&gt; 1,000 U/L) suggest acute viral/toxic hepatitis or acute ischemic hepatic injury; ALT &gt; 150 U/L in pancreatitis suggests gallstone etiology.</li>
      </ul>
    </div>

    <div class="lab-card">
      <div class="lab-card-title"><i class="fa-solid fa-fire-flame-curved"></i> Pancreatic Enzymes</div>
      <ul>
        <li><strong>Serum Lipase:</strong> The investigation of choice for acute pancreatitis. Highly specific and remains elevated for 8–14 days. Value &gt; 3&times; upper limit of normal is diagnostic.</li>
        <li><strong>Serum Amylase:</strong> Rises quickly (within 2–12 hours) but normalizes in 3–5 days. Less specific (can rise in perforated ulcer, bowel ischemia, ruptured ectopic, renal failure, salivary disease).</li>
      </ul>
    </div>

    <div class="lab-card">
      <div class="lab-card-title"><i class="fa-solid fa-shield-halved"></i> Inflammatory Markers & Sepsis</div>
      <ul>
        <li><strong>C-Reactive Protein (CRP):</strong> Levels &gt; 150 mg/L at 48–72 hours correlate strongly with severe/necrotizing pancreatitis or deep intra-abdominal sepsis.</li>
        <li><strong>Serum Procalcitonin:</strong> Excellent marker for systemic bacterial infection, septic shock, and infected pancreatic necrosis.</li>
        <li><strong>Arterial Blood Gas (ABG) & Serum Lactate:</strong> Elevated lactate (&gt; 2 mmol/L) with metabolic acidosis is a critical red flag for mesenteric ischemia, bowel gangrene, or septic shock.</li>
      </ul>
    </div>

    <div class="lab-card">
      <div class="lab-card-title"><i class="fa-solid fa-person-dress"></i> Mandatory Urinalysis & Pregnancy Test</div>
      <ul>
        <li><strong>Urine Pregnancy Test (&beta;-hCG):</strong> <em>MANDATORY in EVERY woman of reproductive age</em> presenting with acute abdominal or pelvic pain regardless of sexual or menstrual history, to rule out life-threatening ruptured ectopic pregnancy.</li>
        <li><strong>Urine Routine Examination (R/E):</strong> Hematuria suggests renal/ureteric stones; pyuria/nitrites indicate UTI. (Microscopic pyuria may occur in appendicitis if adjacent to ureter/bladder).</li>
      </ul>
    </div>
  </div>
</div>
"""
    },
    {
        "id": "topic-4",
        "num": 4,
        "title": "Radiological Approach of Acute Abdomen",
        "category": "acute-abdomen",
        "category_name": "Acute Abdomen",
        "badge": "Imaging Modalities",
        "book_page": "p. 417",
        "summary": "Selection criteria, sensitivity, specific signs, and diagnostic hierarchy for plain radiography, ultrasonography, contrast CT, and MRI/MRCP.",
        "content": """
<div class="clinical-section">
  <p class="lead-text">Initial imaging must be driven strictly by hemodynamic stability and the working clinical diagnosis:</p>

  <div class="imaging-cards">
    <div class="img-modal-card">
      <div class="img-header"><i class="fa-solid fa-film"></i> 1. Plain Radiography (X-Rays)</div>
      <div class="img-body">
        <p><strong>Erect Chest X-Ray (PA View):</strong> The single most sensitive plain radiograph for pneumoperitoneum. Capable of detecting as little as 1 mL of free intraperitoneal air under the right hemidiaphragm.</p>
        <p><strong>Abdominal X-Ray (Supine & Erect):</strong></p>
        <ul class="styled-list">
          <li><strong>Mechanical Small Bowel Obstruction:</strong> Centrally located dilated loops (&gt; 3 cm), valvulae conniventes extending across full bowel diameter, multiple air-fluid levels in a classic "step-ladder" pattern, and absence of colorectal gas.</li>
          <li><strong>Sigmoid Volvulus:</strong> Massive inverted "U-shaped" loop of dilated colon without haustra, originating from the pelvis and pointing toward the RUQ ("coffee-bean sign").</li>
          <li><strong>Cecal Volvulus:</strong> Dilated cecum pointing toward the LUQ ("kidney-bean sign").</li>
          <li><strong>Pneumatosis Intestinalis:</strong> Linear gas radiolucency within the bowel wall indicating transmural ischemia/infarction.</li>
          <li><strong>Stones:</strong> Only 15–20% of gallstones are radiopaque; 60–80% of urinary calculi are visible on KUB.</li>
        </ul>
      </div>
    </div>

    <div class="img-modal-card">
      <div class="img-header"><i class="fa-solid fa-wave-square"></i> 2. Ultrasonography (USG Whole Abdomen & Pelvis)</div>
      <div class="img-body">
        <p><strong>Primary Indications:</strong> First-line imaging of choice for suspected biliary disease, gynecological/pelvic pathology, pediatric acute abdomen, and pregnancy.</p>
        <ul class="styled-list">
          <li><strong>Acute Cholecystitis:</strong> Gallstones with acoustic shadowing, gallbladder wall thickening &gt; 3–4 mm, pericholecystic fluid halo, and a positive sonographic Murphy's sign (maximal probe tenderness over the imaged gallbladder).</li>
          <li><strong>Biliary Obstruction:</strong> Common bile duct (CBD) dilation (&gt; 6–8 mm in diameter).</li>
          <li><strong>Acute Appendicitis:</strong> Blind-ending, non-compressible, aperistaltic tubular structure &gt; 6 mm outer diameter in RLQ, target appearance in transverse view, appendicolith.</li>
          <li><strong>Gynecological Emergencies:</strong> Free fluid in pouch of Douglas, empty uterine cavity with adnexal mass / tubal ring sign (ectopic pregnancy), enlarged edematous ovary with decreased Doppler flow (ovarian torsion).</li>
          <li><strong>FAST Exam (Focused Assessment with Sonography for Trauma):</strong> Rapid bedside detection of hemoperitoneum in Morison's pouch, splenorenal recess, and pelvis.</li>
        </ul>
      </div>
    </div>

    <div class="img-modal-card">
      <div class="img-header"><i class="fa-solid fa-circle-notch"></i> 3. Computed Tomography (CT Abdomen & Pelvis)</div>
      <div class="img-body">
        <p><strong>The Gold Standard:</strong> Highest diagnostic accuracy for undifferentiated acute abdomen, peritonitis, retroperitoneal processes, and complications.</p>
        <ul class="styled-list">
          <li><strong>CT with IV Contrast:</strong> Standard for evaluating acute appendicitis, diverticulitis, mesenteric ischemia, bowel perforation, intra-abdominal abscesses, and acute pancreatitis.</li>
          <li><strong>Non-Contrast CT (CT KUB):</strong> Modality of choice for suspected acute renal and ureteric calculi (high sensitivity for tiny non-opaque stones).</li>
          <li><strong>CT Angiography (CTA):</strong> Mandatory for acute aortic dissection, ruptured AAA, and acute mesenteric arterial ischemia.</li>
        </ul>
      </div>
    </div>

    <div class="img-modal-card">
      <div class="img-header"><i class="fa-solid fa-magnet"></i> 4. Magnetic Resonance Imaging (MRI / MRCP)</div>
      <div class="img-body">
        <p><strong>Magnetic Resonance Cholangiopancreatography (MRCP):</strong> Non-invasive imaging of choice for common bile duct stones (choledocholithiasis) with sensitivity &gt; 95% and specificity &gt; 98%.</p>
        <p><strong>MRI Abdomen/Pelvis:</strong> Safe non-radiation alternative in pregnant patients when ultrasound is inconclusive (e.g., suspected appendicitis in pregnancy).</p>
      </div>
    </div>
  </div>
</div>
"""
    },
    {
        "id": "topic-5",
        "num": 5,
        "title": "Stepwise Management of Acute Abdomen",
        "category": "acute-abdomen",
        "category_name": "Acute Abdomen",
        "badge": "Resuscitation Protocol",
        "book_page": "p. 418",
        "summary": "11-step emergency resuscitation protocol: ABCD&E, venous access, goal-directed fluid resuscitation, analgesia, empiric antibiotics, decompression, and emergency surgical decision making.",
        "content": """
<div class="clinical-section">
  <div class="callout callout-danger">
    <strong><i class="fa-solid fa-bell"></i> Golden Rule of Acute Abdomen:</strong> Resuscitation must proceed simultaneously with diagnostic evaluation. Never delay emergency surgery or transfer to an operating room for prolonged unneeded investigations in an unstable patient!
  </div>

  <div class="protocol-timeline">
    <div class="timeline-step">
      <div class="timeline-badge">1</div>
      <div class="timeline-content">
        <h4>Primary Survey: ABCD&E Protocol</h4>
        <p>Assess and secure <strong>Airway</strong>, ensure adequate <strong>Breathing</strong> (administer high-flow oxygen via face mask if SpO2 &lt; 94% or in shock), support <strong>Circulation</strong>, assess <strong>Disability</strong> (GCS/pupils), and <strong>Expose</strong> the patient while preventing hypothermia.</p>
      </div>
    </div>

    <div class="timeline-step">
      <div class="timeline-badge">2</div>
      <div class="timeline-content">
        <h4>Intravenous Access & Emergency Blood Sampling</h4>
        <p>Establish two large-bore peripheral IV cannulae (16G or 18G) immediately. Draw blood for emergency cross-matching (at least 2–4 units packed RBCs), CBC, Urea, Creatinine, Electrolytes, LFTs, Serum Amylase/Lipase, PT, APTT, INR, and &beta;-hCG.</p>
      </div>
    </div>

    <div class="timeline-step">
      <div class="timeline-badge">3</div>
      <div class="timeline-content">
        <h4>Aggressive Goal-Directed Fluid Resuscitation</h4>
        <p>Administer isotonic crystalloids (<strong>Ringer's Lactate</strong> or <strong>0.9% Normal Saline</strong>). In hypotensive patients, deliver a rapid bolus of 500–1000 mL IV over 15–30 minutes. Target: Mean Arterial Pressure (MAP) &ge; 65 mmHg, urine output &gt; 0.5 mL/kg/hour, heart rate &lt; 100 bpm.</p>
      </div>
    </div>

    <div class="timeline-step">
      <div class="timeline-badge">4</div>
      <div class="timeline-content">
        <h4>Strict NPO (Nil Per Os) & Bowel Rest</h4>
        <p>Strict bowel rest. Keep patient completely fasting until emergency surgical conditions have been conclusively ruled out or patient enters the OR.</p>
      </div>
    </div>

    <div class="timeline-step">
      <div class="timeline-badge">5</div>
      <div class="timeline-content">
        <h4>Gastrointestinal Decompression (NG Tube)</h4>
        <p>Pass a wide-bore <strong>Nasogastric (NG) tube</strong> with continuous low-pressure suction in patients with persistent vomiting, gross abdominal distension, intestinal obstruction, or paralytic ileus to prevent aspiration pneumonia.</p>
      </div>
    </div>

    <div class="timeline-step">
      <div class="timeline-badge">6</div>
      <div class="timeline-content">
        <h4>Urinary Foley Catheterization</h4>
        <p>Insert a Foley catheter with an hourly urometer bag to strictly monitor fluid balance and assess resuscitation efficacy.</p>
      </div>
    </div>

    <div class="timeline-step">
      <div class="timeline-badge">7</div>
      <div class="timeline-content">
        <h4>Early Judicious Analgesia (Myth Dispelled!)</h4>
        <p><em>Clinical Fact:</em> Providing titrated analgesia does NOT mask physical signs or impair diagnostic accuracy. Administer IV analgesia promptly once initial evaluation is underway:</p>
        <ul class="styled-list">
          <li><strong>IV Paracetamol:</strong> 1g (Provas) IV infusion over 15 min TDS.</li>
          <li><strong>IV Ketorolac:</strong> 30mg (Toradol) in 100ml NS IV (only if renal function is normal and no active bleeding).</li>
          <li><strong>IV Opioid Option:</strong> Inj Nalbuphine 10mg (Kinz) or Tramadol 50–100mg (Tramol) + Inj Dimenhydrinate 50mg (Gravinate) diluted in 100ml 0.9% NS IV slow infusion.</li>
        </ul>
      </div>
    </div>

    <div class="timeline-step">
      <div class="timeline-badge">8</div>
      <div class="timeline-content">
        <h4>Empiric IV Antibiotic Therapy (Within 1 Hour)</h4>
        <p>For patients with suspected peritonitis, bowel perforation, septic shock, or acute intra-abdominal sepsis, initiate broad-spectrum coverage within the first hour:</p>
        <div class="rx-box">
          <div class="rx-header"><span class="rx-icon">Rx</span> Empiric Peritoneal Sepsis Regimen:</div>
          <div class="rx-body">
            <p><strong>1. Inj. Ceftriaxone</strong> 1g to 2g (Rocephin, Titan) &times; IV &times; BD</p>
            <p><strong>PLUS 2. Inj. Metronidazole</strong> 500mg/100ml (Flagyl) &times; IV &times; TDS</p>
            <p><em>In Penicillin/Cephalosporin Allergy:</em> Inf. Ciprofloxacin 400mg/100ml (Novidate) IV BD + Flagyl 500mg IV TDS</p>
            <p><em>If Septic Shock / Multi-Drug Resistance:</em> Inj. Piperacillin/Tazobactam 4.5g (Tanzo, Tazocin) IV TDS OR Inj. Meropenem 1g (Meronem) IV TDS</p>
          </div>
        </div>
      </div>
    </div>

    <div class="timeline-step">
      <div class="timeline-badge">9</div>
      <div class="timeline-content">
        <h4>Gastroprotection & Antiemetics</h4>
        <p><strong>Inj. Omeprazole</strong> 40mg (Risek, Ruling) IV OD diluted in 100ml NS.</p>
        <p><strong>Inj. Ondansetron</strong> 8mg (Onset) IV OR <strong>Inj. Dimenhydrinate</strong> 50mg (Gravinate) IV TDS.</p>
      </div>
    </div>

    <div class="timeline-step">
      <div class="timeline-badge">10</div>
      <div class="timeline-content">
        <h4>Correction of Coagulopathy & Electrolytes</h4>
        <p>Correct hypokalemia, hypomagnesemia, and acidosis. If INR &gt; 1.5 and urgent surgery required, administer Fresh Frozen Plasma (FFP 10–15 mL/kg), Prothrombin Complex Concentrate (PCC), and IV Vitamin K (10mg slow IV).</p>
      </div>
    </div>

    <div class="timeline-step">
      <div class="timeline-badge">11</div>
      <div class="timeline-content">
        <h4>Urgent Surgical Consultation & Theatre Transfer</h4>
        <p>Immediate operating theatre transfer for exploratory laparotomy or diagnostic laparoscopy in:</p>
        <ul class="styled-list">
          <li>Free intraperitoneal gas (pneumoperitoneum)</li>
          <li>Generalized peritonitis with abdominal rigidity</li>
          <li>Unstable ruptured AAA or ruptured ectopic pregnancy</li>
          <li>Strangulated bowel obstruction or mesenteric ischemia</li>
          <li>Blunt/penetrating trauma with refractory hemodynamic instability</li>
        </ul>
      </div>
    </div>
  </div>
</div>
"""
    }
]
