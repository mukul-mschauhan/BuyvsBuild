"""Streamlit frontend for the Business Decision Assistant."""

from __future__ import annotations

import streamlit as st

from agent import BusinessDecisionAgent
from gemini_model import GeminiDecisionModel


st.set_page_config(page_title="AI Decision Agent", page_icon="🧭", layout="centered")
st.title("AI Decision Agent")
st.caption("Analyze business problems using Gemini + a ReAct-style decision loop.")

problem_text = st.text_area(
    "Enter Business Problem",
    placeholder="Should our company build or buy an AI chatbot system?",
    height=140,
)

if st.button("Generate Decision Analysis", type="primary"):
    if not problem_text.strip():
        st.warning("Please enter a business problem.")
    else:
        with st.spinner("Running agent reasoning loop..."):
            try:
                agent = BusinessDecisionAgent(model=GeminiDecisionModel())
                analysis = agent.analyze(problem_text.strip())
            except Exception as exc:  # noqa: BLE001
                st.error(f"Unable to run analysis: {exc}")
            else:
                st.subheader("Problem")
                st.write(analysis.problem)

                st.subheader("Options")
                st.write(analysis.options)

                st.subheader("Pros and Cons")
                st.write(analysis.pros_and_cons)

                st.subheader("Cost considerations")
                st.write(analysis.cost_considerations)

                st.subheader("Final recommendation")
                st.success(analysis.final_recommendation)

                with st.expander("Reasoning Trace"):
                    for idx, step in enumerate(agent.trace, start=1):
                        st.markdown(f"**Step {idx} Thought:** {step.thought}")
                        st.markdown(f"**Action:** {step.action}")
                        st.markdown("**Observation:**")
                        st.write(step.observation)
                        st.divider()
