import requests
from typing import Dict, Any
from config import Config
from logger import logger


class OpenAIService:
    """Service for interacting with OpenAI API"""
    
    def __init__(self):
        self.api_key = Config.OPENAI_API_KEY
        self.api_url = Config.OPENAI_API_URL
        self.model = Config.OPENAI_MODEL
        self.system_prompt = Config.AI_SYSTEM_PROMPT
        self.timeout = Config.REQUEST_TIMEOUT
    
    def ask_ai(self, prompt: str, system_prompt: str = None) -> Dict[str, Any]:
        """
        Send a prompt to OpenAI API and get response
        
        Args:
            prompt: User prompt/question
            system_prompt: Custom system prompt (optional)
            
        Returns:
            API response as dictionary
            
        Raises:
            requests.RequestException: If API request fails
        """
        if system_prompt is None:
            system_prompt = self.system_prompt
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        }
        
        try:
            logger.info(f"Sending request to OpenAI API with model: {self.model}")
            response = requests.post(
                self.api_url,
                headers=headers,
                json=data,
                timeout=self.timeout
            )
            response.raise_for_status()
            
            result = response.json()
            logger.info("Successfully received response from OpenAI API")
            return result
            
        except requests.exceptions.Timeout:
            error_msg = f"OpenAI API request timed out after {self.timeout}s"
            logger.error(error_msg)
            raise requests.RequestException(error_msg)
            
        except requests.exceptions.RequestException as e:
            logger.error(f"OpenAI API request failed: {str(e)}")
            raise
    
    def analyze_system(self) -> Dict[str, Any]:
        """
        Analyze system health and performance
        
        Returns:
            Analysis result from OpenAI
        """
        prompt = "分析服务器CPU、内存、网络并给出优化建议"
        return self.ask_ai(prompt)
