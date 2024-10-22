# app.py
import streamlit as st
from server_connection import create_connection, send_question_to_server

# Simulazione di chat storiche fittizie con data
fake_chat_history = [
    {
        "date": "2024-10-15",
        "chats": [
            "Chi si occupa di sicurezza informatica in Var Group?",
            "A chi devo rivolgermi per una nuova campagna pubblicitaria?"
        ]
    },
    {
        "date": "2024-10-16",
        "chats": [
            "Quali sono i requisiti per accedere al programma di stage per mio figlio?",
            "Qual è il processo per richiedere assistenza tecnica?"
        ]
    },
    {
        "date": "2024-10-17",
        "chats": [
            "Vorrei sapere di più sui servizi di cloud offerti.",
            "Mi può dare una panoramica delle soluzioni di cybersecurity?"
        ]
    },
]

# Mantieni la connessione aperta
if 'client_socket' not in st.session_state:
    st.session_state['client_socket'] = create_connection('other')  # Crea una connessione di tipo 'other'

# Inizializza lo storico della chat corrente
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []  # Lista per memorizzare i messaggi

# Titolo dell'app
st.sidebar.title("MarIA")

# Sidebar per mostrare lo storico delle chat
st.sidebar.subheader("Storico delle Chat")

# Mostra lo storico delle chat fittizie, raggruppate per data
for day in fake_chat_history:
    st.sidebar.markdown(f"### {day['date']}")
    for chat in day['chats']:
        st.sidebar.markdown(f"- {chat}")
    st.sidebar.markdown("---")  # Linea di separazione tra i giorni



# Funzione per rendere i messaggi in stile chat WhatsApp
def render_message(speaker, message):
    if speaker == "Utente":
        st.markdown(
            f"""
            <div style='text-align: right;'>
                <div style='display: inline-block; background-color: #DCF8C6; padding: 10px; border-radius: 10px; margin-bottom: 10px;'>
                    {message}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style='text-align: left;'>
                <div style='display: inline-block; padding: 10px; margin-bottom: 10px;'>
                    {message}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# Funzione per renderizzare tutti i messaggi
def render_messages(chat_history=None):
    if chat_history is None:
        chat_history = st.session_state['chat_history']
    
    for speaker, message in chat_history:
        render_message(speaker, message)

# Funzione per inviare domanda
def send_question(question):
    # Se esiste una connessione e c'è una domanda
    if st.session_state['client_socket'] and question:
        # Invia la domanda al server e ricevi la risposta
        response = send_question_to_server(st.session_state['client_socket'], question)

        # Accoda la domanda e la risposta allo storico
        st.session_state['chat_history'].append(("Utente", question))
        st.session_state['chat_history'].append(("Chatbot", response))



# Invia la domanda anche se si preme "Invio"
question = st.chat_input("Fai una domanda al chatbot:")
if question:
    send_question(question)
    
    # Mostra tutti i messaggi
    render_messages(st.session_state['chat_history'])


#TODO:
# 1. Aggiungere la divisone tra nuovi e vecchi dipendenti
# 2. Aggiungere la possibilità di cliccare su vecchie chat nella sidebar per caricarle nella chat principale
    # 2.1. Salvare lo storico delle chat in locale per poterle ricaricare