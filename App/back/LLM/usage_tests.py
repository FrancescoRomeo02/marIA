from groq import Groq

client = Groq()

localMessages = [
        {
            "role": "user",
            "content": "Dimmi una parola"
        },

        {
            "role": "system",
            "content": "melanzana",
        },
        {
            "role": "user",
            "content": "ripetimi l'ulima parola che hai detto",
        }

    ]

completion = client.chat.completions.create(


    model="llama3-8b-8192",
    
    messages = localMessages,
    
    temperature=1,
    max_tokens=1024,
    top_p=1,
    
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")


# Per mantenre un contesto nei messaggi sia le risposte che le domande devono essere salvate nella lista messages.
# Il campo role può essere "user" o "system" e indica chi ha scritto il messaggio.
# Il campo content è il testo del messaggio.
    
# PROBLEMA: come posso mantenere il contesto se il modello viene creato ogni volta che viene chiamato il metodo? 
# SOLUZIONE: creare un modello che mantiene il contesto utilizzando una variabile locale per tenre traccia di messages.
