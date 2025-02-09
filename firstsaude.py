import streamlit as st
from openai import OpenAI
import os

# Configuração da API da OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Interface do FirstSaúde
st.title("🤖 First Saúde - Seu Assistente Virtual da Clínica First")

user_input = st.text_input("Digite sua pergunta aqui:")

# Função para gerar a resposta do FirstSaúde
def gerar_resposta(pergunta):
    try:
        resposta = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é o FirstSaúde, o assistente virtual da Clínica First. Responda de forma elegante e acolhedora, fornecendo informações sobre a clínica, seus programas, médicos e serviços. Sempre mantenha um tom educado e polido, semelhante ao de uma concierge de um hotel 5 estrelas em São Paulo."},
                {"role": "user", "content": pergunta}
            ]
        )
        return resposta.choices[0].message.content.strip()
    except Exception as e:
        return f"Erro na API da OpenAI: {str(e)}"

# Exibir a resposta quando o usuário fizer uma pergunta
if user_input:
    resposta = gerar_resposta(user_input)
    if "Raphael Brandão" in user_input:
        resposta = (
            "Que notícia maravilhosa! O Dr. Raphael Brandão ficará honrado em atendê-lo. "
            "Para agendar sua consulta, por gentileza, entre em contato diretamente pelo número de WhatsApp da Clínica First: (11) 97249-4624. "
            "Nossa equipe estará à disposição para orientá-lo da melhor forma possível.\n\n"
            "Será um prazer recebê-lo na Clínica First!"
        )
    st.write(resposta)

