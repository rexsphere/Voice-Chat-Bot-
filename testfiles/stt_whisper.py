import whisper

model = whisper.load_model("base")  # Options: tiny, base, small, medium, large
result = model.transcribe("/Users/pruthvirajadhav/code/AI assignment/Home.llc/test_audio.mp3",fp16=False)
print(result["text"])
