# VARMAPP

This repository contains the development of an internal configurator to map services, intercept business opportunities, and boost cross-selling. Designed for sales and employee training, it’s interactive, predictive, and enhances decision-making before client meetings.


## Creazione di un ambiente virtuale in Python e installazione delle dipendenze

In questa guida, ti mostrerò come creare un ambiente virtuale in Python e installare le dipendenze da un file chiamato `requirements.txt`.

### 1. Creazione di un ambiente virtuale

Prima di tutto, è una buona pratica creare un ambiente virtuale per isolare il progetto e gestire le dipendenze in modo indipendente dagli altri progetti. Ecco come farlo:

1. Apri il terminale o la shell.
2. Vai alla directory del tuo progetto:
   ```bash
   cd /path/del/tuo/progetto
   ```
3. Crea un ambiente virtuale usando il seguente comando:
   ```bash
   python -m venv env
   ```
Questo creerà una cartella chiamata env all’interno della directory del progetto.
### 2. Attivazione dell’ambiente virtuale
Per attivare l’ambiente virtuale, usa i seguenti comandi in base al tuo sistema operativo:
* su macOS/Linux
```bash
source env/bin/activate
```
* su Windows
```bash
.\env\Scripts\activate
```
Dopo aver attivato l’ambiente virtuale, vedrai il prefisso (env) all’inizio della riga nel terminale.
### 3. Installazione delle dipendenze da un file requirements.txt
Esegui il seguente comando:
```bash
pip install -r requirements.txt
```
Questo installerà tutte le dipendenze specificate nel file requirements.txt nel tuo ambiente virtuale.

## Utilizzo di GroqCloud per eseguire API Llama con Python

Questo repository contiene un esempio su come utilizzare ****GroqCloud**** per eseguire il modello ****Llama**** utilizzando l'SDK di Groq con Python.

### 1. Creazione dell'account su GroqCloud

Per iniziare a usare GroqCloud, segui questi passi:

**-** Vai sul sito ufficiale di [**GroqCloud**](**https://groq.com/**) e crea un account.

**-** Una volta registrato, accedi e ottieni le tue ****API keys**** necessarie per connetterti a GroqCloud dal tuo ambiente Python.

### 2. Installazione del client Python

Per connetterti a GroqCloud, dovrai installare il client Python fornito da Groq. Puoi farlo utilizzando  ****pip**** :

```bash
pip install groq
```

### 3. Configurazione dell'ambiente locale

Una volta ottenuta la chiave API dal tuo account GroqCloud, dovrai configurare il tuo ambiente per l’accesso:

```bash
export GROQ_API_KEY="your_api_key"
```

A questo punto puoi utilizzare [front_test](App/front/front_tests.py) per svolgere i tuoi test e capire come funziona l'LLM

# Utilizzo di Streamlit per creare un'app web con Python

Questo repository contiene un esempio di come utilizzare **Streamlit** per creare una semplice applicazione web in Python.

## 1. Installazione di Streamlit

Per installare Streamlit, puoi usare **pip**. Esegui il seguente comando:

```bash
pip install streamlit
```

## 2. Esecuzione dell'applicazione

Per avviare l’app, esegui il seguente comando dalla tua shell o terminale:

```bash
streamlit run app.py
```

Questo aprirà l’applicazione web nel tuo browser predefinito.
