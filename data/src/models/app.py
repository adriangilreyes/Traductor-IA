import gradio as gr
import sys
import os

css = """

body{
    background-color:#D9D1D0 !important;
}

.gradio-container{
    background-color:#f7f7f7 !important;
}

textArea{
    background-color: #f7f7f7 !important;
    color:black !important;
}
 
button{
    background-color:#278EF5;
    color:white; 
}
"""

# Subimos tres niveles desde models a la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from data.src.models.Transformer import traducir, token_es_en, model_es_en, \
    token_en_es, model_en_es, token_es_de, model_es_de, token_de_es, model_de_es,token_es_fr , model_es_fr, token_fr_es, model_fr_es


# Lista de idiomas y emojis de bandera
langs = {
    "Español 🇪🇸": "es",
    "Inglés 🇬🇧": "en",
    "Alemán 🇩🇪": "de",
    "Francés 🇫🇷": "fr"
}

def traducir_ui(texto, src_lang, tgt_lang): 
    # src_lang y tgt_lang serán códigos: 'es', 'en', 'de','fr'
    #print('src_lang --->',src_lang)
    #print('tgt_lang --->',tgt_lang)

    src_code = langs.get(src_lang) 
    tgt_code = langs.get(tgt_lang)

    if src_code == "es" and tgt_code == "en": # español - inglés
        return traducir(texto, token_es_en, model_es_en)
    elif src_code == "en" and tgt_code == "es": # inglés - español
        return traducir(texto, token_en_es, model_en_es)
    elif src_code == "es" and tgt_code == "de": # español - alemán
        return traducir(texto, token_es_de, model_es_de) 
    elif src_code == "de" and tgt_code == "es": # alemán - español
        return traducir(texto, token_de_es, model_de_es)
    elif src_code == "es" and tgt_code == "fr": #español - francés
        return traducir(texto,token_es_fr,model_es_fr)
    elif src_code == "fr" and tgt_code == "es": # francés - español
        return traducir(texto,token_fr_es, model_fr_es) 
    else:
        return "Traducción no soportada todavía 😅"

demo = gr.Interface(
    fn=traducir_ui,  
    inputs=[
        gr.TextArea(label="Introduce texto"), 
        gr.Dropdown(list(langs.keys()), label="Idioma de origen"),
        gr.Dropdown(list(langs.keys()), label="Idioma destino") 
    ],
    outputs=gr.TextArea(label="Traducción"), 
    title="Traductor IA",
    description="Traduce entre Español, Inglés, Alemán, Francés", 
    live=False,
    submit_btn="Translate", 
    css = css 
) 
    
demo.launch()   