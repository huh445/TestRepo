#!/usr/bin/env python
import os
import sys
from faster_whisper import WhisperModel

# ─── Configuration ─────────────────────────────────────────────────────────────
MODEL_SIZE   = "medium"             # tiny, base, small, medium, large-v2
BEAM_SIZE    = 5
DEFAULT_FILE = "audio.mp3"
# ────────────────────────────────────────────────────────────────────────────────

# Pick up audio filename from CLI or use default
audio_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_FILE

if not os.path.isfile(audio_path):
    print(f"❌ File not found: {audio_path}")
    sys.exit(1)

# Try GPU first, fallback to CPU
# try:
#     model = WhisperModel(MODEL_SIZE, device="cuda",   compute_type="float16")
#     print("✅ Running on GPU")
# except Exception as gpu_err:
# print(f"⚠ GPU unavailable or mismatch ({gpu_err}), falling back to CPU")
model = WhisperModel(MODEL_SIZE, device="cpu",    compute_type="int8")

# Transcribe
segments, info = model.transcribe(audio_path, beam_size=BEAM_SIZE)

# Write transcript
out_txt = os.path.splitext(audio_path)[0] + "_transcript.txt"
with open(out_txt, "w", encoding="utf-8") as f:
    for segment in segments:
        f.write(segment.text.strip() + "\n")

print(f"\n✅ Transcript complete — saved to {out_txt}")
