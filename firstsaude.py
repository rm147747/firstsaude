import streamlit as st
import openai

# ATENÇÃO: Não é seguro manter essa chave no código em produção!
openai.api_key = "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"

# Interface do FirstSaúde
st.title("🤖 FirstSaúde - Seu Assistente Virtual da Clínica First")

# Caixa de entrada do usuário
user_input = st.text_input("Digite sua pergunta aqui:")

# Função para gerar a resposta do FirstSaúde
def gerar_resposta(pergunta):
    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é o FirstSaúde, o assistente virtual da Clínica First. Explique termos médicos de forma simples e acolhedora."},
            {"role": "user", "content": pergunta}
        ]
    )
    return resposta['choices'][0]['message']['content'].strip()

# Exibir a resposta quando o usuário fizer uma pergunta
if user_input:
    resposta = gerar_resposta(user_input)
    st.write(resposta)
