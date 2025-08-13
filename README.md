Jarvis - AI Voice Assistant

📌 Overview:
Jarvis is a Python-based **voice assistant** that can:
- Listen for a wake word ("Jarvis")
- Perform web actions (open Google, YouTube, LinkedIn, etc.)
- Play songs from a predefined music library
- Answer general queries using **OpenAI's GPT model**
- Respond with **text-to-speech** using `gTTS` or `pyttsx3

✨ Features:
Speech Recognition with `speech_recognition`
Voice Output using `gTTS` and `pygame`
Web Automation with `webbrowser`
Music Player with custom music library
AI-Powered Responses using OpenAI API
Wake Word Activation ("Jarvis")

📂 Project Structure:
📦 Jarvis-Assistant
┣ 📜 main.py 
┣ 📜 musiclibrary.py 
┣ 📜 client.txt
┗ 📜 README.md 

🛠 Installation:
1️⃣ Clone the repository
bash
git clone https://github.com/your-username/jarvis-assistant.git
cd jarvis-assistant

2️⃣ Install dependencies
bash
pip install -r requirements.txt

3️⃣ Add your OpenAI API Key
In main.py and aiProcess() function, replace:
openai.api_key = # Set your OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"

📋 Requirements:
* Python 3.8+
* SpeechRecognition
* gTTS
* PyAudio (for microphone input)
* pygame
* openai
* pyttsx3
  
Install all at once:
pip install speechrecognition gTTS pygame openai pyttsx3 pyaudio

Example Commands:
1.Open Google → Opens Google in your browser
2.Open YouTube → Opens YouTube
3.Open LinkedIn → Opens LinkedIn
4.Play Ak → Plays a predefined song from the music library
5.Any other question → AI-generated answer from OpenAI


⚙️ How It Works:
1.Wake Word Detection → Listens for "Jarvis"
2.Command Recognition → Uses Google Speech Recognition to interpret commands
3.Action Execution:
  * Opens websites
  * Plays music
  * Calls OpenAI for AI-generated responses
4.Voice Response → Speaks the response via gTTS or pyttsx3

⚠️ Disclaimer:
- This project is for educational purposes only.
- Ensure you follow OpenAI's usage policy.
- Do not use for malicious or spam activities.

