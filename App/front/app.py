# app.py

import streamlit as st
from chat_manager import render_messages, send_question, ask_summary
from file_manager import save_chat_summary, load_fake_chat_history

st.sidebar.subheader("Storico delle Chat")

st.html("<h1 style='font-size: 70px; font-weight: 600; background-image: linear-gradient(to left, #1a84b8, #1aa4b8); color: transparent; background-clip: text; -webkit-background-clip: text;'>Ciao, sono MarIA.</h1>")
st.html("<h1 style='font-size: 60px; font-weight: 400; background-image: linear-gradient(to left, #f5f5f5, #d3d3d3); color: transparent; background-clip: text; -webkit-background-clip: text;'>Come posso aiutarti oggi?</h1>")

fake_chat_history = load_fake_chat_history()

# Mostra lo storico delle chat fittizie, raggruppate per data
for day in fake_chat_history:
    st.sidebar.markdown(f"### {day['date']}")
    for chat in day['chats']:
        st.sidebar.markdown(f"- {chat}")
    st.sidebar.markdown("---")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Invia la domanda al chatbot
question = st.chat_input("Fai una domanda al chatbot:")
if question:
    send_question(question)
    render_messages(st.session_state['chat_history'])

# Termina la chat e salva il riassunto
if st.sidebar.button("Termina Chat Corrente"):
    ask_summary()
    save_chat_summary(st.session_state.get('chat_summary', {}))

    if 'client_socket' in st.session_state and st.session_state['client_socket']:
        st.session_state['client_socket'].close()
        del st.session_state['client_socket']
    
    st.session_state['chat_history'] = []
    st.session_state['chat_summary'] = None


#TODO:
# 1. Aggiungere la divisone tra nuovi e vecchi dipendenti
# 2. Aggiungere la possibilità di cliccare su vecchie chat nella sidebar per caricarle nella chat principale
    # 2.1. Salvare lo storico delle chat in locale per poterle ricaricare (salvare come oggetto JSON)
    # 2.2 Caricare lo storico delle chat salvate in locale

# BUG:
# 1. il bot sembra rispondere, a volte, a domande a cui ha già risposto come se le ricevesse nuovamente (successo 1 volta)
# 2. se la risposta  trppo lunga verrà usato più di un mesaggio per rispondere (successo durante due sessioni di test)