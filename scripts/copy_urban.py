# ⚠️ DEVELOPMENT ONLY - One-time script for data preparation
import shutil, os, csv

src_base = r'C:\Users\This User\Downloads\UrbanSound8K'
dst_base = r'C:\Users\This User\Desktop\SOS-Audio-Detection\data\raw'
mapping = {'6': 'explosion', '2': 'crying', '3': 'crying'}
copied = {'explosion': 0, 'crying': 0}

csv_path = os.path.join(src_base, 'metadata', 'UrbanSound8K.csv')
rows = list(csv.DictReader(open(csv_path, encoding='utf-8')))
print(f'סה"כ שורות ב-CSV: {len(rows)}')

for row in rows:
    cid = row['classID']
    if cid in mapping:
        cat = mapping[cid]
        src = os.path.join(src_base, 'audio', 'fold' + row['fold'], row['slice_file_name'])
        dst = os.path.join(dst_base, cat, 'us8k_' + row['slice_file_name'])
        if os.path.exists(src):
            shutil.copy2(src, dst)
            copied[cat] += 1

print('הועתקו:', copied)
