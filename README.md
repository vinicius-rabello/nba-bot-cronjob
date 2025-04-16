# ⏰ NBA Bot Cronjob

Este repositório contém a rotina automatizada responsável por coletar diariamente os jogos da NBA e armazená-los em uma base de dados PostgreSQL.

## 🧠 Como funciona

- Todos os dias à meia-noite, são feitas requisições à API [nba-bot-api](https://github.com/vinicius-rabello/nba-bot-api) para as seguintes datas:
  - Ontem
  - Hoje
  - Amanhã
- Os dados retornados são gravados em uma instância RDS (Amazon PostgreSQL), mantendo o histórico atualizado e centralizado.

## 🔧 Tecnologias

- Python
- `requests` para comunicação com a API
- `psycopg2` para inserção no PostgreSQL

## 📦 Deploy

Este job roda automaticamente no [Render.com](https://render.com), com agendamento diário via painel.