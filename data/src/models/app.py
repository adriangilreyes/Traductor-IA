import gradio as gr
import sys
import os

# Subimos tres niveles desde models a la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from data.src.models.Transformer import traducir, token_es_en, model_es_en, \
    token_en_es, model_en_es, token_es_de, model_es_de, token_de_es, model_de_es

# Lista de idiomas y emojis de bandera
langs = {
    "Español 🇪🇸": "es",
    "Inglés 🇬🇧": "en",
    "Alemán 🇩🇪": "de"
}

def traducir_ui(texto, src_lang, tgt_lang):
    # src_lang y tgt_lang serán códigos: 'es', 'en', 'de'
    
    if src_lang == "es" and tgt_lang == "en":
        return traducir(texto, token_es_en, model_es_en)
    elif src_lang == "en" and tgt_lang == "es":
        return traducir(texto, token_en_es, model_en_es)
    elif src_lang == "es" and tgt_lang == "de":
        return traducir(texto, token_es_de, model_es_de)
    elif src_lang == "de" and tgt_lang == "es":
        return traducir(texto, token_de_es, model_de_es)
    else:
        return "Traducción no soportada todavía 😅"

demo = gr.Interface(
    fn=traducir_ui, 
    inputs=[
        gr.Textbox(label="Introduce texto"),
        gr.Dropdown(list(langs.keys()), label="Idioma de origen"),
        gr.Dropdown(list(langs.keys()), label="Idioma destino") 
    ],
    outputs=gr.Textbox(label="Traducción"),
    title="Traductor IA",
    description="Traduce entre Español, Inglés y Alemán"
)

demo.launch() 