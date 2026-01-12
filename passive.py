import socket
import whois
import dns.resolver
import requests
import ssl

def passive_recon(url):
    domain = url.replace("https://", "").replace("http://", "").split("/")[0]

    # IP Address
    ip = socket.gethostbyname(domain)
    print(f"[+] IP Address: {ip}")

    # WHOIS Info
    try:
        w = whois.whois(domain)
        print(f"[+] Registrar: {w.registrar}")
        print(f"[+] Creation Date: {w.creation_date}")
    except:
        print("[-] WHOIS lookup failed")

    # DNS Records
    try:
        print("[+] DNS Records:")
        for rdata in dns.resolver.resolve(domain, 'A'):
            print("   A Record:", rdata)
    except:
        print("[-] DNS lookup failed")

    # HTTP Headers
    try:
        response = requests.get(url, timeout=5)
        print("[+] HTTP Headers:")
        for header in response.headers:
            print(f"   {header}: {response.headers[header]}")
    except:
        print("[-] Header extraction failed")
