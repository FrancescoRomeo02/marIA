# file_manager.py

import json
import os
import random

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



def load_fake_chat_history(items: int):
    # Ampia lista di chat simulate disponibili
    all_fake_chat_history = [
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
                "Qual è il processo per richiedere assistenza tecnica?",
                "Come posso aggiornare i miei dati di contatto nel sistema?"
            ]
        },
        {
            "date": "2024-10-17",
            "chats": [
                "Vorrei sapere di più sui servizi di cloud offerti.",
                "Mi può dare una panoramica delle soluzioni di cybersecurity?",
                "Qual è il vantaggio competitivo del vostro sistema di backup?"
            ]
        },
        {
            "date": "2024-10-18",
            "chats": [
                "Quali sono le opzioni per migliorare la mia infrastruttura IT?",
                "Esistono soluzioni per l’automazione del servizio clienti?",
                "Come posso integrare i vostri servizi di rete con la mia attuale configurazione?"
            ]
        },
        {
            "date": "2024-10-19",
            "chats": [
                "Come posso pianificare una consulenza con il team tecnico?",
                "Posso ricevere un elenco di referenze dei clienti di Var Group?",
                "C’è un’opzione per ricevere aggiornamenti settimanali sui trend tecnologici?"
            ]
        },
        {
            "date": "2024-10-20",
            "chats": [
                "Quali sono le policy di protezione dati?",
                "Il team supporta anche progetti di trasformazione digitale?",
                "Esistono piani per il supporto post-implementazione?"
            ]
        },
        {
            "date": "2024-10-21",
            "chats": [
                "Come posso monitorare le performance dei server in tempo reale?",
                "Quali tool consigliate per la gestione dei rischi informatici?",
                "Potete spiegarmi la differenza tra i vostri piani di cloud storage?"
            ]
        },
        {
            "date": "2024-10-22",
            "chats": [
                "Come viene garantita la continuità operativa dei vostri servizi?",
                "Quali sono le opzioni di backup automatico?",
                "È possibile ricevere assistenza on-site in caso di emergenza?"
            ]
        },
        {
            "date": "2024-10-23",
            "chats": [
                "C’è un numero di emergenza per il supporto tecnico?",
                "Il team può aiutarmi a creare report personalizzati?",
                "Quali certificazioni di sicurezza possiede Var Group?"
            ]
        },
        {
            "date": "2024-10-24",
            "chats": [
                "Qual è il processo per la migrazione al cloud?",
                "Offrite servizi di audit per la conformità GDPR?",
                "Come viene garantita la scalabilità delle vostre soluzioni?"
            ]
        },
        {
            "date": "2024-10-25",
            "chats": [
                "È possibile programmare una formazione sul software?",
                "Quali misure sono adottate per proteggere i dati sensibili?",
                "Posso avere una demo dei vostri prodotti di cybersecurity?"
            ]
        },
        {
            "date": "2024-10-26",
            "chats": [
                "Chi posso contattare per una collaborazione in ambito R&D?",
                "Offrite soluzioni per il monitoraggio dei social media?",
                "Come posso ricevere report mensili di attività?"
            ]
        },
        {
            "date": "2024-10-27",
            "chats": [
                "Quali sono le modalità di pagamento disponibili?",
                "Posso avere un resoconto dei costi dei vostri servizi?",
                "Quali soluzioni proponete per le aziende del settore bancario?"
            ]
        },
        {
            "date": "2024-10-28",
            "chats": [
                "Il team può supportare il mio reparto IT nella transizione al cloud?",
                "Avete risorse per la formazione del personale su nuove tecnologie?",
                "Posso ricevere un supporto dedicato per la gestione del mio account?"
            ]
        },
        {
            "date": "2024-10-29",
            "chats": [
                "Come viene monitorata la latenza della rete?",
                "Quali soluzioni proponete per l’e-commerce?",
                "Posso configurare un sistema di notifica per eventi critici?"
            ]
        },
        {
            "date": "2024-10-30",
            "chats": [
                "Come posso richiedere una nuova configurazione del server?",
                "Esistono servizi di consulenza sulla sicurezza digitale?",
                "Offrite supporto per l'implementazione di VPN aziendali?"
            ]
        }
    ]

    # Seleziona casualmente un numero di giorni tra 3 e 4
    selected_history = random.sample(all_fake_chat_history, random.randint(1, items))
    
    return selected_history
