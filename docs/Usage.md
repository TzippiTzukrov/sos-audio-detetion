# 🚀 Usage Guide - השימוש בייצור

זה מדריך לשימוש בדיקטור SOS בזמן אמת.

## ⚡ QuickStart - התחלה מהירה

```bash
# התקנה (חד-פעמי)
pip install -r requirements.txt

# הרצה (זה כל מה שצריך!)
python src/realtime_detector.py
```

זהו! המערכת מקלטת אודיו מהמיקרופון ומכריזה על קולות מצוקה בזמן אמת.

---

## 📝 פעולה בפירוט

כשאתה מריץ את `src/realtime_detector.py`:

```
מאזין... (Ctrl+C לעצירה)
[שומע] background (23%)
[שומע] background (18%)
[שומע] explosion (87%)  ← מותר
[התרעה!] explosion (87%)  ← כאן מדפיס התרעה!
```

---

## ⚙️ הפרמטרים שאתה יכול לשנות

כל הקבועים אלה בראש `src/realtime_detector.py`:

```python
THRESHOLD = 0.50      # רף ביטחון (50% = דרוש לפחות 50% confidence)
DURATION = 2          # משך חלון האזנה (שניות)
STEP = 1              # קפיצה בין חלונות (שניות)
SR = 22050            # Sample rate
```

### דוגמאות שינויים:

**להיות יותר מחמיר:**
```python
THRESHOLD = 0.75  # דרוש לפחות 75% confidence
```

**להיות יותר רגיש:**
```python
THRESHOLD = 0.30  # דרוש רק 30% confidence
```

---

## 🎤 הגדרת מיקרופון

ברוב המחשבים, הקוד משתמש בברירת המחדל של המיקרופון.

אם יש בעיות, תוכל לבדוק אילו מיקרופונים זמינים:

```python
import sounddevice as sd
print(sd.query_devices())
```

ואז לשנות בקוד:
```python
new_audio = sd.rec(chunk_size, samplerate=SR, channels=1, dtype="float32", device=2)
```

---

## 🔍 הבנת ה-Output

```
[שומע] category (confidence%)
```

- **שומע**: זה מה שהמערכת זוהה
- **category**: אחת מ-["scream", "crying", "explosion", "background"]
- **confidence**: כמה בטוח המודל (0-100%)

```
[התרעה!] category (confidence%)
```

- מופיע רק כאשר:
  1. זה **לא** "background"
  2. confidence >= THRESHOLD

---

## 📊 קטגוריות

המודל מזהה 4 קטגוריות:

| קטגוריה | תיאור |
|---------|-------|
| **scream** | זעקה, סירנה, רעש פתאומי גבוה |
| **crying** | בכי, קול של כאב |
| **explosion** | פיצוץ, רעם, רעש חזק |
| **background** | רעש רגיל, לא חירום |

---

## 🛑 עצירה

```bash
Ctrl+C
```

---

## 🐛 בעיות נפוצות

**Q: "No audio input device found"**
```
בעיה: אין מיקרופון מחובר
פתרון: חבר מיקרופון או בדוק עם sd.query_devices()
```

**Q: "ModuleNotFoundError"**
```bash
pip install -r requirements.txt
```

**Q: "לא קורים התרעות כלל"**
```
פתרון: שנה את THRESHOLD להיות נמוך יותר
THRESHOLD = 0.30  # ניסיון
```

**Q: "יותר מדי התרעות שווא"**
```
פתרון: הגבה את THRESHOLD
THRESHOLD = 0.75  # יותר מחמיר
```

---

## 📈 ביצועים

- **Latency**: ~500ms (זמן בין קול לזיהוי)
- **Accuracy**: תלוי בסביבה (דקות יותר בשקט, פחות בתוך רעש)
- **CPU**: שימוש נמוך, יעבוד על Raspberry Pi

---

## 🔗 עבודה עם קוד אחר

אם אתה רוצה להשתמש ב-`realtime_detector` מתוך אפליקציה שלך:

```python
from src import extract_melspectrogram
from tensorflow import keras

model = keras.models.load_model("src/sos_model.keras")

# Your audio processing...
mel = extract_melspectrogram(audio)
probs = model.predict(mel)
```

---

## 💡 טיפים

1. **בדוק את ה-Model:** לפעמים מודל ישן יכול להיות גרוע יותר. אם דיוק נמוך, ניסיון אימון חדש עם DEVELOPMENT.md

2. **Noise Floor:** בסביבה רועשת מאוד, יתכנו יותר false positives. שנה את THRESHOLD או שפר את הנתונים.

3. **Microphone Quality:** מיקרופון טוב יותר = קלט טוב יותר = זיהוי טוב יותר

4. **Real-time Constraints:** אם צריך עיבוד יותר מהיר, תוכל להנמיך את DURATION