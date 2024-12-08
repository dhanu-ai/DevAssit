import streamlit as st
import model
from instructions import Code

st.set_page_config(page_title="Code 🧑‍💻", page_icon="🧑‍💻", layout="wide")
st.header("Code 🧑‍💻")

# Initialize session state for message_code if not already present
if "message_code" not in st.session_state:
    st.session_state.message_code = []

# Display chat message_code from history on app rerun
for message in st.session_state.message_code:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if user_prompt := st.chat_input("What is up?"):
    prompt = f"build a{user_prompt} for me. Feel free to write the code as long as you can. I am not looking for production level code I am here to kickstart the application idea. What i am saying now donot respond to it focus {user_prompt} and remeber these with{Code}"
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(user_prompt)
    # Add user message to chat history
    st.session_state.message_code.append({"role": "user", "content": prompt})
   
    instructions = Code
    
    # Get response from the model
    response = model.model(prompt, st.session_state.message_code, instructions)
    
    with st.chat_message("assistant"):
        st.markdown(response)
        
    # Add assistant response to chat history
    st.session_state.message_code.append({"role": "assistant", "content": response})
