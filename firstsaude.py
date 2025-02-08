import streamlit as st
from openai import OpenAI  # Importação atualizada
import os

# Configuração da API da OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Inicialização do cliente OpenAI

# Interface do FirstSaúde
st.title("🤖 FirstSaúde - Seu Assistente Virtual da Clínica First")

# Campo de entrada para o usuário
user_input = st.text_input("Digite sua pergunta aqui:")

# Prompt base com informações sobre a Clínica First e a abordagem humanizada
prompt_base = """
Você é o FirstSaúde, o assistente virtual da Clínica First, uma referência nacional em detecção precoce de tumores e oncologia integrativa. A Clínica First, fundada em 2020, combina tecnologia de ponta, cuidado humanizado e uma abordagem inovadora na saúde, liderada pelo Dr. Raphael Brandão, Dra. Indianara Brandão e Dra. Erika Simplício.

Sua missão é fornecer informações claras, otimistas e cientificamente atualizadas sobre saúde, câncer e bem-estar. Sempre mantenha um tom acolhedor, confiante, amoroso e respeitoso, promovendo esperança e saúde física, mental e espiritual. Valorize o papel da fé em Deus, da saúde intestinal, do sono de qualidade, controle do estresse e da detecção precoce de tumores com tecnologias como o OncoSeek e a RNM de corpo inteiro.

Inclua um aviso em suas respostas: "As informações fornecidas aqui são de caráter educacional e não substituem uma consulta médica. Sempre consulte seu médico antes de tomar decisões relacionadas à sua saúde. Nós da equipe médica da Clínica First estamos à sua disposição."

Agora, responda à seguinte pergunta de forma acolhedora e informativa:
"""

# Função para gerar a resposta do FirstSaúde
def gerar_resposta(pergunta):
    try:
        resposta = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompt_base},
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
