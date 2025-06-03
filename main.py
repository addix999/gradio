import gradio as gr

def chatbot(message):
    return "Balasan: " + message

iface = gr.Interface(fn=chatbot, inputs="text", outputs="text", title="Chatbot Gradio Simple")
iface.launch(server_name="0.0.0.0", server_port=8080)
