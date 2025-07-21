import requests
import re
import os

HUGGINGFACE_SUMMARIZATION_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"

def strip_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def fetch_abstracts_from_europepmc(query: str, max_results: int = 3):
    base_url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
    params = {
        "query": query,
        "format": "json",
        "pageSize": max_results,
        "resultType": "core"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    results = []
    for item in data.get("resultList", {}).get("result", []):
        if "abstractText" in item and item["abstractText"].strip():
            results.append({
                "abstract": strip_html_tags(item["abstractText"]),
                "pmid": item.get("pmid"),
                "doi": item.get("doi"),
                "title": item.get("title"),
                "journal": item.get("journalTitle")
            })
    return results

def hf_summarize(text):
    token = os.getenv("RWE_THREE_COPILOT")
    if not token:
        return "[Error: Hugging Face API token not set. Please set RWE_THREE_COPILOT in your environment.]"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"inputs": text}
    response = requests.post(HUGGINGFACE_SUMMARIZATION_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()[0].get("summary_text", "[No summary returned]")
    else:
        return f"[Error: Hugging Face API returned status {response.status_code}]"

def summarize_abstract(abstracts):
    if not abstracts:
        return "No abstracts found."
    abstracts = abstracts[:2]
    summaries = []
    for a in abstracts:
        summary = hf_summarize(a["abstract"][:800])
        summaries.append(summary)
    combined = " ".join(summaries)[:2000]
    return hf_summarize(combined)

def get_tech_stack():
    return (
        "Tech stack: Streamlit (UI), EuropePMC API (data), Hugging Face Inference API (DistilBART CNN summarization), "
        "Pandas (table), Python 3."
    )
