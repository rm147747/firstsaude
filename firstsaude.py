import streamlit as st
import openai

# Configuração da API da OpenAI
openai.api_key = "OPENAI_API_KEY"  # Substitua com sua chave da API da OpenAI

# Interface do FirstSaúde
st.title("🤖 FirstSaúde - Seu Assistente Virtual da Clínica First")

# Caixa de entrada do usuário
user_input = st.text_input("Digite sua pergunta aqui:")

# Função para gerar a resposta do FirstSaúde
def gerar_resposta(pergunta):
    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é o FirstSaúde, o assistente virtual da Clínica First. Explique termos médicos de forma simples e acolhedora. Responda dúvidas sobre diagnósticos, tratamentos, exames, prevenção de câncer, oncologia, hematologia, clínica médica e medicina interna. Se não souber a resposta, oriente o paciente a buscar a equipe da clínica."},
            {"role": "user", "content": pergunta}
        ],
        max_tokens=150,
        temperature=0.4
    )
    return resposta.choices[0]["message"]["content"].strip()

# Exibir a resposta quando o usuário fizer uma pergunta
if user_input:
    resposta = gerar_resposta(user_input)
    st.write(resposta)

