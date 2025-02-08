import streamlit as st
import openai

# Configuração da API da OpenAI usando segredo do Streamlit
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Interface do FirstSaúde
st.title("🤖 FirstSaúde - Seu Assistente Virtual da Clínica First")

# Caixa de entrada do usuário
user_input = st.text_input("Digite sua pergunta aqui:")

# Função para gerar a resposta do FirstSaúde
def gerar_resposta(pergunta):
    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é o FirstSaúde, o assistente virtual da Clínica First. Explique termos médicos de forma simples e acolhedora. Responda dúvidas sobre diagnósticos, tratamentos e prevenção."},
            {"role": "user", "content": pergunta}
        ],
        max_tokens=150,
        temperature=0.4
    )
    return resposta.choices[0].message["content"].strip()

# Exibir a resposta quando o usuário fizer uma pergunta
if user_input:
    resposta = gerar_resposta(user_input)
    st.write(resposta)
