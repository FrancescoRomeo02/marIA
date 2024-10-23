import json
import os


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
            existing_summary = json.load(file)
    else:
        existing_summary = {}

    print("Existing Summary:")
    print(existing_summary)
    for summary in existing_summary:
        print(summary, type(summary))
    print('-'*50)

if __name__ == '__main__':
    save_chat_history()
    