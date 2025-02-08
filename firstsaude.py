import streamlit as st
import openai

# Configuração da API da OpenAI
openai.api_key = "SUA_CHAVE_API_AQUI"  # Substitua pela sua chave de API

# Interface do FirstSaúde
st.title("🤖 FirstSaúde - Seu Assistente Virtual da Clínica First")

# Caixa de entrada do usuário
user_input = st.text_input("Digite sua pergunta aqui:")

# Função para gerar a resposta do FirstSaúde
def gerar_resposta(pergunta):
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é o FirstSaúde, o assistente virtual da Clínica First. Explique termos médicos de forma simples e acolhedora. Responda dúvidas sobre diagnósticos, tratamentos, exames, prevenção de câncer e informações relacionadas à saúde."},
                {"role": "user", "content": pergunta}
            ]
        )
        return resposta.choices[0].message.content.strip()

    except Exception as e:  # Alterado para capturar qualquer exceção genérica
        return f"Erro na API da OpenAI: {str(e)}"

# Exibir a resposta quando o usuário fizer uma pergunta
if user_input:
    resposta = gerar_resposta(user_input)
    st.write(resposta)
