from openai import OpenAI  # Corrigido para importar a OpenAI corretamente
import streamlit as st  # Corrigido para importar o Streamlit corretamente

# Inicializa o cliente OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])  # Corrigido para usar a chave da API corretamente

def gerar_resposta(prompt):
    # Faz a chamada à API da OpenAI
    response = client.chat.completions.create(
        model="gpt-4",  # Modelo que você deseja usar
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content  # Retorna a resposta gerada

# Interface do Streamlit
st.title("FirstSaddle - Seu Assistente Virtual")  # Título da aplicação
user_input = st.text_input("Digite sua pergunta aqui:")  # Campo de entrada de texto

if user_input:
    resposta = gerar_resposta(user_input)  # Gera a resposta com base na entrada do usuário
    st.write(resposta)  # Exibe a resposta na interface
