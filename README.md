# 🤖 Voice Chatbot with Cohere

This project is a simple, real-time voice chatbot built in Python. It creates a conversational AI assistant that listens to your voice, generates intelligent responses using the Cohere Chat API, and speaks the replies back to you in real time.

The assignment was completed as part of a training task for Smart Methods.

---

## 🚀 Features
- Real-time, continuous voice conversation
- Utilizes the powerful `command-nightly` large language model from Cohere
- Provides a continuous conversational loop
- Simple and easy to set up
- Graceful exit by pressing `Ctrl + C`

---

## 🛠 Prerequisites
Before you begin, you need to have the following software installed on your system:
- **Anaconda**: A powerful platform for data science and machine learning, which includes Python and a package manager (conda)
- **Visual Studio Code (VS Code)**: A lightweight but powerful source code editor

---

## ⚙️ Installation & Setup

### ⬇️ Step 1: Install Python and Libraries
1. Open Anaconda Prompt
2. Create a dedicated environment (Recommended) to avoid conflicts with other projects:
   
   conda create --name voice_chatbot python=3.10
  
3. Activate the environment before installing libraries:
   
   conda activate voice_chatbot
  
4. Install the necessary libraries for the project:
   
   pip install cohere RealtimeSTT RealtimeTTS

### 📂 Step 2: Prepare the Project Files
1. Open VS Code
2. Go to `File -> Open Folder...` and select an empty folder for your project
3. Create a new file named `voice_chatbot.py` and copy the project code into it
4. Replace `"YOUR_API_KEY"` with your actual Cohere API key (You can get one from the [Cohere Dashboard](https://dashboard.cohere.com/))

### ▶️ Step 3: Run the Application
To run the code, use the Anaconda Prompt:
1. Open Anaconda Prompt and activate your environment:
   
   conda activate voice_chatbot
  
2. Navigate to your project directory using the `cd` command:
   
   cd C:\Path\To\Your\Project\Folder
  
3. Execute the script using the `python` command:
   
   python voice_chatbot.py
  
   The application will start, and you can begin speaking. To exit, press `Ctrl + C`.

---

## � How It Works
- The program enters a continuous `while` loop to listen for your voice using `AudioToTextRecorder`
- It converts your speech to text and sends it to the Cohere Chat API via `co.chat()`
- The AI's text response is then streamed and converted into a natural voice using `TextToAudioStream`
- The loop continues, allowing for a seamless, ongoing conversation until you choose to exit

---

## 👩‍💻 Author
Developed by Raghad Alrashidi
