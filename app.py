# ======================================== #
# Lógica de Programação do LS English - AI Teacher
# ======================================== #

#Importe de bibliotecas necessárias
import os
import openai
import streamlit as st
from dotenv import load_dotenv
from openai.error import RateLimitError, InvalidRequestError, AuthenticationError, APIConnectionError

#Carrega variaveis do arquivo .env
load_dotenv()

#Configuração da API KEY
openai.api_key = os.getenv("OPENAI_KEY")


# ======================================== #
# Prompt fixo (System Prompt) com as instruções para o modelo
# ======================================== #
system_prompt = """
Você é um professor de inglês virtual, paciente, didático e extremamente competente. Seu objetivo é ajudar o aluno a aprender inglês de forma eficaz, respeitando o nível de conhecimento atual do aluno.

Regras de conduta:
- Sempre utilize uma linguagem clara e objetiva.
- Adapte a complexidade do vocabulário e explicações com base no nível de inglês informado pelo aluno (iniciante, intermediário, avançado).
- Quando for solicitado, corrija erros de forma respeitosa e sempre explique o motivo da correção.
- Sempre incentive o aluno a tentar, mesmo que ele erre.
- Use exemplos práticos, comparações, analogias e explicações culturais sempre que possível.
- Nunca assuma que o aluno sabe o significado de palavras difíceis: ofereça uma tradução e um exemplo em inglês e português.
- Corrija pronúncia, gramática, vocabulário, escrita e compreensão auditiva, conforme o contexto da interação.
- Quando apropriado, ofereça pequenos exercícios interativos, como: Tradução de frases, Completar lacunas, Escolha múltipla, Pequenos diálogos.
- Ao apresentar novas palavras ou expressões, sempre explique: Significado, Uso no contexto, Exemplo em frase, Tradução da frase.

Instruções adicionais:
- Sempre peça confirmação se o aluno compreendeu.
- Utilize emojis moderadamente para tornar a aula mais leve e amigável.
- Mantenha a interação fluida como se fosse uma conversa real com um professor humano.
- Jamais critique negativamente o aluno. Sempre incentive o progresso.
"""

# ======================================== #
# Inicializa o histórico da conversa na sessão do Streamlit
# ======================================== #
if "mensagem" not in st.session_state:
    st.session_state.mensagem = [
        {"role": "system", "content": system_prompt}
    ]

#Inicialização do nível com state controlado
if "nivel" not in st.session_state:
    st.session_state.nivel = "Iniciante"

# ======================================== #
# Layout e estilização da página (frontend)
# ======================================== #
st.set_page_config(layout="centered", page_title="LS English - AI Teacher")

#Estilo com melhor aparência (CSS)
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    background-color: #0A192F;
    color: #FFFFFF;
}
.stTextInput input {
    border-radius: 10px;
    padding: 10px;
    background-color: #ffffff12;
    color: #000000;
}
.stTextInput label, .stRadio label, label, legend {
    color: #FFFFFF !important;
}
.stRadio label span {
    color: #FFFFFF !important;
}
.stButton button {
    background-color: #4CAF50;
    color: #FAF9F6;
    padding: 10px 24px;
    border-radius: 10px;
    border: none;
    font-size: 16px;
    transition: 0.3s;
}
.stButton button:hover {
    background-color: #45a049;
}
.stRadio div {
    display: flex;
    justify-content: center;
    gap: 20px;
}
</style>
""", unsafe_allow_html=True)

#Centralizar logo
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("lsenglish.png", width=300)

#Titulo com estilo cennralizado
st.markdown("<h1 style='text-align: center;'>LS English - AI Teacher </h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Seu professor de inglês com inteligência artificial</h4>", unsafe_allow_html=True)


# ======================================== #
# Seleção de nível de inglês (armazenado na sessão)
# ======================================== #
nivel_selecionado = st.radio(
    "Selecione o seu nível de inglês:",
    ("Iniciante", "Intermediário", "Avançado"),
    index=("Iniciante", "Intermediário", "Avançado").index(st.session_state.nivel),
    horizontal=True,
    key="nivel"
)

st.write(f"Nível selecionado: **{st.session_state.nivel}**")

# ======================================== #
# Campo de entrada de perguntas do usuário
# ======================================== #
entrada = st.text_input("Digite sua pergunta, dúvida ou tema que deseja estudar:")

# ======================================== #
# Função de interação com a API do ChatGPT com tratamento de erros
# ======================================== #
def chatgpt():
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.mensagem,
            max_tokens=500,
            temperature=0.7,
        )
        return resposta.choices[0].message['content']

    #Todos os tratamentos de erro
    except RateLimitError:
        return "Limite de uso atingido na sua conta da OpenAI"

    except InvalidRequestError:
        return "Sua conta não possui billing ativo."

    except AuthenticationError:
        return "Problema na autenticação da API Key"

    except APIConnectionError:
        return "Falha de conexão com a API da OpenAI. Tente novamente mais tarde"

    except Exception as e:
        return f"Erro inesperado: {str(e)}"


# ======================================== #
# Quando o usuário clica no botão "Enviar"
# ======================================== #
if st.button("Enviar"):
    if entrada.strip() == "":
        st.warning("Please, digite sua pergunta!")
    else:
        if len(st.session_state.mensagem) == 1:
            info_nivel = f"O aluno possui conhecimento nível {st.session_state.nivel.lower()}."
            st.session_state.mensagem.append({"role": "user", "content": info_nivel + " " + entrada})
        else:
            st.session_state.mensagem.append({"role": "user", "content": entrada})

        resposta = chatgpt()
        st.session_state.mensagem.append({"role": "assistant", "content": resposta})

# ======================================== #
# Exibir histórico da conversa na tela
# ======================================== #
for mensagens in st.session_state.mensagem[1:]:
    if mensagens["role"] == "user":
        st.markdown(f"**Aluno:** {mensagens['content']}")
    else:
        st.markdown(f"**Professor:** {mensagens['content']}")
