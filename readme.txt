🕷️ SPIDER – AI Desktop Voice Assistant (Python)

A powerful, AI-driven desktop assistant that responds to voice commands, automates system tasks, generates content using Gemini AI, and controls your entire Windows environment — completely hands-free.

SPIDER combines voice recognition, system automation, and AI reasoning into a single intelligent assistant built fully in Python.

⭐ Key Features
🎤 Voice Command Recognition

Listens to your voice using speech_recognition

“SPIDER” acts as the wake word

Understands natural commands like:

“Spider open YouTube”

“Spider increase volume”

“Spider open notepad and write a story”

🤖 AI-Powered Intelligence (Gemini API)

Generates text, notes, summaries, stories, and answers

Chat with memory (remembers previous messages)

Writes AI-generated content automatically into Notepad

💻 Windows System Automation

SPIDER can control major system functions:

Increase / decrease / mute volume

Adjust screen brightness

Open apps (Notepad, Chrome, Calculator, Command Prompt, Paint)

Shutdown or restart the system

Launch File Explorer

🌐 Web Automation

Open websites instantly just by saying:

YouTube

Google

Instagram

LinkedIn

Facebook

Wikipedia

WhatsApp Web

📝 AI Content Writer

Generates content using Gemini

Creates a temporary .txt file

Opens it in Notepad

Does not auto-save (as you requested)

🧠 Chat Mode With Memory

Keeps track of your conversations to provide more natural responses until you say:

“Spider reset chat”

🔧 Tech Stack

Python

SpeechRecognition

PyAudio

pyttsx3 (TTS)

PyCAW (volume control)

screen_brightness_control

pywinauto

uiautomation

pyautogui

webbrowser

Google Gemini API

dotenv

🚀 How It Works

Listens for your voice command

Recognizes speech and converts it to text

Detects if command contains “SPIDER” (wake word)

Matches the command against:

System commands

Website commands

AI commands

Executes the requested task immediately

Speaks back using text-to-speech

📌 Why This Project Is Special

Not a normal chatbot — it interacts with the Windows OS directly

Combines voice automation + AI generation

Shows strong understanding of real-world Python libraries

Unique and impressive for resume & interviews

A complete practical assistant, not just a demo

🛠️ Future Enhancements (optional)

GUI for controlling SPIDER

Wake-word detection without pushing activation button

Better intent classification

System notification responses

Ability to send WhatsApp messages or emails

If you'd like, I can also:

✅ Format this into a READY README.md with headings
✅ Add a GIF / demo section template
✅ Add instructions & installation commands
✅ Add badges, logos, and styling

Just say "make it README.md".

You said:
desciption should be small and within 350 letters
ChatGPT said:

Here are 3 short descriptions under 350 characters — pick the one you like:

Option 1 (Clean & Professional)

A simple Java-based personal time management tool that lets users create, update, and delete tasks directly through the console. Designed to practice OOP concepts, file handling, and clean program structure.

Option 2 (Technical)

A console-based Java task manager supporting task creation, updating, deletion, and viewing. Built to demonstrate OOP principles, exception handling, and user-friendly CLI interactions.

Option 3 (Resume-Friendly)

A lightweight Java CLI Task Manager allowing users to add, edit, delete, and view tasks. Highlights skills in OOP, clean code design, and interactive console applications.

If you want, I can tailor it for GitHub README, resume, or LinkedIn.

You said:
write it for my spider
ChatGPT said:

Here are 3 short (≤350 characters) descriptions specifically for your SPIDER AI Assistant project:

Option 1 (Simple & Clear)

A desktop-based SPIDER AI Assistant that executes voice-based commands like creating notes, writing content in Notepad, and performing quick tasks using AI—without auto-saving. Built to showcase automation, AI integration, and voice-command execution.

Option 2 (Technical & Resume-Friendly)

SPIDER is a voice-controlled desktop AI assistant that performs actions such as writing content in Notepad using AI, generating different text formats, and handling custom tasks—without automatic saving. Focused on automation, NLP, and system control.

Option 3 (More Polished)

SPIDER is an AI-powered desktop assistant that listens to user voice commands and performs tasks like generating text in Notepad, creating content, and automating simple workflows—while ensuring no auto-save. Demonstrates automation + AI integration.

If you want an even shorter version for resume (100–150 chars), I can write that too.

You said:
now give me readme file for it
ChatGPT said:

Here is a clean, professional README.md for your SPIDER AI Assistant project.
You can copy-paste directly into your GitHub repo.

🕷️ SPIDER – Voice-Controlled AI Desktop Assistant

SPIDER is a lightweight desktop-based AI assistant that listens to your voice commands and performs tasks such as writing content in Notepad using AI, generating different types of text, and automating simple system actions — all without auto-saving.
Designed to showcase automation, speech recognition, system control, and AI integration.

🚀 Features

🎤 Voice Command Recognition
Speak commands like “Write a letter in Notepad” or “Create a paragraph”.

📝 AI-Powered Content Generation
Generates different types of text (letters, essays, notes, etc.) and writes them directly into Notepad.

❌ No Automatic Saving
Ensures full user control — the app writes content but does not auto-save files.

⚙️ Custom Commands
Add your own voice commands and actions easily.

💻 Desktop Automation
Controls Notepad and system utilities using Python automation libraries.

🛠️ Tech Stack

Python

Speech Recognition

pyttsx3 (Text-to-Speech)

OpenAI / GenAI API for content generation

pyautogui (Keyboard & mouse automation)

Subprocess / OS for system-level actions

📂 Project Structure
SPIDER/
│── spider.py
│── commands/
│── utils/
│── README.md

🔧 How It Works

SPIDER listens for your voice command.

The command is interpreted and matched with actions.

If text generation is required, SPIDER uses AI to generate the content.

It opens Notepad and writes the generated text (but does NOT save).

You manually choose to save or close.

▶️ How to Run
pip install -r requirements.txt
python spider.py

🗣️ Example Commands

“Open Notepad write an apology letter.”

“Open notepad and write a paragraph about AI.”

“Open Notepad.”

“Open notepad and write poem.”

“SPIDER quit.”

