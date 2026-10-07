# JARVIS-SecurityAssistant

Assistente IA com foco em segurança cibernética, automação, análise de código e dashboard holográfico.

## Visão geral

Este projeto combina:
- backend em Python com FastAPI
- frontend em React + Vite
- integração com OpenAI/Claude (opcional)
- análise estática de código
- monitoramento de rede em ambiente autorizado
- automação de tarefas internas
- interface visual estilo holograma

## Principais módulos

- IA conversational
- Análise de vulnerabilidades em código
- Verificação básica de serviços e portas
- Dashboard de comandos e eventos
- Logs e auditoria

## Stack

- Python 3.11+
- FastAPI
- Pydantic
- React
- Vite
- CSS moderno

## Como executar

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev -- --host 0.0.0.0
```

### Variáveis de ambiente

Crie um arquivo `.env` no backend com:

```env
OPENAI_API_KEY=your_key_here
MODEL_NAME=gpt-4o-mini
```

> Se a chave não for informada, o sistema usa respostas locais simuladas para funcionar sem cobrança.

## Funcionalidades implementadas neste protótipo

- chat com o assistente
- análise de código em busca de padrões suspeitos
- verificação simples de portas em host informado
- execução de tarefas automatizadas em ambiente controlado
- interface holográfica com painel visual

## Limitações

- Isso é um projeto educacional e ético.
- Não foi pensado para atividade não autorizada.
- Qualquer uso em redes ou sistemas sem permissão é proibido.

## Licença

MIT
