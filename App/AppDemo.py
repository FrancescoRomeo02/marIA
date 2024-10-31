import random
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
from front.file_manager import load_fake_chat_history

GROQ_API_KEY = st.secrets["groq_api_key"]

# Inizializzazione del file di conoscenza
file = open('App/back/LLM/knowledge/knowBase2.txt', 'r')

# Funzione per mostrare i messaggi
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

# Funzione per inviare una domanda e ottenere la risposta
def send_question(question: str):
    if question:
        response = st.session_state['conversation'].predict(human_input=question)
        st.session_state['chat_history'].append(("Utente", question))
        st.session_state['chat_history'].append(("Chatbot", response))

# Inizializzazione dello storico della chat e del modello
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
    st.session_state['model'] = None
    
    # Caricamento di chat fittizie per la sidebar
    st.session_state['fake_chat_history'] = load_fake_chat_history()
    
    # Configurazione dell'API e del modello
    model = random.choice(["gemma-7b-it", "llama-3.1-8b-instant", "llama-3.1-70b-versatile", "gemma2-9b-it"])
    st.session_state['model'] = model
    groq_chat = ChatGroq(groq_api_key=GROQ_API_KEY, model_name=model)

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
    memory = ConversationBufferWindowMemory(k=10, memory_key="chat_history", return_messages=True)

    # Creazione della conversazione con LLM
    st.session_state['conversation'] = LLMChain(
        llm=groq_chat,
        prompt=prompt,
        verbose=False,
        memory=memory  # Usa la memoria condivisa per mantenere lo storico della conversazione
    )

    global static_model
    static_model = model

# Sidebar per mostrare lo storico delle chat
st.sidebar.subheader("Storico delle Chat")
for day in st.session_state['fake_chat_history']:
    st.sidebar.markdown(f"### {day['date']}")
    for chat in day['chats']:
        st.sidebar.markdown(f"- {chat}")
    st.sidebar.markdown("---")

# Pulsante per terminare la chat e resettare lo storico
if st.sidebar.button("Termina Chat Corrente"):
    st.session_state['chat_history'] = []
    st.balloons()
    st.session_state['chat_summary'] = None

# Titoli e sottotitoli nell'app
st.markdown(
    """
    <style>
    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .animated-gradient-text {
        font-size: clamp(2rem, 10vw, 5rem);
        font-weight: 600;
        background-image: linear-gradient(270deg, #1a84b8, #1aa4b8, #1a84b8);
        color: transparent;
        background-clip: text;
        -webkit-background-clip: text;
        background-size: 300% 300%;
        animation: gradientAnimation 6s ease-in-out infinite;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    </style>

    <h1 class="animated-gradient-text">Ciao, sono MarIA.</h1>
    """,
    unsafe_allow_html=True
)
st.html("<h1 style='font-size : clamp(1rem, 5vw, 2.5rem); font-weight: 400; background-image: linear-gradient(to left, #f5f5f5, #d3d3d3); color: transparent; background-clip: text; -webkit-background-clip: text;'>Come posso aiutarti oggi?</h1>")

st.warning("Questa è una demo limitata: alcune funzionalità saranno disponibili nella versione finale.", icon="⚠️")
st.info("Modello utilizzato: " + st.session_state['model'])

# Input della domanda e invio
question = st.chat_input("Fai una domanda al chatbot:")
if question:
    send_question(question)
    render_messages(st.session_state['chat_history'])


