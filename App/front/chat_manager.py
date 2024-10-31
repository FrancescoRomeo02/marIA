# chat_manager.py

import streamlit as st
from datetime import datetime
from server_connection import create_connection, send_question_to_server

def render_message(speaker: str, message: str):
    st.markdown(
    """
    <style>
    [data-testid="stChatMessageContent"] p{
        font-size: 1.2vw;
    }
    </style>
    """, unsafe_allow_html=True
    )

    name = 'user' if speaker == 'Utente' else 'ai'
    with st.chat_message(name):
        st.markdown(message)

def render_messages(chat_history):
    for speaker, message in chat_history:
        render_message(speaker, message)

def send_question(question: str):
    if 'client_socket' not in st.session_state:
        st.session_state['client_socket'] = create_connection('other')

    if st.session_state['client_socket'] and question:
        response = send_question_to_server(st.session_state['client_socket'], question)
        st.session_state['chat_history'].append(("Utente", question))
        st.session_state['chat_history'].append(("Chatbot", response))

def ask_summary():
    if 'client_socket' not in st.session_state:
        st.session_state['client_socket'] = create_connection('other')
    
    if st.session_state['client_socket']:
        response = send_question_to_server(st.session_state['client_socket'], 
                                           "Riassumi la conversazione usando un titolo come se fosse il titolo di un libro. non più di 7 parole")
        date = datetime.today().strftime('%Y-%m-%d')
        st.session_state['chat_summary'] = {"date": date, "summary": response}