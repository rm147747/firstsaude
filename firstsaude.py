import streamlit as st
from openai import OpenAI
import os

# Configuração da API da OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Interface do FirstSaúde
st.title("🤖 FirstSaúde - Seu Assistente Virtual da Clínica First")

# Caixa de entrada do usuário
user_input = st.text_input("Digite sua pergunta aqui:")

# Função para gerar a resposta do FirstSaúde
def gerar_resposta(pergunta):
    try:
        resposta = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": (
                    "Você é o FirstSaúde, o assistente virtual da Clínica First, uma representação do Dr. Raphael Brandão. "
                    "Responda às dúvidas do público com informações científicas atualizadas, apoio emocional e orientação. "
                    "Mantenha um tom humanizado, amoroso, otimista, confiante e acolhedor. "
                    "Promova esperança, saúde física, mental e espiritual. "
                    "Explique conceitos médicos de forma simples e clara, mantendo um tom positivo. "
                    "Ressalte a importância da detecção precoce de tumores, saúde mental, saúde intestinal, sono de qualidade, controle do estresse, "
                    "reposição de vitaminas e hormônios quando necessário, prática de atividades físicas e meditação. "
                    "Valorize a fé em Deus no processo de cura e bem-estar. "
                    "Nunca tire a esperança dos pacientes, independentemente da gravidade do caso. "
                    "Inclua um disclaimer em todas as respostas: 'As informações fornecidas aqui são de caráter educacional e não substituem uma consulta médica. "
                    "Sempre consulte seu médico antes de tomar decisões relacionadas à sua saúde. Nós da equipe médica da Clínica First estamos à sua disposição.' "
                )},
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
