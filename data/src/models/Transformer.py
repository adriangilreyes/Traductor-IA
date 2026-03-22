from transformers import MarianTokenizer, MarianMTModel
from langdetect import detect_langs, DetectorFactory


# 🔹 Configuración reproducible de langdetect
DetectorFactory.seed = 0 

# 🔹 Carga de modelos

# Español → Inglés
token_es_en = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-es-en')
model_es_en = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-es-en')

# Inglés → Español
token_en_es = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-es')
model_en_es = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-es')

# Español → Alemán
token_es_de = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-es-de')
model_es_de = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-es-de')

# Alemán → Español
token_de_es = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-de-es')
model_de_es = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-de-es')

#Español → Francés
token_es_fr = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-es-fr')
model_es_fr = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-es-fr')
 
#Francés → Español
token_fr_es = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-fr-es')
model_fr_es = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-fr-es')

# 🔹 Función de traducción
def traducir_texto(texto, tokenizer, model):
    inputs = tokenizer(texto, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


# 🔹 Diccionario para palabras cortas
short_words = {"hola": "es", "hello": "en", "hallo": "de", "adiós": "es", "bye": "en", "bonjour":"fr"}

# 🔹 Función para detectar idioma
def detectar_idioma(texto):
    texto = texto.strip()
    
    # Palabras cortas o frases de 1-2 palabras
    if len(texto.split()) <= 2:
        idioma = short_words.get(texto.lower(), None)
    else:
    # Frases más largas: usar langdetect
        try:
            idioma = detect_langs(texto)
            if not idioma:
                return None
            return idioma[0].lang
        except:
            return None

 
# 🔹 Bucle principal
while True:
    text_translate = input('Introduce a text:').strip() 
    
    if text_translate.lower() == 'exit':
        break

    idioma = detectar_idioma(text_translate)

    match idioma:
        case 'es':
            traduccion = traducir_texto(text_translate, token_es_en, model_es_en)
        case 'en':
            traduccion = traducir_texto(text_translate, token_en_es, model_en_es)
        case 'de':
            traduccion = traducir_texto(text_translate, token_de_es, model_de_es)
        case 'fr':
            traduccion = traducir_texto(text_translate, token_fr_es, model_fr_es)
        case _:
            print('Idioma no "RECONOCIDO POR EL SISTEMA"') 
            continue

    print('Idioma detectado:', idioma)
    print('Traducción:', traduccion)