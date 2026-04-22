import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # loads .env file


class AIAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def analyze_service(self, target, port, service):
        prompt = f"""
You are an expert VAPT analyst.

Target: {target}
Port: {port}
Service: {service}

Provide:
1. Possible actions
2. Exact commands (nmap, curl, etc.)
3. Short explanation for each step
Avoid exploitation.
"""

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content