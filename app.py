from flask import Flask, request, jsonify
import traceback

from config import Config
from logger import logger
from openai_service import OpenAIService
from validators import RequestValidator


def create_app():
    """Create and configure Flask application"""
    app = Flask(__name__)
    
    # Validate configuration on startup
    try:
        Config.validate()
    except ValueError as e:
        logger.error(f"Configuration error: {str(e)}")
        raise
    
    # Initialize services
    ai_service = OpenAIService()
    
    # Error handler for JSON decode errors
    @app.errorhandler(400)
    def bad_request(error):
        logger.warning(f"Bad request: {str(error)}")
        return jsonify({
            "error": "Bad Request",
            "message": "Invalid JSON or malformed request"
        }), 400
    
    # Error handler for internal server errors
    @app.errorhandler(500)
    def internal_error(error):
        logger.error(f"Internal server error: {str(error)}")
        return jsonify({
            "error": "Internal Server Error",
            "message": "An unexpected error occurred"
        }), 500
    
    # Health check endpoint
    @app.route("/", methods=["GET"])
    def home():
        """Health check endpoint"""
        logger.info("Health check requested")
        return jsonify({
            "status": "success",
            "message": "🚀 鸿森智汇 AI 运维系统已运行",
            "version": "1.0.0"
        }), 200
    
    # AI chat endpoint
    @app.route("/ai", methods=["POST"])
    def ai_chat():
        """
        AI chat endpoint
        
        Request body:
        {
            "prompt": "Your question or command"
        }
        """
        try:
            if not request.is_json:
                return jsonify({
                    "error": "Content-Type must be application/json"
                }), 400
            
            # Validate request
            try:
                prompt = RequestValidator.validate_prompt(request.json)
            except ValueError as e:
                logger.warning(f"Validation error: {str(e)}")
                return jsonify({
                    "error": "Validation Error",
                    "message": str(e)
                }), 422
            
            # Sanitize prompt
            prompt = RequestValidator.sanitize_prompt(prompt)
            
            logger.info(f"Processing AI request with prompt length: {len(prompt)}")
            
            # Get AI response
            result = ai_service.ask_ai(prompt)
            
            return jsonify(result), 200
            
        except Exception as e:
            logger.error(f"Error in /ai endpoint: {str(e)}\n{traceback.format_exc()}")
            return jsonify({
                "error": "AI Request Failed",
                "message": "Failed to process request"
            }), 500
    
    # Auto-analysis endpoint
    @app.route("/auto", methods=["GET"])
    def auto_analyze():
        """
        Automatic system analysis endpoint
        Analyzes server CPU, memory, network and provides optimization suggestions
        """
        try:
            logger.info("Starting automatic system analysis")
            result = ai_service.analyze_system()
            return jsonify(result), 200
            
        except Exception as e:
            logger.error(f"Error in /auto endpoint: {str(e)}\n{traceback.format_exc()}")
            return jsonify({
                "error": "Analysis Failed",
                "message": "Failed to analyze system"
            }), 500
    
    return app


if __name__ == "__main__":
    app = create_app()
    
    logger.info(f"Starting application on {Config.HOST}:{Config.PORT}")
    logger.info(f"Environment: {Config.FLASK_ENV}")
    
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.FLASK_DEBUG
    )
