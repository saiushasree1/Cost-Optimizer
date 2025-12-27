import json
from llmcall import call_llm_json

def generate_project_profile():
    with open("data/project_description.txt", "r", encoding="utf-8") as file:
        project_text = file.read()

    prompt = f"""
You are a backend system.
Extract structured project information from the text below.
Return ONLY valid JSON.
Do not add explanations.
Do not add markdown.

Required JSON format:
{{
  "name": "",
  "budget_inr_per_month": number,
  "description": "",
  "tech_stack": {{
    "frontend": "",
    "backend": "",
    "database": "",
    "storage": "",
    "hosting": ""
  }},
  "non_functional_requirements": []
}}

Text:
{project_text}
"""

    result = call_llm_json(prompt, temperature=0)

    with open("output/project_profile.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
