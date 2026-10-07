def assistant_reply(message: str, mode: str = "assistant") -> str:
    if not message or not message.strip():
        return "Preciso de uma mensagem válida para processar."

    lower = message.lower()

    if "segurança" in lower or "vulnerabilidade" in lower:
        return "Posso ajudar com análise de segurança, revisão de código e recomendações éticas para hardening."

    if "rede" in lower or "network" in lower:
        return "Estou pronto para verificar serviços de rede em ambientes autorizados e resumir riscos operacionais."

    if "automação" in lower:
        return "Posso montar scripts e workflows de automação para tarefas internas de segurança e produtividade."

    if "jarvis" in lower:
        return "Sistema JARVIS online. Módulos ativos: IA, monitoramento, automação e análise de segurança."

    if mode == "security":
        return "Análise de segurança ativada. Posso revisar código, apontar riscos e sugerir hardening."

    return (
        f"Mensagem recebida: '{message}'. "
        "Estou operando como assistente cibernético com foco em segurança, automação e produtividade."
    )
