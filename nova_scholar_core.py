import os
import boto3
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

def scrape_arxiv(query):
    print(f"Scraping ArXiv for: '{query}'...")
    scraped_data = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) 
        page = browser.new_page()
        
        print("Navigating to ArXiv...")
        page.goto("https://arxiv.org/")
        
        print("Typing query and hitting Enter...")
        page.fill("input[name='query']", query)
        page.press("input[name='query']", "Enter")
        
        print("Waiting for results...")
        page.wait_for_selector(".arxiv-result", timeout=15000)
        
        results = page.query_selector_all(".arxiv-result")
        for i in range(min(3, len(results))):
            title_elem = results[i].query_selector("p.title")
            
            if title_elem:
                title = title_elem.text_content().strip()
                scraped_data.append(title)
            
        browser.close()
    return scraped_data

def analyze_with_nova(data, query):
    print("\nSending data to Nova 2 Lite...")
    bedrock = boto3.client(
        service_name='bedrock-runtime',
        region_name=os.getenv("AWS_DEFAULT_REGION", "us-east-1")
    )
    
    prompt = f"I searched for '{query}'. Here are the top papers: {data}. Write a short, highly technical 3-sentence summary of what this research field is currently focused on."
    
    messages = [{
        "role": "user",
        "content": [{"text": prompt}]
    }]

    try:
        res = bedrock.converse(
            modelId='us.amazon.nova-2-lite-v1:0',
            messages=messages
        )
        return res['output']['message']['content'][0]['text']
    except Exception as e:
        return f"Nova Analysis Failed: {e}"

if __name__ == "__main__":
    target_topic = "Agentic AI UI Automation"
    
    papers = scrape_arxiv(target_topic)
    for p in papers:
        print(f"- {p}")
        
    print("\n--- Nova Analysis ---")
    analysis = analyze_with_nova(papers, target_topic)
    print(analysis)