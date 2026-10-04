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

## 3. Read the API Key

```python
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
```

`os.getenv()` retrieves the value of the `ANTHROPIC_API_KEY` environment variable.

This allows the API key to remain outside the source code.

---

## 4. Create the Anthropic Client

```python
client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    base_url="https://api.anthropic.com"
)
```

This creates an Anthropic client that the application uses to communicate with the Claude API.

The API key authenticates the requests.

---

# 💾 Conversation Memory

One of the main concepts demonstrated in this project is **conversation memory**.

The application creates an empty list:

```python
messages = []
```

This list stores the conversation between the user and Claude.

When the user sends a message:

```python
messages.append({
    "role": "user",
    "content": user_input
})
```

the message is added to the conversation history.

After Claude responds successfully, the assistant's response is also stored:

```python
messages.append({
    "role": "assistant",
    "content": assistant_text
})
```

The conversation therefore becomes something like:

```text
User → Hello
Claude → Hello! How can I help?

User → What did I just say?
Claude → You said "Hello."
```

The chatbot can do this because previous messages are included in subsequent API requests.

---

# 🔄 Sending Conversation History

The stored conversation is passed to Claude here:

```python
with client.messages.stream(
    model=MODEL,
    max_tokens=MAX_TOKENS,
    messages=messages,
) as stream:
```

Instead of sending only the latest user message, the application sends the complete conversation history.

This allows Claude to understand the context of previous messages.

---

# ⚡ Streaming Responses

The project uses Anthropic's streaming functionality:

```python
with client.messages.stream(
    model=MODEL,
    max_tokens=MAX_TOKENS,
    messages=messages,
) as stream:
```

The response is then streamed using:

```python
for text in stream.text_stream:
    print(text, end="", flush=True)
```

Instead of waiting for the entire response before displaying anything, Claude's response appears piece by piece.

For example, instead of waiting for:

```text
A rainbow forms when sunlight interacts with water droplets...
```

the terminal can display the response progressively as it is generated.

---

# 📝 Collecting the Complete Response

After the stream finishes, the application retrieves the complete response:

```python
assistant_text = stream.get_final_text()
```

This is important because the complete response needs to be stored in the conversation history.

The response is then added:

```python
messages.append({
    "role": "assistant",
    "content": assistant_text
})
```

This allows future requests to maintain the conversation context.

---

# 🛡️ Error Handling

The chatbot uses a `try/except` block:

```python
try:
    ...
except anthropic.APIError as error:
    ...
```

This catches API-related errors instead of allowing the entire application to crash.

When an API request fails:

```python
messages.pop()
```

removes the user's most recent message from the conversation history.

This is important because the failed request did not produce a successful assistant response.

Without removing the message, the conversation history could contain an unmatched user message.

The application then displays:

```python
print(f"\nRequest failed: {error}")
```

and continues waiting for another user message:

```python
continue
```

---

# 🚪 Exiting the Chatbot

The application checks whether the user entered:

```text
/exit
```

using:

```python
if user_input.lower() == "/exit":
    print("Goodbye!")
    break
```

`break` terminates the chatbot loop and ends the program.

---

# 🔍 Empty Input Handling

The application also ignores empty messages:

```python
if not user_input:
    continue
```

This prevents unnecessary API requests when the user simply presses Enter.

---

# 🔐 Security

The project uses an environment variable for the Anthropic API key:

```text
ANTHROPIC_API_KEY
```

The API key should never be placed directly in:

```python
quickstart.py
```

and should never be committed to GitHub.

The `.gitignore` file also excludes environment files:

```text
.env
.env.*
```

and the virtual environment:

```text
.venv/
```

---

# 🧪 Testing the Chatbot

After starting the application, try a few different conversations.

### Test 1 — Basic Question

```text
You: What is machine learning?
```

Claude should provide an answer.

### Test 2 — Conversation Memory

Ask:

```text
You: My favorite programming language is Python.
```

Then ask:

```text
You: What is my favorite programming language?
```

Claude should be able to answer based on the stored conversation history.

### Test 3 — Streaming

Ask a question that requires a longer response and observe how Claude's answer appears progressively in the terminal.

### Test 4 — Exit

Enter:

```text
/exit
```

The chatbot should terminate gracefully.

### Test 5 — API Failure

If an API request fails, the application catches the error and removes the unmatched user message from the conversation history before continuing.

---

# 📚 Key Concepts Learned

This project demonstrates several important concepts for building AI applications:

### 1. API Integration

How to connect a Python application to an external AI API.

### 2. Environment Variables

How to keep sensitive credentials such as API keys outside the source code.

### 3. Conversation History

How to manually maintain context when working with a stateless message-based API.

### 4. Streaming

How to display AI-generated responses incrementally rather than waiting for the entire response.

### 5. Error Handling

How to use `try/except` to handle API failures gracefully.

### 6. State Management

How to maintain and update the chatbot's conversation state throughout the application lifecycle.

### 7. Command-Line Interfaces

How to build a simple interactive chatbot directly in the terminal.

---

# 🚀 Possible Improvements

This project provides a foundation that can be extended in several ways:

- Add `/reset` to clear conversation history
- Add conversation history persistence
- Save conversations to a database
- Build a web interface
- Add authentication
- Add tool/function calling
- Give Claude access to external tools
- Add file/document support
- Add Retrieval-Augmented Generation (RAG)
- Build an AI agent capable of completing multi-step tasks
- Add logging and more specific error handling

---

# 🎯 Project Goal

The goal of this project was to understand the fundamental building blocks of an AI chatbot before moving into more advanced AI agent development.

Rather than relying on a framework that hides the implementation details, this project demonstrates the core concepts directly:

```text
User Input
    ↓
Conversation History
    ↓
Anthropic API
    ↓
Claude
    ↓
Streaming Response
    ↓
Updated Conversation History
```

Understanding these fundamentals provides a strong foundation for building more advanced AI applications and agents.

---

# 👨🏽‍💻 Author

**Chinedu Okeke**

Software Engineer | AI/ML Engineer | Open Source Contributor

GitHub: [@chiscookeke11](https://github.com/chiscookeke11)

---

# 📄 License

This project is intended for learning and educational purposes.
