from transformers import pipeline
from langdetect import detect

español_ingles = pipeline("any-to-any",model='Helsinki-NLP/opus-mt-es-en') #ESPAÑOL - INGLÉS
ingles_español = pipeline("any-to-any",model='Helsinki-Nlp/opus-mt-en-es') # INGLÉS - ESPAÑOL

while True:
    text_translate = input('Introduce a text:') 

    if text_translate.lower() == 'exit':
        break 

    idioma = detect(text_translate)

    if idioma == "es":
        traduccion = español_ingles(text_translate)[0]('generated_text')
    
    elif idioma == "en":
        traduccion = ingles_español(text_translate)[0]('generated_text')  