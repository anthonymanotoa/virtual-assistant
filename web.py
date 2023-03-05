import gradio as gr
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def transcribe(audio):
    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print(transcript)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": transcript["text"]}
        ]
    )
    print(response)

    return transcript["text"]


ui = gr.Interface(fn=transcribe, inputs=gr.Audio(source="microphone", type="filepath"), outputs="text")

ui.launch()
