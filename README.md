# 2° ETAPA PROCESSO ESTÁGIO - b2bflow

A ideia principal aqui é integrar um banco de dados (Supabase) com uma API de WhatsApp (Z-API) usando Python, criando um fluxo automatizado que busca contatos cadastrados e envia uma mensagem personalizada para cada um deles.

---

##  O que foi usado no projeto?

Para construir essa automação, utilizei as seguintes tecnologias:
* **Python 3.13+** como linguagem base do script.
* **Supabase Client** para conectar e puxar os dados direto da tabela de contatos.
* **Requests** para fazer a comunicação HTTP com os endpoints da Z-API.
* **Python-dotenv** para não expor nenhuma senha ou token de forma pública.

---

##  O que a automação faz na prática?

* **Proteção de Credenciais:** O código lê chaves sensíveis através de um arquivo `.env` protegido pelo `.gitignore`. Nada de chaves expostas no código!
* **Busca Otimizada:** O script conecta na tabela `contatos` do Supabase e traz os registros limitados conforme a regra de negócio estabelecida.
* **Mensagem Customizada:** Formatação dinâmica usando a string exata que o desafio pediu: `"Olá, <nome> tudo bem com você?"`.
* **Delay de Segurança (Anti-ban):** Pensando em boas práticas de envio e para evitar bloqueios no WhatsApp, adicionei um intervalo inteligente de 3 segundos entre o disparo de uma mensagem e outra.

---
## PARA RODAR O CODIGO

### 1. Baixa o Arquivo.zip
 [Clique aqui para baixar o projeto em formato ZIP](https://github.com/ygor14444/Repositorio-2-etapa/archive/refs/heads/main.zip)

