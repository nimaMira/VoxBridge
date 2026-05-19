"""
AI Engine — communicates with the chosen LLM backend.
Supports OpenAI API and Ollama (local).
"""

import os
# from openai import OpenAI


SYSTEM_PROMPT = """You are VoxBridge, a voice-first AI assistant designed to be
accessible, empathetic, and human-centered. Keep responses concise and natural,
suitable for being spoken aloud. Adapt to the user's tone and emotional state."""


def get_response(user_message: str, history: list | None = None) -> str:
    """
    Send a user message to the configured AI backend and return its response.

    Args:
        user_message: the user's spoken input as transcribed text
        history: optional list of previous {role, content} messages

    Returns:
        The AI's response as a string.
    """
    backend = os.getenv("AI_BACKEND", "openai")

    if backend == "openai":
        return _get_openai_response(user_message, history)
    elif backend == "ollama":
        return _get_ollama_response(user_message, history)
    else:
        raise ValueError(f"Unknown AI_BACKEND: {backend}")


def _get_openai_response(user_message: str, history: list | None) -> str:
    """Internal: OpenAI API call."""
    # TODO: implement
    # client = OpenAI()
    # messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    # if history:
    #     messages.extend(history)
    # messages.append({"role": "user", "content": user_message})
    #
    # response = client.chat.completions.create(
    #     model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    #     messages=messages
    # )
    # return response.choices[0].message.content
    raise NotImplementedError("OpenAI backend is not implemented yet.")


def _get_ollama_response(user_message: str, history: list | None) -> str:
    """Internal: Ollama local LLM call."""
    # TODO: implement
    raise NotImplementedError("Ollama backend is not implemented yet.")
