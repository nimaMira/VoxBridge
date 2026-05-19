"""
Text-to-Speech module.
Uses pyttsx3 for offline TTS in v0.1.
"""

# import pyttsx3


def speak(text: str, rate: int = 175, volume: float = 1.0) -> None:
    """
    Speak the given text out loud.

    Args:
        text: text to read aloud
        rate: words per minute
        volume: 0.0 to 1.0
    """
    # TODO: implement
    # engine = pyttsx3.init()
    # engine.setProperty("rate", rate)
    # engine.setProperty("volume", volume)
    # engine.say(text)
    # engine.runAndWait()
    raise NotImplementedError("speak is not implemented yet.")
