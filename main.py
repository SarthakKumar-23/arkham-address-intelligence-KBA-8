import os 
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ARKHAM_API_KEY")

address = "0x3a9F7ab2B042242097c5d51922Aa82e70c7991ca"

url = f"https://api.arkhamintelligence.com/intelligence/address/{address}/all"

headers = {
    "API-key": API_KEY
}

response = requests.get(
    url,
    headers=headers,
    timeout=30
)

print("HTTP Status:", response.status_code)
print("Response:")
print(response.json())