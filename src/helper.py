import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS

# print("perfect!!")

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY


def voice_input():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("listening...")
        audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("you said: ", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, Could not understand the audio")
    except sr.RequestError as e:
        print("could not request result from google speech recognition service: {0}".format(e))
    

def text_to_speech(text, lang="en"):
    """Enhanced text-to-speech with language support"""
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save("speech.mp3")
        print(f"Speech generated in {lang}")
    except Exception as e:
        print(f"Error generating speech: {e}")
        # Fallback to English if language not supported
        tts = gTTS(text=text, lang="en", slow=False)
        tts.save("speech.mp3")

def llm_model_object(user_text):
    """Enhanced LLM function with better error handling and model fallback"""
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        
        # Try different model names in order of preference (using actual available models)
        model_names = [
            'models/gemini-2.5-flash',
            'models/gemini-2.0-flash',
            'models/gemini-flash-latest',
            'models/gemini-pro-latest',
            'models/gemini-2.5-pro'
        ]
        
        for model_name in model_names:
            try:
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(user_text)
                
                if response and response.text:
                    print(f"Successfully used model: {model_name}")
                    return response.text
                    
            except Exception as model_error:
                print(f"Model {model_name} failed: {model_error}")
                continue
        
        # If all models fail, return a fallback response
        return "I apologize, but I'm having trouble connecting to the AI service right now. Please check your API key and try again."
        
    except Exception as e:
        print(f"General error in LLM function: {e}")
        return f"Error: Unable to process your request. Please check your Google API key configuration. Error details: {str(e)}"
    
def list_available_models():
    """List all available Gemini models for debugging"""
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        models = genai.list_models()
        
        print("Available Gemini models:")
        for model in models:
            if 'generateContent' in model.supported_generation_methods:
                print(f"- {model.name}")
        
        return [model.name for model in models if 'generateContent' in model.supported_generation_methods]
    
    except Exception as e:
        print(f"Error listing models: {e}")
        return []

def test_api_connection():
    """Test if the API key and connection work"""
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        
        # Try a simple test with available model names
        model_names = [
            'models/gemini-2.5-flash',
            'models/gemini-2.0-flash', 
            'models/gemini-flash-latest'
        ]
        
        for model_name in model_names:
            try:
                model = genai.GenerativeModel(model_name)
                response = model.generate_content("Say 'Hello, API is working!'")
                if response and response.text:
                    print(f"✅ Successfully connected using model: {model_name}")
                    return True
            except Exception as e:
                print(f"Model {model_name} failed: {e}")
                continue
        
        if response and response.text:
            print("✅ API connection successful!")
            return True
        else:
            print("❌ API connection failed - no response")
            return False
            
    except Exception as e:
        print(f"❌ API connection failed: {e}")
        return False