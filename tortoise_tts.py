from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio, load_voice, load_voices
import torchaudio


def tts(text: str, out_path: str):
    tts = TextToSpeech(use_deepspeed=True, kv_cache=True)

    # This is the text that will be spoken.
    text = "Joining two modalities results in a surprising increase in generalization! What would happen if we combined them all?"

    # Here's something for the poetically inclined.. (set text=)
    """
    Then took the other, as just as fair,
    And having perhaps the better claim,
    Because it was grassy and wanted wear;
    Though as for that the passing there
    Had worn them really about the same,"""

    # Pick a "preset mode" to determine quality. Options: {"ultra_fast", "fast" (default), "standard", "high_quality"}. See docs in api.py
    preset = "ultra_fast"
    # Pick a voice
    voice = "tom"
    voice_samples, conditioning_latents = load_voice(voice)
    gen = tts.tts_with_preset(
        text,
        voice_samples=voice_samples,
        conditioning_latents=conditioning_latents,
        preset=preset,
    )

    # Save the audio to a file
    torchaudio.save(out_path, gen.squeeze(0).cpu(), 24000)
