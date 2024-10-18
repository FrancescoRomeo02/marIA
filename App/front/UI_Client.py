import socket
import streamlit as st

# Funzione per connettersi al server e mantenere la connessione aperta
def create_connection():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 8080))  # Connetti al server sulla porta 8080
    return client_socket

# Funzione per inviare la domanda al server attraverso la connessione esistente
def send_question_to_server(client_socket, question):
    try:
        # Invia la domanda al server
        client_socket.send(question.encode('utf-8'))

        # Ricevi la risposta dal server
        response = client_socket.recv(1024).decode('utf-8')
        return response
    except Exception as e:
        return f"Errore nella comunicazione: {str(e)}"

# Mantieni la connessione aperta
if 'client_socket' not in st.session_state:
    st.session_state['client_socket'] = create_connection()

# Inizializza lo storico della chat
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []  # Lista per memorizzare i messaggi

# UI di Streamlit
st.title("MarIA")

# Mostra tutto lo storico delle chat con un po' di stile
for speaker, message in st.session_state['chat_history']:
    if speaker == "Utente":
        st.markdown(f"<div style='text-align: right; background-color: #E0F7FA; padding: 5px; border-radius: 10px; margin-bottom: 10px;'>**{speaker}**: {message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: left; background-color: #E8F5E9; padding: 5px; border-radius: 10px; margin-bottom: 10px;'>**{speaker}**: {message}</div>", unsafe_allow_html=True)

# Input della domanda
question = st.text_input("Fai una domanda al chatbot:")

# Quando il bottone viene premuto
if st.button("Invia"):
    if question:
        # Invia la domanda al server e ricevi la risposta attraverso la connessione mantenuta
        response = send_question_to_server(st.session_state['client_socket'], question)

        # Accoda la domanda e la risposta allo storico
        st.session_state['chat_history'].append(("Utente", question))
        st.session_state['chat_history'].append(("Chatbot", response))