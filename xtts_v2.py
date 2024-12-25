import torch
import sys
from TTS.api import TTS
from TTS.tts.configs.xtts_config import XttsConfig, XttsAudioConfig, XttsArgs
from TTS.config import BaseDatasetConfig

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
torch.serialization.add_safe_globals([XttsConfig, XttsAudioConfig, BaseDatasetConfig, XttsArgs])

def tts(text: str, out_path: str):
    # Initialize TTS with XTTS v2 model
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    print(tts.is_multi_speaker)
    print("TTS model loaded")
    print("Speakers: ", tts.synthesizer.tts_model.speaker_manager.name_to_id)

    # Generate speech
    tts.tts_to_file(
        text=text,
        file_path=out_path,
        speaker="Claribel Dervla",
        speaker_wav=None,  # Can specify speaker reference audio
        language="en"
    )
    print(f"Audio content written to file '{out_path}'")
