from collections import Counter
import matplotlib.pyplot as plt
import streamlit as st

def analyze_conversation_patterns(conversation_history):
    """Analyze conversation patterns and return insights"""
    if not conversation_history:
        return {}
    
    # Count personality modes used
    modes = [conv['mode'] for conv in conversation_history]
    mode_counts = Counter(modes)
    
    # Count conversation times (hour of day)
    hours = [int(conv['time'].split(':')[0]) for conv in conversation_history]
    hour_counts = Counter(hours)
    
    # Average response length
    response_lengths = [len(conv['assistant'].split()) for conv in conversation_history]
    avg_response_length = sum(response_lengths) / len(response_lengths) if response_lengths else 0
    
    return {
        'total_conversations': len(conversation_history),
        'favorite_mode': mode_counts.most_common(1)[0][0] if mode_counts else 'None',
        'mode_distribution': dict(mode_counts),
        'peak_hour': hour_counts.most_common(1)[0][0] if hour_counts else 'None',
        'avg_response_length': round(avg_response_length, 1)
    }

def display_analytics(conversation_history):
    """Display analytics in Streamlit"""
    analytics = analyze_conversation_patterns(conversation_history)
    
    if analytics['total_conversations'] > 0:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Chats", analytics['total_conversations'])
        
        with col2:
            st.metric("Favorite Mode", analytics['favorite_mode'])
        
        with col3:
            st.metric("Avg Words/Response", analytics['avg_response_length'])
        
        # Mode distribution chart
        if analytics['mode_distribution']:
            st.subheader("📊 Usage Patterns")
            mode_data = analytics['mode_distribution']
            st.bar_chart(mode_data)