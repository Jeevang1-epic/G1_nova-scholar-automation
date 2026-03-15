import os
import json
import boto3
from dotenv import load_dotenv

load_dotenv()

def test_connection():
    token = os.getenv("AWS_BEARER_TOKEN_BEDROCK")
    if not token:
        print("Bruh, the .env file isn't loading! Check the spelling.")
        return
        
    print("Token found! Connecting to AWS...")
    
    bedrock = boto3.client(
        service_name='bedrock-runtime',
        region_name=os.getenv("AWS_DEFAULT_REGION", "us-east-1")
    )
    
    body = json.dumps({
        "inputText": "Hey Nova, just say 'System Online'.",
        "textGenerationConfig": {"maxTokenCount": 50, "temperature": 0.5}
    })

    try:
        res = bedrock.invoke_model(
            body=body,
            modelId='amazon.nova-2-lite-v1:0',
            accept='application/json',
            contentType='application/json'
        )
        out = json.loads(res.get('body').read())
        print("Success =>", out.get('results')[0].get('outputText'))
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    test_connection()