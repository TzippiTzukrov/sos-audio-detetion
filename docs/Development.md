# 🔧 Development Guide - אימון מודל חדש

מדריך זה מסביר איך להכן נתונים ולאמן מודל חדש.

## 📋 דרישות מקדימות

```bash
pip install -r requirements.txt
```

## 🎯 זרימת האימון (מ-0 עד 100)

### **1️⃣ הכנת נתונים גולמיים**

בחר אחד מהשניים:

#### **אפשרות A: UrbanSound8K**
```bash
python scripts/copy_urban.py
```

#### **אפשרות B: ESC-50**
```bash
python scripts/prepare_data.py
```

### **2️⃣ עיבוד נתונים (Raw → Mel Spectrograms)**

```bash
python scripts/preprocess.py
```

### **3️⃣ אימון מודל**

```bash
python scripts/train.py
```

---

## ⚙️ הפרמטרים הקריטיים

### **src/preprocess.py:**
```python
sr=22050              # Sample rate - תדירות דגימה
duration=5.0          # משך כל דגימה (שניות)
n_mels=128            # מספר Mel bands
```

### **src/train.py:**
```python
epochs=50             # מספר epochs (EarlyStopping עשוי לעצור קודם)
batch_size=32         # גודל batch
validation_split=0.2  # 20% לתרValidation
```

### **src/realtime_detector.py:**
```python
SR = 22050            # צריך להיות שווה ל-preprocess.py!
DURATION = 2          # משך חלון האזנה (שניות)
THRESHOLD = 0.50      # רף ביטחון להתרעה
```

⚠️ **חשוב:** SR ו-n_mels צריכים להיות **זהים** בכל הקבצים!

---

## 🔄 סדר ה-implementation בפועל

```
1. Download dataset (UrbanSound8K or ESC-50)
   ↓
2. scripts/copy_urban.py OR scripts/prepare_data.py
   ↓
3. src/preprocess.py
   ↓
4. src/train.py
   ↓
5. src/realtime_detector.py ← סיום! המודל מוכן לשימוש
```

---

## 🐛 Troubleshooting

**Q: "ModuleNotFoundError: No module named 'tensorflow'"**
```bash
pip install --upgrade tensorflow
```

**Q: "FileNotFoundError: data/raw/ לא קיים"**
```bash
mkdir -p data/raw/{scream,crying,explosion,background}
mkdir -p data/processed
```

**Q: "MFCC shape mismatch"**
- בדוק ש-preprocess.py ו-realtime_detector.py משתמשים באותם פרמטרים
- preprocess.py: `n_mels=128`, realtime: הם צריכים להיות 128

---

## 📊 מדדים לעקוב

כשמריצים את `src/train.py`, שימו לב ל:
- **Accuracy** - יתחיל בערך 40-50% ויעלה
- **Validation Accuracy** - צריך לעלות בעקביות
- **Confusion Matrix** - בדקו איזה קטגוריות מבולבלות

---

## 💾 שמירת מודלים

כל הפעם שאתה מריץ את `src/train.py`:
- הוא משכתב את `src/sos_model.keras`
- יוצר confusion matrix חדש

אם אתה רוצה לשמור מודל ישן:
```bash
cp src/sos_model.keras src/sos_model_backup_v1.keras
```