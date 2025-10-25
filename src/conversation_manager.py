import json
import os
from datetime import datetime

class ConversationManager:
    def __init__(self, save_dir="conversations"):
        self.save_dir = save_dir
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
    
    def save_conversation(self, conversation_history):
        """Save conversation history to JSON file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"conversation_{timestamp}.json"
        filepath = os.path.join(self.save_dir, filename)
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(conversation_history, f, indent=2, ensure_ascii=False)
            return filepath
        except Exception as e:
            print(f"Error saving conversation: {e}")
            return None
    
    def load_conversations(self):
        """Load all saved conversations"""
        conversations = []
        if not os.path.exists(self.save_dir):
            return conversations
            
        for filename in os.listdir(self.save_dir):
            if filename.endswith('.json'):
                filepath = os.path.join(self.save_dir, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        conversation = json.load(f)
                        conversations.append({
                            'filename': filename,
                            'data': conversation
                        })
                except Exception as e:
                    print(f"Error loading {filename}: {e}")
        
        return conversations