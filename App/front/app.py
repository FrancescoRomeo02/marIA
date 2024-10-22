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
    st.session_state['client_socket'] = create_connection()

# Inizializza lo storico della chat corrente
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []  # Lista per memorizzare i messaggi

# Sidebar per mostrare lo storico delle chat
st.sidebar.title("Storico delle Chat")

# Mostra lo storico delle chat fittizie, raggruppate per data
for day in fake_chat_history:
    st.sidebar.markdown(f"### {day['date']}")
    for chat in day['chats']:
        st.sidebar.markdown(f"- {chat}")
    st.sidebar.markdown("---")  # Linea di separazione tra i giorni

# UI principale
st.title("MarIA - Chatbot")

# Funzione per rendere i messaggi in stile chat WhatsApp
def render_message(speaker, message):
    if speaker == "Utente":
        st.markdown(
            f"""
            <div style='text-align: right;'>
                <div style='display: inline-block; background-color: #DCF8C6; padding: 10px; border-radius: 10px; margin-bottom: 10px;'>
                    <strong>{speaker}:</strong> {message}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style='text-align: left;'>
                <div style='display: inline-block; background-color: #E0F7FA; padding: 10px; border-radius: 10px; margin-bottom: 10px;'>
                    <strong>{speaker}:</strong> {message}
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

    # Se non ci sono messaggi, mostra un messaggio vuoto
    if not chat_history:
        st.markdown("Ancora nessun messaggio.")



# Funzione per inviare domanda e aggiornare la UI
def send_question():
    # Se esiste una connessione e c'è una domanda
    if st.session_state['client_socket'] and st.session_state['question']:
        # Invia la domanda al server e ricevi la risposta
        response = send_question_to_server(st.session_state['client_socket'], st.session_state['question'])

        # Accoda la domanda e la risposta allo storico
        st.session_state['chat_history'].append(("Utente", st.session_state['question']))
        st.session_state['chat_history'].append(("Chatbot", response))

        # Cancella la domanda
        st.session_state['question'] = ""  # Reset dell'input

# Inizializza l'input della domanda
if 'question' not in st.session_state:
    st.session_state['question'] = ""

# Mostra tutti i messaggi
render_messages(st.session_state['chat_history'])

# Invia la domanda anche se si preme "Invio"
st.text_input("Fai una domanda al chatbot:", key="question", value=st.session_state['question'], placeholder="Scrivi qui...", on_change=send_question)
