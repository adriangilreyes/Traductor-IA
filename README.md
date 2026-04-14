"# Traductor-IA" 

# 🌍 AI Translator

Automatic translation application using Transformer models + interface in Gradio.

## 🚀 Features
- Multi-language translation
- Graphical interface with Gradio
- Language swapping
- Basic history
- Custom UI with CSS
## 🛠 Tech
- Python
- HuggingFace Transformers
- Gradio

## Models
This is a pre-trained Transformer model called "MarianMTModel," which, together with the UI, creates a stable and scalable translator.
We have primarily chosen three dominant languages: German, English, and French.
## Documentation

Documentation MarianMTModel : https://huggingface.co/docs/transformers/model_doc/marian

Model Trasformer : https://www.ibm.com/es-es/think/topics/transformer-model

UI : https://www.gradio.app/ 


## Add new language
To add any language, we'll need to create a new model along with its token. We create a new case with the added language in the file (Transformer.py). Finally, in app.py, we add a new elif statement with the Helsinki model and its token, where we specify the input and output of the language.


## Improvements
* You can add as many languages ​​as you want. A future improvement would be a language interpreter, eliminating the need to add a new model and token for each language.

*Important --> Import the Transformer models created in Transformer.py into app.py
## Translations

                            -- ESPAÑOL - INGLÉS --


 ![SpainGIF](https://github.com/user-attachments/assets/24df3e5b-c6d5-4396-9582-830b4792255e)


 
![UnitedKingdomFlagGIF](https://github.com/user-attachments/assets/4f7c2ea7-6d74-4f57-bf1a-91c9b5965231)



                              -- INGLÉS - ESPAÑOL --


![UnitedKingdomFlagGIF](https://github.com/user-attachments/assets/4f7c2ea7-6d74-4f57-bf1a-91c9b5965231)







![SpainGIF](https://github.com/user-attachments/assets/24df3e5b-c6d5-4396-9582-830b4792255e)


                                     
                                   --ESPAÑOL - ALEMÁN--


![SpainGIF](https://github.com/user-attachments/assets/24df3e5b-c6d5-4396-9582-830b4792255e)








![GermanyFlagGIF](https://github.com/user-attachments/assets/70c596e7-bf1c-4c1c-b6b7-f042a3aa290e)

 







                                        --ALEMÁN - ESPAÑOL--




![GermanyFlagGIF](https://github.com/user-attachments/assets/70c596e7-bf1c-4c1c-b6b7-f042a3aa290e)










![SpainGIF](https://github.com/user-attachments/assets/24df3e5b-c6d5-4396-9582-830b4792255e)

  

                                          --ESPAÑOL - FRANCÉS--


![SpainGIF](https://github.com/user-attachments/assets/24df3e5b-c6d5-4396-9582-830b4792255e)









![FranceFlagGifGIF](https://github.com/user-attachments/assets/82622fa0-88c1-4ae4-b73d-e8ed69cd3a5a)





                                          --FRANCÉS - ESPAÑOL--


![FranceFlagGifGIF](https://github.com/user-attachments/assets/82622fa0-88c1-4ae4-b73d-e8ed69cd3a5a)














![SpainGIF](https://github.com/user-attachments/assets/24df3e5b-c6d5-4396-9582-830b4792255e)








## test the model
cd traductor_ia

cd data

cd src

cd models

## Run the Model (app.py)
1st) Recommended option (contains the main function)
python app.py

## Run locally
 Running on local URL:  http://127.0.0.1:7860
 
