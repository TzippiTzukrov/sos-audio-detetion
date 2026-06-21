def load_audio(file_path, sr=22050, mono=True):
    audio, sample_rate = librosa.load(file_path, sr=sr, mono=mono)
    return audio, sample_rate

def extract_melspectrogram(audio, sr=22050, n_mels=128):
    mel = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=n_mels)
    mel_db = librosa.power_to_db(mel, ref=np.max)
    return mel_db

def normalize_audio(audio, target_length=None):
    max_val = np.max(np.abs(audio))
    if max_val > 0:
        audio = audio / max_val
    
    if target_length:
        if len(audio) < target_length:
            audio = np.pad(audio, (0, target_length - len(audio)))
        else:
            audio = audio[:target_length]
    
    return audio