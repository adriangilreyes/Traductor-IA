import gradio as gr
import sys
import os

# Añadimos la ruta donde está Transformer.py
sys.path.append(os.path.join(os.path.dirname(__file__), "data", "src", "models"))

# Importamos las funciones y modelos
from Transformer import detectar_idioma, traducir, token_es_en, model_es_en, token_en_es, model_en_es, token_de_es, model_de_es

def traducir_ui(texto):
    """
    Detecta el idioma del texto y lo traduce usando los modelos correctos.
    """
    idioma = detectar_idioma(texto)  # tu función de detección
    if idioma == "es":
        return traducir(texto, token_es_en, model_es_en)
    elif idioma == "en":
        return traducir(texto, token_en_es, model_en_es)
    elif idioma == "de":
        return traducir(texto, token_de_es, model_de_es)
    else:
        return 'Idioma no "RECONOCIDO POR EL SISTEMA"' 

# Creamos la interfaz Gradio
demo = gr.Interface(
    fn=traducir_ui,
    inputs="text",
    outputs="text",
    title="Traductor IA",
    description="Traduce entre Español, Inglés y Alemán"
)

if __name__ == "__main__":
    demo.launch() 