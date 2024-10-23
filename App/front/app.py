# app.py
import streamlit as st
import json
import os
from datetime import datetime
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
    # Lista di dizionari (date, messages(sender, message))
    st.session_state['chat_history'] = []

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
    # Se non c'è una connessione, crea una nuova connessione
    if not st.session_state['client_socket']:
        st.session_state['client_socket'] = create_connection('other')

    # Se esiste una connessione e c'è una domanda
    if st.session_state['client_socket'] and question:
        # Invia la domanda al server e ricevi la risposta
        response = send_question_to_server(st.session_state['client_socket'], question)

        # Accoda la domanda e la risposta allo storico
        st.session_state['chat_history'].append(("Utente", question))
        st.session_state['chat_history'].append(("Chatbot", response))

# Funzione per salvare lo storico della chat come oggetto JSON
def save_chat_history(chat_history=None, chat_summary=None):
    # # Verifica se esistono già i file JSON
    # chat_history_path = "chat_history.json"
    chat_summary_path = "chat_summary.json"
    
    # # Carica i dati esistenti, se presenti
    # if os.path.exists(chat_history_path):
    #     with open(chat_history_path, "r") as file:
    #         existing_history = json.load(file)
    # else:
    #     existing_history = {}

    if os.path.exists(chat_summary_path):
        with open(chat_summary_path, "r") as file:
            existing_summary = json.load(file) # Lista di dizionari
    else:
        existing_summary = {}

    # Aggiungo i nuovi summary alla lista
    existing_summary.append(chat_summary)

    # # Salva lo storico della chat in un file JSON
    # with open(chat_history_path, "w") as file:
    #     json.dump(chat_history, file, indent=4)

    # Salva i summary della chat
    with open(chat_summary_path, "w") as file:
        json.dump(existing_summary, file, indent=4)

# Funzione per chiedere un riassunto della chat
def ask_summary():
    # Controlla se esiste una connessione, altrimenti crea una nuova connessione
    if not st.session_state['client_socket']:
        st.session_state['client_socket'] = create_connection('other')
    
    # Se c'è una connessione, richiedi il riassunto
    if st.session_state['client_socket']:
        # Invia la domanda al server e ricevi la risposta
        response = send_question_to_server(st.session_state['client_socket'], "Riassumi la conversazione usando un titolo come se fosse il titolo di un libro. non più di 7 parole")
        date = datetime.today().strftime('%Y-%m-%d')

        # Salva il riassunto nella sessione
        if 'chat_summary' not in st.session_state:
            st.session_state['chat_summary'] = {"date": date, "summary": response}
        else:
            st.session_state['chat_summary'] = {"date": date, "summary": response}

# Invia la domanda anche se si preme "Invio"
question = st.chat_input("Fai una domanda al chatbot:")
if question:
    send_question(question)
    # Mostra tutti i messaggi
    render_messages(st.session_state['chat_history'])

# Termina la chat (posizionato alla fine dell'app)
if st.sidebar.button("Termina Chat Corrente"):
    # Chiedi un riassunto della chat
    ask_summary()

    # Salva lo storico della chat e il riassunto
    save_chat_history(st.session_state['chat_history'], st.session_state['chat_summary'])
    
    # Chiudi la connessione
    st.session_state['client_socket'].close()
    st.session_state['client_socket'] = None
    
    # Resetta lo storico della chat
    st.session_state['chat_history'] = None
    # Resetta i summary della chat
    st.session_state['chat_summary'] = None


#TODO:
# 1. Aggiungere la divisone tra nuovi e vecchi dipendenti
# 2. Aggiungere la possibilità di cliccare su vecchie chat nella sidebar per caricarle nella chat principale
    # 2.1. Salvare lo storico delle chat in locale per poterle ricaricare (salvare come oggetto JSON)
    # 2.2 Caricare lo storico delle chat salvate in locale


# BUG:
# 1. il bot sembra rispondere, a volte, a domande a cui ha già risposto come se le ricevesse nuovamente (successo 1 volta)
# 2. se la risposta  trppo lunga verrà usato più di un mesaggio per rispondere (successo durante due sessioni di test)