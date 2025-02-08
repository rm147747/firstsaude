import streamlit as st
import openai

# Configuração da API da OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"]  # Usando segredo do Streamlit

# Interface do FirstSaúde
st.title("🤖 First Saúde - Seu Assistente Virtual da Clínica First")

# Caixa de entrada do usuário
user_input = st.text_input("Digite sua pergunta aqui:")

# Função para gerar a resposta do FirstSaúde
def gerar_resposta(pergunta):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Você é o FirstSaúde, o assistente virtual da Clínica First. Explique termos médicos de forma simples e acolhedora. Responda dúvidas sobre diagnósticos, tratamentos e prevenção.\n\nPergunta: {pergunta}\nResposta:",
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:  # Alterado para capturar qualquer exceção genérica
        return f"Erro na API da OpenAI: {str(e)}"

# Exibir a resposta quando o usuário fizer uma pergunta
if user_input:
    resposta = gerar_resposta(user_input)
    st.write(resposta)
