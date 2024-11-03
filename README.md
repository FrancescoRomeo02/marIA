MAR/IA

This repository contains the development of an internal configurator to map services, identify business opportunities, and boost cross-selling. Designed for sales and employee training, it’s interactive, predictive, and enhances decision-making before client meetings.

Creating a Virtual Environment in Python and Installing Dependencies

In this guide, I’ll show you how to create a virtual environment in Python and install dependencies from a file named requirements.txt.

1. Creating a Virtual Environment

First, it’s a good practice to create a virtual environment to isolate the project and manage dependencies independently from other projects. Here’s how to do it:

	1.	Open your terminal or shell.
	2.	Navigate to your project directory:

cd /path/to/your/project


	3.	Create a virtual environment using the following command:

python -m venv env

This will create a folder named env within the project directory.

2. Activating the Virtual Environment

To activate the virtual environment, use the following commands based on your operating system:

	•	on macOS/Linux:

source env/bin/activate


	•	on Windows:

.\env\Scripts\activate



After activating the virtual environment, you’ll see the prefix (env) at the beginning of the line in the terminal.

3. Installing Dependencies from a requirements.txt File

Run the following command:

pip install -r requirements.txt

This will install all dependencies specified in the requirements.txt file within your virtual environment.

Using GroqCloud to Run Llama API with Python

This repository contains an example of how to use GroqCloud to run the Llama model using Groq’s SDK with Python.

1. Creating an Account on GroqCloud

To start using GroqCloud, follow these steps:

- Go to the official GroqCloud website and create an account.

- Once registered, log in and retrieve your API keys needed to connect to GroqCloud from your Python environment.

2. Installing the Python Client

To connect to GroqCloud, you’ll need to install the Python client provided by Groq. You can do this using pip:

pip install groq

3. Configuring the Local Environment

After obtaining your API key from your GroqCloud account, you’ll need to set up your environment for access:

export GROQ_API_KEY="your_api_key"

At this point, you can use front_test to run tests and understand how the LLM works.

Using Streamlit to Create a Web App with Python

This repository contains an example of how to use Streamlit to create a simple web application in Python.

1. Installing Streamlit

To install Streamlit, you can use pip. Run the following command:

pip install streamlit

2. Running the Application

To launch the app, run the following command from your shell or terminal:

streamlit run app.py

This will open the web application in your default browser.
