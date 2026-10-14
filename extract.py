import time
import requests

CIDADES = {
    "Barreiras": (-12.15, -44.99),
    "Salvador": (-12.97, -38.51),
    "Fortaleza": (-3.73, -38.52),
}

def get_with_retry(tentativas=3, espera=2, **kwargs):
    for tentativa in range(1, tentativas + 1):
        try:
            req = requests.get(timeout=10, **kwargs)
            req.raise_for_status()
            return req
        
        except (requests.exceptions.Timeout,
                requests.exceptions.ConnectionError):
            print(f"Tentativa {tentativa}: falha de conexão.")

        except requests.exceptions.HTTPError as e:
            if e.response.status_code < 500:
                raise
            print(f"Tentativa {tentativa}: erro do servidor ({e.response.status_code}).")
            
        if tentativa <= tentativas:
            print('Testando...')
            time.sleep(espera)
            tentativa += 1
            continue

def buscar_clima(cidade, latitude, longitude):
    