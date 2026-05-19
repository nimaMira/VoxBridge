"""
Speech-to-Text module using OpenAI Whisper.
This is a skeleton — actual implementation comes in v0.1.
"""

# import whisper
# import sounddevice as sd
# import numpy as np


def transcribe_audio(audio_data=None, language: str = "en") -> str:
    """
    Transcribe audio to text using Whisper.

    Args:
        audio_data: numpy array of audio samples (16kHz mono recommended)
        language: ISO language code (en, de, fa, ...)

    Returns:
        Transcribed text as a string.
    """
    # TODO: implement
    # model = whisper.load_model("base")
    # result = model.transcribe(audio_data, language=language)
    # return result["text"]
    raise NotImplementedError("transcribe_audio is not implemented yet.")


def record_audio(duration_seconds: float = 5.0, sample_rate: int = 16000):
    """
    Record audio from the default microphone for a fixed duration.

    Returns:
        numpy array of audio samples.
    """
    # TODO: implement
    # audio = sd.rec(int(duration_seconds * sample_rate),
    #                samplerate=sample_rate, channels=1, dtype="float32")
    # sd.wait()
    # return audio.flatten()
    raise NotImplementedError("record_audio is not implemented yet.")
