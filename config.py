"""
SOS Audio Detection - Configuration

כל ה-constants של הפרויקט במקום אחד
"""

# ═══════════════════════════════════════════════════════════════════
# 🎵 AUDIO PROCESSING
# ═══════════════════════════════════════════════════════════════════

SR = 22050                  # Sample rate (Hz) - תדר דגימה
DURATION = 2                # Duration of audio window (seconds) - משך החלון
N_MELS = 128                # Number of mel bands - כמה פסים של תדרים
MONO = True                 # Convert to mono - ערוץ יחיד

# ═══════════════════════════════════════════════════════════════════
# 🎯 MODEL & CATEGORIES
# ═══════════════════════════════════════════════════════════════════

MODEL_PATH = "src/sos_model.keras"          # Path to trained model
CATEGORIES = [
    "scream",       # זעקה, סירנה
    "crying",       # בכי, קול כאב
    "explosion",    # פיצוץ, רעם
    "background"    # רעע רגיל, לא חירום
]

# ═══════════════════════════════════════════════════════════════════
# 🔍 REAL-TIME DETECTION
# ═══════════════════════════════════════════════════════════════════

THRESHOLD = 0.50            # Confidence threshold for alert (0.0-1.0)
STEP = 1                    # Overlap between windows (seconds)

# Normalization constants (from training data)
MEAN = -30.0                # Mean of mel spectrograms
STD = 15.0                  # Standard deviation of mel spectrograms

# ═══════════════════════════════════════════════════════════════════
# 🏋️ TRAINING
# ═══════════════════════════════════════════════════════════════════

EPOCHS = 50                 # Number of epochs
BATCH_SIZE = 32             # Batch size
VALIDATION_SPLIT = 0.2      # 20% for validation

# Data augmentation parameters
NOISE_FACTOR = 0.005        # Noise level for augmentation
TIME_SHIFT_RANGE = 0.1      # Time shift range (as fraction)

# ═══════════════════════════════════════════════════════════════════
# 📁 PATHS
# ═══════════════════════════════════════════════════════════════════

DATA_RAW = "data/raw"              # Raw audio files
DATA_PROCESSED = "data/processed"   # Processed mel spectrograms

# ═══════════════════════════════════════════════════════════════════
# 📊 LOGGING & OUTPUT
# ═══════════════════════════════════════════════════════════════════

LOG_LEVEL = "INFO"          # DEBUG, INFO, WARNING, ERROR
VERBOSE = False             # Print details during processing

# ═══════════════════════════════════════════════════════════════════
# 🧪 DEBUGGING
# ═══════════════════════════════════════════════════════════════════

DEBUG = False               # Enable debug mode
SAVE_INTERMEDIATE = False   # Save intermediate outputs (spectrograms, etc)