#!/usr/bin/env python3
"""
Test script to verify multilingual AI responses
"""

from src.helper import llm_model_object
from dotenv import load_dotenv

def test_multilingual_responses():
    load_dotenv()
    
    # Test prompts for different languages
    test_cases = [
        {
            "language": "English",
            "prompt": "Please respond in English. Tell me about the weather.",
            "expected_lang": "English"
        },
        {
            "language": "Hindi", 
            "prompt": "Please respond in Hindi (हिंदी में जवाब दें). मौसम के बारे में बताएं।",
            "expected_lang": "Hindi"
        },
        {
            "language": "Marathi",
            "prompt": "Please respond in Marathi (मराठीत उत्तर द्या). हवामान बद्दल सांगा।", 
            "expected_lang": "Marathi"
        },
        {
            "language": "Gujarati",
            "prompt": "Please respond in Gujarati (ગુજરાતીમાં જવાબ આપો). હવામાન વિશે કહો।",
            "expected_lang": "Gujarati"
        }
    ]
    
    print("🌍 Testing Multilingual AI Responses")
    print("=" * 50)
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n{i}. Testing {test['language']} Response:")
        print(f"Prompt: {test['prompt']}")
        print("-" * 30)
        
        try:
            response = llm_model_object(test['prompt'])
            print(f"Response: {response}")
            print(f"✅ {test['language']} test completed")
        except Exception as e:
            print(f"❌ Error in {test['language']} test: {e}")

if __name__ == "__main__":
    test_multilingual_responses()