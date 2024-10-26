# file_manager.py

import json
import os

def load_existing_summary():
    summary_path = "chat_summary.json"
    if os.path.exists(summary_path):
        with open(summary_path, "r") as file:
            return json.load(file)
    return []

def save_chat_summary(chat_summary):
    summary_path = "chat_summary.json"
    existing_summary = load_existing_summary()
    existing_summary.append(chat_summary)

    with open(summary_path, "w") as file:
        json.dump(existing_summary, file, indent=4)

def load_fake_chat_history():
    # Simulazione di chat storiche fittizie con data
    return [
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