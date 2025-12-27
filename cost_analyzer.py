import json
from llmcall import call_llm_json

def generate_cost_report():
    with open("output/project_profile.json", "r", encoding="utf-8") as file:
        project_profile = json.load(file)

    with open("output/mock_billing.json", "r", encoding="utf-8") as file:
        billing_data = json.load(file)["records"]

    total_cost = sum(item["cost_inr"] for item in billing_data)

    service_costs = {}
    for item in billing_data:
        service_name = item["description"].split()[0]
        service_costs[service_name] = service_costs.get(service_name, 0) + item["cost_inr"]

    analysis = {
        "total_monthly_cost": total_cost,
        "budget": project_profile["budget_inr_per_month"],
        "budget_variance": total_cost - project_profile["budget_inr_per_month"],
        "service_costs": service_costs,
        "is_over_budget": total_cost > project_profile["budget_inr_per_month"]
    }

    prompt = f"""
You are a cloud cost optimization expert.
Based on the project profile and cost analysis below, generate 6 to 10 actionable cost optimization recommendations.
Recommendations must include multi-cloud options and open-source alternatives where applicable.
Return ONLY valid JSON.
Do not add explanations.
Do not add markdown.

Required format:
[
  {{
    "title": "",
    "service": "",
    "current_cost": number,
    "potential_savings": number,
    "recommendation_type": "",
    "description": "",
    "implementation_effort": "",
    "risk_level": "",
    "cloud_providers": []
  }}
]

Project Profile:
{json.dumps(project_profile)}

Cost Analysis:
{json.dumps(analysis)}
"""

    recommendations = call_llm_json(prompt, temperature=0.3)

    report = {
        "project_name": project_profile["name"],
        "analysis": analysis,
        "recommendations": recommendations
    }

    with open("output/cost_optimization_report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)
