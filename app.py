import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech
from datetime import datetime


def process_user_input(text, response_mode, language):
    """Process user input and generate response"""
    # Language mapping for AI instructions
    language_instructions = {
        "en": "Please respond in English. ",
        "hi": "Please respond in Hindi (हिंदी में जवाब दें). ",
        "mr": "Please respond in Marathi (मराठीत उत्तर द्या). ",
        "gu": "Please respond in Gujarati (ગુજરાતીમાં જવાબ આપો). ",
    
    }
    
    # Add personality to the prompt
    personality_prompts = {
        "Professional": "Please respond in a professional and formal manner. ",
        "Casual & Friendly": "Please respond in a casual, friendly, and conversational way. ",
        "Educational": "Please explain this in simple terms as if teaching a beginner. ",
        "Creative": "Please respond creatively and imaginatively. "
    }
    
    # Combine language instruction + personality + user question
    language_instruction = language_instructions.get(language, language_instructions["en"])
    personality_instruction = personality_prompts[response_mode]
    
    enhanced_prompt = language_instruction + personality_instruction + "User question: " + text
    
    with st.spinner("🤖 Thinking..."):
        response = llm_model_object(enhanced_prompt)
    
    # Only generate speech if response is valid
    if response and not response.startswith("Error:"):
        text_to_speech(response, language)
    
    # Add to conversation history
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.conversation_history.append({
        "time": timestamp,
        "user": text,
        "assistant": response,
        "mode": response_mode
    })
    
    # Display current response
    if response.startswith("Error:"):
        st.error(response)
    else:
        st.text_area(label="🤖 AI Response:", value=response, height=200)
        
        # Audio playback
        try:
            audio_file = open("speech.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes)
            
            st.download_button(
                label="📥 Download Speech",
                data=audio_bytes,
                file_name=f"ai_response_{timestamp.replace(':', '')}.mp3",
                mime="audio/mp3"
            )
        except FileNotFoundError:
            st.warning("Audio file not generated (text-only response)")


def main():
    st.title(" AI Voice Assistant 🤖")
    st.subheader("Your Personal Multilingual AI Companion")
    
    # Initialize session state for conversation history
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []
    
    # Sidebar for features+
    with st.sidebar:
        st.header("🎛️ Controls")
        
        # Response mode selection
        response_mode = st.selectbox(
            "Choose AI Personality:",
            ["Professional", "Casual & Friendly", "Educational", "Creative"]
        )
        
        # Language selection with better labels
        language_options = {
            "English": "en",
            "Hindi (हिंदी)": "hi", 
            "Marathi (मराठी)": "mr",
            "Gujarati (ગુજરાતી)": "gu",
            
        }
        
        selected_language_name = st.selectbox(
            "Response Language:",
            list(language_options.keys())
        )
        language = language_options[selected_language_name]
        
        # Clear history button
        if st.button("🗑️ Clear History"):
            st.session_state.conversation_history = []
            st.success("History cleared!")
        
        st.markdown("---")
        
        # Debug section
        with st.expander("🔧 Debug & Test"):
            if st.button("Test API Connection"):
                from src.helper import test_api_connection
                if test_api_connection():
                    st.success("✅ API Working!")
                else:
                    st.error("❌ API Failed")
            
            
    
    # Main interaction area
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Voice input button
        if st.button("🎤 Ask me anything", use_container_width=True):
            with st.spinner("🎧 Listening..."):
                text = voice_input()
                if text:
                    process_user_input(text, response_mode, language)
        
        st.markdown("**OR**")
        
        # Text input as backup
        user_text = st.text_input("💬 Type your question here:", placeholder="Ask me anything...")
        if st.button("📝 Send Text", use_container_width=True) and user_text:
            process_user_input(user_text, response_mode, language)
    
    with col2:
        st.metric("Conversations", len(st.session_state.conversation_history))
    
    # Conversation History
    if st.session_state.conversation_history:
        st.header("💬 Conversation History")
        
        for i, conv in enumerate(reversed(st.session_state.conversation_history[-5:])):  # Show last 5
            with st.expander(f"🕐 {conv['time']} - {conv['mode']} Mode"):
                st.write(f"**You:** {conv['user']}")
                st.write(f"**AI:** {conv['assistant']}")
    
    
            
if __name__=='__main__':
    main()