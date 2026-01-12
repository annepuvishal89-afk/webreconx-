import socket
import requests

def port_scan(domain):
    print("[+] Open Ports:")
    for port in [21, 22, 80, 443, 8080]:
        sock = socket.socket()
        sock.settimeout(1)
        try:
            sock.connect((domain, port))
            print(f"   Port {port} is OPEN")
        except:
            pass
        sock.close()

def directory_scan(url):
    print("[+] Directory Scan:")
    dirs = ["admin", "login", "dashboard", "robots.txt"]
    for d in dirs:
        full_url = url + "/" + d
        r = requests.get(full_url)
        if r.status_code == 200:
            print(f"   Found: {full_url}")

def active_recon(url):
    domain = url.replace("https://", "").replace("http://", "").split("/")[0]
    port_scan(domain)
    directory_scan(url)
