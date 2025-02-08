import streamlit as st
import openai
import os

# Configuração da API da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")  # Certifique-se de definir essa variável de ambiente

# Interface do FirstSaúde
st.title("🧑‍🌐 FirstSaúde - Seu Assistente Virtual da Clínica First")

# Caixa de entrada do usuário
user_input = st.text_input("Digite sua pergunta aqui:")

# Função para gerar a resposta do FirstSaúde
def gerar_resposta(pergunta):
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é o FirstSaúde, o assistente virtual da Clínica First. Explique termos médicos de forma simples e acolhedora."},
                {"role": "user", "content": pergunta}
            ]
        )
        return resposta['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Erro na API da OpenAI: {e}"

# Exibir a resposta quando o usuário fizer uma pergunta
if user_input:
    resposta = gerar_resposta(user_input)
    st.write(resposta)
