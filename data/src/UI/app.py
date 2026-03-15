import sys
import os
import gradio as gr

sys.path.append(os.path.join(os.path.dirname(__file__), "data/src"))

from data.src.models.Transformer import traducir_texto


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
