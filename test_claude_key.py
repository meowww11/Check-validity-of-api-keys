import os
import requests

def test_claude_key():
    api_key = os.getenv("CLAUDE_API_KEY")
    if not api_key or api_key.strip() == "":
        raise ValueError("❌ CLAUDE_API_KEY not set or empty.")

    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "claude-3-opus-20240229",  # You can use claude-3-sonnet if opus is not available
        "max_tokens": 50,
        "messages": [{"role": "user", "content": "Hello!"}]
    }

    print("🟡 Sending test request to Claude...")
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        print("✅ Valid API key. Claude response:")
        print(response.json())
    except requests.exceptions.HTTPError as e:
        print(f"❌ API call failed with status {response.status_code}")
        print(response.text)
        raise
    except Exception as e:
        print("❌ Unexpected error:", e)
        raise

if __name__ == "__main__":
    test_claude_key()
