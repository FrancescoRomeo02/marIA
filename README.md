# MAR/IA

This repository contains the development of an internal configurator to map services, intercept business opportunities, and boost cross-selling. Designed for sales and employee training, it’s interactive, predictive, and enhances decision-making before client meetings.

## Creating a virtual environment in Python and installing dependencies

In this guide, I'll show you how to create a virtual environment in Python and install dependencies from a file called `requirements.txt`.

### 1. Creating a virtual environment

First of all, it is a good practice to create a virtual environment to isolate the project and manage dependencies independently from other projects. Here's how to do it:

1. Open terminal or shell.
2. Go to your project directory:
   ```bash
   cd /path/of/your/project
   ```
3. Create a virtual environment using the following command:
   ```bash
   python -m venv env
   ```
This will create a folder called env inside the project directory.
### 2. Activation of the virtual environment
To activate the virtual environment, use the following commands based on your operating system:
* on macOS/Linux
```bash
source env/bin/activate
```
* on Windows
```bash
.\env\Scripts\activate
```
After activating the virtual environment, you will see the prefix (env) at the beginning of the line in the terminal.
### 3. Installing dependencies from a requirements.txt file
Run the following command:
```bash
pip install -r requirements.txt
```
This will install all dependencies specified in the requirements.txt file into your virtual environment.

## Using GroqCloud to run Llama API with Python

This repository contains an example on how to use ****GroqCloud**** to run the ****Llama**** model using the Groq SDK with Python.

### 1. Creating your GroqCloud account

To get started using GroqCloud, follow these steps:

**-** Go to the official website of [**GroqCloud**](**https://groq.com/**) and create an account.

**-** Once registered, log in and get your ****API keys**** needed to connect to GroqCloud from your Python environment.

### 2. Installing the Python client

To connect to GroqCloud, you will need to install the Python client provided by Groq. You can do this using ****pip**** :

```bash
pip install groq
```

### 3. Configuring the local environment

Once you have the API key from your GroqCloud account, you will need to set up your environment for access:

```bash
export GROQ_API_KEY="your_api_key"
```

At this point you can use [front_test](App/front/front_tests.py) to carry out your tests and understand how the LLM works

# Using Streamlit to build a web app with Python

This repository contains an example of how to use **Streamlit** to create a simple web application in Python.

## 1. Installing Streamlit

To install Streamlit, you can use **pip**. Run the following command:

```bash
pip install streamlit
```

## 2. Running the application

To launch the app, run the following command from your shell or terminal:

```bash
streamlit run app.py
```

This will open the web application in your default browser.
