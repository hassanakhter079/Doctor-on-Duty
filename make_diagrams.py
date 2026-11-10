# -*- coding: utf-8 -*-
"""
Generate specialized clinical medical diagrams (SVG) for Doctor on Duty Chapter 17
Saved into /root/doctor-on-duty/img/
"""
import os

os.makedirs('/root/doctor-on-duty/img', exist_ok=True)

def create_svg(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    print(f"Generated {path}")

# Topic 1: Abdominal Quadrants & Regions
create_svg('/root/doctor-on-duty/img/topic_01.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 360" width="100%" height="100%">
  <rect width="600" height="360" fill="#0f172a" rx="12"/>
  <text x="300" y="32" fill="#2dd4bf" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">ACUTE ABDOMEN: TOPOGRAPHICAL ANATOMY & PAIN REFERRAL</text>
  
  <!-- Left: 4 Quadrants -->
  <g transform="translate(40, 60)">
    <rect width="240" height="240" fill="#1e293b" rx="8" stroke="#334155" stroke-width="2"/>
    <line x1="120" y1="0" x2="120" y2="240" stroke="#0d9488" stroke-width="2" stroke-dasharray="4"/>
    <line x1="0" y1="120" x2="240" y2="120" stroke="#0d9488" stroke-width="2" stroke-dasharray="4"/>
    <circle cx="120" cy="120" r="8" fill="#d97706"/>
    <text x="120" y="140" fill="#f59e0b" font-size="10" font-family="system-ui" text-anchor="middle">Umbilicus</text>
    
    <text x="60" y="45" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">RUQ</text>
    <text x="60" y="65" fill="#94a3b8" font-size="10" text-anchor="middle">Liver, Gallbladder,</text>
    <text x="60" y="80" fill="#94a3b8" font-size="10" text-anchor="middle">Biliary Tree, Duodenum</text>
    
    <text x="180" y="45" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">LUQ</text>
    <text x="180" y="65" fill="#94a3b8" font-size="10" text-anchor="middle">Stomach, Spleen,</text>
    <text x="180" y="80" fill="#94a3b8" font-size="10" text-anchor="middle">Pancreas Body/Tail</text>
    
    <text x="60" y="165" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">RLQ</text>
    <text x="60" y="185" fill="#94a3b8" font-size="10" text-anchor="middle">Appendix, Cecum,</text>
    <text x="60" y="200" fill="#94a3b8" font-size="10" text-anchor="middle">Terminal Ileum, Ovary</text>
    
    <text x="180" y="165" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">LLQ</text>
    <text x="180" y="185" fill="#94a3b8" font-size="10" text-anchor="middle">Sigmoid Colon,</text>
    <text x="180" y="200" fill="#94a3b8" font-size="10" text-anchor="middle">Left Ovary/Trophoblast</text>
    
    <text x="120" y="260" fill="#cbd5e1" font-size="12" font-weight="bold" text-anchor="middle">Four Clinical Quadrants</text>
  </g>

  <!-- Right: Visceral to Somatic Pain Progression -->
  <g transform="translate(320, 60)">
    <rect width="240" height="240" fill="#1e293b" rx="8" stroke="#334155" stroke-width="2"/>
    <text x="120" y="28" fill="#f8fafc" font-size="12" font-weight="bold" text-anchor="middle">Pain Pathophysiology</text>
    
    <rect x="20" y="45" width="200" height="42" fill="#0f172a" rx="6" stroke="#38bdf8"/>
    <text x="30" y="62" fill="#38bdf8" font-size="11" font-weight="bold">1. Visceral Pain (Autonomic)</text>
    <text x="30" y="78" fill="#94a3b8" font-size="9.5">Dull, poorly localized, midline periumbilical</text>
    
    <line x1="120" y1="90" x2="120" y2="108" stroke="#e2e8f0" stroke-width="2" marker-end="url(#arrow)"/>
    
    <rect x="20" y="110" width="200" height="42" fill="#0f172a" rx="6" stroke="#f59e0b"/>
    <text x="30" y="127" fill="#f59e0b" font-size="11" font-weight="bold">2. Parietal Pain (Somatic)</text>
    <text x="30" y="143" fill="#94a3b8" font-size="9.5">Sharp, severe, precisely localized (RIF/RLQ)</text>
    
    <line x1="120" y1="155" x2="120" y2="173" stroke="#e2e8f0" stroke-width="2"/>
    
    <rect x="20" y="175" width="200" height="42" fill="#0f172a" rx="6" stroke="#f43f5e"/>
    <text x="30" y="192" fill="#f43f5e" font-size="11" font-weight="bold">3. Peritonitis / Rigidity</text>
    <text x="30" y="208" fill="#94a3b8" font-size="9.5">Involuntary guarding, board-like rigidity</text>
    
    <text x="120" y="260" fill="#cbd5e1" font-size="12" font-weight="bold" text-anchor="middle">Progression Timeline (12–24h)</text>
  </g>
</svg>
''')

# Topic 6: Appendicitis & Alvarado
create_svg('/root/doctor-on-duty/img/topic_06.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 360" width="100%" height="100%">
  <rect width="600" height="360" fill="#0f172a" rx="12"/>
  <text x="300" y="32" fill="#2dd4bf" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">ACUTE APPENDICITIS: SIGNS & ALVARADO TRIAGE</text>
  
  <g transform="translate(40, 60)">
    <rect width="250" height="260" fill="#1e293b" rx="8" stroke="#334155"/>
    <text x="125" y="26" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">Anatomical & Physical Signs</text>
    
    <circle cx="125" cy="85" r="30" fill="none" stroke="#64748b" stroke-width="2"/>
    <circle cx="125" cy="85" r="4" fill="#f59e0b"/>
    <text x="135" y="88" fill="#f59e0b" font-size="10">Umbilicus</text>
    <circle cx="65" cy="140" r="4" fill="#38bdf8"/>
    <text x="35" y="155" fill="#38bdf8" font-size="10">ASIS</text>
    <line x1="125" y1="85" x2="65" y2="140" stroke="#94a3b8" stroke-dasharray="3"/>
    
    <!-- McBurney point -->
    <circle cx="85" cy="122" r="7" fill="#f43f5e"/>
    <text x="100" y="125" fill="#f43f5e" font-size="11" font-weight="bold">McBurney's Point</text>
    <text x="100" y="138" fill="#94a3b8" font-size="9">(Junction lateral 1/3 & medial 2/3)</text>
    
    <g transform="translate(15, 160)" font-size="10" fill="#cbd5e1">
      <text y="15">&bull; <tspan font-weight="bold" fill="#2dd4bf">Rovsing Sign:</tspan> LLQ pressure &rarr; RLQ pain</text>
      <text y="32">&bull; <tspan font-weight="bold" fill="#2dd4bf">Psoas Sign:</tspan> Hip extension &rarr; pain (retrocecal)</text>
      <text y="49">&bull; <tspan font-weight="bold" fill="#2dd4bf">Obturator Sign:</tspan> Hip internal rotation &rarr; pain</text>
      <text y="66">&bull; <tspan font-weight="bold" fill="#2dd4bf">Blumberg Sign:</tspan> Rebound tenderness</text>
      <text y="83">&bull; <tspan font-weight="bold" fill="#2dd4bf">Ultrasound:</tspan> Target sign, diameter &gt; 6 mm</text>
    </g>
  </g>

  <g transform="translate(310, 60)">
    <rect width="250" height="260" fill="#1e293b" rx="8" stroke="#334155"/>
    <text x="125" y="26" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">Alvarado Score (MANTRELS)</text>
    
    <g transform="translate(15, 45)" font-size="10.5">
      <text y="15" fill="#cbd5e1"><strong>M</strong>igration of pain to RLQ ............ <tspan fill="#2dd4bf" font-weight="bold">1</tspan></text>
      <text y="32" fill="#cbd5e1"><strong>A</strong>norexia ................................... <tspan fill="#2dd4bf" font-weight="bold">1</tspan></text>
      <text y="49" fill="#cbd5e1"><strong>N</strong>ausea / Vomiting ..................... <tspan fill="#2dd4bf" font-weight="bold">1</tspan></text>
      <text y="66" fill="#f43f5e" font-weight="bold"><strong>T</strong>enderness in RLQ .................... 2</text>
      <text y="83" fill="#cbd5e1"><strong>R</strong>ebound tenderness ................. <tspan fill="#2dd4bf" font-weight="bold">1</tspan></text>
      <text y="100" fill="#cbd5e1"><strong>E</strong>levated temperature (&gt;37.3&deg;C) ... <tspan fill="#2dd4bf" font-weight="bold">1</tspan></text>
      <text y="117" fill="#f43f5e" font-weight="bold"><strong>L</strong>eukocytosis (&gt;10,000/&mu;L) .......... 2</text>
      <text y="134" fill="#cbd5e1"><strong>S</strong>hift to left (&ge;75% neutrophils) .. <tspan fill="#2dd4bf" font-weight="bold">1</tspan></text>
    </g>
    
    <rect x="15" y="195" width="220" height="50" fill="#0f172a" rx="6" stroke="#0d9488"/>
    <text x="125" y="215" fill="#f59e0b" font-size="11" font-weight="bold" text-anchor="middle">Score &ge; 7: High Probability (Surgery!)</text>
    <text x="125" y="232" fill="#94a3b8" font-size="9.5" text-anchor="middle">5–6: Intermediate (CT/Observe) | &le; 4: Low Risk</text>
  </g>
</svg>
''')

# Topic 7: Acute Cholecystitis & Biliary Tree
create_svg('/root/doctor-on-duty/img/topic_07.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 360" width="100%" height="100%">
  <rect width="600" height="360" fill="#0f172a" rx="12"/>
  <text x="300" y="32" fill="#2dd4bf" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">ACUTE CHOLECYSTITIS & BILIARY CALCULI</text>
  
  <g transform="translate(40, 60)">
    <rect width="250" height="260" fill="#1e293b" rx="8" stroke="#334155"/>
    <text x="125" y="26" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">Ultrasound Hallmark Signs</text>
    
    <path d="M 60,80 C 40,110 50,170 90,190 C 130,200 160,180 170,140 C 180,100 130,60 90,70 Z" fill="#064e3b" stroke="#10b981" stroke-width="4"/>
    <!-- Gallbladder lumen -->
    <path d="M 70,90 C 55,115 65,160 95,175 C 125,185 145,165 155,135 C 160,105 125,75 95,80 Z" fill="#022c22"/>
    <!-- Gallstone with acoustic shadow -->
    <circle cx="110" cy="145" r="14" fill="#f59e0b" stroke="#fff" stroke-width="2"/>
    <polygon points="100,160 85,230 135,230 120,160" fill="rgba(0,0,0,0.6)"/>
    <text x="110" y="220" fill="#94a3b8" font-size="9" text-anchor="middle">Acoustic Shadow</text>
    
    <text x="125" y="248" fill="#38bdf8" font-size="10.5" font-weight="bold" text-anchor="middle">Thickened Wall &gt; 4mm + Stone</text>
  </g>

  <g transform="translate(310, 60)">
    <rect width="250" height="260" fill="#1e293b" rx="8" stroke="#334155"/>
    <text x="125" y="26" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">Tokyo Guidelines (TG18)</text>
    
    <rect x="15" y="45" width="220" height="50" fill="#0f172a" rx="6" stroke="#38bdf8"/>
    <text x="25" y="65" fill="#38bdf8" font-size="11" font-weight="bold">A. Local Signs:</text>
    <text x="25" y="82" fill="#cbd5e1" font-size="10">Murphy's sign, RUQ pain, tender mass</text>
    
    <rect x="15" y="105" width="220" height="50" fill="#0f172a" rx="6" stroke="#f59e0b"/>
    <text x="25" y="125" fill="#f59e0b" font-size="11" font-weight="bold">B. Systemic Signs:</text>
    <text x="25" y="142" fill="#cbd5e1" font-size="10">Fever, Leukocytosis (WBC &gt; 10k), &uarr;CRP</text>
    
    <rect x="15" y="165" width="220" height="50" fill="#0f172a" rx="6" stroke="#10b981"/>
    <text x="25" y="185" fill="#10b981" font-size="11" font-weight="bold">C. Imaging Confirmation:</text>
    <text x="25" y="202" fill="#cbd5e1" font-size="10">US: wall &gt; 4mm, pericholecystic fluid</text>
    
    <text x="125" y="245" fill="#f43f5e" font-size="10.5" font-weight="bold" text-anchor="middle">&bull; Definite Diagnosis: A + B + C &bull;</text>
  </g>
</svg>
''')

# Topic 12: Hemorrhoids
create_svg('/root/doctor-on-duty/img/topic_12.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 360" width="100%" height="100%">
  <rect width="600" height="360" fill="#0f172a" rx="12"/>
  <text x="300" y="32" fill="#2dd4bf" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">HEMORRHOIDS: ANATOMY & INTERNAL STAGING</text>
  
  <g transform="translate(40, 60)">
    <rect width="250" height="260" fill="#1e293b" rx="8" stroke="#334155"/>
    <text x="125" y="26" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">Dentate Line Distinction</text>
    
    <!-- Anal canal schematic -->
    <path d="M 60,50 L 190,50 L 170,220 L 80,220 Z" fill="#0f172a" stroke="#475569" stroke-width="2"/>
    <!-- Dentate line -->
    <path d="M 75,130 Q 95,120 115,130 Q 135,140 155,130 Q 175,120 175,130" fill="none" stroke="#e11d48" stroke-width="3" stroke-dasharray="3"/>
    <text x="190" y="134" fill="#f43f5e" font-size="10" font-weight="bold">Dentate Line</text>
    
    <!-- Internal pile -->
    <circle cx="110" cy="95" r="14" fill="#3b82f6" opacity="0.8"/>
    <text x="110" y="98" fill="#fff" font-size="9" text-anchor="middle" font-weight="bold">Internal</text>
    <text x="110" y="70" fill="#38bdf8" font-size="9.5" text-anchor="middle">Above Line (Painless)</text>
    
    <!-- External pile -->
    <circle cx="140" cy="175" r="14" fill="#f59e0b" opacity="0.8"/>
    <text x="140" y="178" fill="#fff" font-size="9" text-anchor="middle" font-weight="bold">External</text>
    <text x="140" y="202" fill="#f59e0b" font-size="9.5" text-anchor="middle">Below Line (Painful)</text>
    
    <text x="125" y="248" fill="#94a3b8" font-size="10" text-anchor="middle">3, 7, 11 o'clock cushion sites</text>
  </g>

  <g transform="translate(310, 60)">
    <rect width="250" height="260" fill="#1e293b" rx="8" stroke="#334155"/>
    <text x="125" y="26" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">Internal Hemorrhoid Degrees</text>
    
    <g transform="translate(15, 45)" font-size="11">
      <rect x="0" y="0" width="220" height="42" fill="#0f172a" rx="5" stroke="#3b82f6"/>
      <text x="10" y="18" fill="#38bdf8" font-weight="bold">1st Degree</text>
      <text x="10" y="34" fill="#cbd5e1" font-size="9.5">Painless bleeding only; NO prolapse.</text>
      
      <rect x="0" y="50" width="220" height="42" fill="#0f172a" rx="5" stroke="#10b981"/>
      <text x="10" y="68" fill="#34d399" font-weight="bold">2nd Degree</text>
      <text x="10" y="84" fill="#cbd5e1" font-size="9.5">Prolapses on defecation; reduces spontaneously.</text>
      
      <rect x="0" y="100" width="220" height="42" fill="#0f172a" rx="5" stroke="#f59e0b"/>
      <text x="10" y="118" fill="#fbbf24" font-weight="bold">3rd Degree</text>
      <text x="10" y="134" fill="#cbd5e1" font-size="9.5">Prolapses; requires manual reduction.</text>
      
      <rect x="0" y="150" width="220" height="42" fill="#0f172a" rx="5" stroke="#f43f5e"/>
      <text x="10" y="168" fill="#f87171" font-weight="bold">4th Degree</text>
      <text x="10" y="184" fill="#cbd5e1" font-size="9.5">Permanently prolapsed; irreducible.</text>
    </g>
    
    <text x="125" y="248" fill="#2dd4bf" font-size="10.5" font-weight="bold" text-anchor="middle">Rx: Daflon 500mg + High Fiber + Banding/Surgery</text>
  </g>
</svg>
''')

# Topic 19: Pressure Ulcers Staging
create_svg('/root/doctor-on-duty/img/topic_19.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 360" width="100%" height="100%">
  <rect width="600" height="360" fill="#0f172a" rx="12"/>
  <text x="300" y="32" fill="#2dd4bf" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">PRESSURE ULCER (BED SORE) STAGING (NPUAP)</text>
  
  <g transform="translate(30, 60)">
    <!-- Stage 1 -->
    <g transform="translate(0, 0)">
      <rect width="125" height="230" fill="#1e293b" rx="6" stroke="#334155"/>
      <text x="62" y="24" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Stage 1</text>
      <rect x="12" y="40" width="101" height="15" fill="#f87171" rx="2"/>
      <rect x="12" y="58" width="101" height="40" fill="#fed7aa" rx="2"/>
      <rect x="12" y="101" width="101" height="50" fill="#fef08a" rx="2"/>
      <rect x="12" y="154" width="101" height="30" fill="#cbd5e1" rx="2"/>
      <text x="62" y="200" fill="#94a3b8" font-size="9.5" text-anchor="middle">Non-blanchable</text>
      <text x="62" y="214" fill="#94a3b8" font-size="9.5" text-anchor="middle">erythema (intact)</text>
    </g>

    <!-- Stage 2 -->
    <g transform="translate(135, 0)">
      <rect width="125" height="230" fill="#1e293b" rx="6" stroke="#334155"/>
      <text x="62" y="24" fill="#34d399" font-size="12" font-weight="bold" text-anchor="middle">Stage 2</text>
      <path d="M 12,40 L 45,40 Q 62,60 80,40 L 113,40 L 113,55 L 12,55 Z" fill="#ef4444"/>
      <rect x="12" y="58" width="101" height="40" fill="#fed7aa" rx="2"/>
      <rect x="12" y="101" width="101" height="50" fill="#fef08a" rx="2"/>
      <rect x="12" y="154" width="101" height="30" fill="#cbd5e1" rx="2"/>
      <text x="62" y="200" fill="#94a3b8" font-size="9.5" text-anchor="middle">Partial-thickness</text>
      <text x="62" y="214" fill="#94a3b8" font-size="9.5" text-anchor="middle">loss into dermis</text>
    </g>

    <!-- Stage 3 -->
    <g transform="translate(270, 0)">
      <rect width="125" height="230" fill="#1e293b" rx="6" stroke="#334155"/>
      <text x="62" y="24" fill="#fbbf24" font-size="12" font-weight="bold" text-anchor="middle">Stage 3</text>
      <path d="M 12,40 L 35,40 Q 62,110 90,40 L 113,40 L 113,55 L 12,55 Z" fill="#b91c1c"/>
      <rect x="12" y="101" width="101" height="50" fill="#fef08a" rx="2"/>
      <rect x="12" y="154" width="101" height="30" fill="#cbd5e1" rx="2"/>
      <text x="62" y="200" fill="#94a3b8" font-size="9.5" text-anchor="middle">Full-thickness;</text>
      <text x="62" y="214" fill="#94a3b8" font-size="9.5" text-anchor="middle">fat exposed</text>
    </g>

    <!-- Stage 4 -->
    <g transform="translate(405, 0)">
      <rect width="135" height="230" fill="#1e293b" rx="6" stroke="#334155"/>
      <text x="67" y="24" fill="#f87171" font-size="12" font-weight="bold" text-anchor="middle">Stage 4</text>
      <path d="M 12,40 L 25,40 Q 67,170 110,40 L 123,40 L 123,55 L 12,55 Z" fill="#7f1d1d"/>
      <rect x="12" y="154" width="111" height="30" fill="#cbd5e1" rx="2"/>
      <text x="67" y="200" fill="#94a3b8" font-size="9.5" text-anchor="middle">Deep destruction;</text>
      <text x="67" y="214" fill="#94a3b8" font-size="9.5" text-anchor="middle">bone/muscle bare</text>
    </g>
  </g>
  
  <text x="300" y="325" fill="#cbd5e1" font-size="11.5" text-anchor="middle">Key Care: 2-Hour Repositioning &bull; Floating Heels &bull; Saline Only &bull; Hydrocolloid / VAC Dressings</text>
</svg>
''')

# Topic 26: Ingrown Toenail
create_svg('/root/doctor-on-duty/img/topic_26.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 360" width="100%" height="100%">
  <rect width="600" height="360" fill="#0f172a" rx="12"/>
  <text x="300" y="32" fill="#2dd4bf" font-family="system-ui, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">INGROWN TOENAIL: SPICULE FORMATION & RESECTION</text>
  
  <g transform="translate(40, 60)">
    <rect width="250" height="260" fill="#1e293b" rx="8" stroke="#334155"/>
    <text x="125" y="26" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">Mechanism of Spicule Injury</text>
    
    <!-- Toe outline -->
    <path d="M 65,60 C 65,40 185,40 185,60 L 185,210 L 65,210 Z" fill="#fdba74" opacity="0.6"/>
    <!-- Nail plate -->
    <rect x="85" y="70" width="80" height="90" fill="#fef3c7" stroke="#d97706" rx="4"/>
    <!-- Embedded spike -->
    <path d="M 85,75 L 72,82 L 85,90 Z" fill="#ef4444"/>
    <!-- Granulation tissue -->
    <circle cx="70" cy="85" r="10" fill="#dc2626" opacity="0.8"/>
    
    <text x="125" y="185" fill="#f43f5e" font-size="10.5" font-weight="bold" text-anchor="middle">Lateral Spike Pierces Fold</text>
    <text x="125" y="202" fill="#cbd5e1" font-size="9.5" text-anchor="middle">Granulation tissue & secondary S. aureus</text>
    <text x="125" y="240" fill="#38bdf8" font-size="10" text-anchor="middle">Trigger: Curved lateral trimming!</text>
  </g>

  <g transform="translate(310, 60)">
    <rect width="250" height="260" fill="#1e293b" rx="8" stroke="#334155"/>
    <text x="125" y="26" fill="#f8fafc" font-size="13" font-weight="bold" text-anchor="middle">Surgical Phenol Matrixectomy</text>
    
    <g transform="translate(15, 45)" font-size="11" fill="#cbd5e1">
      <text y="15"><strong>1. Digital Ring Block:</strong></text>
      <text y="30" fill="#f43f5e" font-weight="bold">Plain 1% Lidocaine (NO ADRENALINE!)</text>
      
      <text y="60"><strong>2. Tourniquet:</strong> Bloodless field</text>
      <text y="85"><strong>3. Partial Avulsion:</strong></text>
      <text y="100" fill="#94a3b8">Excise lateral 3–4 mm longitudinal strip</text>
      
      <text y="130"><strong>4. Chemical Matrixectomy:</strong></text>
      <text y="145" fill="#38bdf8" font-weight="bold">88% Liquefied Phenol for 1–2 minutes</text>
      <text y="160" fill="#94a3b8">Neutralize with 70% Isopropyl Alcohol</text>
      
      <text y="190"><strong>5. Permanent Cure:</strong></text>
      <text y="205" fill="#34d399" font-weight="bold">Recurrence rate drops to &lt; 3–5%</text>
    </g>
  </g>
</svg>
''')

print("Custom medical diagrams created successfully!")
