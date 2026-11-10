# -*- coding: utf-8 -*-
"""
Module 2: Hepatobiliary, Pancreas & Appendix (Topics 6 - 10, 15)
Doctor on Duty 3rd Edition — Chapter 17 (Book pp. 419-425, 429-431)
"""

TOPICS = [
    {
        "id": "topic-6",
        "num": 6,
        "title": "Acute Appendicitis",
        "category": "hpb-pancreas",
        "category_name": "HPB & Appendix",
        "badge": "High Yield Surgical Emergency",
        "book_page": "p. 419",
        "summary": "Pathophysiology, classical periumbilical-to-RLQ pain migration, physical exam signs (McBurney, Rovsing, Psoas, Obturator), Alvarado Score (MANTRELS), ultrasound/CT, and definitive medical-surgical protocol.",
        "content": """
<div class="clinical-section">
  <div class="row-2col">
    <div class="col-main">
      <h4><i class="fa-solid fa-stethoscope"></i> Clinical Features & Physical Signs</h4>
      <p><strong>Chief Complaints (C/C):</strong></p>
      <ul class="styled-list">
        <li><strong>Abdominal Pain:</strong> Initial dull periumbilical pain for the first 12–24 hours (visceral pain from midgut small bowel origin), which then migrates and localizes sharply to the Right Iliac Fossa / Right Lower Quadrant (RIF/RLQ) due to somatic irritation of the parietal peritoneum by the inflamed appendix.</li>
        <li><strong>Constitutional Symptoms:</strong> Anorexia ("if patient is hungry, question the diagnosis of appendicitis!"), nausea, vomiting (typically occurs <em>after</em> pain onset), and low-grade pyrexia.</li>
        <li><strong>Urinary Symptoms:</strong> Burning micturition (dysuria) or urinary frequency can occur if an inflamed retrocecal or pelvic appendix lies directly in contact with the right ureter or bladder wall.</li>
      </ul>

      <h4><i class="fa-solid fa-hand-holding-medical"></i> Physical Examination Findings</h4>
      <ul class="styled-list">
        <li><strong>Pediatric Caution:</strong> Always examine the throat and ears in children to exclude mesenteric adenitis secondary to viral tonsillitis/pharyngitis.</li>
        <li><strong>Vitals:</strong> Mildly elevated pulse rate (+/-) and low-grade fever (+/-). Marked high fever (&gt; 38.5&deg;C) indicates perforation or periappendiceal abscess.</li>
        <li><strong>McBurney's Point Tenderness:</strong> Maximal tenderness at junction of lateral 1/3 and medial 2/3 of a line from ASIS to umbilicus.</li>
        <li><strong>Rebound Tenderness (Blumberg Sign):</strong> Sudden release of deep palpation produces sharp pain indicating local peritonitis.</li>
        <li><strong>Rovsing's Sign:</strong> Deep palpation of the Left Lower Quadrant (LLQ) produces referred pain in the Right Lower Quadrant (RLQ).</li>
        <li><strong>Psoas Sign:</strong> Pain on passive hyperextension of the right hip while lying in left lateral position (suggests retrocecal appendicitis touching the psoas muscle).</li>
        <li><strong>Obturator Sign:</strong> Pain on passive internal rotation of the flexed right hip (suggests pelvic appendicitis irritating the obturator internus).</li>
        <li><strong>Digital Rectal Examination (DRE):</strong> Right-sided pelvic tenderness if pelvic appendix is present.</li>
      </ul>

      <h4><i class="fa-solid fa-flask"></i> Laboratory & Imaging Workup</h4>
      <div class="pill-cloud">
        <span class="pill-item"><strong>CBC:</strong> Neutrophilic leukocytosis (WBC &gt; 10,000/&mu;L, &ge; 75% neutrophils)</span>
        <span class="pill-item"><strong>Urine R/E:</strong> Nitrites negative (rules out uncomplicated UTI)</span>
        <span class="pill-item"><strong>Urine Pregnancy Test:</strong> Mandatory in all reproductive-age females to exclude ruptured ectopic</span>
        <span class="pill-item"><strong>Ultrasound:</strong> Non-compressible, aperistaltic blind loop &gt; 6 mm, target sign</span>
        <span class="pill-item"><strong>CT Abdomen with Contrast:</strong> Diagnostic gold standard (periappendiceal fat stranding, appendicolith, abscess)</span>
      </div>
    </div>

    <div class="col-side">
      <div class="calc-box" id="alvarado-box">
        <h4><i class="fa-solid fa-calculator"></i> Alvarado Score (MANTRELS)</h4>
        <p class="calc-sub">Interactive 10-Point Scoring System</p>
        <div class="calc-checks">
          <label class="calc-label"><input type="checkbox" class="alv-check" data-pts="1"> <strong>M</strong>igration of pain to RLQ (1 pt)</label>
          <label class="calc-label"><input type="checkbox" class="alv-check" data-pts="1"> <strong>A</strong>norexia (1 pt)</label>
          <label class="calc-label"><input type="checkbox" class="alv-check" data-pts="1"> <strong>N</strong>ausea / Vomiting (1 pt)</label>
          <label class="calc-label"><input type="checkbox" class="alv-check" data-pts="2"> <strong>T</strong>enderness in RLQ (2 pts)</label>
          <label class="calc-label"><input type="checkbox" class="alv-check" data-pts="1"> <strong>R</strong>ebound tenderness (1 pt)</label>
          <label class="calc-label"><input type="checkbox" class="alv-check" data-pts="1"> <strong>E</strong>levated temperature &gt; 37.3&deg;C (1 pt)</label>
          <label class="calc-label"><input type="checkbox" class="alv-check" data-pts="2"> <strong>L</strong>eukocytosis &gt; 10,000/&mu;L (2 pts)</label>
          <label class="calc-label"><input type="checkbox" class="alv-check" data-pts="1"> <strong>S</strong>hift to the left &ge; 75% neutrophils (1 pt)</label>
        </div>
        <div class="calc-result">
          <div class="score-display">Total Score: <span id="alv-score" class="score-badge">0 / 10</span></div>
          <div id="alv-interp" class="interp-text">Score &le; 4: Appendicitis unlikely (Low risk). Consider outpatient observation.</div>
        </div>
      </div>
    </div>
  </div>

  <h4><i class="fa-solid fa-prescription"></i> Stepwise Clinical Management & Prescription (Rx)</h4>
  <div class="rx-box">
    <div class="rx-header"><span class="rx-icon">Rx</span> Inpatient Appendicitis Protocol:</div>
    <div class="rx-body">
      <ol class="rx-ordered-list">
        <li><strong>Maintain ABCD&E:</strong> Vital signs monitoring (BP, PR, RR, Temperature, SpO2).</li>
        <li><strong>IV Access:</strong> Pass two large-bore IV cannulae (16G or 18G).</li>
        <li><strong>Laboratory Orders:</strong> Send CBC, Blood Urea, Serum Creatinine, Electrolytes, LFTs, PT/APTT/INR, Viral Markers (Anti-HCV, HBsAg), Blood Grouping & Cross-match, and RBS.</li>
        <li><strong>Strict NPO (Bowel Rest):</strong> No oral feeds until surgical decision.</li>
        <li><strong>Gastrointestinal Decompression:</strong> Pass Nasogastric (NG) tube and Foley's catheterization for urine output record.</li>
        <li><strong>IV Fluid Hydration:</strong>
          <br>&bull; Inf. Ringer's Lactate (R/L) &times; IV &times; BD
          <br>&bull; Inf. 0.9% Normal Saline (NS) OR D5%W &times; IV &times; OD (adjust for losses).
        </li>
        <li><strong>Empiric IV Antibiotics (Preoperative Prophylaxis):</strong>
          <div class="med-item">
            <span class="drug-name">&bull; Inj. Ceftriaxone 1g</span> (Brands: <span class="brand">Rocephin, Titan, Cefotax</span>) &times; IV &times; BD
            <br><strong>PLUS</strong> <span class="drug-name">Inj. Metronidazole 500mg/100ml</span> (Brand: <span class="brand">Flagyl</span>) &times; IV &times; TDS
          </div>
        </li>
        <li><strong>IV Pain Management / Analgesia:</strong>
          <div class="med-item">
            &bull; <span class="drug-name">Inj. Paracetamol 1g/100ml</span> (Brands: <span class="brand">Provas, Paracet</span>) &times; IV infusion &times; TDS / SOS
            <br>&bull; <em>OR</em> <span class="drug-name">Inj. Ketorolac 30mg/ml</span> (Brand: <span class="brand">Toradol</span>) in 4–8ml 0.9% NS &times; IV
            <br>&bull; <em>OR for Severe Pain:</em> <span class="drug-name">Inj. Tramadol 100mg/2ml</span> (Brand: <span class="brand">Tramol</span>) + <span class="drug-name">Inj. Dimenhydrinate 50mg/ml</span> (Brand: <span class="brand">Gravinate</span>) diluted in 100ml 0.9% NS &times; IV slow
            <br>&bull; <em>OR</em> <span class="drug-name">Inj. Nalbuphine 10mg/ml</span> (Brand: <span class="brand">Kinz</span>) + <span class="drug-name">Inj. Dimenhydrinate 50mg</span> (Gravinate) diluted in 100ml NS &times; IV
          </div>
        </li>
        <li><strong>Gastroprotection:</strong>
          <br>&bull; <span class="drug-name">Inj. Omeprazole 40mg</span> (Brands: <span class="brand">Risek, Ruling</span>) &times; IV diluted in 100ml 0.9% NS &times; OD
        </li>
        <li><strong>Antiemetic Therapy:</strong>
          <br>&bull; <span class="drug-name">Inj. Metoclopramide 10mg/2ml</span> (Brand: <span class="brand">Metaclon</span>) &times; IV &times; TDS
          <br>&bull; <em>OR</em> <span class="drug-name">Inj. Dimenhydrinate 50mg/ml</span> (Brand: <span class="brand">Gravinate</span>) &times; IV &times; TDS
          <br>&bull; <em>OR</em> <span class="drug-name">Inj. Ondansetron 8mg/4ml</span> (Brands: <span class="brand">Onset, Onseron</span>) diluted in 50–100ml 0.9% NS &times; IV over 15 min.
        </li>
        <li><strong>Definitive Surgical Intervention:</strong> After completion of preoperative resuscitation, arrange blood transfusion if indicated and transfer to the Operation Theatre for <strong>Emergency Laparoscopic or Open Appendectomy</strong>.</li>
      </ol>
    </div>
  </div>
</div>
"""
    },
    {
        "id": "topic-7",
        "num": 7,
        "title": "Acute Cholecystitis",
        "category": "hpb-pancreas",
        "category_name": "HPB & Appendix",
        "badge": "Tokyo Guidelines 2018",
        "book_page": "pp. 420–421",
        "summary": "Pathophysiology, 6 Fs risk factors, Murphy & Boas signs, Tokyo Guidelines diagnostic criteria and severity grading (Grades I–III), critical Ceftriaxone avoidance warning, and emergency cholecystostomy.",
        "content": """
<div class="clinical-section">
  <h4><i class="fa-solid fa-triangle-exclamation"></i> Pathophysiology & Presentation</h4>
  <p><strong>Etiology & Risk Factors:</strong> Gallbladder stone impaction in cystic duct &rarr; acute luminal distension, mucosal ischemia, chemical inflammation, and secondary bacterial proliferation. Classically associated with the <strong>Rule of 6 Fs:</strong> <em>Fat, Female, Forty, Flatulent, Fertile, and Fair-skinned</em>.</p>

  <p><strong>Chief Complaints (C/C):</strong></p>
  <ul class="styled-list">
    <li>Right Hypochondriac (RHC / RUQ) severe, constant, sharp pain due to local peritoneal irritation.</li>
    <li>Pain is typically prolonged (lasting &gt; 6 hours), distinguishing it from simple uncomplicated biliary colic (&lt; 6 hours).</li>
    <li>Postprandial exacerbation (especially after heavy, fatty meals).</li>
    <li><strong>Referred Pain:</strong> Radiates to the right shoulder and right infrascapular area (Boas sign) due to phrenic nerve (C3–C5 dermatome) sensory irritation.</li>
    <li>Associated fever, malaise, anorexia, nausea, and vomiting.</li>
  </ul>

  <h4><i class="fa-solid fa-stethoscope"></i> Physical Examination Findings</h4>
  <ul class="styled-list">
    <li><strong>Murphy's Sign Positive:</strong> Sudden inspiratory arrest (pause in breathing) upon deep palpation of the right upper quadrant during inspiration due to sharp pain when the inflamed gallbladder touches the examiner's fingers. (May be falsely negative in elderly &gt; 60 years).</li>
    <li><strong>Boas' Sign:</strong> Hyperesthesia to light touch in the right lower scapular or infrascapular zone.</li>
    <li><strong>Palpable Mass:</strong> A tender, tense, rounded mass (swollen gallbladder covered by omentum) may be palpable in the RUQ in 30–40% of cases.</li>
    <li><strong>Jaundice:</strong> Mild jaundice can occur, but deep jaundice indicates common bile duct obstruction (choledocholithiasis or Mirizzi syndrome).</li>
  </ul>

  <h4><i class="fa-solid fa-table-list"></i> Tokyo Guidelines (TG18) Diagnostic Criteria</h4>
  <div class="table-responsive">
    <table class="med-table">
      <thead>
        <tr><th>Criterion Category</th><th>Clinical Features</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>A. Local Signs of Inflammation</strong></td>
          <td>Murphy's sign, RUQ pain, tenderness, or palpable RUQ mass.</td>
        </tr>
        <tr>
          <td><strong>B. Systemic Signs of Inflammation</strong></td>
          <td>Fever, elevated C-Reactive Protein (CRP &gt; 3 mg/dL), Leukocytosis (WBC &gt; 10,000/&mu;L).</td>
        </tr>
        <tr>
          <td><strong>C. Radiological Findings</strong></td>
          <td>Ultrasound findings characteristic of acute cholecystitis (GB wall &gt; 4 mm, pericholecystic fluid halo, sonographic Murphy's, impacted stone).</td>
        </tr>
      </tbody>
    </table>
  </div>
  <p><strong>Diagnostic Interpretation:</strong></p>
  <ul>
    <li><em>Suspected Diagnosis:</em> One item from A + One item from B.</li>
    <li><em>Definite Diagnosis:</em> One item from A + One item from B + Confirmatory imaging from C.</li>
  </ul>

  <h4><i class="fa-solid fa-layer-group"></i> Tokyo Guidelines Severity Grading & Definitive Management</h4>
  <div class="cards-subgrid">
    <div class="subcard">
      <div class="subcard-header primary-header">Grade I (Mild Acute Cholecystitis)</div>
      <p>Healthy patient with mild gallbladder inflammation and NO organ dysfunction.</p>
      <div class="diag-tags"><strong>Management:</strong> Early laparoscopic cholecystectomy within 24–72 hours of admission.</div>
    </div>
    <div class="subcard">
      <div class="subcard-header warning-header">Grade II (Moderate Acute Cholecystitis)</div>
      <p>Associated with any of: WBC &gt; 18,000/&mu;L, palpable tender RUQ mass, symptom duration &gt; 72 hours, or marked local inflammation (gangrenous, emphysematous, pericholecystic abscess).</p>
      <div class="diag-tags"><strong>Management:</strong> Empiric IV antibiotics + early laparoscopic cholecystectomy if low surgical risk; delayed/interval cholecystectomy if high surgical risk.</div>
    </div>
    <div class="subcard">
      <div class="subcard-header danger-header">Grade III (Severe Acute Cholecystitis)</div>
      <p>Accompanied by dysfunction of at least one organ system (Cardiovascular, Neurological, Respiratory, Renal, Hepatic, or Hematological).</p>
      <div class="diag-tags"><strong>Management:</strong> ICU resuscitation + IV antibiotics + Emergency Percutaneous Transhepatic Cholecystostomy (PTC) tube drainage.</div>
    </div>
  </div>

  <div class="callout callout-danger">
    <strong><i class="fa-solid fa-triangle-exclamation"></i> CRITICAL CLINICAL WARNING (Avoid Ceftriaxone):</strong>
    <p>Avoid Ceftriaxone in acute cholecystitis and biliary colic! According to clinical literature, patients receiving ceftriaxone can develop drug-induced biliary sludge (ceftriaxone pseudolithiasis), which precipitates existing gallstones, triggers acute cholecystitis, and causes biliary ductal obstruction.</p>
  </div>

  <h4><i class="fa-solid fa-prescription"></i> Inpatient Treatment Protocol (Rx)</h4>
  <div class="rx-box">
    <div class="rx-header"><span class="rx-icon">Rx</span> Acute Cholecystitis Medical & Pharmacological Regimen:</div>
    <div class="rx-body">
      <ol class="rx-ordered-list">
        <li>Maintain ABCD&E, two large-bore IV lines, vitals monitoring (BP, PR, RR, Temp, SpO2).</li>
        <li><strong>Strict NPO (Bowel Rest):</strong> 2–3 days.</li>
        <li><strong>Nasogastric (NG) Tube Aspiration:</strong> Aspiration of gastric HCl eliminates the cephalic/gastric stimulus for cholecystokinin (CCK) release and bile secretion, resting the gallbladder and reducing spasms. NG tube removed when tenderness subsides, followed by clear liquids.</li>
        <li><strong>IV Fluid Hydration:</strong> Inf. Ringer's Lactate &times; BD + 0.9% Normal Saline or D5%W &times; IV &times; OD.</li>
        <li><strong>Empiric IV Antibiotics (Ceftriaxone-Free Regimens):</strong>
          <div class="med-item">
            &bull; <span class="drug-name">Inj. Metronidazole 500mg/100ml</span> (Brand: <span class="brand">Flagyl</span>) &times; IV &times; TDS
            <br><strong>PLUS ONE OF THE FOLLOWING:</strong>
            <br>&bull; <span class="drug-name">Inj. Cefuroxime 750mg</span> (Brand: <span class="brand">Zinacef</span>) &times; IV &times; BD
            <br>&bull; <em>OR</em> <span class="drug-name">Inj. Ceftazidime 1g</span> (Brands: <span class="brand">Fortum, Fortazim</span>) &times; IV &times; BD
            <br>&bull; <em>OR</em> <span class="drug-name">Inf. Ciprofloxacin 400mg/100ml</span> (Brand: <span class="brand">Novidat</span>) &times; IV &times; BD
            <br>&bull; <em>In Severe / Grade II–III Sepsis:</em> <span class="drug-name">Inj. Piperacillin/Tazobactam 4.5g</span> (Tanzo) IV TDS OR <span class="drug-name">Inj. Meropenem 1g</span> (Meronem) IV TDS.
          </div>
        </li>
        <li><strong>IV Gastroprotection:</strong> <span class="drug-name">Inj. Omeprazole 40mg</span> (Brands: <span class="brand">Risek, Ruling</span>) &times; IV in 100ml NS &times; OD.</li>
        <li><strong>Analgesia:</strong> <span class="drug-name">Inj. Paracetamol 1g</span> (Provas) IV TDS / SOS OR <span class="drug-name">Inj. Ketorolac 30mg</span> (Toradol) IV OR <span class="drug-name">Inj. Tramadol 100mg</span> (Tramol) + <span class="drug-name">Gravinate 50mg</span> IV.</li>
        <li><strong>Antispasmodic for Biliary Spasm:</strong>
          <br>&bull; <span class="drug-name">Inj. Drotaverine 40mg to 80mg</span> (Brands: <span class="brand">Nospa, Relispa</span>) IV STAT
          <br>&bull; <em>OR</em> <span class="drug-name">Inj. Phloroglucinol + Trimethylphloroglucinol 40+0.04mg/4ml</span> (Brands: <span class="brand">Spasrid, Anafortan Plus, Spasfon</span>) diluted in 100ml 0.9% NS &times; IV STAT.
        </li>
        <li><strong>Surgical Intervention:</strong> Elective/Early Laparoscopic Cholecystectomy ideally within 24–72 hours of symptom onset. Interval cholecystectomy performed after 6–8 weeks in delayed presentations.</li>
      </ol>
    </div>
  </div>
</div>
"""
    },
    {
        "id": "topic-8",
        "num": 8,
        "title": "Cholelithiasis (Gallstones)",
        "category": "hpb-pancreas",
        "category_name": "HPB & Appendix",
        "badge": "Calculous Disease",
        "book_page": "p. 422",
        "summary": "Pathogenesis, types of gallstones (cholesterol vs black/brown pigment), biliary colic features, ultrasound acoustic shadowing, and elective laparoscopic cholecystectomy.",
        "content": """
<div class="clinical-section">
  <h4><i class="fa-solid fa-shapes"></i> Definition & Stone Classification</h4>
  <p><strong>Definition:</strong> Presence of abnormal concretions (calculi) within the gallbladder lumen. Female-to-male ratio is 2–3:1 with peak incidence &gt; 40 years.</p>
  <div class="table-responsive">
    <table class="med-table">
      <thead>
        <tr><th>Stone Type</th><th>Composition</th><th>Etiology & Characteristics</th><th>Radiopacity</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Cholesterol Stones</strong> (75–80%)</td>
          <td>&gt; 50% crystalline cholesterol monohydrate</td>
          <td>Bile supersaturation with cholesterol, gallbladder hypomotility, rapid nucleation. Associated with obesity, rapid weight loss, multiparity, clofibrate.</td>
          <td>Radiolucent (only 10–15% calcified)</td>
        </tr>
        <tr>
          <td><strong>Black Pigment Stones</strong> (10–15%)</td>
          <td>Calcium bilirubinate & copper polymers</td>
          <td>Chronic hemolysis (sickle cell, thalassemia, hereditary spherocytosis), cirrhosis, ileal resection. Sterile bile origin.</td>
          <td>Radiopaque (50–70% visible on X-ray)</td>
        </tr>
        <tr>
          <td><strong>Brown Pigment Stones</strong> (&lt; 5%)</td>
          <td>Calcium salts of unconjugated bilirubin & fatty acids</td>
          <td>Biliary tract infection (bacterial beta-glucuronidase), stasis, foreign bodies, biliary parasites (Clonorchis sinensis, Ascaris).</td>
          <td>Radiolucent</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4><i class="fa-solid fa-stethoscope"></i> Clinical Features: Asymptomatic vs Biliary Colic</h4>
  <ul class="styled-list">
    <li><strong>Asymptomatic Gallstones:</strong> &gt; 80% of patients remain completely asymptomatic throughout life (discovered incidentally on ultrasound).</li>
    <li><strong>Biliary Colic:</strong>
      <ul class="sub-list">
        <li>Constant, dull or aching pain in Right Upper Quadrant or epigastrium. (Despite the term "colic", the pain is typically steady and constant rather than fluctuating spasmodically).</li>
        <li><strong>Duration:</strong> Typically lasts 1 to 5 hours (&lt; 6 hours). Spontaneously subsides once the impacted stone falls back into the gallbladder lumen.</li>
        <li><strong>Triggers:</strong> Precipitated by ingestion of fatty or greasy meals (CCK release causes gallbladder contraction against the blocked neck).</li>
        <li><strong>Radiation:</strong> Radiates around the right costal margin to the epigastrium, right scapular tip, or mid-back.</li>
        <li>Early satiety, abdominal fullness, bloating, and dyspepsia.</li>
      </ul>
    </li>
  </ul>

  <h4><i class="fa-solid fa-x-ray"></i> Diagnostic Workup</h4>
  <div class="pill-cloud">
    <span class="pill-item"><strong>Ultrasound Abdomen:</strong> Investigation of choice (&gt; 95% sensitivity). Shows mobile echogenic foci with posterior acoustic shadowing.</span>
    <span class="pill-item"><strong>Plain X-Ray / CT:</strong> Rarely diagnostic (only 15–20% of gallstones have sufficient calcium to be radiopaque).</span>
    <span class="pill-item"><strong>LFTs:</strong> Completely normal in uncomplicated cholelithiasis.</span>
  </div>

  <h4><i class="fa-solid fa-prescription"></i> Management & Surgical Strategy (Rx)</h4>
  <div class="rx-box">
    <div class="rx-header"><span class="rx-icon">Rx</span> Cholelithiasis Management Protocol:</div>
    <div class="rx-body">
      <p><strong>1. Asymptomatic Gallstones:</strong> Watchful waiting. Prophylactic cholecystectomy is NOT indicated except in high-risk subsets: calcified porcelain gallbladder (high risk of carcinoma), stones &gt; 3 cm, congenital hemolytic anemia, or candidates for bariatric surgery.</p>
      <p><strong>2. Acute Episode of Biliary Colic:</strong></p>
      <ul>
        <li>Strict NPO, IV fluid hydration (0.9% NS / Ringer's Lactate).</li>
        <li>NSAIDs are first-line for pain: <span class="drug-name">Inj. Ketorolac 30mg</span> (Toradol) IV OR <span class="drug-name">Inj. Diclofenac 75mg</span> (Voltral) IM (NSAIDs inhibit prostaglandin-mediated gallbladder wall distension).</li>
        <li>Antispasmodic: <span class="drug-name">Inj. Drotaverine 40mg</span> (Nospa) IV STAT.</li>
      </ul>
      <p><strong>3. Definitive Gold Standard Treatment:</strong> <strong>Elective Laparoscopic Cholecystectomy</strong> (Day-case surgical procedure of choice).</p>
    </div>
  </div>
</div>
"""
    },
    {
        "id": "topic-9",
        "num": 9,
        "title": "Choledocholithiasis",
        "category": "hpb-pancreas",
        "category_name": "HPB & Appendix",
        "badge": "CBD Calculi",
        "book_page": "p. 423",
        "summary": "Common bile duct stones, cholestatic jaundice, MRCP vs ERCP diagnostics, laparoscopic bile duct exploration, and full antibiotic/analgesic regimens.",
        "content": """
<div class="clinical-section">
  <h4><i class="fa-solid fa-microscope"></i> Pathogenesis & Clinical Presentation</h4>
  <p><strong>Definition:</strong> Presence of gallstones within the Common Bile Duct (CBD). Primary stones form de novo within bile ducts (usually brown pigment); Secondary stones migrate from the gallbladder through the cystic duct (&gt; 90% of cases).</p>
  <p><em>Treatment is recommended in ALL patients with choledocholithiasis, even if asymptomatic, because of the high risk of life-threatening complications (acute cholangitis and acute pancreatitis).</em></p>

  <p><strong>Chief Complaints (C/C):</strong></p>
  <ul class="styled-list">
    <li><strong>Right Upper Quadrant / Epigastric Pain:</strong> More severe, deep, and prolonged (lasting &gt; 6 hours) than simple cholelithiasis, postprandial, radiating to the right scapula/back.</li>
    <li><strong>Extrahepatic Cholestatic Jaundice:</strong> Scleral icterus, tea-colored dark urine (conjugated hyperbilirubinemia), pale acholic clay-colored stools, and generalized pruritus (bile salt deposition in skin).</li>
    <li>Nausea, vomiting, anorexia.</li>
  </ul>

  <h4><i class="fa-solid fa-flask-vial"></i> Diagnostic Workup</h4>
  <div class="table-responsive">
    <table class="med-table">
      <thead>
        <tr><th>Investigation</th><th>Diagnostic Findings & Significance</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Liver Function Tests (LFTs)</strong></td>
          <td>Classic cholestasis pattern: Marked &uarr; Total & Direct Bilirubin, &uarr; Alkaline Phosphatase (ALP), &uarr; GGT. Mild to moderate elevation in ALT/AST.</td>
        </tr>
        <tr>
          <td><strong>Serum Lipase & Amylase</strong></td>
          <td>Mandatory to rule out secondary gallstone pancreatitis.</td>
        </tr>
        <tr>
          <td><strong>Ultrasound Abdomen</strong></td>
          <td>First imaging test. Detects gallbladder stones and <strong>dilated CBD (&gt; 8 mm)</strong> in patients with gallstones and jaundice. Direct visualization of CBD stones on US is only ~50% sensitive.</td>
        </tr>
        <tr>
          <td><strong>MRCP (Magnetic Resonance)</strong></td>
          <td>Non-invasive gold standard imaging. Sensitivity 95%, Specificity 98%. Accurately demonstrates stone size, number, and exact anatomical location.</td>
        </tr>
        <tr>
          <td><strong>ERCP (Endoscopic Retrograde)</strong></td>
          <td>Diagnostic AND therapeutic gold standard. Allows sphincterotomy, basket/balloon stone extraction, and stent placement.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4><i class="fa-solid fa-prescription"></i> Stepwise Treatment Protocol (Rx)</h4>
  <div class="rx-box">
    <div class="rx-header"><span class="rx-icon">Rx</span> Choledocholithiasis Medical & Surgical Protocol:</div>
    <div class="rx-body">
      <ol class="rx-ordered-list">
        <li>Maintain ABCD&E, two large-bore IV lines, vitals monitoring (BP, PR, RR, Temp, SpO2).</li>
        <li>Strict NPO, IV fluid therapy with Ringer's Lactate or 0.9% Normal Saline.</li>
        <li>Pass NG tube and Foley catheter if severe vomiting/distension.</li>
        <li><strong>Empiric IV Antibiotics (Covering Gram-negative coliforms & enterococci):</strong>
          <div class="med-item">
            &bull; <span class="drug-name">Inj. Metronidazole 500mg/100ml</span> (Flagyl) &times; IV &times; TDS
            <br><strong>PLUS ONE OF THE FOLLOWING:</strong>
            <br>&bull; <span class="drug-name">Inj. Ceftriaxone 1g</span> (Rocephin, Titan) &times; IV &times; BD
            <br>&bull; <em>OR</em> <span class="drug-name">Inf. Ciprofloxacin 400mg/100ml</span> (Novidate) &times; IV &times; BD
            <br>&bull; <em>OR</em> <span class="drug-name">Inj. Ceftazidime 1g</span> (Fortum) &times; IV &times; BD
            <br>&bull; <em>OR</em> <span class="drug-name">Inj. Cefepime 1g</span> (Uceph, Cefstar) &times; IV &times; BD
            <br>&bull; <em>If Severe Infection / High Risk:</em> <span class="drug-name">Inj. Imipenem-Cilastatin 500mg</span> (Tienam) IV TDS OR <span class="drug-name">Inj. Meropenem 1g</span> (Meronem) IV TDS OR <span class="drug-name">Inj. Piperacillin-Tazobactam 4.5g</span> (Tanzo) IV TDS.
          </div>
        </li>
        <li><strong>IV Pain Management:</strong>
          <br>&bull; <span class="drug-name">Inj. Ketorolac 30mg/ml</span> (Toradol) in 4–8ml 0.9% NS &times; IV
          <br>&bull; <em>OR</em> <span class="drug-name">Inj. Buprenorphine 0.3mg/ml</span> (Buepron, Norpin) + <span class="drug-name">Gravinate 50mg</span> in 100ml NS &times; IV
          <br>&bull; <em>OR</em> <span class="drug-name">Inj. Nalbuphine 10mg/ml</span> (Kinz) + <span class="drug-name">Gravinate 50mg</span> in 100ml NS &times; IV.
        </li>
        <li><strong>Gastroprotection:</strong> <span class="drug-name">Inj. Omeprazole 40mg</span> (Risek, Ruling) &times; IV &times; OD.</li>
        <li><strong>Surgical / Endoscopic Options for Duct Clearance:</strong>
          <ul class="sub-list">
            <li><strong>Option A (Two-Stage):</strong> Preoperative ERCP with endoscopic sphincterotomy (EST) and stone extraction, followed by elective interval laparoscopic cholecystectomy.</li>
            <li><strong>Option B (Single-Stage):</strong> Laparoscopic Cholecystectomy combined with Laparoscopic Common Bile Duct Exploration (LCBDE).</li>
            <li><strong>Option C:</strong> Mechanical lithotripsy or electrohydraulic/laser lithotripsy for large impacted CBD stones.</li>
          </ul>
        </li>
      </ol>
    </div>
  </div>
</div>
"""
    },
    {
        "id": "topic-10",
        "num": 10,
        "title": "Acute Cholangitis",
        "category": "hpb-pancreas",
        "category_name": "HPB & Appendix",
        "badge": "Life-Threatening Emergency",
        "book_page": "pp. 424–425",
        "summary": "Ascending biliary infection, Charcot's Triad, Reynolds' Pentad, Tokyo Guidelines diagnostic criteria and severity grading (Grades I–III), emergency ERCP biliary drainage, and critical resuscitation.",
        "content": """
<div class="clinical-section">
  <div class="callout callout-danger">
    <strong><i class="fa-solid fa-bell"></i> Critical Surgical Emergency:</strong> Acute ascending cholangitis is an infection of an obstructed biliary ductal system with high potential for rapid progression to fatal septic shock. Immediate resuscitation, IV antibiotics, and urgent biliary decompression are life-saving!
  </div>

  <h4><i class="fa-solid fa-stethoscope"></i> Clinical Manifestations: The Classic Signs</h4>
  <div class="row-2col">
    <div class="col-main">
      <div class="subcard danger-border">
        <div class="subcard-header danger-header"><i class="fa-solid fa-triangle-exclamation"></i> Charcot's Cholangitis Triad (Present in 50–70%)</div>
        <ol class="styled-list">
          <li><strong>Right Upper Quadrant (RUQ) Abdominal Pain:</strong> Severe, constant biliary ache.</li>
          <li><strong>High Spiking Fever with Rigors/Chills:</strong> Intermittent bacteremia.</li>
          <li><strong>Jaundice:</strong> Dark urine, scleral icterus, fluctuating pale stools.</li>
        </ol>
      </div>
    </div>
    <div class="col-side">
      <div class="subcard danger-border">
        <div class="subcard-header danger-header"><i class="fa-solid fa-skull-crossbones"></i> Reynolds' Pentad (Severe Toxic Cholangitis)</div>
        <p>Charcot's Triad <strong>PLUS:</strong></p>
        <ol start="4" class="styled-list">
          <li><strong>Hypotension / Septic Shock:</strong> SBP &lt; 90 mmHg, cold clammy extremities.</li>
          <li><strong>Altered Mental Status / Confusion:</strong> Toxic encephalopathy, lethargy.</li>
        </ol>
      </div>
    </div>
  </div>

  <h4><i class="fa-solid fa-table-list"></i> Tokyo Guidelines (TG18) Diagnostic Criteria</h4>
  <div class="table-responsive">
    <table class="med-table">
      <thead>
        <tr><th>Criterion</th><th>Clinical & Laboratory Indicators</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>A. Systemic Inflammation</strong></td>
          <td>Fever and/or chills with rigors (&ge; 38.0&deg;C); WBC &lt; 4,000 or &gt; 10,000/&mu;L; elevated CRP.</td>
        </tr>
        <tr>
          <td><strong>B. Cholestasis</strong></td>
          <td>Jaundice (Total Bilirubin &ge; 2 mg/dL); abnormal LFTs (ALP, GGT, AST, ALT &gt; 1.5&times; ULN).</td>
        </tr>
        <tr>
          <td><strong>C. Imaging Findings</strong></td>
          <td>Biliary dilatation or evidence of underlying etiology (CBD stones, stricture, stent occlusion).</td>
        </tr>
      </tbody>
    </table>
  </div>
  <p><strong>Diagnostic Rule:</strong> Suspected = A + B (or C); Definite Diagnosis = A + B + C.</p>

  <h4><i class="fa-solid fa-layer-group"></i> Severity Grading (Tokyo Guidelines TG18)</h4>
  <div class="cards-subgrid">
    <div class="subcard">
      <div class="subcard-header primary-header">Grade I (Mild Acute Cholangitis)</div>
      <p>Responds to initial medical therapy; does not meet criteria for Grade II or Grade III.</p>
    </div>
    <div class="subcard">
      <div class="subcard-header warning-header">Grade II (Moderate Acute Cholangitis)</div>
      <p>Associated with any two of: WBC &gt; 12,000 or &lt; 4,000/&mu;L, Temperature &ge; 39.0&deg;C, Age &ge; 75 years, Total Bilirubin &ge; 5 mg/dL, or Serum Albumin &lt; 70% of lower normal limit.</p>
    </div>
    <div class="subcard">
      <div class="subcard-header danger-header">Grade III (Severe Acute Cholangitis)</div>
      <p>Accompanied by dysfunction in at least one organ system: Cardiovascular (hypotension requiring dopamine &ge; 5 &mu;g/kg/min or norepinephrine), Neurological (impaired consciousness), Respiratory (PaO2/FiO2 &lt; 300), Renal (oliguria, creatinine &gt; 2.0 mg/dL), Hepatic (PT-INR &gt; 1.5), or Hematological (platelets &lt; 100,000/&mu;L).</p>
    </div>
  </div>

  <h4><i class="fa-solid fa-prescription"></i> Emergency Resuscitation & Prescription (Rx)</h4>
  <div class="rx-box">
    <div class="rx-header"><span class="rx-icon">Rx</span> Acute Cholangitis Resuscitation & Antimicrobial Regimen:</div>
    <div class="rx-body">
      <ol class="rx-ordered-list">
        <li>Maintain ABCD&E, high-flow oxygen, two large-bore IV lines, continuous vitals and SpO2 monitoring.</li>
        <li><strong>Blood Cultures:</strong> Draw 2 sets of peripheral blood cultures immediately prior to starting antibiotics.</li>
        <li>Strict NPO, pass NG tube and Foley catheter (strict hourly urine monitoring).</li>
        <li><strong>Fluid Resuscitation:</strong> Aggressive IV boluses of Ringer's Lactate or Normal Saline (500–1000 mL boluses) to restore tissue perfusion.</li>
        <li><strong>Urgent Broad-Spectrum IV Antibiotics:</strong>
          <div class="med-item">
            &bull; <span class="drug-name">Inj. Metronidazole 500mg/100ml</span> (Flagyl) &times; IV &times; TDS
            <br><strong>PLUS ONE OF:</strong>
            <br>&bull; <span class="drug-name">Inj. Ceftriaxone 1g</span> (Rocephin, Titan) &times; IV &times; BD
            <br>&bull; <em>OR</em> <span class="drug-name">Inf. Ciprofloxacin 400mg/100ml</span> (Novidate) &times; IV &times; BD
            <br>&bull; <em>OR</em> <span class="drug-name">Inj. Ceftazidime 1g</span> (Fortum) &times; IV &times; BD
            <br>&bull; <em>OR</em> <span class="drug-name">Inj. Cefepime 1g</span> (Uceph) &times; IV &times; BD
            <br>&bull; <em>In Grade II / III (Severe) Cholangitis:</em> <span class="drug-name">Inj. Piperacillin-Tazobactam 4.5g</span> (Tanzo) IV TDS OR <span class="drug-name">Inj. Meropenem 1g</span> (Meronem) IV TDS.
          </div>
        </li>
        <li><strong>IV Analgesia:</strong> <span class="drug-name">Inj. Ketorolac 30mg</span> (Toradol) in 4ml NS IV. If severe pain: <span class="drug-name">Inj. Tramadol 100mg</span> (Tramol) OR <span class="drug-name">Inj. Nalbuphine 10mg</span> (Kinz) + <span class="drug-name">Gravinate 50mg</span> in 100ml NS IV slow.</li>
        <li><strong>Gastroprotection:</strong> <span class="drug-name">Inj. Omeprazole 40mg</span> (Risek, Ruling) &times; IV &times; OD.</li>
        <li><strong>EMERGENCY BILIARY DECOMPRESSION (The Definitive Life-Saving Step):</strong>
          <ul class="sub-list">
            <li><strong>Grade I:</strong> Antibiotics and supportive care; if no response within 24–48 hours, perform early biliary drainage.</li>
            <li><strong>Grade II:</strong> Early endoscopic (ERCP) or percutaneous transhepatic biliary drainage (PTBD) within 24–48 hours.</li>
            <li><strong>Grade III:</strong> <strong>Immediate emergency biliary drainage (ERCP with sphincterotomy/stenting or PTBD)</strong> along with intensive organ support in the ICU.</li>
          </ul>
        </li>
      </ol>
    </div>
  </div>
</div>
"""
    },
    {
        "id": "topic-15",
        "num": 15,
        "title": "Acute Pancreatitis",
        "category": "hpb-pancreas",
        "category_name": "HPB & Appendix",
        "badge": "Prognostic Scoring & Critical Care",
        "book_page": "pp. 429–431",
        "summary": "I GET SMASHED etiologies, Revised Atlanta classification, CTSI/MCTSI scoring, Ranson and BISAP criteria, goal-directed fluid therapy, enteral nutrition, and sterile vs infected necrosis management.",
        "content": """
<div class="clinical-section">
  <h4><i class="fa-solid fa-list-check"></i> Etiology: The Classic Mnemonic "I GET SMASHED"</h4>
  <div class="pill-cloud">
    <span class="pill-item"><strong>I:</strong> Idiopathic (15–25%), Infections (Mumps, Coxsackie, CMV, EBV, Ascaris)</span>
    <span class="pill-item"><strong>G:</strong> Gallstones (~40% of cases — most common cause worldwide!)</span>
    <span class="pill-item"><strong>E:</strong> Ethanol / Alcohol (20–30% of cases)</span>
    <span class="pill-item"><strong>T:</strong> Trauma (blunt abdominal trauma, handle-bar injury)</span>
    <span class="pill-item"><strong>S:</strong> Steroids (corticosteroids)</span>
    <span class="pill-item"><strong>M:</strong> Mumps, Malignancy (pancreatic adenocarcinoma, ampullary tumor)</span>
    <span class="pill-item"><strong>A:</strong> Autoimmune pancreatitis (IgG4-related disease)</span>
    <span class="pill-item"><strong>S:</strong> Scorpion venom / Spider bite</span>
    <span class="pill-item"><strong>H:</strong> Hypertriglyceridemia (&gt; 1,000 mg/dL), Hypercalcemia, Hereditary (PRSS1, SPINK1, CFTR)</span>
    <span class="pill-item"><strong>E:</strong> ERCP (post-procedural pancreatitis 2–5%)</span>
    <span class="pill-item"><strong>D:</strong> Drugs (Azathioprine, 6-MP, Statins, Sulfonamides, Metronidazole, Tetracycline, Thiazides, Furosemide, Valproate, Didanosine)</span>
  </div>

  <h4><i class="fa-solid fa-stethoscope"></i> Clinical Features & Physical Exam</h4>
  <ul class="styled-list">
    <li><strong>Abdominal Pain:</strong> Sudden onset of severe, excruciating, constant epigastric pain that characteristically radiates straight through to the mid-back (50% of cases). Exacerbated by lying supine and partially relieved by sitting upright and leaning forward (the "pancreatic position").</li>
    <li>Persistent nausea, retching, and bilious vomiting that does NOT relieve the abdominal pain.</li>
    <li>Abdominal distension, reduced or absent bowel sounds (due to localized or generalized paralytic ileus).</li>
    <li><strong>Signs of Retroperitoneal Hemorrhage (Severe Necrotizing Pancreatitis):</strong>
      <ul class="sub-list">
        <li><strong>Cullen's Sign:</strong> Periumbilical blue-purple ecchymosis (tracking of retroperitoneal blood along the falciform ligament).</li>
        <li><strong>Grey Turner's Sign:</strong> Flank ecchymosis / bruising (tracking of hemoperitoneum through the posterior pararenal space to abdominal wall).</li>
        <li><strong>Fox's Sign:</strong> Bruising over the upper anterior thigh below the inguinal ligament.</li>
      </ul>
    </li>
  </ul>

  <h4><i class="fa-solid fa-layer-group"></i> Prognostic Scoring & Severity Systems</h4>
  <div class="row-2col">
    <div class="col-main">
      <div class="subcard">
        <div class="subcard-header primary-header">Revised Atlanta Classification (2012)</div>
        <ul class="styled-list">
          <li><strong>Mild Acute Pancreatitis:</strong> Absence of organ failure AND absence of local or systemic complications. Resolves quickly.</li>
          <li><strong>Moderately Severe Acute Pancreatitis:</strong> Transient organ failure (resolves within &lt; 48 hours) AND/OR local complications (fluid collections, pseudocyst, necrosis).</li>
          <li><strong>Severe Acute Pancreatitis:</strong> Persistent organ failure (&gt; 48 hours), single or multiple organs (modified Marshall score &ge; 2 for shock, respiratory failure, or renal failure). Mortality 20–40%.</li>
        </ul>
      </div>

      <div class="subcard">
        <div class="subcard-header warning-header">CT Severity Index (CTSI / Balthazar) & Modified CTSI (MCTSI)</div>
        <p>CT scan is performed ideally <strong>&gt; 72 hours (or 5–7 days)</strong> after symptom onset (early CT underestimates necrosis):</p>
        <ul class="styled-list">
          <li><strong>Balthazar Grade:</strong> Normal (0), Enlargement (1), Peripancreatic inflammation (2), Single fluid collection (3), &ge; 2 collections / retroperitoneal gas (4).</li>
          <li><strong>Parenchymal Necrosis:</strong> None (0), &le; 30% (2), 30–50% (4), &gt; 50% (6).</li>
          <li><em>CTSI Interpretation:</em> 0–3 points: Mild; 4–6 points: Moderate; 7–10 points: Severe (high mortality).</li>
        </ul>
      </div>
    </div>

    <div class="col-side">
      <div class="subcard">
        <div class="subcard-header danger-header">Ranson's Criteria (11 Points)</div>
        <p><strong>At Admission (0 Hours) — GA LAW:</strong></p>
        <ul class="compact-list">
          <li>Glucose &gt; 200 mg/dL (11 mmol/L)</li>
          <li>Age &gt; 55 years</li>
          <li>LDH &gt; 350 IU/L</li>
          <li>AST &gt; 250 IU/L</li>
          <li>WBC &gt; 16,000/&mu;L</li>
        </ul>
        <p><strong>During First 48 Hours — C HOBBS:</strong></p>
        <ul class="compact-list">
          <li>Calcium (serum) &lt; 8 mg/dL (2 mmol/L)</li>
          <li>Hematocrit drop &gt; 10%</li>
          <li>Oxygen (PaO2) &lt; 60 mmHg</li>
          <li>BUN increase &gt; 5 mg/dL (1.8 mmol/L)</li>
          <li>Base deficit &gt; 4 mEq/L</li>
          <li>Sequestration of fluid &gt; 6 L</li>
        </ul>
        <p><em>Interpretation:</em> Score &ge; 3 indicates severe pancreatitis with high mortality.</p>
      </div>

      <div class="subcard">
        <div class="subcard-header primary-header">BISAP Score (Bedside Index)</div>
        <p>1 point for each at 24 hours: <strong>B</strong>UN &gt; 25 mg/dL; <strong>I</strong>mpaired mental status; <strong>S</strong>IRS &ge; 2 criteria; <strong>A</strong>ge &gt; 60; <strong>P</strong>leural effusion on CXR. Score &ge; 3 predicts high in-hospital mortality.</p>
      </div>
    </div>
  </div>

  <h4><i class="fa-solid fa-prescription"></i> Stepwise Management Protocol (Rx)</h4>
  <div class="rx-box">
    <div class="rx-header"><span class="rx-icon">Rx</span> Acute Pancreatitis Inpatient Protocol:</div>
    <div class="rx-body">
      <ol class="rx-ordered-list">
        <li><strong>Maintain ABCD&E:</strong> Oxygen therapy if hypoxic (SpO2 &lt; 94%). Establish two large-bore IV lines.</li>
        <li><strong>Laboratory Investigations:</strong> Serum Lipase (diagnostic), Amylase, CBC, BUN, Creatinine, Electrolytes, Serum Calcium, Blood Glucose, LFTs, CRP, Arterial Blood Gas (ABG), and Serum Lactate.</li>
        <li><strong>Goal-Directed IV Fluid Resuscitation (Cornerstone of Therapy):</strong>
          <ul class="sub-list">
            <li><strong>Fluid of Choice:</strong> Balanced crystalloids — <strong>Ringer's Lactate (LR)</strong> is preferred over Normal Saline (reduces systemic acidosis and SIRS).</li>
            <li><strong>Stable Patients:</strong> Infuse at 5–10 mL/kg/hour (250–500 mL/hour).</li>
            <li><strong>Unstable / Shock:</strong> Rapid bolus of 500–1000 mL over 15–30 minutes, repeated as needed.</li>
            <li><strong>Clinical Targets:</strong> Heart rate &lt; 120 bpm, MAP 65–85 mmHg, urine output &gt; 0.5–1.0 mL/kg/hour, and hematocrit between 35–44%.</li>
          </ul>
        </li>
        <li><strong>Nasogastric (NG) Tube:</strong> Not routinely required; indicated only for intractable vomiting or severe paralytic ileus/gastric distension.</li>
        <li><strong>Analgesia:</strong> Prompt multimodal analgesia. <span class="drug-name">Inj. Paracetamol 1g</span> (Provas) IV TDS + <span class="drug-name">Inj. Nalbuphine 10mg</span> (Kinz) or <span class="drug-name">Inj. Tramadol 100mg</span> (Tramol) + <span class="drug-name">Gravinate 50mg</span> in 100ml NS IV slow.</li>
        <li><strong>Nutritional Support:</strong> Early oral feeding with low-fat solid or liquid diet as soon as abdominal pain subsides and ileus resolves. Enteral tube feeding (NG or nasojejunal) is superior to TPN if oral feeds not tolerated.</li>
        <li><strong>Prophylactic Antibiotics:</strong> <em>NOT recommended for sterile acute pancreatitis!</em> Indicated ONLY for confirmed or strongly suspected <strong>infected necrosis</strong>:
          <div class="med-item">
            &bull; <span class="drug-name">Inj. Meropenem 1g</span> (Meronem) &times; IV &times; TDS
            <br>&bull; <em>OR</em> <span class="drug-name">Inj. Imipenem-Cilastatin 500mg</span> (Tienam) &times; IV &times; TDS
            <br>&bull; <em>OR</em> <span class="drug-name">Inf. Ciprofloxacin 400mg</span> &times; IV &times; BD + <span class="drug-name">Flagyl 500mg</span> &times; IV &times; TDS (drugs with proven pancreatic tissue penetration).
          </div>
        </li>
        <li><strong>Urgent Therapeutic ERCP (within 24–48 hours):</strong> Indicated for severe acute biliary pancreatitis with concurrent acute cholangitis or persistent common bile duct obstruction.</li>
      </ol>
    </div>
  </div>
</div>
"""
    }
]
