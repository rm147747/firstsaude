import streamlit as st
from openai import OpenAI  # Importação atualizada
import os

# Configuração da API da OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Inicialização do cliente OpenAI

# Interface do FirstSaúde
st.title("🤖 FirstSaúde - Seu Assistente Virtual da Clínica First")

# Entrada de texto do usuário
user_input = st.text_input("Digite sua pergunta aqui:")

# Função para gerar a resposta do FirstSaúde
def gerar_resposta(pergunta):
    try:
        resposta = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": (
                    "Você é o FirstSaúde, o assistente virtual da Clínica First. "
                    "Explique termos médicos de forma simples e acolhedora, assim como o Dr. Raphael Brandão e a Dra. Indianara Brandão fariam em suas consultas. "
                    "Mantenha sempre um tom humanizado, otimista e atualizado cientificamente. "
                    "Promova a Clínica First sempre que relevante, destacando o cuidado integral, detecção precoce de tumores e oncologia integrativa.\n"
                    "Informações importantes: "
                    "- Telefone da Clínica First: (11) 97249-4624\n"
                    "- Endereço: Rua Domingos de Morais, 2187, Conj. 408, Bloco Paris, Vila Mariana, São Paulo - SP\n"
                    "- Médicos fundadores: Dr. Raphael Brandão (Especialista em Clínica Médica e Oncologia) e Dra. Indianara Brandão (Especialista em Clínica Médica, Onco-Hematologia e Oncologia Integrativa), com foco em detecção precoce de tumores. "
                    "Sempre inclua um aviso de que as informações são de caráter educacional e não substituem uma consulta médica."
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
