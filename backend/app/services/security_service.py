import re


RISK_PATTERNS = {
    "exec": ["exec(", "eval(", "os.system(", "subprocess.run("],
    "command_injection": ["shell=True", "popen(", "bash -c", "cmd.exe /c"],
    "hardcoded_secret": ["password =", "api_key =", "secret =", "token ="],
    "sql_injection": ["SELECT", "INSERT", "UPDATE", "DELETE"],
    "unsafe_deserialization": ["pickle.load", "yaml.load", "marshal.load"],
}


def analyze_code(code: str) -> dict:
    findings = []
    code_clean = code or ""

    for category, patterns in RISK_PATTERNS.items():
        matches = []
        for pattern in patterns:
            if pattern in code_clean:
                matches.append(pattern)

        if matches:
            findings.append({
                "category": category,
                "severity": "medium" if category in ["exec", "command_injection"] else "low",
                "matches": matches,
                "note": "Padrão detectado em código de aplicação. Revisar e compensar com validações e controles."
            })

    return {
        "status": "ok",
        "summary": "Análise concluída." if findings else "Nenhum risco crítico identificado na revisão superficial.",
        "findings": findings,
    }
