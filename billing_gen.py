import json
from llmcall import call_llm_json

def generate_mock_billing():
    with open("output/project_profile.json", "r", encoding="utf-8") as file:
        project_profile = json.load(file)

    prompt = f"""
You are a cloud billing system.
Generate realistic monthly cloud billing data based on the project profile below.
Ensure total cost is close to but does not exceed the monthly budget.
Return ONLY valid JSON.
Do not add explanations.
Do not add markdown.

Requirements:
- Generate 12 to 20 records
- Include compute, database, storage, networking, monitoring
- Each record must contain:
  month, service, resource_id, region, usage_type, usage_quantity, unit, cost_inr, description

Project Profile:
{json.dumps(project_profile)}
"""

    parsed_json = call_llm_json(prompt, temperature=0.2)

    with open("output/mock_billing.json", "w", encoding="utf-8") as file:
        json.dump(parsed_json, file, indent=2)
