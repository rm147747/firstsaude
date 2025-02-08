import streamlit as st
from openai import OpenAI
import os

# Configuração da API da OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Informações da Clínica First
informacoes_first = """
Detecção Precoce e Oncologia Integrativa Transformando o Cuidado Oncológico

Desde sua fundação em setembro de 2020, a Clínica First tem sido um farol de inovação e esperança para quem busca uma abordagem diferenciada na saúde. Sob a liderança visionária do Dr. Raphael Brandão (Oncologista), da Dra. Indianara Brandão (Onco-Hematologista) e da Dra. Erika Simplício (Oncologista), a First nasceu com uma missão clara: revolucionar o cuidado oncológico, integrando tecnologia de ponta, detecção precoce de tumores e uma abordagem profundamente humanizada.

A First Saúde é mais do que uma clínica; é o encontro perfeito entre ciência avançada e um cuidado profundamente humano. Com expertise em Oncologia Convencional, sustentada pelas melhores práticas científicas, Oncologia Integrativa e Detecção Precoce, transformamos o tratamento oncológico em uma experiência personalizada. Cada paciente é único, e na First Saúde, esse princípio guia tudo o que fazemos. Em pouco tempo, nos tornamos referência nacional, oferecendo não apenas saúde, mas uma nova perspectiva de vida.

Telefone da Clínica First: 011 97249-4624
"""

# Interface do FirstSaúde
st.title("🤖 FirstSaúde - Seu Assistente Virtual da Clínica First")

# Entrada de dados do usuário
user_input = st.text_input("Digite sua pergunta aqui:")

# Função para gerar a resposta do FirstSaúde
def gerar_resposta(pergunta):
    try:
        resposta = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"Você é o FirstSaúde, o assistente virtual da Clínica First. Explique termos médicos de forma simples e acolhedora. As informações mais importantes incluem: {informacoes_first}"},
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

# Disclaimer
st.markdown("""
**Aviso:** As informações fornecidas aqui são de caráter educacional e não substituem uma consulta médica. Sempre consulte seu médico antes de tomar decisões relacionadas à sua saúde. Nós da equipe médica da Clínica First estamos à sua disposição.
""")
