import requests
import socket
import threading

results = []

# -----------------------------
# Port Scanner (Threaded)
# -----------------------------
def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))
    
    if result == 0:
        results.append(f"[OPEN] Port {port}")
    
    s.close()


def scan_ports(target):
    ports = [21, 22, 23, 25, 80, 443]
    threads = []

    for port in ports:
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


# -----------------------------
# Headers Check
# -----------------------------
def check_headers(url):
    try:
        response = requests.get(url, timeout=3)
        headers = response.headers

        security_headers = [
            "Content-Security-Policy",
            "X-Frame-Options",
            "Strict-Transport-Security"
        ]

        for header in security_headers:
            if header in headers:
                results.append(f"[OK] {header} found")
            else:
                results.append(f"[MISSING] {header}")

    except:
        results.append("[ERROR] Header check failed")


# -----------------------------
# SQL Injection
# -----------------------------
def test_sql(url):
    payload = "' OR '1'='1"
    try:
        res = requests.get(url + "?id=" + payload, timeout=3)
        if any(err in res.text.lower() for err in ["sql", "mysql", "syntax"]):
            results.append("[VULNERABLE] SQL Injection")
        else:
            results.append("[SAFE] SQL Injection")
    except:
        results.append("[ERROR] SQL test failed")


# -----------------------------
# XSS
# -----------------------------
def test_xss(url):
    payload = "<script>alert('XSS')</script>"
    try:
        res = requests.get(url + "?q=" + payload, timeout=3)
        if payload in res.text:
            results.append("[VULNERABLE] XSS")
        else:
            results.append("[SAFE] XSS")
    except:
        results.append("[ERROR] XSS test failed")


# -----------------------------
# Run Full Scan
# -----------------------------
def run_scan(target):
    results.clear()
    url = "http://" + target

    threads = [
        threading.Thread(target=scan_ports, args=(target,)),
        threading.Thread(target=check_headers, args=(url,)),
        threading.Thread(target=test_sql, args=(url,)),
        threading.Thread(target=test_xss, args=(url,))
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    return results