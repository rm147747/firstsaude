from openai import OpenAI
import streamlit as st

# Inicializa o cliente OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def gerar_resposta(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Interface do Streamlit
st.title("FirstSaddle - Seu Assistente Virtual")
user_input = st.text_input("Digite sua pergunta aqui:")

if user_input:
    resposta = gerar_resposta(user_input)
    st.write(resposta)
