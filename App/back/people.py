import pandas as pd  # Importa la libreria Pandas, utile per gestire dati tabellari (simili a tabelle Excel)
import random  # Importa la libreria random, usata per selezionare elementi casuali da una lista

# Definiamo una funzione che creerà un file CSV a partire da 4 liste di dati.
# 'num_oggetti' indica il numero di righe (o "oggetti") che si desidera generare.
# 'output_file' è il nome del file CSV che verrà creato (default: 'output.csv').
def crea_csv_aziende(nomi_aziendali, referenti, telefoni, mail, num_oggetti, output_file='output.csv'):
    
    # Creiamo una lista vuota che conterrà i dati di ogni azienda.
    data = []
    
    # Ciclo for che viene eseguito 'num_oggetti' volte. Ad ogni ciclo si crea un nuovo oggetto (azienda).
    for _ in range(num_oggetti):
        # Per ogni oggetto, selezioniamo un nome aziendale casuale dalla lista 'nomi_aziendali'
        azienda = random.choice(nomi_aziendali)
        # Selezioniamo un referente (persona di contatto) casuale dalla lista 'referenti'
        referente = random.choice(referenti)
        # Selezioniamo un numero di telefono casuale dalla lista 'telefoni'
        telefono = random.choice(telefoni)
        # Selezioniamo un indirizzo email casuale dalla lista 'mail'
        email = random.choice(mail)
        
        # Aggiungiamo i dati dell'azienda appena creati (azienda, referente, telefono, email) alla lista 'data'
        data.append({
            'Nome Azienda': azienda,  # Colonna "Nome Azienda"
            'Referente': referente,   # Colonna "Referente"
            'Telefono': telefono,     # Colonna "Telefono"
            'Email': email            # Colonna "Email"
        })
    
    # Utilizziamo Pandas per creare un DataFrame, che è una struttura dati simile a una tabella, con i dati raccolti.
    df = pd.DataFrame(data)
    
    # Salviamo il DataFrame in un file CSV, con il nome specificato in 'output_file'.
    # L'argomento 'index=False' serve per non includere una colonna di indici numerici nel file CSV.
    df.to_csv(output_file, index=False)
    
    # Stampa un messaggio per informare che il file CSV è stato creato correttamente.
    print(f'File CSV creato con {num_oggetti} oggetti: {output_file}')


# Esempio di liste con i dati da usare per creare il CSV (da espandere, buon divertimento!)
nomi_aziendali = ["Azienda A", "Azienda B", "Azienda C", "Azienda D"]  # Lista di nomi aziendali
referenti = ["Mario Rossi", "Luca Bianchi", "Giulia Verdi", "Sara Neri"]  # Lista di referenti (persone di contatto)
telefoni = ["123-456-7890", "098-765-4321", "555-123-4567", "333-444-5555"]  # Lista di numeri di telefono
mail = ["mario.rossi@azienda.it", "luca.bianchi@azienda.it", "giulia.verdi@azienda.it", "sara.neri@azienda.it"]  # Lista di email

# Chiamata alla funzione per creare un file CSV con 1 oggetto (riga) e salvarlo come 'aziende.csv'
crea_csv_aziende(nomi_aziendali, referenti, telefoni, mail, num_oggetti=30, output_file='aziende.csv')