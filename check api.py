import requests
import time

# Paste your keys in this list to check their validity
# Note: These keys are not real and are just for demonstration purposes.
api_keys = [
"sk-5678e",
"sk-efgjk",
"sk-ijkl1",


   
]

url = "https://api.openai.com/v1/models"

for key in api_keys:
    headers = {
        "Authorization": f"Bearer {key}"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"✅ VALID: {key}")
        elif response.status_code == 401:
            print(f"❌ INVALID: {key}")
        else:
            print(f"⚠️ ERROR ({response.status_code}): {key}")
    except requests.exceptions.RequestException as e:
        print(f"⛔ Request failed for {key}: {e}")

    
    time.sleep(1)
