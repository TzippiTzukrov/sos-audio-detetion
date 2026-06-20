# SOS Audio Detection

זיהוי קולות מצוקה (SOS) באמצעות בינה מלאכותית - מודל CNN עם הקלטה בזמן אמת.

## 🚀 QuickStart

```bash
# התקנה
pip install -r requirements.txt

# שימוש בייצור
python src/realtime_detector.py
```

---

## 📋 מבנה הפרויקט

```
SOS-Audio-Detection/
├── src/                          # קוד ייצור בלבד
│   ├── realtime_detector.py      # 🎯 זיהוי אודיו בזמן אמת
│   ├── audio_utils.py            # פונקציות עזר
│   ├── sos_model.keras           # מודל מאומן
│   └── confusion_matrix.png       # תוצאת אימון
│
├── scripts/                      # קוד פיתוח בלבד (חד-פעמי)
│   ├── copy_urban.py             # העתקת UrbanSound8K
│   ├── prepare_data.py           # העתקת ESC-50
│   ├── preprocess.py             # עיבוד ל-mel spectrograms
│   └── train.py                  # אימון מודל
│
├── data/
│   ├── raw/                      # קבצי WAV
│   └── processed/                # mel spectrograms
│
├── USAGE.md                      # איך להשתמש בייצור
├── DEVELOPMENT.md                # איך לאמן מודל חדש
└── requirements.txt
```

---

## 📖 תיעוד

- **[USAGE.md](USAGE.md)** - איך להריץ את המערכת בייצור
- **[DEVELOPMENT.md](DEVELOPMENT.md)** - איך לאמן מודל חדש

---

## 🎯 זרימת העבודה

### ייצור (שימוש יום יום)
```bash
python src/realtime_detector.py
```

### פיתוח (אימון מודל חדש)
```bash
# 1. הכנת נתונים
python scripts/copy_urban.py

# 2. עיבוד ל-mel spectrograms
python src/preprocess.py

# 3. אימון
python src/train.py
```

---

## 🔧 טכנולוגיה

- **librosa** - עיבוד אודיו
- **tensorflow/keras** - מודל עמוק (CNN)
- **scikit-learn** - טעינת נתונים ומדדים
- **numpy, matplotlib** - עיבוד וויזואליזציה

---

## ⚠️ הערות חשובות

- **notebooks/**: כל ה-notebooks הוסרו - כל קוד נמצא ב-src/
- **scripts/**: סקריפטים חד-פעמיים לפיתוח בלבד, לא בייצור
- **sos_model.keras**: מודל מאומן, אל תמחוק!

---

## 📞 שאלות?

ראה [USAGE.md](USAGE.md) או [DEVELOPMENT.md](DEVELOPMENT.md)