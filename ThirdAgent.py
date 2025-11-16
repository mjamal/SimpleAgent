import requests
import json

def chat_with_context(messages_history):
    """
    Send a message with full conversation history to maintain context
    
    Args:
        messages_history: List of message dictionaries in format 
                         [{"role": "user/assistant", "content": "message"}]
    """
    url = "http://localhost:1234/v1/chat/completions"
    
    payload = {
        "model": "qwen3-coder-30b",
        "messages": messages_history,
        "temperature": 0.7,
        "max_tokens": 150
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        else:
            return f"Error: {response.status_code} - {response.text}"
            
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

# Example usage with manual context management
conversation_history = [
    {"role": "user", "content": "Hello, what's your name?"},
    {"role": "assistant", "content": "I'm Qwen, a language model developed by Tongyi Lab."},
    {"role": "user", "content": "Can you help me with Python programming?"}
]

response = chat_with_context(conversation_history)
print(response)
