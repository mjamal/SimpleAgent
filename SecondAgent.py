import requests
import json

# LMStudio API endpoint (default local address)
url = "http://localhost:1234/v1/chat/completions"

# Define the request payload
payload = {
    "model": "qwen3-coder-30b",  # Replace with your model name if different
    "messages": [
        {"role": "user", "content": "Hello, how are you?"}
    ],
    "temperature": 0.7,
    "max_tokens": 150
}

# Set headers
headers = {
    "Content-Type": "application/json"
}

try:
    # Make the API request
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse and print the response
        result = response.json()
        print("Response:", result['choices'][0]['message']['content'])
    else:
        print(f"Error: {response.status_code} - {response.text}")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
