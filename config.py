import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Base configuration"""
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
    OPENAI_MODEL = "gpt-4o-mini"
    
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 3000))
    
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    # AI System prompt
    AI_SYSTEM_PROMPT = "你是企业级AI运维专家"
    
    # Request timeout (seconds)
    REQUEST_TIMEOUT = 30
    
    @staticmethod
    def validate():
        """Validate required configuration"""
        if not Config.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
