import gradio as gr
from tts_stt import speak, take_command_whisper
from AI_call import get_chatgpt_response_with_user_info,call_ai_with_tools
import os
import subprocess
# Global variable to hold the TTS process
tts_process = None
# Global flag to control TTS
stop_tts = False
def reset_ui():
    return "", ""  
def stop_speaking():
    global stop_tts
    stop_tts = True  # Set flag to stop TTS

def process_query(text_input):
    global stop_tts
    stop_tts = False  # Reset stop flag
    # Get response from AI based on user input
    response = get_chatgpt_response_with_user_info(text_input)
    speak_text(response)
    return response
def process_query_tools(text_input):
    global stop_tts
    stop_tts = False  # Reset stop flag
    # Get response from AI based on user input
    response = call_ai_with_tools(text_input)
    speak_text(response)
    return response
def record_audio():
    # Record audio and transcribe it to text
    audio_query = take_command_whisper()
    if audio_query != "None":
        response = get_chatgpt_response_with_user_info(audio_query)
        speak_text(response)
        return audio_query, response
    return "No audio input detected.", "Please try again."

def speak_text(text):
    global tts_process
    # Start the TTS process
    tts_process = subprocess.Popen(['say', text])
    tts_process.wait()  # Wait for the process to complete
    return text  #

def stop_speaking():
    global tts_process
    if tts_process is not None:
        tts_process.terminate()  # Terminate the TTS process
        tts_process = None  # Reset the process variable

def speak_text_old(text):
    os.system(f'say "{text}"')  # Uses macOS built-in TTS
    return text  # Return text for display
def start():
    # Create Gradio interface
    with gr.Blocks() as demo:
        gr.Markdown("## Voice Assistant")
        
        with gr.Row():
            text_input = gr.Textbox(label="Enter your query:", placeholder="Type your question here...")
            text_output = gr.Textbox(label="AI Response:", interactive=False)
            
        submit_btn = gr.Button("Submit")
        record_btn = gr.Button("Record Audio")
        stop_btn = gr.Button("Stop")
        reset_btn = gr.Button("Reset")
        submit_btn.click(fn=process_query_tools, inputs=text_input, outputs=text_output)
        record_btn.click(fn=record_audio, outputs=[text_input, text_output])
        stop_btn.click(fn=stop_speaking)
        reset_btn.click(fn=reset_ui, outputs=[text_input, text_output])
 
    demo.launch()
start()