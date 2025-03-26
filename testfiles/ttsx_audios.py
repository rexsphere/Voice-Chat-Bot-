import pyttsx3
engine = pyttsx3.init('nsss')
def print_audios():
# Get and print available voices
    voices = engine.getProperty('voices')
    for index, voice in enumerate(voices):
        print(f"{index}: {voice.name} - {voice.languages}")
    # 117 rishi ind
    engine.stop()

def chech_audio():
    # engine = pyttsx3.init('nsss')
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')  # Choose a more natural voice
    engine.setProperty('rate', 180)  # Adjust speed (Default ~200, slower sounds more human)
    engine.setProperty('volume', 1.0)  # Full volume

    engine.say("Hello! This is a much better sounding voice.")

chech_audio()
engine.runAndWait()