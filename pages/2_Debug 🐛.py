import streamlit as st
import model
from instructions import Debug

st.set_page_config(page_title="Debug 🐛", page_icon="🐛", layout="wide")
st.header("Debug 🐛")

# Initialize session state for message_debug if not already present
if "message_debug" not in st.session_state:
    st.session_state.message_debug = []

# Display chat message_debug from history on app rerun
for message in st.session_state.message_debug:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.message_debug.append({"role": "user", "content": prompt})
   
    instructions = Debug
   
    # Get response from the model
    response = model.model(prompt, st.session_state.message_debug, instructions)
    
    # Ensure the response is properly handled as text
    
    
    with st.chat_message("assistant"):
        st.markdown(response)
        
    # Add assistant response to chat history
    st.session_state.message_debug.append({"role": "assistant", "content": response})
