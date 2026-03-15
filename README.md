# Nova-Scholar

**Agentic Web Research & Automation Assistant**

Nova-Scholar is an autonomous AI agent built to revolutionize academic literature reviews. Instead of relying on static, outdated datasets, Nova-Scholar utilizes UI automation to browse the live web, extract the latest research papers, and synthesize highly technical summaries using Amazon's frontier models.

### Features
* **Live UI Automation:** Uses Playwright to autonomously navigate the ArXiv database, bypass basic bot detection, and scrape real-time academic titles.
* **Agentic Reasoning:** Integrates with **Amazon Nova 2 Lite** via the AWS Bedrock Converse API to instantly process and summarize disparate research papers.
* **Secure Web Interface:** Built with Streamlit, featuring a modern dark-mode UI and a secure sidebar configuration that requires users to input their own AWS Bedrock keys, protecting the developer's credentials.

### Tech Stack
* **Frontend:** Streamlit, Custom CSS
* **Automation:** Python, Playwright
* **AI / LLM:** AWS Bedrock, Amazon Nova 2 Lite

### How to Run Locally
1. Clone this repository.
2. Install the required dependencies:
   
       pip install -r requirements.txt
       playwright install
