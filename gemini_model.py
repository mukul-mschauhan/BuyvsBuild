"""Gemini model integration for the Business Decision Assistant."""

from __future__ import annotations

import os
import google.generativeai as genai


class GeminiDecisionModel:
    """Small wrapper around Gemini for decision-analysis prompts."""

    def __init__(self, model_name: str = "gemini-1.5-flash") -> None:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError(
                "GOOGLE_API_KEY is not set. Add it to your environment before running the app."
            )

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate(self, prompt: str, *, temperature: float = 0.2) -> str:
        """Generate a model response for a prompt."""
        response = self.model.generate_content(
            prompt,
            generation_config={"temperature": temperature},
        )
        return (response.text or "").strip()
