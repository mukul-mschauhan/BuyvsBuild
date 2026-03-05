"""Decision framework utilities used by the reasoning agent."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class DecisionAnalysis:
    """Structured decision output for rendering in Streamlit."""

    problem: str
    options: str
    pros_and_cons: str
    cost_considerations: str
    final_recommendation: str


def build_framework_prompt(problem: str, context_notes: str = "") -> str:
    """Create a prompt aligned to a simple enterprise decision framework."""
    return f"""
    You are a Business Decision Assistant.
    Analyze the business problem using this framework:
    1) Problem understanding
    2) Option identification
    3) Pros and cons analysis
    4) Cost considerations
    5) Final recommendation
    
    Business problem:
    {problem}
    
    Reasoning context from previous steps:
    {context_notes}
    
    Return your answer in this exact format with markdown headings:
    ## Problem
    ## Options
    ## Pros and Cons
    ## Cost considerations
    ## Final recommendation""".strip()


def parse_structured_response(problem: str, text: str) -> DecisionAnalysis:
    """Parse markdown sections into a DecisionAnalysis object."""
    sections = {
        "Problem": "",
        "Options": "",
        "Pros and Cons": "",
        "Cost considerations": "",
        "Final recommendation": "",
    }

    current_section = None
    lines = text.splitlines()

    for line in lines:
        normalized = line.strip()
        if normalized.startswith("## "):
            header = normalized.replace("## ", "", 1).strip()
            if header in sections:
                current_section = header
                continue
        if current_section:
            sections[current_section] += (line + "\n")

    return DecisionAnalysis(
        problem=(sections["Problem"].strip() or problem),
        options=sections["Options"].strip() or "No options identified.",
        pros_and_cons=sections["Pros and Cons"].strip()
        or "No pros/cons analysis returned.",
        cost_considerations=sections["Cost considerations"].strip()
        or "No cost considerations returned.",
        final_recommendation=sections["Final recommendation"].strip()
        or "No recommendation returned.",
    )
