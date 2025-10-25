#!/usr/bin/env python3
"""
Simple script to list available Gemini models
"""

import google.generativeai as genai
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        print("❌ ERROR: GOOGLE_API_KEY not found in .env file")
        return
    
    try:
        genai.configure(api_key=api_key)
        
        print("📋 Available Gemini models:")
        print("=" * 50)
        
        models = genai.list_models()
        
        for model in models:
            if 'generateContent' in model.supported_generation_methods:
                print(f"✅ {model.name}")
                print(f"   Display Name: {model.display_name}")
                print(f"   Description: {model.description}")
                print()
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()