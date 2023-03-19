import openai

openai.api_key = "Enter your API key here"
audio_file= open("ZOOM0030_small.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

print(transcript)

# save the transcript to a text file
with open("transcript.txt", "w", encoding="utf-8") as text_file:
    text_file.write(transcript.text)
