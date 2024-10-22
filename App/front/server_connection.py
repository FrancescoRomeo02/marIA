# server_connection.py
import socket

def create_connection(type_conn):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("127.0.0.1", 8080))  # Connetti al server sulla porta 8080
        client_socket.send(type_conn.encode('utf-8'))  # Invia lo scope della connessione
        return client_socket
    except Exception as e:
        return None

def send_question_to_server(client_socket, question):
    try:
        client_socket.send(question.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        return response
    except Exception as e:
        return f"Errore nella comunicazione: {str(e)}"