"""
SimpleAgent implementation using OpenAI's GPT model for responses.

This module provides an agent that uses OpenAI's API to process messages
and maintain conversation context.
"""
import os
from typing import Optional, List, Dict
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration for local LMStudio environment
LMSTUDIO_BASE_URL = "http://localhost:1234/v1"
# No API key needed for local LMStudio, but we'll set a dummy one as OpenAI client requires it
os.environ["OPENAI_API_KEY"] = "dummy-key"


class SimpleAgent:
    """An agent implementation that uses OpenAI's GPT model for responses."""

    def __init__(self, name: str = "SimpleAgent"):
        """Initialize the agent with a name and OpenAI client.

        Args:
            name (str): The name of the agent. Defaults to "SimpleAgent".
        """
        self._name = name
        self._is_active = False
        self._client = OpenAI(
            base_url=LMSTUDIO_BASE_URL,
            api_key="dummy-key"  # Required by client but not used by LMStudio
        )
        self._context: List[Dict[str, str]] = []

    @property
    def name(self) -> str:
        """Get the agent's name.

        Returns:
            str: The name of the agent.
        """
        return self._name

    def activate(self) -> None:
        """Activate the agent and clear conversation context."""
        self._is_active = True
        self._context = []
        print(f"Agent {self.name} is now active with cleared context.")

    def deactivate(self) -> None:
        """Deactivate the agent."""
        self._is_active = False
        print(f"Agent {self.name} has been deactivated.")

    def _call_openai(self) -> str:
        """Make a call to OpenAI API with the current context.

        Returns:
            str: The response text from the API.
        """
        response = self._client.chat.completions.create(
            model="qwen3-coder-30b",
            messages=self._context,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content

    def process_message(self, message: str) -> Optional[str]:
        """Process an incoming message using OpenAI and return a response.

        Args:
            message (str): The message to process.

        Returns:
            Optional[str]: The agent's response, if any.
        """
        if not self._is_active:
            return None

        # Add user message to context
        self._context.append({
            "role": "user",
            "content": message
        })

        # Get response from OpenAI
        response = self._call_openai()

        # Add assistant response to context
        self._context.append({
            "role": "assistant",
            "content": response
        })

        return response


def main():
    """Main function to demonstrate agent functionality with OpenAI integration."""
    # Create and activate the agent
    agent = SimpleAgent("FirstAgent")
    agent.activate()
    
    # Demonstrate interaction with context maintenance
    messages = [
        "Hello! Can you help me today?",
        "What's the weather like?",
        "Thank you for your help!"
    ]
    
    for message in messages:
        print(f"\nUser: {message}")
        response = agent.process_message(message)
        print(f"Agent: {response}")
    
    # Deactivate the agent
    agent.deactivate()


if __name__ == "__main__":
    main()
