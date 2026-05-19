"""
VoxBridge — Voice-First AI Assistant
Main entry point.

This is a minimal skeleton. It runs in text mode by default so that
you can verify the AI loop before integrating microphone and TTS.
"""

import sys
from pathlib import Path

# Allow imports from the src/ folder
sys.path.insert(0, str(Path(__file__).parent))

# Modules to be implemented step by step
# from speech_to_text import transcribe_audio
# from text_to_speech import speak
# from ai_engine import get_response


def greet():
    """Print a startup banner."""
    print("=" * 50)
    print("  VoxBridge — Voice-First AI Assistant")
    print("  v0.1 (development)")
    print("=" * 50)
    print("Type 'exit' or press Ctrl+C to quit.\n")


def main():
    """Main interaction loop (text mode for now)."""
    greet()

    try:
        while True:
            # Step 1: receive user input
            # TODO: replace with transcribe_audio() once microphone module is ready
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in {"exit", "quit", "bye"}:
                print("Goodbye!")
                break

            # Step 2: process through the AI engine
            # TODO: replace with get_response(user_input) once AI module is ready
            response = f"[placeholder AI response to]: {user_input}"

            # Step 3: deliver the response
            # TODO: replace with speak(response) once TTS module is ready
            print(f"VoxBridge: {response}\n")

    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
