"""ReAct-style business decision agent."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from decision_framework import (
    DecisionAnalysis,
    build_framework_prompt,
    parse_structured_response,
)
from gemini_model import GeminiDecisionModel


@dataclass
class ReasoningStep:
    thought: str
    action: str
    observation: str


@dataclass
class BusinessDecisionAgent:
    """Agent with a lightweight ReAct reasoning loop."""

    model: GeminiDecisionModel
    max_steps: int = 3
    trace: List[ReasoningStep] = field(default_factory=list)

    def _run_reasoning_loop(self, problem: str) -> str:
        self.trace.clear()
        running_notes: List[str] = []

        for step_number in range(1, self.max_steps + 1):
            thought = (
                f"Step {step_number}: clarify decision scope and improve recommendation quality."
            )
            action = "Evaluate build-vs-buy options with benefits, risks, and cost trade-offs."

            prompt = build_framework_prompt(problem=problem, context_notes="\n".join(running_notes))
            observation = self.model.generate(prompt)

            self.trace.append(
                ReasoningStep(thought=thought, action=action, observation=observation)
            )
            running_notes.append(observation)

        return self.trace[-1].observation

    def analyze(self, problem: str) -> DecisionAnalysis:
        """Run reasoning loop and return structured recommendation."""
        final_text = self._run_reasoning_loop(problem)
        return parse_structured_response(problem, final_text)
