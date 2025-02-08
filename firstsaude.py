import streamlit as st
import openai
import os

# Configuração da API da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")  # Substitua pela sua chave de API da OpenAI

# Contexto do assistente
CONTEXT = """
Você é o FirstSaúde, o assistente virtual da Clínica First. 
Explique termos médicos de forma simples e acolhedora.

Se o usuário perguntar sobre "First Member", responda:
"O First Member é um programa exclusivo da Clínica First focado em saúde preventiva e acompanhamento personalizado. Ele inclui check-ups completos, suporte contínuo com nossa equipe médica e benefícios exclusivos para membros."

Se o usuário perguntar sobre "OncoSeek", responda:
"O OncoSeek é um exame avançado oferecido pela Clínica First, voltado para a detecção precoce do câncer, utilizando tecnologias inovadoras para identificar alterações genéticas associadas a diferentes tipos de câncer."
"""

# Interface do FirstSaúde
st.title("🤖 First Saúde - Seu Assistente Virtual")

# Caixa de entrada do usuário
user_input = st.text_input("Digite sua pergunta aqui:")

# Função para gerar a resposta do FirstSaúde
def gerar_resposta(pergunta):
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": CONTEXT},
                {"role": "user", "content": pergunta}
            ],
            max_tokens=150,
            temperature=0.4
        )
        return resposta['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Erro na API da OpenAI: {str(e)}"

# Exibir a resposta quando o usuário fizer uma pergunta
if user_input:
    resposta = gerar_resposta(user_input)
    st.write(resposta)
