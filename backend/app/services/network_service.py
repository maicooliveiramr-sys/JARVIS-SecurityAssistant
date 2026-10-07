import socket


def scan_host(host: str, ports: list[int]):
    results = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((host, port))
                status = "open" if result == 0 else "closed"
            results.append({"port": port, "status": status})
        except Exception as exc:
            results.append({"port": port, "status": "error", "details": str(exc)})

    return {"host": host, "results": results}
