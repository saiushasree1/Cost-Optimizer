import json

def export_html_report():
    with open("output/cost_optimization_report.json", "r", encoding="utf-8") as file:
        report = json.load(file)

    rows = ""
    for item in report["recommendations"]:
        risk_class = item["risk_level"].lower()
        rows += f"""
        <tr>
            <td>{item["title"]}</td>
            <td>{item["service"]}</td>
            <td>₹{item["current_cost"]}</td>
            <td class="positive">₹{item["potential_savings"]}</td>
            <td>{item["implementation_effort"]}</td>
            <td><span class="pill {risk_class}">{item["risk_level"]}</span></td>
        </tr>
        """

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Cloud Cost Optimization Report</title>
        <style>
            :root {{
                --bg-main: #f5f7fb;
                --bg-card: #ffffff;
                --primary: #1f4fd8;
                --primary-soft: #e8efff;
                --text-main: #0f172a;
                --text-muted: #64748b;
                --border-soft: #e5e7eb;
                --success: #15803d;
                --success-bg: #dcfce7;
                --warning: #92400e;
                --warning-bg: #fef3c7;
                --danger: #991b1b;
                --danger-bg: #fee2e2;
            }}

            body {{
                margin: 0;
                font-family: "Segoe UI", Inter, system-ui, sans-serif;
                background: var(--bg-main);
                color: var(--text-main);
            }}

            .layout {{
                max-width: 1200px;
                margin: 50px auto;
                padding: 0 20px;
            }}

            .header {{
                background: linear-gradient(135deg, #1f4fd8, #3b82f6);
                color: white;
                padding: 36px;
                border-radius: 18px;
                box-shadow: 0 20px 45px rgba(31,79,216,0.35);
            }}

            .header h1 {{
                margin: 0;
                font-size: 34px;
                font-weight: 600;
            }}

            .header p {{
                margin-top: 10px;
                font-size: 16px;
                opacity: 0.9;
            }}

            .stats {{
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 24px;
                margin-top: 32px;
            }}

            .stat {{
                background: var(--bg-card);
                border-radius: 16px;
                padding: 28px;
                box-shadow: 0 12px 30px rgba(0,0,0,0.06);
                border: 1px solid var(--border-soft);
            }}

            .stat span {{
                font-size: 14px;
                color: var(--text-muted);
            }}

            .stat strong {{
                margin-top: 8px;
                display: block;
                font-size: 26px;
                font-weight: 600;
                color: var(--primary);
            }}

            .section {{
                margin-top: 56px;
            }}

            .section h2 {{
                font-size: 26px;
                margin-bottom: 20px;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                background: var(--bg-card);
                border-radius: 18px;
                overflow: hidden;
                box-shadow: 0 18px 40px rgba(0,0,0,0.08);
                border: 1px solid var(--border-soft);
            }}

            th {{
                background: #f1f5ff;
                color: var(--text-main);
                padding: 16px;
                font-size: 13px;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }}

            td {{
                padding: 16px;
                border-bottom: 1px solid var(--border-soft);
                font-size: 14px;
            }}

            tr:last-child td {{
                border-bottom: none;
            }}

            tr:hover {{
                background: #f8fafc;
            }}

            .positive {{
                color: var(--success);
                font-weight: 600;
            }}

            .pill {{
                padding: 6px 14px;
                border-radius: 999px;
                font-size: 12px;
                font-weight: 600;
            }}

            .low {{
                background: var(--success-bg);
                color: var(--success);
            }}

            .medium {{
                background: var(--warning-bg);
                color: var(--warning);
            }}

            .high {{
                background: var(--danger-bg);
                color: var(--danger);
            }}

            .footer {{
                margin: 48px 0 24px;
                text-align: center;
                font-size: 13px;
                color: var(--text-muted);
            }}
        </style>
    </head>
    <body>
        <div class="layout">
            <div class="header">
                <h1>Cloud Cost Optimization Report</h1>
                <p>Project: {report["project_name"]}</p>
            </div>

            <div class="stats">
                <div class="stat">
                    <span>Total Monthly Cost</span>
                    <strong>₹{report["analysis"]["total_monthly_cost"]}</strong>
                </div>
                <div class="stat">
                    <span>Budget</span>
                    <strong>₹{report["analysis"]["budget"]}</strong>
                </div>
                <div class="stat">
                    <span>Over Budget</span>
                    <strong>{report["analysis"]["is_over_budget"]}</strong>
                </div>
            </div>

            <div class="section">
                <h2>Optimization Recommendations</h2>
                <table>
                    <tr>
                        <th>Title</th>
                        <th>Service</th>
                        <th>Current Cost</th>
                        <th>Potential Savings</th>
                        <th>Effort</th>
                        <th>Risk</th>
                    </tr>
                    {rows}
                </table>
            </div>

            <div class="footer">
                Generated by AI-Powered Cloud Cost Optimizer
            </div>
        </div>
    </body>
    </html>
    """

    with open("output/cost_report.html", "w", encoding="utf-8") as file:
        file.write(html)

    print("HTML report exported")
