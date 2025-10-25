# Configuration file for Enhanced AI Voice Assistant

# Supported languages for text-to-speech
SUPPORTED_LANGUAGES = {
    "en": "English",
    "hi": "Hindi", 
    "mr": "Marathi",
    "gu": "Gujarati",
    "es": "Spanish",
    "fr": "French",
    "de": "German"
}

# AI Personality modes
PERSONALITY_MODES = {
    "Professional": {
        "prompt": "Please respond in a professional and formal manner: ",
        "description": "Formal, business-like responses"
    },
    "Casual & Friendly": {
        "prompt": "Please respond in a casual, friendly, and conversational way: ",
        "description": "Relaxed, friendly conversation"
    },
    "Educational": {
        "prompt": "Please explain this in simple terms as if teaching a beginner: ",
        "description": "Simple explanations for learning"
    },
    "Creative": {
        "prompt": "Please respond creatively and imaginatively: ",
        "description": "Creative and artistic responses"
    }
}

# App settings
MAX_HISTORY_DISPLAY = 5
DEFAULT_LANGUAGE = "en"
DEFAULT_PERSONALITY = "Casual & Friendly"