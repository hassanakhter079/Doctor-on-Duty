# -*- coding: utf-8 -*-
"""
Download real clinical photos & diagrams from Wikipedia / Wikimedia Commons
for all 29 General Surgery topics in Doctor on Duty Chapter 17.
"""
import urllib.request
import urllib.parse
import json
import os

IMG_DIR = '/root/doctor-on-duty/img'
os.makedirs(IMG_DIR, exist_ok=True)

TOPIC_ARTICLES = {
    1: 'Abdomen',
    2: 'Abdominal pain',
    3: 'Physical examination',
    4: 'Abdominal x-ray',
    5: 'Intravenous therapy',
    6: 'Appendicitis',
    7: 'Cholecystitis',
    8: 'Gallstone',
    9: 'Endoscopic retrograde cholangiopancreatography',
    10: 'Ascending cholangitis',
    11: 'Anal fissure',
    12: 'Hemorrhoid',
    13: 'Anorectal abscess',
    14: 'Pilonidal disease',
    15: 'Acute pancreatitis',
    16: 'Bowel obstruction',
    17: 'Ascites',
    18: 'Peritonitis',
    19: 'Pressure ulcer',
    20: 'Diabetic foot ulcer',
    21: 'Hypertrophic scar',
    22: 'Keloid',
    23: 'Lipoma',
    24: 'Skin tag',
    25: 'Ganglion cyst',
    26: 'Ingrown nail',
    27: 'Herpetic whitlow',
    28: 'Paronychia',
    29: 'Onychomycosis'
}

HEADERS = {
    'User-Agent': 'DoctorOnDutyClinicalGuide/1.0 (contact: clinical@doctoronduty.org)'
}

def fetch_image_for_topic(num, article):
    dest = os.path.join(IMG_DIR, f'clinical_topic_{num:02d}.jpg')
    if os.path.exists(dest) and os.path.getsize(dest) > 2000:
        print(f"Topic {num:02d}: Already exists ({os.path.getsize(dest)} bytes)")
        return True

    api_url = f'https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(article)}&prop=pageimages&format=json&pithumbsize=800'
    try:
        req = urllib.request.Request(api_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            img_url = None
            for pid, pdata in pages.items():
                if 'thumbnail' in pdata:
                    img_url = pdata['thumbnail']['source']
                    break
            
            if not img_url:
                print(f"Topic {num:02d} ({article}): No thumbnail in API")
                return False

            print(f"Topic {num:02d} ({article}): Downloading {img_url} ...")
            img_req = urllib.request.Request(img_url, headers=HEADERS)
            with urllib.request.urlopen(img_req, timeout=12) as img_resp:
                img_bytes = img_resp.read()
                with open(dest, 'wb') as f:
                    f.write(img_bytes)
                print(f"  -> Saved {len(img_bytes)} bytes to {dest}")
                return True
    except Exception as e:
        print(f"Topic {num:02d} ({article}) ERROR: {e}")
        return False

if __name__ == '__main__':
    success_count = 0
    for num, article in TOPIC_ARTICLES.items():
        if fetch_image_for_topic(num, article):
            success_count += 1
    print(f"\nDone: {success_count} / {len(TOPIC_ARTICLES)} images downloaded successfully.")
