===================================================

# **LS English - AI Teacher**


Descrição do Projeto:
----------------------
O LS English - AI Teacher é um sistema inteligente de ensino de inglês com suporte à conversação, histórico de chat, personalização de nível de aprendizado e integração com a API da OpenAI (gpt-3.5-turbo). 

Este projeto foi desenvolvido utilizando:
- Python 3.11+
- Streamlit (frontend web)
- OpenAI (IA)
- dotenv (gerenciamento de variáveis)
- Session State do Streamlit (histórico de conversa)

---------------------------------------------------
FUNCIONAMENTO DO SISTEMA
---------------------------------------------------

Fluxo do Usuário:
-------------------
1. O usuário acessa a interface web.
2. Seleciona seu nível de inglês (iniciante, intermediário, avançado).
3. Digita qualquer pergunta ou tema.
4. Recebe uma resposta personalizada e didática.
5. A conversa completa fica registrada durante a sessão.

Fluxo do Código:
-------------------
- A IA utiliza o modelo gpt-3.5-turbo.
- O histórico da conversa é mantido em memória com st.session_state.
- Toda nova pergunta é enviada junto com o histórico acumulado.
- Um system_prompt organiza o comportamento pedagógico do "professor IA".

Principais Arquivos:
---------------------
- app.py: código principal.
- .env: contém sua chave da API da OpenAI.
- requirements.txt: contém dependências necessárias 
- lsenglish.png: logo do projeto.


---------------------------------------------------
INSTRUÇÕES DE INSTALAÇÃO E EXECUÇÃO
---------------------------------------------------

Pré-requisitos:
-----------------
- Python 3.11+
- Conta na OpenAI com API Key
- Ambiente virtual recomendado

Passo a passo:
---------------
1. (Opcional) Clonar o repositório:
    git clone https://github.com/seu-usuario/ls-english-ai-teacher.git
    cd ls-english-ai-teacher

2. Criar ambiente virtual:
    python -m venv venv

3. Ativar o ambiente virtual:
    - Windows: venv\Scripts\activate
    - Linux/Mac: source venv/bin/activate

4. Instalar as dependências:
    pip install -r requirements.txt

5. Criar o arquivo .env com sua chave OpenAI:
    OPENAI_KEY=sua-chave-aqui

6. Rodar o sistema:
    streamlit run app.py

O sistema abrirá em: http://localhost:8501

---------------------------------------------------
INTERAÇÃO DO USUÁRIO
---------------------------------------------------

O usuário interage diretamente pela interface web:
- Seleciona o nível de inglês.
- Faz perguntas sobre gramática, vocabulário, expressões, traduções, etc.
- Recebe respostas didáticas baseadas em IA com correção e exemplos.
- Todo o histórico de conversa permanece na tela.

---------------------------------------------------
CUSTO DO USO DA API OPENAI
---------------------------------------------------

Modelo utilizado: gpt-3.5-turbo

- Input (prompt enviado): $0.0005 por 1.000 tokens
- Output (resposta recebida): $0.0015 por 1.000 tokens

Exemplo de custo:
- Se uma interação consome 1.000 tokens (pergunta + resposta), o custo total será aproximadamente $0.00065.

Cotação oficial: https://openai.com/pricing

---------------------------------------------------
CONTROLE DE ERROS
---------------------------------------------------

O sistema possui tratamento para:
- API Key inválida
- Billing inativo
- Limite de quota excedido
- Problemas de conexão

Obs: Caso o Limite da sua conta seja atingido, o sistema informará com uma mensagem de aviso

---------------------------------------------------
POSSÍVEIS EVOLUÇÕES FUTURAS
---------------------------------------------------

- Deploy SaaS com múltiplos usuários.
- Controle de consumo e planos pagos.
- Registro de histórico completo entre sessões.
- Modo de aula interativo com exercícios.
- Painel administrativo de acompanhamento.

---------------------------------------------------
DESENVOLVEDOR
---------------------------------------------------
**LS English - AI Teacher** 

Projeto criado e desenvolvido por **Lucas Gabriel de O. Silva**

Email para contato: lucasgsilva520@gmail.com


===================================================