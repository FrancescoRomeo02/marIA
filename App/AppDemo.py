import streamlit as st
from langchain.chains import LLMChain  # type: ignore
from langchain_core.prompts import (  # type: ignore
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage  # type: ignore
from langchain.chains.conversation.memory import ConversationBufferWindowMemory  # type: ignore
from langchain_groq import ChatGroq  # type: ignore
from back.LLM import Constants
from front.file_manager import load_fake_chat_history

# Inizializzazione del file di conoscenza
file = open(Constants.FILE_PATH + 'App/back/LLM/knowledge/knowBase2.txt', 'r')

# Definizione della funzione per mostrare i messaggi
def render_message(speaker: str, message: str):
    st.markdown(
        """
        <style>
        [data-testid="stChatMessageContent"] p {
            font-size: 1.2rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    name = 'user' if speaker == 'Utente' else 'ai'
    with st.chat_message(name):
        st.markdown(message)

# Funzione per mostrare lo storico dei messaggi
def render_messages(chat_history):
    for speaker, message in chat_history:
        render_message(speaker, message)

# Configurazione dell'API e del modello
groq_api_key = Constants.GROQ_API_KEY
model = 'llama3-8b-8192'
groq_chat = ChatGroq(groq_api_key=groq_api_key, model_name=model)

# Prompt per il chatbot
context = file.read()
prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content=context),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{human_input}")
    ]
)

# Memoria della conversazione
memory = ConversationBufferWindowMemory(k=20, memory_key="chat_history", return_messages=True)

# Creazione della conversazione con LLM
conversation = LLMChain(
    llm=groq_chat,
    prompt=prompt,
    verbose=False,
    memory=memory  # Usa la memoria condivisa per mantenere lo storico della conversazione
)

# Funzione per inviare una domanda e ottenere la risposta
def send_question(question: str):
    if question:
        response = conversation.predict(human_input=question)
        st.session_state['chat_history'].append(("Utente", question))
        st.session_state['chat_history'].append(("Chatbot", response))

# Sidebar per mostrare lo storico delle chat
st.sidebar.subheader("Storico delle Chat")

# Titoli e sottotitoli nell'app
st.html("<h1 style='font-size: 70px; font-weight: 600; background-image: linear-gradient(to left, #1a84b8, #1aa4b8); color: transparent; background-clip: text; -webkit-background-clip: text;'>Ciao, sono MarIA.</h1>")
st.html("<h1 style='font-size: 60px; font-weight: 400; background-image: linear-gradient(to left, #f5f5f5, #d3d3d3); color: transparent; background-clip: text; -webkit-background-clip: text;'>Come posso aiutarti oggi?</h1>")

# Caricamento di chat fittizie per la sidebar
fake_chat_history = load_fake_chat_history()

# Mostra lo storico delle chat fittizie nella sidebar
for day in fake_chat_history:
    st.sidebar.markdown(f"### {day['date']}")
    for chat in day['chats']:
        st.sidebar.markdown(f"- {chat}")
    st.sidebar.markdown("---")

# Inizializzazione dello storico della chat
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input della domanda e invio
question = st.chat_input("Fai una domanda al chatbot:")
if question:
    send_question(question)
    render_messages(st.session_state['chat_history'])

# Pulsante per terminare la chat e resettare lo storico
if st.sidebar.button("Termina Chat Corrente"):
    st.session_state['chat_history'] = []
    st.session_state['chat_summary'] = None