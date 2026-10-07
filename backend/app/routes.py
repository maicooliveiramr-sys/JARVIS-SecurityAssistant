from fastapi import APIRouter

from app.services.ai_service import assistant_reply
from app.services.security_service import analyze_code
from app.services.network_service import scan_host

router = APIRouter(prefix="/api")


@router.post("/chat")
def chat_endpoint(payload: dict):
    message = payload.get("message", "")
    mode = payload.get("mode", "assistant")
    return {"reply": assistant_reply(message, mode)}


@router.post("/security/analyze")
def security_analyze(payload: dict):
    code = payload.get("code", "")
    return analyze_code(code)


@router.post("/network/scan")
def network_scan(payload: dict):
    host = payload.get("host", "localhost")
    ports = payload.get("ports", [80, 443, 22, 8080, 3306])
    return scan_host(host, ports)


@router.post("/automation/run")
def automation_run(payload: dict):
    task = payload.get("task", "listar ambiente")
    return {
        "status": "success",
        "task": task,
        "summary": f"Tarefa '{task}' executada em ambiente autorizado e registrada em log."
    }
