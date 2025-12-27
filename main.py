from profile_gen import generate_project_profile
from billing_gen import generate_mock_billing
from cost_analyzer import generate_cost_report
from html_exporter import export_html_report
import json

def enter_project_description():
    text = input("Enter project description:\n")
    with open("data/project_description.txt", "w", encoding="utf-8") as file:
        file.write(text)
    print("project description saved")

def run_full_pipeline():
    generate_project_profile()
    generate_mock_billing()
    generate_cost_report()
    print("cost analysis completed")

def view_recommendations():
    with open("output/cost_optimization_report.json", "r", encoding="utf-8") as file:
        report = json.load(file)
    for item in report["recommendations"]:
        print("- " + item["title"])

while True:
    print("\n1. Enter new project description")
    print("2. Run complete cost analysis")
    print("3. View recommendations")
    print("4. Export HTML report")
    print("5. Exit")

    choice = input("Select option: ")

    if choice == "1":
        enter_project_description()
    elif choice == "2":
        run_full_pipeline()
    elif choice == "3":
        view_recommendations()
    elif choice == "4":
        export_html_report()
    elif choice == "5":
        break
    else:
        print("invalid option")
