import gradio as gr
from models.Transformer import traducir_texto
import sys
import os

sys.path.append(os.path.abspath("../"))

def traducir_ui(texto):
    return traducir_texto(texto)

demo = gr.Interface(
    fn = traducir_ui,
    inputs="text",
    outputs="text",
    title="Traductor IA",
    description="Traductor Español/ Inglés / Alemán"
)

demo.launch()
