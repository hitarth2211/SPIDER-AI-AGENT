import os
import time
import subprocess
import webbrowser
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
import google.generativeai as genai
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc



# ================== CONFIGURATION ==================
SITES = {
    "youtube": "https://www.youtube.com",
    "wikipedia": "https://www.wikipedia.com",
    "google": "https://www.google.com",
    "instagram": "https://www.instagram.com",
    "whatsapp": "https://web.whatsapp.com",
    "facebook": "https://www.facebook.com",
    "linkedin": "https://www.linkedin.com",
    "gpt":"https://chatgpt.com/"
}

# ================== GLOBALS ==================
chatStr = ""
is_speaking = False
engine = pyttsx3.init()

# ================== SPEECH FUNCTIONS ==================
def say(text):
    """Speak out the given text."""
    global is_speaking
    is_speaking = True
    engine.stop()
    engine.say(text)
    engine.runAndWait()
    is_speaking = False

def takeCommand():
    """Listen to user's voice and convert to text."""
    r = sr.Recognizer()
    r.pause_threshold = 1.2
    r.energy_threshold = 300
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception:
            return ""

# ================== AI FUNCTIONS ==================
def get_gemini_response(prompt):
    """Get a response from the Gemini API."""
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment!")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    try:
        return model.generate_content(prompt).text
    except Exception as e:
        say("Sorry, I have reached my daily usage limit.")
        print("Gemini API error:", e)
        return None

def chat(query):
    """Chat mode with memory."""
    global chatStr
    chatStr += f"Hitarth: {query}\nSpider: "
    response = get_gemini_response(chatStr)
    if response:
        say(response)
        chatStr += response + "\n"

def ai(prompt):
    """One-time AI content generation."""
    text = get_gemini_response(prompt)
    if text:
        print(text)
        if not os.path.exists("Geminiai"):
            os.mkdir("Geminiai")
        safe_filename = prompt.replace(" ", "_")[:50]
        with open(f"Geminiai/{safe_filename}.txt", "w", encoding="utf-8") as f:
            f.write(f"Gemini response for prompt: {prompt}\n**************\n\n{text}")
    return text

# ================== SYSTEM CONTROL FUNCTIONS ==================
def change_volume(delta):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    minVol, maxVol, _ = volume.GetVolumeRange()
    current = volume.GetMasterVolumeLevel()
    volume.SetMasterVolumeLevel(min(max(current + delta, minVol), maxVol), None)

def mute_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(1, None)

def change_brightness(delta):
    try:
        current = sbc.get_brightness()[0]
        sbc.set_brightness(min(max(current + delta, 0), 100))
    except Exception:
        say("Brightness control not supported.")



def write_in_notepad(prompt):
    say("Opening Notepad and writing sir...")
    content = ai(prompt)  # your AI function
    if not content:
        say("I couldn't generate any content to write.")
        return

    try:
        # 1. Create a temporary file
        filepath = os.path.join(os.getcwd(), "spider_note.txt")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        # 2. Open it with Notepad (always fresh window)
        subprocess.Popen(["notepad.exe", filepath])
        time.sleep(1)

        say("Done writing in Notepad.")
    except Exception as e:
        say(f"Something went wrong: {e}")


# ================== COMMAND MAPPING ==================
COMMANDS = {
    "open notepad": lambda: os.system("start notepad"),
    "open calculator": lambda: os.system("start calc"),
    "open command prompt": lambda: os.system("start cmd"),
    "open paint": lambda: os.system("start mspaint"),
    "open explorer": lambda: os.system("explorer"),
    "open chrome": lambda: os.system("start chrome"),
    "increase volume": lambda: (change_volume(3.0), say("Volume increased.")),
    "decrease volume": lambda: (change_volume(-3.0), say("Volume decreased.")),
    "mute volume": lambda: (mute_volume(), say("Volume muted.")),
    "increase brightness": lambda: (change_brightness(10), say("Brightness increased.")),
    "decrease brightness": lambda: (change_brightness(-10), say("Brightness decreased.")),
    "shutdown system": lambda: os.system("shutdown /s /t 5"),
    "restart system": lambda: os.system("shutdown /r /t 5"),
}

# ================== MAIN LOOP ==================
if __name__ == '__main__':
    print("SPIDER started...")
    say("HELLO I AM SPIDER")

    while True:
        print("Listening...")
        query = takeCommand()
        if not query:
            continue

        if "spider" in query.lower():
            # Stop speech
            if "spider stop" in query.lower():
                if is_speaking:
                    engine.stop()
                    is_speaking = False
                    print("[SPIDER] Speech stopped.")
                continue

            # Quit
            if "spider quit" in query.lower():
                say("Goodbye, sir.")
                break

            # Reset chat
            if "reset chat" in query.lower():
                chatStr = ""
                say("Chat history cleared.")
                continue

            # Write in Notepad
            if "open notepad" in query.lower():
                prompt = query.lower().replace("write", "").replace("in notepad", "").strip()
                write_in_notepad(prompt)
                continue

            # Open websites
            for site, url in SITES.items():
                if f"open {site}" in query.lower():
                    say(f"Opening {site} sir...")
                    webbrowser.open(url)
                    break
            else:
                # System commands
                matched = False
                for cmd, action in COMMANDS.items():
                    if cmd in query.lower():
                        action()
                        matched = True
                        break
                if not matched:
                    chat(query)
