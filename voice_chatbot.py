import cohere
from RealtimeSTT import AudioToTextRecorder
from RealtimeTTS import TextToAudioStream
from RealtimeTTS.engines import GTTSEngine

# 1. Initialize Cohere API
COHERE_API_KEY = "YOUR_API_KEY"
co = cohere.Client(COHERE_API_KEY)

if __name__ == '__main__':
    # Initialize the GTTS engine
    engine = GTTSEngine()

    # 2. Initialize AudioToTextRecorder (RealtimeSTT)
    recorder = AudioToTextRecorder(
        language="en" 
    )

    # 3. Initialize TextToAudioStream (RealtimeTTS)
    tts_stream = TextToAudioStream(engine)

    print("Ready. Start speaking...")
    print("Press Ctrl + C at any time to end the conversation.")

    # Start a continuous conversation loop
    try:
        while True:
            # Step 1: Convert speech to text
            text_input = recorder.text()
            print(f"You said: {text_input}")

            # Step 2: Generate a response using Cohere's Chat API
            response = co.chat(
                model='command-nightly',
                message=text_input
            )
            generated_text = response.text
            print(f"LLM response: {generated_text}")

            # Step 3: Convert the response to audio
            tts_stream.feed(generated_text)
            tts_stream.play()

    except KeyboardInterrupt:
        print("\nGoodbye! Chatbot has finished.")

    except Exception as e:
        print(f"An error occurred: {e}")
        tts_stream.feed("I'm sorry, an error occurred. Please try again.")

        tts_stream.play()
