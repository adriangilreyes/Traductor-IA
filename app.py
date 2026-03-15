import gradio as gr
import sys,os

sys.path.append(os.path.join(os.path.dirname(__file__), "data", "src"))


from data.src.models.Transformer import traducir_texto 

def traducir_ui(texto):
    if not texto.strip():
        return "Introduce algún texto"
    try:
        return traducir_texto(texto)
    except Exception as e: 
        return f"Error : {e}"
    
demo = gr.Interface(
    fn = traducir_ui,
    inputs= "text",
    outputs= "text",
    title = "traductor IA",
    description= "Traductor Español / Inglés / Alemán",
    allow_flagging = "never"
)
 
if __name__ == "__main__": 
    demo.launch()