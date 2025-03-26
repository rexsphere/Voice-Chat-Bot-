import pyttsx3
import speech_recognition as sr
import whisper
from AI_call import get_chatgpt_response
import traceback
import tempfile
import wave
import pyaudio
import tempfile
import os
import tempfile
class WhisperModelSingleton:
    _instance = None

    @staticmethod
    def get_instance():
        if WhisperModelSingleton._instance is None:
            WhisperModelSingleton._instance = whisper.load_model("base")  # Options: tiny, base, small, medium, large
        return WhisperModelSingleton._instance


class TextToSpeechEngineSingleton:
    _instance = None
    
    @staticmethod
    def get_instance():
        if TextToSpeechEngineSingleton._instance is None:
            TextToSpeechEngineSingleton._instance = pyttsx3.init('nsss')
            engine = TextToSpeechEngineSingleton._instance
                # engine = pyttsx3.init('nsss')
            engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')  # Choose a more natural voice
            engine.setProperty('rate', 180)  # Adjust speed (Default ~200, slower sounds more human)
            engine.setProperty('volume', 1.0)  # Full volume

    
        return TextToSpeechEngineSingleton._instance

    def save_to_audio_file(self, text):
        engine = self.get_instance()
           # Create temporary audio file
        temp_audio_path = tempfile.mktemp(suffix=".aiff")  
        engine.save_to_file(text, temp_audio_path)
        engine.runAndWait()

        return temp_audio_path  # Return file path
     
      

def get_answer(question):
    prompt = f'USER: {question}\n Jarvis: '
    answer = get_chatgpt_response(prompt)
    return answer

def speak_old(text):
    engine = TextToSpeechEngineSingleton.get_instance()
    engine.say(text)
    engine.runAndWait()
    
def speak(text):
    temp_audio_path = tempfile.mktemp(suffix=".aiff")  # Use AIFF format
    os.system(f'say -v Samantha "{text}" -o {temp_audio_path}')  # Uses macOS voices
    return temp_audio_path
# speak("Hello How Are You? ")

 

def take_command_whisper():
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=16000) as source:
        print('Listening....')
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source, duration=1)  # Noise reduction
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        
        # Save the audio data to a temporary WAV file
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio_file:
            temp_audio_path = temp_audio_file.name  # Store the path before closing
            
        # Write audio to the WAV file properly
        with wave.open(temp_audio_path, 'wb') as wave_file:
            wave_file.setnchannels(1)
            wave_file.setsampwidth(audio.sample_width)  # Use sample width from audio object
            wave_file.setframerate(16000)
            wave_file.writeframes(audio.get_wav_data())

        model = WhisperModelSingleton.get_instance()
        result = model.transcribe(temp_audio_path, fp16=False)
        query = result["text"]

        print("USER Said: {} \n".format(query))

    except Exception as e:
        traceback.print_exc()
        print(f"Error in takeCommand: {e}")
        print("Say That Again....")
        return "None"

    return query


def run():
    while True:
        query = take_command_whisper().lower()
        print("query %s",query)
        ans = Reply(query)
        print(ans)
        speak(ans)
        if 'bye' in query:
            break

def test_save_to_audio_file():
    text = "Hello, this is a test of the text-to-speech engine."
    file_path = "test_output2.aiff"
    
    # Save the text to an audio file
    saved_file_path = TextToSpeechEngineSingleton().save_to_audio_file(text)
    
    # Print the path of the saved audio file
    print(f"Audio file saved at: {saved_file_path}")
 
if __name__ == '__main__':
    test_save_to_audio_file()
    # speak("why you need text")
    pass
