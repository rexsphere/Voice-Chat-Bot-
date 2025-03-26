#test_tts_sst.py

import unittest
from tts_stt import speak, takeCommand,take_command_whisper, Reply
import speech_recognition as sr
import whisper
import tempfile
import wave
import os

class TestTTSSTT(unittest.TestCase):

    def test_speak(self):
        """Test the speak function to ensure it runs without errors."""
        try:
            speak("This is a test of the speak function.")
            result = True
        except Exception as e:
            print(f"Error in speak: {e}")
            result = False
        self.assertTrue(result, "The speak function should run without errors.")

    def test_takeCommand(self):
        """Test the takeCommand function to ensure it runs without errors."""
        try:
            print("Please say something for the takeCommand test...")
            command = take_command_whisper()
            print(f"Command received: {command}")
            result = command != "None"
        except Exception as e:
            result = False
            print(f"Error in takeCommand: {e}")
       
        self.assertTrue(result, "The takeCommand function should capture audio input.")

    def test_reply(self):
        """Test the Reply function to ensure it returns a response."""
        question = "What is the weather like today?"
        try:
            response = Reply(question)
            print(f"Response: {response}")
            result = response is not None and response != ""
        except Exception as e:
            print(f"Error in Reply: {e}")
            result = False
        self.assertTrue(result, "The Reply function should return a valid response.")

    def test_microphone(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something...")
            audio = r.listen(source)

        print("Captured Audio Length:", len(audio.frame_data))  # Should be > 0
        print("Sample Width:", audio.sample_width)  
    

    def takeCommandWhisper_here(self):
        r = sr.Recognizer()
        with sr.Microphone(sample_rate=16000) as source:
            print('Listening....')
            r.pause_threshold = 0.8
            r.adjust_for_ambient_noise(source, duration=1)  # Noise reduction
            audio = r.listen(source)

        try:
            print("Recognizing.....")
            
            # Save audio data to a WAV file
            temp_audio_path = "test_audio.wav"  # Use a named file for debugging
            with wave.open(temp_audio_path, 'wb') as wave_file:
                wave_file.setnchannels(1) # Mono audio
                wave_file.setsampwidth(audio.sample_width)
                wave_file.setframerate(16000)
                wave_file.writeframes(audio.get_wav_data())

            print(f"Audio saved to: {temp_audio_path}")
            print("Checking file size:", os.path.getsize(temp_audio_path), "bytes")

            # Play the file to manually check it
            # os.system(f"afplay {temp_audio_path}")  # macOS only, use `ffplay` on Linux/Windows

            # Load Whisper model and transcribe the audio file
            model = whisper.load_model("base")
            result = model.transcribe(temp_audio_path, fp16=False)

            query = result["text"]
            print("Whisper Output:", query)

        except Exception as e:
            print(f"Error: {e}")
            return "None"

        return query


    def test_microphone_quality(self):
        r = sr.Recognizer()
        with sr.Microphone(sample_rate=16000) as source:  # Force 16kHz for Whisper
            print("Adjusting for ambient noise... (Wait a second)")
            r.adjust_for_ambient_noise(source, duration=1)  # Noise reduction
            print("Listening...")
            audio = r.listen(source)

        # Save raw recorded data for debugging
        with open("raw_audio.wav", "wb") as f:
            f.write(audio.get_wav_data())

        print("Saved test audio: raw_audio.wav")
 

if __name__ == '__main__':
    # unittest.main()
    obj = TestTTSSTT()
    # obj.test_takeCommand()
    # obj.test_microphone()
    # obj.test_microphone_quality()
    # obj.takeCommandWhisper()
    
