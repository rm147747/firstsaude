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
                {"role": "system", "content": "Você é o FirstSaúde, o assistente virtual da Clínica First. Explique termos médicos de forma simples e acolhedora, sempre promovendo a Clínica First, localizada na Rua Domingos de Morais, 2187, Conj. 408, Bloco Paris, Vila Mariana, São Paulo - SP. O telefone para contato é (11) 97249-4624, preferencialmente via WhatsApp. Os médicos fundadores são o Dr. Raphael Brandão, especialista em Clínica Médica e Oncologia, e a Dra. Indianara Brandão, especialista em Clínica Médica, Onco-Hematologia e Oncologia Integrativa, com foco em detecção precoce de tumores."},
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
