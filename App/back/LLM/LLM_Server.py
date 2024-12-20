import socket
import threading
from langchain.chains import LLMChain # type: ignore
from langchain_core.prompts import ( # type: ignore
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage # type: ignore
from langchain.chains.conversation.memory import ConversationBufferWindowMemory # type: ignore
from langchain_groq import ChatGroq # type: ignore
import Constants


def handle_client(client_socket, groq_chat, memory, scope):
    """
    Handle client connection and exchange messages.
    """
    try:
        while True:
            # Ricevi la domanda dal client
            question = client_socket.recv(1024).decode('utf-8')
            if not question:
                break

            if scope == 'new_employee':
                file = open(Constants.FILE_PATH+'App/back/LLM/knowledge/knowBase1.txt', 'r')
            else:
                file = open(Constants.FILE_PATH+'App/back/LLM/knowledge/knowBase2.txt', 'r')

            context = file.read()

            # Costruisci il prompt per il chatbot
            prompt = ChatPromptTemplate.from_messages(
                [
                    SystemMessage(content=context),
                    MessagesPlaceholder(variable_name="chat_history"),
                    HumanMessagePromptTemplate.from_template("{human_input}")
                ]
            )

            # Crea la conversazione con LLM
            conversation = LLMChain(
                llm=groq_chat,
                prompt=prompt,
                verbose=False,
                memory=memory,  # Usa la memoria condivisa per mantenere lo storico della conversazione
            )

            # Ottieni la risposta dal chatbot
            response = conversation.predict(human_input=question)

            # Invia la risposta al client
            client_socket.send(response.encode('utf-8'))

    except Exception as e:
        print(f"Errore: {e}")
    
    finally:
        client_socket.close()  # Chiude solo quando il client termina la connessione
        print("Connessione chiusa")

def main():
    # Configura il server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 8080))  # Ascolta su tutte le interfacce alla porta 8080
    server.listen(5)
    print("Server in ascolto sulla porta 8080...")

    # Inizializza il modello Groq
    groq_api_key = Constants.GROQ_API_KEY
    model = 'llama3-8b-8192'
    groq_chat = ChatGroq(groq_api_key=groq_api_key, model_name=model)


    while True:
        # Accetta una nuova connessione
        client_socket, addr = server.accept()
        print(f"Connessione accettata da {addr}")

        # Ottieni lo scope del client
        scope = client_socket.recv(1024).decode('utf-8')

        # Inizializza la memoria della conversazione per ogni nuova connessione
        memory = ConversationBufferWindowMemory(k=20, memory_key="chat_history", return_messages=True)

        # Gestisci il client in un thread separato e passa la memoria al client
        client_handler = threading.Thread(target=handle_client, args=(client_socket, groq_chat, memory, scope))
        client_handler.start()

if __name__ == "__main__":
    main()