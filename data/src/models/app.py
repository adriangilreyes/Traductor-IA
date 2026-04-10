import gradio as gr

from Transformer import (
    traducir_texto,
    token_es_en, model_es_en,
    token_en_es, model_en_es,
    token_es_de, model_es_de,
    token_de_es, model_de_es,
    token_es_fr, model_es_fr,
    token_fr_es, model_fr_es
)

# -----------------------------
# CSS LIMPIO Y FUNCIONAL
# -----------------------------
css = """
.gradio-container {
    background-color: #DBD9D9 !important;
    border-radius: 10px !important;
    border: 2px solid black !important;
}

textarea {
    background-color: white !important;
    color: black !important;
    animation: fadeIn 0.4s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

#btn_traducir, #btn_limpiar {
    width: 180px !important;
    border-radius: 10px !important;
}

#btn_traducir:hover, #btn_limpiar:hover {
    transform: scale(1.05);
    transition: 0.2s;
}
"""

# -----------------------------
# IDIOMAS
# -----------------------------
langs = {
    "Español": "es",
    "Inglés": "en",
    "Alemán": "de",
    "Francés": "fr"
}

# -----------------------------
# TRADUCCIÓN
# -----------------------------
def traducir_ui(texto, src_lang, tgt_lang):

    if not texto:
        return ""

    src_code = langs.get(src_lang)
    tgt_code = langs.get(tgt_lang)

    if src_code == "es" and tgt_code == "en":
        return traducir_texto(texto, token_es_en, model_es_en)

    elif src_code == "en" and tgt_code == "es":
        return traducir_texto(texto, token_en_es, model_en_es)

    elif src_code == "es" and tgt_code == "de":
        return traducir_texto(texto, token_es_de, model_es_de)

    elif src_code == "de" and tgt_code == "es":
        return traducir_texto(texto, token_de_es, model_de_es)

    elif src_code == "es" and tgt_code == "fr":
        return traducir_texto(texto, token_es_fr, model_es_fr)

    elif src_code == "fr" and tgt_code == "es":
        return traducir_texto(texto, token_fr_es, model_fr_es)

    else:
        return "Traducción no soportada 😅"


# -----------------------------
# LIMPIAR
# -----------------------------
def limpiar_textos():
    return "", ""


# -----------------------------
# INTERCAMBIAR IDIOMAS
# -----------------------------
def intercambiar(src, tgt, texto, resultado):
    return tgt, src, resultado, texto


# -----------------------------
# UI
# -----------------------------
with gr.Blocks(css=css) as demo:

    gr.Markdown("## 🌍 Traductor IA")

    with gr.Row():
        src_lang = gr.Dropdown(
            list(langs.keys()),
            label="Origen"
        )

        tgt_lang = gr.Dropdown(
            list(langs.keys()),
            label="Destino"
        )

    with gr.Row():
        input_text = gr.TextArea(label="Texto")
        output_text = gr.TextArea(label="Traducción") 
    with gr.Row():
        btn_traducir = gr.Button("Traducir 🚀", elem_id="btn_traducir")
        btn_swap = gr.Button("🔁")
        btn_limpiar = gr.Button("Limpiar 🧹", elem_id="btn_limpiar")

    # eventos
    btn_traducir.click(
        traducir_ui,
        inputs=[input_text, src_lang, tgt_lang],
        outputs=output_text
    )

    btn_swap.click(
        intercambiar,
        inputs=[src_lang, tgt_lang, input_text, output_text],
        outputs=[src_lang, tgt_lang, input_text, output_text]
    )

    btn_limpiar.click(
        limpiar_textos,
        inputs=[],
        outputs=[input_text, output_text]
    )


demo.launch(share=True, inbrowser=True)