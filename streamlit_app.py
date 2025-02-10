import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)

#dad_joke_model = "ft:gpt-4o-mini-2024-07-18:personal::AjAj8dcn"
dad_joke_model =  "ft:gpt-4o-mini-2024-07-18:personal::AjAj8dcn"

# Initialize session state for chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are Soğuk Savaşçı. You are a dad joke expert. Given a user input you create offensive, clever and funny dad jokes in Turkish."}
    ]

def get_response(messages):
    response = client.chat.completions.create(
        model=dad_joke_model,
        messages=messages
    )
    return response.choices[0].message.content

# Streamlit UI
st.title("Soğuk Savaşçı 👨‍👦")
st.write("Selam! İstediğin konuyla ilgili sana soğuk bir espri yapabilirim.")

# Chat input
user_input = st.chat_input("Type your message here...")

# Display chat history
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Handle user input
if user_input:
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get bot response
    response = get_response(st.session_state.messages)
    
    # Display assistant response
    with st.chat_message("assistant"):
        st.write(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})