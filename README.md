# Business Decision Assistant (Gemini + ReAct)
A Python AI agent application that analyzes business problems and generates structured recommendations for businesses.

## Features
- Google Gemini API integration for analysis generation
- ReAct-style reasoning loop in `agent.py`
- Decision framework covering:
  - Problem understanding
  - Option identification
  - Pros and cons analysis
  - Cost considerations
  - Final recommendation
- Streamlit UI for interactive usage
## Project Structure
app.py
agent.py
decision_framework.py
gemini_model.py
requirements.txt
README.md
## Setup
1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set your Gemini API key:

   ```bash
   export GOOGLE_API_KEY="your_api_key_here"
   ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

## Example Business Problem
> Should our company build or buy an AI chatbot system?

The output is structured into:
- Problem
- Options
- Pros and Cons
- Cost considerations
- Final recommendation
## Notes
- If `GOOGLE_API_KEY` is missing, the UI will show an actionable error message.
- The agent exposes a reasoning trace in the UI for demonstration and teaching purposes.



