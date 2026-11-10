# -*- coding: utf-8 -*-
"""
Module 4: Peritoneal Sepsis & Peritonitis (Topics 17 - 18)
Doctor on Duty 3rd Edition — Chapter 17 (Book pp. 433-434)
"""

TOPICS = [
    {
        "id": "topic-17",
        "num": 17,
        "title": "Spontaneous Bacterial Peritonitis (SBP)",
        "category": "peritonitis",
        "category_name": "Peritoneal Sepsis",
        "badge": "Hepatology / Surgical Interface",
        "book_page": "p. 433",
        "summary": "Pathogenesis in decompensated cirrhosis, subtle presentation, diagnostic paracentesis (PMN >= 250/mm3), critical IV albumin prophylaxis for hepatorenal syndrome, IV Ceftriaxone, and lifetime secondary prophylaxis.",
        "content": """
<div class="clinical-section">
  <h4><i class="fa-solid fa-bacterium"></i> Pathogenesis & Clinical Presentation</h4>
  <p><strong>Definition:</strong> Monomicrobial bacterial infection of ascitic fluid in patients with advanced liver cirrhosis and portal hypertension, without an identifiable surgically treatable intra-abdominal source.</p>
  <p><strong>Mechanism:</strong> Bacterial translocation of enteric flora (predominantly <em>Escherichia coli</em> ~70%, <em>Klebsiella pneumoniae</em> ~15%, and <em>Streptococcus pneumoniae</em>) across an edematous bowel wall into mesenteric lymph nodes and ascitic fluid, exacerbated by impaired hepatic reticuloendothelial phagocytic clearance and deficient ascitic opsonic activity.</p>

  <p><strong>Clinical Signs & Symptoms (Often Subtle or Atypical!):</strong></p>
  <ul class="styled-list">
    <li>Symptoms may be surprisingly mild or absent in up to 30% of patients!</li>
    <li>Diffuse dull abdominal pain, abdominal tenderness, and rebound tenderness (+/-).</li>
    <li>Low-grade fever and chills, or hypothermia in advanced hepatic failure.</li>
    <li><strong>Worsening or Refractory Ascites:</strong> Sudden increase in ascites volume or resistance to diuretics.</li>
    <li><strong>New-Onset or Worsening Hepatic Encephalopathy:</strong> Confusion, asterixis, drowsiness, lethargy.</li>
    <li>Acute kidney injury, progressive oliguria, nausea, vomiting, or diarrhea.</li>
  </ul>

  <h4><i class="fa-solid fa-syringe"></i> Diagnostic Paracentesis: The Gold Standard</h4>
  <div class="callout callout-danger">
    <strong><i class="fa-solid fa-triangle-exclamation"></i> Mandatory Rule:</strong> Diagnostic paracentesis must be performed <em>WITHOUT DELAY</em> in every cirrhotic patient admitted with ascites, and always <em>BEFORE</em> the first dose of antibiotics!
  </div>

  <div class="table-responsive">
    <table class="med-table">
      <thead>
        <tr><th>Ascitic Fluid Parameter</th><th>Diagnostic Value for SBP</th><th>Clinical Interpretation</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Polymorphonuclear (PMN) Count</strong></td>
          <td><strong>&ge; 250 cells/mm&sup3; (&ge; 0.25 &times; 10&sup9;/L)</strong></td>
          <td><strong>DIAGNOSTIC OF SBP!</strong> Initiate empiric IV antibiotic therapy immediately.</td>
        </tr>
        <tr>
          <td><strong>Bedside Blood Culture Bottles</strong></td>
          <td>Inoculate 10 mL ascitic fluid at bedside</td>
          <td>Identifies causative single organism in 70–80% (monomicrobial).</td>
        </tr>
        <tr>
          <td><strong>Total Ascitic Protein</strong></td>
          <td>&lt; 1.0 g/dL</td>
          <td>Signifies poor opsonic activity and high risk for recurrent SBP.</td>
        </tr>
        <tr>
          <td><strong>Serum-Ascites Albumin Gradient (SAAG)</strong></td>
          <td>&ge; 1.1 g/dL</td>
          <td>Confirms portal hypertension etiology of ascites.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4><i class="fa-solid fa-prescription"></i> Emergency Resuscitation & Prescription (Rx)</h4>
  <div class="rx-box">
    <div class="rx-header"><span class="rx-icon">Rx</span> Inpatient SBP Medical Regimen:</div>
    <div class="rx-body">
      <ol class="rx-ordered-list">
        <li>Maintain ABCD&E, establish peripheral IV line, vitals monitoring (BP, PR, RR, Temp, SpO2).</li>
        <li><strong>Strict NPO initially;</strong> pass NG tube and Foley catheter if encephalopathic or distended.</li>
        <li><strong>Bowel Care & Encephalopathy Management:</strong>
          <br>&bull; <span class="drug-name">Syp. Lactulose 30ml</span> (Duphalac) &times; TDS orally or via NG tube (titrated to achieve 2–3 soft bowel movements/day and eliminate enteric nitrogenous toxins).
        </li>
        <li><strong>Empiric IV Antibiotic Therapy (Initiate Immediately):</strong>
          <div class="med-item">
            &bull; <span class="drug-name">Inj. Ceftriaxone 1g to 2g</span> (Brands: <span class="brand">Titan, Rocephin</span>) &times; IV &times; BD (or Cefotaxime 2g IV TDS) for 5–7 days.
            <br>&bull; <em>If Severe Sepsis / Nosocomial Infection:</em> <span class="drug-name">Inj. Meropenem 1g</span> (Meronem) IV TDS OR <span class="drug-name">Inj. Piperacillin-Tazobactam 4.5g</span> (Tanzo) IV TDS.
          </div>
        </li>
        <li><strong>INTRAVENOUS ALBUMIN INFUSION (Life-Saving for Renal Protection):</strong>
          <div class="med-item">
            <em>Clinical Trial Evidence:</em> Adding IV Albumin reduces the incidence of fatal Hepatorenal Syndrome (HRS) from 30% to 10% and significantly decreases mortality!
            <br>&bull; <strong>Dose 1 (Within 6 hours of diagnosis):</strong> <span class="drug-name">IV Human Albumin 20%</span> at <strong>1.5 g/kg body weight</strong>.
            <br>&bull; <strong>Dose 2 (On Day 3):</strong> <span class="drug-name">IV Human Albumin 20%</span> at <strong>1.0 g/kg body weight</strong>.
          </div>
        </li>
        <li><strong>Supportive Fluid & Electrolyte Care:</strong>
          <br>&bull; Inf. Dextrose 5% or 10% 1L &times; IV &times; STAT (exercise caution with sodium fluids in ascites).
        </li>
        <li><strong>Discontinue Nephrotoxic Agents:</strong> Immediately stop NSAIDs, aminoglycosides, and ACE inhibitors. Temporarily withhold non-selective beta-blockers (propranolol/carvedilol) if SBP &lt; 90 mmHg.</li>
        <li><strong>Long-Term Secondary Prophylaxis (Indefinite until Liver Transplant):</strong>
          <div class="med-item">
            &bull; <span class="drug-name">Tab. Ciprofloxacin 500mg</span> (Novidate) &times; 1 tab OD orally
            <br>&bull; <em>OR</em> <span class="drug-name">Tab. Cotrimoxazole DS</span> (Septrin DS) &times; 1 tab daily.
          </div>
        </li>
      </ol>
    </div>
  </div>
</div>
"""
    },
    {
        "id": "topic-18",
        "num": 18,
        "title": "Secondary Bacterial Peritonitis",
        "category": "peritonitis",
        "category_name": "Peritoneal Sepsis",
        "badge": "Acute Surgical Peritoneum",
        "book_page": "p. 434",
        "summary": "Peritoneal contamination from hollow viscus perforation, board-like abdominal rigidity, distinguishing criteria from SBP, pneumoperitoneum on erect CXR, and emergency exploratory laparotomy.",
        "content": """
<div class="clinical-section">
  <h4><i class="fa-solid fa-radiation"></i> Definition & Etiology</h4>
  <p><strong>Definition:</strong> Generalized or localized acute inflammation of the peritoneum caused by bacterial and chemical contamination originating from a surgically treatable intra-abdominal hollow organ defect.</p>
  <p><strong>Major Etiologies:</strong></p>
  <ul class="styled-list">
    <li><strong>Perforation of Hollow Viscus:</strong> Perforated peptic ulcer (duodenal/gastric), perforated acute appendicitis, perforated diverticulitis, perforated typhoid enteritis (terminal ileum), perforated stercoral ulcer.</li>
    <li><strong>Bowel Ischemia & Gangrene:</strong> Strangulated hernia, mesenteric infarction, volvulus with gangrene.</li>
    <li><strong>Trauma:</strong> Penetrating abdominal stab/gunshot wounds or blunt rupture of hollow viscera.</li>
    <li><strong>Iatrogenic:</strong> Postoperative anastomotic leak, bowel injury during laparoscopy or colonoscopy.</li>
  </ul>

  <h4><i class="fa-solid fa-stethoscope"></i> Clinical Presentation & Distinguishing from SBP</h4>
  <div class="table-responsive">
    <table class="med-table">
      <thead>
        <tr><th>Feature</th><th>Secondary Bacterial Peritonitis</th><th>Spontaneous Bacterial Peritonitis (SBP)</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Underlying Source</strong></td>
          <td>Surgically treatable anatomical breach (perforation, leak).</td>
          <td>No surgically treatable source (bacterial translocation).</td>
        </tr>
        <tr>
          <td><strong>Abdominal Exam</strong></td>
          <td><strong>Board-like involuntary rigidity</strong>, excruciating diffuse rebound tenderness, absent bowel sounds.</td>
          <td>Soft abdomen or mild diffuse tenderness; board-like rigidity is absent.</td>
        </tr>
        <tr>
          <td><strong>Ascitic / Peritoneal Fluid</strong></td>
          <td><strong>Polymicrobial</strong> on Gram stain/culture (aerobes + anaerobes).
            <br>&bull; Protein &gt; 1.0 g/dL
            <br>&bull; Glucose &lt; 50 mg/dL (consumed by bacteria)
            <br>&bull; LDH &gt; upper limit of normal for serum</td>
          <td><strong>Monomicrobial</strong> (single organism, usually E. coli).
            <br>&bull; Protein &lt; 1.0 g/dL
            <br>&bull; Glucose normal (&gt; 50 mg/dL)
            <br>&bull; LDH normal</td>
        </tr>
        <tr>
          <td><strong>Treatment</strong></td>
          <td><strong>EMERGENCY SURGICAL LAPAROTOMY</strong> + antibiotics.</td>
          <td><strong>MEDICAL PHARMACOTHERAPY</strong> (IV antibiotics + albumin).</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h4><i class="fa-solid fa-prescription"></i> Emergency Resuscitation & Management Protocol (Rx)</h4>
  <div class="rx-box">
    <div class="rx-header"><span class="rx-icon">Rx</span> Secondary Peritonitis Surgical Resuscitation Protocol:</div>
    <div class="rx-body">
      <ol class="rx-ordered-list">
        <li><strong>Immediate Emergency Operating Theatre Activation:</strong> Peritonitis from hollow viscus perforation is a surgical catastrophe requiring immediate exploration.</li>
        <li>Maintain ABCD&E, administer high-flow oxygen via non-rebreather mask, establish two 16G IV lines.</li>
        <li><strong>Strict NPO;</strong> insert wide-bore Nasogastric (NG) tube on continuous suction; insert Foley catheter with urometer.</li>
        <li><strong>Rapid Crystalloid Fluid Resuscitation:</strong>
          <br>&bull; Inf. 0.9% Normal Saline or Ringer's Lactate (1000–2000 mL rapid IV infusion to combat profound septic shock and third-space fluid sequestration).
        </li>
        <li><strong>Stat Preoperative IV Broad-Spectrum Antibiotics:</strong>
          <div class="med-item">
            &bull; <span class="drug-name">Inj. Metronidazole 500mg/100ml</span> (Flagyl) &times; IV &times; TDS
            <br><strong>PLUS ONE OF:</strong>
            <br>&bull; <span class="drug-name">Inj. Ceftriaxone 1g to 2g</span> (Rocephin, Titan) &times; IV &times; BD
            <br>&bull; <em>OR</em> <span class="drug-name">Inj. Cefuroxime 750mg</span> (Zinacef) &times; IV &times; TDS
            <br>&bull; <em>OR</em> <span class="drug-name">Inf. Ciprofloxacin 400mg/100ml</span> (Novidate) &times; IV &times; BD
            <br>&bull; <em>In Septic Shock / Multi-Drug Resistance:</em> <span class="drug-name">Inj. Piperacillin-Tazobactam 4.5g</span> (Tanzo) IV TDS OR <span class="drug-name">Inj. Meropenem 1g</span> (Meronem) IV TDS.
          </div>
        </li>
        <li><strong>IV Gastroprotection:</strong> <span class="drug-name">Inj. Omeprazole 40mg</span> (Risek) diluted in 10ml NS &times; IV &times; OD.</li>
        <li><strong>Emergency Exploratory Laparotomy / Laparoscopy:</strong>
          <ul class="sub-list">
            <li>Identify and control the source of contamination: Graham patch omentopexy for perforated duodenal ulcer; appendectomy for perforated appendix; resection of gangrenous bowel; exteriorization/colostomy (Hartmann's procedure) for perforated diverticulitis/malignancy.</li>
            <li>Copious peritoneal lavage with copious liters of warm normal saline until effluent is crystal clear.</li>
            <li>Strategic placement of closed suction drains in the pelvis and subhepatic spaces.</li>
          </ul>
        </li>
      </ol>
    </div>
  </div>
</div>
"""
    }
]
