#!/usr/bin/env python3
"""
Test script to check Google Gemini API connection and available models
Run this to debug API issues
"""

from src.helper import test_api_connection, list_available_models
from dotenv import load_dotenv
import os

def main():
    print("🔍 Testing Google Gemini API Connection...")
    print("=" * 50)
    
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        print("❌ ERROR: GOOGLE_API_KEY not found in .env file")
        print("Please add your API key to the .env file:")
        print("GOOGLE_API_KEY=your_api_key_here")
        return
    
    print(f"✅ API Key found: {api_key[:10]}...{api_key[-4:]}")
    print()
    
    # Test API connection
    print("🧪 Testing API connection...")
    if test_api_connection():
        print("✅ API is working correctly!")
    else:
        print("❌ API connection failed")
        print("\n🔧 Troubleshooting tips:")
        print("1. Check if your API key is correct")
        print("2. Ensure you have enabled the Gemini API in Google Cloud Console")
        print("3. Check if you have sufficient quota/credits")
        return
    
    print()
    
    # List available models
    print("📋 Listing available models...")
    models = list_available_models()
    
    if models:
        print(f"✅ Found {len(models)} available models")
    else:
        print("❌ No models found or error occurred")

if __name__ == "__main__":
    main()