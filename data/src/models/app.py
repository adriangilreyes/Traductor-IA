import gradio as gr 
import sys
import os
from Transformer import traducir_texto 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../DB")))
from conexion import obtener_historial, guardar_traduccion


# Función para limpiar los textos
def limpiar_textos():
    return "", "" 

css = """

body{ 
    background-color:#DBD9D9 !important;  
}

.gradio-container{ 
    background-color:#DBD9D9 !important
    border-radius:7px !important
    border: 2px solid black !important;

}    
    
.gradio-container{ 
    background-color:#DBD9D9 !important
    border-radius:7px solid black !important;
     
}

textArea{
    background-color: #f7f7f7 !important;
    color:black !important
    border-radius:7px solid black !important; 
    
}

textArea{
    background-color: #f7f7f7 !important;
    color:black !important
    border-radius:7px !important
    border: 2px solid black !important;
    animation: fadeIn 0.5s ease-int-out;

    @Keyframes fadeIn {
        from{
            opacity: 0;
        } to {
            opacity: 1; 
        }
    }  
}
 
#btn_traducir, #btn_limpiar {
    width: 180px !important;
    border-radius: 10px !important
    background-color: #866156;  
}  

#title_page {
    position:absolute;
    right: 150px;
}

"""

# Subimos tres niveles desde models a la raíz del proyecto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from data.src.models.Transformer import traducir_texto, token_es_en, model_es_en, \
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
        return traducir_texto(texto, token_es_en, model_es_en)
    elif src_code == "en" and tgt_code == "es": # inglés - español
        return traducir_texto(texto, token_en_es, model_en_es)
    elif src_code == "es" and tgt_code == "de": # español - alemán
        return traducir_texto(texto, token_es_de, model_es_de) 
    elif src_code == "de" and tgt_code == "es": # alemán - español
        return traducir_texto(texto, token_de_es, model_de_es)
    elif src_code == "es" and tgt_code == "fr": #español - francés
        return traducir_texto(texto,token_es_fr,model_es_fr)
    elif src_code == "fr" and tgt_code == "es": # francés - español
        return traducir_texto(texto,token_fr_es, model_fr_es)  
    else: 
        return "Traducción no soportada todavía 😅"  

    #guardamos la traducción en la base de datos
    guardar_traduccion(texto,traduccion,src_code,tgt_code)

    return traduccion

with gr.Blocks() as demo:

    gr.Markdown("## 🌍 Traductor IA", elem_id="title_page") 

    # 🔹 Selectores de idioma
    with gr.Row():
        src_lang = gr.Dropdown(
            choices=list(langs.keys()),
            label="Origen",
            value="Español 🇪🇸"
        )

        tgt_lang = gr.Dropdown(
            choices=list(langs.keys()),
            label="Destino",
            value="Inglés 🇬🇧"
        )

    # 🔹 Textos
    with gr.Row():
        input_text = gr.TextArea(label="Texto")
        output_text = gr.TextArea(label="Traducción")

    # 🔹 Botón
    btn_traducir = gr.Button("Traducir 🚀", elem_id="btn_traducir")

    btn_traducir.click(
        traducir_ui,
        inputs=[input_text, src_lang, tgt_lang],  # 👈 aquí está la clave
        outputs=output_text
    )

    btn_limpiar = gr.Button("Limpiar 🧹", elem_id="btn_limpiar")
    btn_limpiar.click(
    limpiar_textos,
    inputs=[],
    outputs=[input_text, output_text]
    )

    btn_historial = gr.Button("Historial 🕒")
    historial_text = gr.TextArea(label="Últimas traducciones",interactive=False, lines=10)

    btn_historial.click(
    lambda: "\n".join(
        [f"{t[0]} → {t[1]} ({t[2]}→{t[3]})" for t in obtener_historial()]
    ) or "No hay traducciones todavía 😅",
    inputs=[],
    outputs=historial_text
) 
    
demo.launch()     