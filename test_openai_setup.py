"""Test LMStudio local environment configuration and model access."""
from openai import OpenAI
from dotenv import load_dotenv
import os

# Configuration for local LMStudio environment
LMSTUDIO_BASE_URL = "http://localhost:1234/v1"
os.environ["OPENAI_API_KEY"] = "dummy-key"  # Required but not used by LMStudio

def test_lmstudio_setup():
    """Test connection to local LMStudio server."""
    
    try:
        # Initialize client with LMStudio configuration
        client = OpenAI(
            base_url=LMSTUDIO_BASE_URL,
            api_key="dummy-key"
        )
        
        # Try a simple API call
        response = client.chat.completions.create(
            model="qwen3-coder-30b",
            messages=[{"role": "user", "content": "Hello, are you working?"}],
            max_tokens=10,
            temperature=0.7
        )
        
        print("✅ LMStudio connection successful!")
        print(f"✅ Model responded: {response.choices[0].message.content}")
        return True
        
    except Exception as e:
        print(f"❌ Error testing LMStudio connection: {str(e)}")
        return False

if __name__ == "__main__":
    test_lmstudio_setup()