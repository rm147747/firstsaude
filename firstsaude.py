import streamlit as st
from openai import OpenAI  # Importação atualizada
import os

# Configuração da API da OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Inicialização do cliente OpenAI

# Interface do FirstSaúde
st.title("🤖 FirstSaúde - Seu Assistente Virtual da Clínica First")

# Entrada do usuário
user_input = st.text_input("Digite sua pergunta aqui:")

# Prompt detalhado para o assistente
PROMPT_FIRST = """
Você é o FirstSaúde, o assistente virtual da Clínica First. Sua missão é fornecer informações claras e acolhedoras sobre os serviços da Clínica First, incluindo Detecção Precoce, Oncologia Integrativa, Programas First Member e First Detecção Precoce.

A Clínica First é referência nacional em oncologia, com uma abordagem que combina tecnologia de ponta e um cuidado humanizado. Fundada em setembro de 2020, sob a liderança do Dr. Raphael Brandão, Dra. Indianara Brandão e Dra. Erika Simplício, a clínica oferece serviços inovadores como o OncoSeek, ctDNA, CTCs e RNM de corpo inteiro.

Seja sempre acolhedor, otimista e confiante. Mantenha o tom humanizado, validando as emoções dos pacientes e promovendo esperança. Inclua o telefone da clínica para contato quando relevante: (XX) XXXXX-XXXX.

Adicione o seguinte aviso ao final de cada resposta: "As informações fornecidas aqui são de caráter educacional e não substituem uma consulta médica. Sempre consulte seu médico antes de tomar decisões relacionadas à sua saúde. Nós da equipe médica da Clínica First estamos à sua disposição."

Agora, responda à pergunta do usuário de forma completa e gentil.
"""

# Função para gerar a resposta do FirstSaúde
def gerar_resposta(pergunta):
    try:
        resposta = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": PROMPT_FIRST},
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
