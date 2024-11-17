"""
This class controls the connection between the knowledge base the ai apis provided by OpenAI or Anthropic models.
"""

import openai
import os
import json
import requests
from dotenv import load_dotenv

class Controller:
    """
    The controller class manages the connection between the knowledge base an the ai apis.
    """
    def __init__(self):
        """
        Load the environment variables for access to the ai apis.
        """
        load_dotenv()
        self.openai_key = os.getenv("OPENAI_API_KEY")
        self.anthropic_key = os.getenv("ANTHROPIC_API_KEY")

