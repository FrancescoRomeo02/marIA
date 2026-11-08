# MAR/IA

An internal AI configurator for mapping services, identifying business opportunities, and supporting sales preparation and employee training.

The project combines a Streamlit interface with Groq-hosted LLMs to make service information easier to explore and use before client meetings.

## Features

- Service and opportunity mapping
- Interactive Streamlit interface
- LLM-assisted exploration through Groq
- Support for sales enablement and training workflows

## Local setup

Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate
```

On Windows:

```text
.\\env\\Scripts\\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure the Groq API key:

```bash
export GROQ_API_KEY="your_api_key"
```

Run the application:

```bash
streamlit run app.py
```

## Repository areas

- `App/front/` — Streamlit application and front-end experiments
- `requirements.txt` — Python dependencies
- `GROQ_API_KEY` — required for Groq-backed features

## Status

This repository contains the development version of the configurator and related LLM experiments.
