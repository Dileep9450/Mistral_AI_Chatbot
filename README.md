# Mistral AI Chatbot

A modern AI chatbot application built with Python, Streamlit, and the Mistral AI API.

The application provides a professional conversational interface with multi-turn conversation history, Mistral model selection, secure API key management, error handling, and a responsive Streamlit interface.

## Features

* Mistral AI chat completion API
* Python and Streamlit
* Secure API key handling with `.env`
* Multi-turn conversations
* Conversation history using Streamlit session state
* Mistral model selection
* User and AI chat bubbles
* Loading indicator
* Clear conversation option
* Responsive modern interface
* API error handling
* Invalid API key handling
* Rate-limit handling
* Network error handling
* Model error handling
* GitHub-safe `.gitignore`
* Beginner-friendly project structure

## Project Structure

```text
Mistral_AI_Chatbot/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

Before running the project, install:

* Python 3.10 or newer
* Internet connection
* Mistral AI account
* Mistral API key

## Step 1: Create the Project Folder

Create a folder named:

```text
Mistral_AI_Chatbot
```

Open Command Prompt inside this folder.

## Step 2: Create a Virtual Environment

Windows:

```cmd
python -m venv venv
```

Activate it:

```cmd
venv\Scripts\activate
```

If PowerShell is being used:

```powershell
venv\Scripts\Activate.ps1
```

After activation, the command prompt should show something similar to:

```text
(venv) C:\...\Mistral_AI_Chatbot>
```

## Step 3: Upgrade pip

Run:

```cmd
python -m pip install --upgrade pip
```

## Step 4: Install Dependencies

Run:

```cmd
pip install -r requirements.txt
```

If the `pip` command does not work, use:

```cmd
python -m pip install -r requirements.txt
```

## Step 5: Create the `.env` File

Inside the project folder create:

```text
.env
```

Add:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

Replace `your_mistral_api_key_here` with your actual Mistral API key.

Do not add your API key to `app.py`.

## Step 6: Create the `.gitignore` File

Create:

```text
.gitignore
```

Add:

```gitignore
.env
.env.*
__pycache__/
*.py[cod]
venv/
.venv/
env/
.streamlit/
.vscode/
.idea/
.DS_Store
Thumbs.db
*.log
```

## Step 7: Run the Application

Run:

```cmd
python -m streamlit run app.py
```

Streamlit should display a local URL such as:

```text
http://localhost:8501
```

Open that address in your browser.

## Mistral API Key

Create a Mistral account and open Mistral Studio.

Go to the API Keys section and create a new API key.

Copy the key and place it in the `.env` file:

```env
MISTRAL_API_KEY=your_actual_key
```

Never upload the `.env` file to GitHub.

## Available Models

The sidebar provides model selection.

The application currently includes:

```text
mistral-small-latest
mistral-medium-latest
mistral-large-latest
```

The available models and account access can change over time, so use the Mistral documentation and Studio model list as the authoritative source.

## How the Application Works

The user enters a message in the Streamlit interface.

The message is stored in:

```python
st.session_state.messages
```

The previous conversation is combined with the new message.

The application sends the conversation to Mistral using:

```python
client.chat.complete(
    model=model,
    messages=messages
)
```

Mistral generates an AI response.

The response is displayed in the chat interface and saved to the conversation history.

This allows the application to understand previous messages during the current session.

## Error Handling

The application handles common problems including:

### Invalid API Key

If the API key is incorrect, the application displays an authentication error.

Check:

```env
MISTRAL_API_KEY=your_actual_key
```

Make sure there are no unnecessary spaces.

### Rate Limit

If the API returns a rate-limit error, wait and try again.

A rate limit can occur when too many requests are sent within the allowed period.

### Network Error

Check your internet connection and try again.

### Missing API Key

If `.env` does not contain:

```env
MISTRAL_API_KEY=...
```

the application will display an API key configuration message.

### Missing Package

If you see:

```text
ModuleNotFoundError
```

run:

```cmd
python -m pip install -r requirements.txt
```

### Streamlit Command Not Found

If you see:

```text
'streamlit' is not recognized as an internal or external command
```

use:

```cmd
python -m streamlit run app.py
```

This is the recommended fallback because it runs Streamlit through the active Python environment.

### Virtual Environment Not Activated

If packages appear to be missing, activate the environment:

```cmd
venv\Scripts\activate
```

Then run:

```cmd
python -m pip install -r requirements.txt
```

## Stopping the Application

Press:

```text
Ctrl + C
```

in Command Prompt.

## GitHub

Before pushing the project to GitHub, verify that `.env` is ignored.

You can run:

```cmd
git status
```

The `.env` file should not appear as an untracked file.

Never upload your real Mistral API key.

## Portfolio Description

You can describe this project on your resume as:

"Mistral AI Chatbot — Developed a professional conversational AI web application using Python, Streamlit, and the Mistral API, implementing secure environment-based API key management, multi-turn conversation history, model selection, responsive UI design, and robust API error handling."

## Technologies

Python

Streamlit

Mistral AI API

Mistral Python SDK

python-dotenv

Git

GitHub

## Future Improvements

Possible future enhancements include:

* Streaming responses
* Chat export
* Conversation download
* Markdown rendering
* Code syntax highlighting
* Authentication
* Persistent chat history
* File upload
* Document question answering
* Retrieval-Augmented Generation
* Voice input
* Voice output
* AI-powered document summarization
* Deployment using Streamlit Community Cloud
