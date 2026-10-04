# Claude Chatbot with Memory

A simple command-line chatbot built with **Python** and the **Anthropic API**. This project demonstrates how to build an interactive AI chatbot that maintains conversation history, streams Claude's responses in real time, and handles API failures without corrupting the conversation state.

## 🚀 Features

- Interactive command-line chatbot
- Powered by Anthropic's Claude API
- Conversation memory using message history
- Real-time streaming responses
- API error handling
- Graceful `/exit` command
- Environment variable support for API credentials
- Simple and beginner-friendly Python implementation

## 🛠️ Technologies Used

- **Python**
- **Anthropic Python SDK**
- **Claude Sonnet 5.5**
- **Environment Variables**
- **Python Virtual Environment**

## 📁 Project Structure

```text
claude-chat-bot/
│
├── .gitignore
├── README.md
├── quickstart.py
└── requirements.txt
```

### `quickstart.py`

The main Python application containing the chatbot logic.

### `requirements.txt`

Contains the project's Python dependency:

```text
anthropic==1.11.0
```

### `.gitignore`

Prevents files such as the virtual environment, environment variables, Python cache files, and logs from being committed to Git.

---

# ⚙️ How the Project Works

The chatbot follows a simple flow:

```text
Start Application
       ↓
Load Anthropic API Key
       ↓
Create Anthropic Client
       ↓
Initialize Conversation History
       ↓
Ask User for Input
       ↓
Add User Message to History
       ↓
Send Conversation to Claude
       ↓
Stream Claude's Response
       ↓
Save Assistant Response
       ↓
Ask for Another Message
       ↓
      /exit
       ↓
     Exit
```

---

# 📦 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/chiscookeke11/claude-chat-bot.git
```

Move into the project directory:

```bash
cd claude-chat-bot
```

---

## 2. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

After activation, you should see something similar to:

```text
(.venv)
```

at the beginning of your terminal prompt.

---

## 3. Install Dependencies

Install the required Python package:

```bash
pip install -r requirements.txt
```

This installs:

```text
anthropic==1.11.0
```

---

# 🔑 Configure the Anthropic API Key

The application requires an Anthropic API key.

The project reads the API key from an environment variable called:

```text
ANTHROPIC_API_KEY
```

The key should **not** be written directly inside the Python source code.

This is important because API keys are sensitive credentials and should never be committed to a public GitHub repository.

## Windows

You can temporarily set the environment variable in PowerShell:

```powershell
$env:ANTHROPIC_API_KEY="your-api-key"
```

Or in Command Prompt:

```cmd
set ANTHROPIC_API_KEY=your-api-key
```

You can also configure it permanently through Windows Environment Variables.

---

# ▶️ Running the Application

Once the environment is configured, run:

```bash
python quickstart.py
```

You should see:

```text
Claude Chatbot
Type /exit to quit.
```

You can then enter a question:

```text
You: How does a rainbow form?
```

Claude's response will appear progressively in the terminal.

To stop the chatbot:

```text
You: /exit
```

The application will respond:

```text
Goodbye!
```

---

# 🧠 Understanding the Code

## 1. Import Dependencies

```python
import anthropic
import os
```

`anthropic` provides the Python SDK used to communicate with Claude.

`os` is used to access environment variables such as the API key.

---

## 2. Define the Model and Token Limit

```python
MODEL = "claude-sonnet-5-5"
MAX_TOKENS = 512
```

`MODEL` specifies which Claude model the application should use.

`MAX_TOKENS` limits the maximum number of tokens Claude can generate for each response.

---

## 3. Read the API
