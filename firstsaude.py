import streamlit as st
from openai import OpenAI
import os

# Configuração da API da OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Interface do FirstSaúde
st.title("🤖 FirstSaúde - Seu Assistente Virtual da Clínica First")

# Entrada do usuário
user_input = st.text_input("Digite sua pergunta aqui:")

# Função para gerar a resposta do FirstSaúde
def gerar_resposta(pergunta):
    try:
        resposta = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": (
                    "Você é um assistente virtual da Clínica First, atuando como uma concierge de um hotel 5 estrelas de São Paulo. "
                    "Sua missão é fornecer informações sobre tratamentos oncológicos, programas da clínica, suporte para pacientes em tratamento, e capturar novos pacientes. "
                    "Mantenha um tom de voz elegante, acolhedor e empático, semelhante ao Dr. Raphael Brandão e Dra. Indianara Brandão. "
                    "Ofereça sempre suporte emocional, reforce a importância da detecção precoce e, se necessário, direcione o paciente para a equipe humana." 
                )},
                {"role": "user", "content": pergunta}
            ]
        )
        return resposta.choices[0].message.content.strip()
    except Exception as e:
        return (
            "Desculpe, não consegui processar sua solicitação no momento. "
            "Por favor, entre em contato conosco pelo WhatsApp (11) 97249-4624 para assistência imediata."
        )

# Exibir a resposta quando o usuário fizer uma pergunta
if user_input:
    resposta = gerar_resposta(user_input)
    st.write(resposta)

# Informações de rodapé
st.markdown(
    """
    ---
    📍 **Endereço da Clínica First:** Rua Domingos de Morais, 2187, Conj. 408, Bloco Paris, Vila Mariana, São Paulo - SP  
    📞 **WhatsApp:** (11) 97249-4624  
    🚀 **Médicos Fundadores:** Dr. Raphael Brandão (Oncologia Clínica) e Dra. Indianara Brandão (Onco-Hematologia e Oncologia Integrativa)  
    *As informações fornecidas aqui são de caráter educacional e não substituem uma consulta médica. Sempre consulte seu médico para decisões de saúde.*
    """
)
