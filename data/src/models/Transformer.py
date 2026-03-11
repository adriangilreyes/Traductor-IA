from transformers import  MarianTokenizer, MarianMTModel 
from langdetect import detect 

#ESPAÑOL - INGLÉS
token_es_en = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-es-en')  
model_es_en = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-es-en')  

#INGLÉS - ESPAÑOL
token_en_es = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-es') 
model_en_es = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-es')  

#ESPAÑOL - ALEMÁN
token_es_de = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-es-de')  
model_es_de = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-es-de')

def traducir(texto,tokenizer,model):
    inputs = tokenizer(texto,return_tensors="pt")
    outputs = model.generate(**inputs,max_new_tokens=100)
    return tokenizer.decode(outputs[0],skip_special_tokens=True)
    
while True:
    text_translate = input('Introduce a text:').strip()

    if text_translate.lower() == 'exit':
        break 

    idioma = detect(text_translate)
    #print(idioma)
 
    match idioma:
        case 'es':
            traduccion = traducir(text_translate,token_es_en,model_es_en)
            print(traduccion)
    

        case 'en':
            traduccion = traducir(text_translate,token_en_es,model_en_es)
            print(traduccion)

        case 'de':
            traduccion = traducir(text_translate, token_es_de, model_es_de) 
            print(traduccion)

        case _:
            print('Idioma no reconocido')  
