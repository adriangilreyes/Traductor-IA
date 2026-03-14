from transformers import  MarianTokenizer, MarianMTModel 
from langdetect import detect_langs
import os
 
#ESPAÑOL - INGLÉS
token_es_en = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-es-en')  
model_es_en = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-es-en')  

#INGLÉS - ESPAÑOL
token_en_es = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-es') 
model_en_es = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-es')  

#ESPAÑOL - ALEMÁN
token_es_de = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-es-de')
model_es_de = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-es-de')

#ALEMÁN - ESPAÑOL
token_de_es = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-de-es')
model_de_es = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-de-es') 


def traducir(texto,tokenizer,model):
    inputs = tokenizer(texto,return_tensors="pt")
    outputs = model.generate(**inputs,max_new_tokens=100)
    return tokenizer.decode(outputs[0],skip_special_tokens=True)  
    
while True:
    text_translate = input('Introduce a text:').strip() 

    if text_translate.lower() == 'exit':  
        break

    langs = detect_langs(text_translate)
    idioma = langs[0].lang


    short_words = {"hola":"es","hello":"en","hallo":"de"}
    if len(short_words) < 5:
        idioma = short_words.get(text_translate.lower(),None)
    else:
        idioma = detect_langs(text_translate)
 
    match idioma:
        case 'es':
            traduccion = traducir(text_translate,token_es_en,model_es_en) 
            print('Idioma detectado:',idioma)
            print('Traducción:',traduccion)
    

        case 'en':
            traduccion = traducir(text_translate,token_en_es,model_en_es)
            print('Idioma detectado:',idioma)
            print('Traducción:',traduccion)

        case 'de':
            traduccion = traducir(text_translate, token_de_es, model_de_es)
            print('Idioma detectado:',idioma)   
            print('Traducción:',traduccion) 

        case _:
            print('Idioma no reconocido')   