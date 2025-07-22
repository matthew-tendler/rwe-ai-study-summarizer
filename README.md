# AI Study Summarizer

A lightweight GenAI tool that lets researchers, clinical scientists, and pharma teams rapidly summarize real PubMed studies using real-world data (RWD) queries.

## Who is this for?

- **Primary Users**:
  - Clinical scientists designing or evaluating trial protocols
  - RWE leads in pharma seeking literature context
  - Outcomes researchers screening literature for cohort-relevant data

- **Secondary Users**:
  - Medical affairs teams preparing literature summaries
  - Analysts doing landscape analysis or signal detection

## 💡 What does it do?

This app fetches real PubMed abstracts from the [Europe PMC API](https://europepmc.org/) and uses a Hugging Face language model to generate concise, AI-powered summaries of the top few studies.

The goal is to provide **quick context** — not deep NLP — in a format that’s:
- Easy to copy
- Fast to skim
- Repeatable for any search term

## ⚙️ Tech Stack

- **Streamlit**: UI framework
- **Europe PMC API**: Abstract + metadata source (free)
- **Hugging Face Transformers API**: Model for summarization (`distilbart-cnn-12-6`)
- **Python**: Logic and backend
- **Pandas**: Table rendering

## 📦 Run Locally

1. Create a `.venv`:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

2. Set your Hugging Face key:
    ```bash
    export RWE_THREE_COPILOT=your_hf_key_here
    ```

3. Launch the app:
    ```bash
    streamlit run app.py
    ```

## 🧪 Coming Soon

This is one app in a broader **RWE GenAI App Portfolio**. Future apps may include:
- Comparator study finders
- Cohort overlap detection
- AI-assisted protocol eligibility matchers
