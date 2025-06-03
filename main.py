import gradio as gr

def chatbot(msg):
    return f"Bot: {msg}"

gr.Interface(fn=chatbot, inputs="text", outputs="text").launch(
    server_name="0.0.0.0",
    server_port=8080,
    share=True
)
