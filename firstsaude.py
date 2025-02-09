import streamlit as st
from openai import OpenAI
import os

# Configuração da API da OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Interface do FirstSaúde
st.title("🤖 FirstSaúde - Seu Assistente Virtual da Clínica First")

user_input = st.text_input("Digite sua pergunta aqui:")

# Função para gerar a resposta do FirstSaúde
def gerar_resposta(pergunta):
    try:
        resposta = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é o FirstSaúde, o assistente virtual da Clínica First. Sua missão é fornecer informações sobre tratamentos, captar novos pacientes, oferecer suporte a pacientes em tratamento, responder dúvidas sobre a Clínica First, seus programas e médicos. O tom deve ser polido, elegante, acolhedor e semelhante ao de uma concierge de um hotel 5 estrelas de São Paulo. Sempre que possível, mencione o Dr. Raphael Brandão, Dra. Indianara Brandão e Dra. Erika Simplício. Caso não saiba a resposta, oriente o usuário a entrar em contato pelo WhatsApp da Clínica First: (11) 97249-4624."},
                {"role": "user", "content": pergunta}
            ]
        )
        return resposta.choices[0].message.content.strip()
    except Exception as e:
        return f"Erro na API da OpenAI: {str(e)}"

# Exibir a resposta quando o usuário fizer uma pergunta
if user_input:
    resposta = gerar_resposta(user_input)
    st.write(resposta)

