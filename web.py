import gradio as gr


def transcribe(audio):
    print(audio)
    return "Transcription goes here"


ui = gr.Interface(fn=transcribe, inputs=gr.Audio(source="microphone", type="filepath"), outputs="text")

ui.launch()
