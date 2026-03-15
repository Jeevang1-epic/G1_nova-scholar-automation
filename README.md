# Nova-Scholar

**Agentic Web Research & Automation Assistant**

Nova-Scholar is an autonomous AI agent designed to revolutionize academic literature reviews. Moving beyond static datasets, this system utilizes dynamic UI automation to browse the live web, extract the latest research papers, and synthesize highly technical summaries using Amazon's frontier models.

## Core Features
* **Live UI Automation:** Utilizes Playwright to autonomously navigate academic databases (e.g., ArXiv), bypass basic bot detection, and extract real-time research titles directly from the DOM.
* **Agentic Reasoning:** Integrates with Amazon Nova 2 Lite via the AWS Bedrock Converse API to process and summarize disparate research papers instantly.
* **Secure Web Interface:** Built with Streamlit, featuring a modern dark-mode UI and a secure configuration sidebar. Users must input their own AWS Bedrock keys, ensuring the developer's credentials remain completely protected from public exposure.

## System Architecture
* **Frontend:** Streamlit, Custom CSS
* **Automation Engine:** Python, Playwright
* **LLM / Intelligence:** AWS Bedrock, Amazon Nova 2 Lite (us.amazon.nova-2-lite-v1:0)

## Prerequisites
* Python 3.10+
* AWS Account with access to Amazon Bedrock (Nova 2 Lite model enabled)
* AWS Bedrock API Key (ABSK prefix)

## Installation and Setup

1. **Clone the repository:**
   
       git clone [https://github.com/yourusername/nova-scholar.git](https://github.com/yourusername/nova-scholar.git)
       cd nova-scholar

2. Install dependencies:**

       pip install -r requirements.txt

3. **Install Playwright browser binaries:**

       playwright install

4. **Launch the application:**

       streamlit run app.py


## Usage

* Launch the Streamlit application via the terminal command above.

* Open the configuration sidebar on the left and securely enter your AWS Bedrock API Key.

* Enter a complex research query into the main search interface (e.g., "Self-reflecting capabilities in autonomous LLM agents").

* Click "Deploy Autonomous Agent" and allow the engine to navigate the web, extract data, and generate the analytical summary.

## Disclaimer

* This project was developed as a proof-of-concept for the Devpost hackathon. Users are responsible for their own AWS Bedrock API usage costs when running this application locally or via cloud deployment.
