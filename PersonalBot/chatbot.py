#Instalando o SDK Google e as bibliotecas numpy e pandas
#pip install google-generativeai
# ... (código anterior)

from flask import jsonify, request
from PersonalBot import app  
import google.generativeai as genai


@app.route("/chatbot", methods=["POST"])
def chatbot():
   input_usuario =request.get_json()
   tipoFisico =request.get_json()
   objetivoTreino= request.get_json()
   resposta = gerar_resposta(input_usuario,tipoFisico,objetivoTreino)
   #print("ChatBot:",resposta,"\n")
   return jsonify({'resposta': resposta})




def gerar_resposta(idade, tipoFisico, objetivoTreino):
   
    #guardando nossa Api Key
    GOOGLE_API_KEY='AIzaSyDe1-sxsVkimF7tPIVjU7DJP6in0RMrl_8'
    genai.configure(api_key=GOOGLE_API_KEY)


    #Configurações da execução  
    generation_config = {
        "candidate_count": 1,
        "temperature" : 0.5,
    }

    safety_settings = {
    "HARASSMENT" : "BLOCK_NONE",
    "HATE" : "BLOCK_NONE",
    "SEXUAL" : "BLOCK_NONE",
    "DANGEROUS" : "BLOCK_NONE",
    }

    #inializando o Modelo com as devidas configurações, antes de executa-lo
    model = genai.GenerativeModel(model_name='gemini-1.0-pro', generation_config=generation_config, safety_settings=safety_settings)


    chat = model.start_chat(history=[])
    
    
    while True:
        texto = f'Haja como um Personal Trainer e Nutricionista, e gere uma rotina semanal de treino e  de dieta para uma pessoa que tenha a idade:{idade} anos, tipo físico: {tipoFisico}  e objetivo de {objetivoTreino} consiga resultados de forma eficiente e consistente'
        
        response = chat.send_message(texto)
        print("ChatBot:",response.text,"\n")
        return response.text
        
