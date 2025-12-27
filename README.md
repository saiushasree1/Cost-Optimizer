# AI-Powered Cloud Cost Optimizer (LLM-Driven)

## Overview
This project is an AI-powered cloud cost optimization tool built using Python and Large Language Models (LLMs).  
Users provide a plain-English project description, and the system automatically:

- Extracts a structured project profile
- Generates realistic synthetic cloud billing data
- Analyzes costs against a given budget
- Produces actionable, multi-cloud cost optimization recommendations
- Presents results via a CLI and an optional HTML report

The system is designed to be modular, robust, and extensible, following real-world backend engineering practices.

## Project Structure

```
cost_optimizer/
│
├── main.py
├── llmcall.py
├── profile_gen.py
├── billing_gen.py
├── cost_analyzer.py
├── html_exporter.py
│
├── data/
│   └── project_description.txt
│
├── output/
│   ├── project_profile.json
│   ├── mock_billing.json
│   ├── cost_optimization_report.json
│   └── cost_report.html
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Tech Stack
- Language: Python 3.10+
- LLM Provider: Hugging Face Inference API
- Model: meta-llama/Meta-Llama-3-8B-Instruct
- Environment Management: venv, python-dotenv
- Interface: Command Line Interface (CLI)
- Output Formats: JSON, HTML

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-github-repo-url>
cd cost_optimizer
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file:
```
HF_TOKEN=your_huggingface_api_key
```

---

## How to Run

```bash
python main.py
```

### CLI Options
```
1. Enter new project description
2. Run complete cost analysis
3. View recommendations
4. Export HTML report
5. Exit
```

---

## Sample Outputs
- project_profile.json
- mock_billing.json
- cost_optimization_report.json
- cost_report.html

---

## Design Highlights
- Single reusable LLM client
- Clean modular architecture
- Defensive programming with retries and validation
- Easy to extend for additional cloud providers

---

## Tools Used
- Hugging Face Inference API
- Meta LLaMA 3 Instruct
- Python standard libraries
- coding assistant: chatgpt
- Please checkout project.pdf to see how I have leveraged coding assistant
---

## Notes on AI Usage
AI tools were used for assistance.  
All code was reviewed, understood, and customized to meet assignment requirements.

---

## Author
Saiushasree Kasu
B.Tech – Electronics and Communication Engineering  
IIIT Allahabad  

---
