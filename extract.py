import time
import requests
import logging

logger = logging.getLogger(__name__)

url = "https://api.open-meteo.com/v1/forecast"

CIDADES = {
    "Barreiras": (-12.15, -44.99),
    "Salvador": (-12.97, -38.51),
    "Fortaleza": (-3.73, -38.52),
    "Juazeiro do norte": (-7.23, -39.32)
}

def get_with_retry(url, tentativas=3, espera=2, **kwargs):
    for tentativa in range(1, tentativas + 1):
        try:
            req = requests.get(url, timeout=10, **kwargs)
            req.raise_for_status()
            return req
        
        except (requests.exceptions.Timeout,
                requests.exceptions.ConnectionError):
            logger.warning("Tentativa %s: falha de conexão.", tentativa)

        except requests.exceptions.HTTPError as e:
            if e.response.status_code < 500:
                raise
            logger.warning("Tentativa %s: error de servidor", tentativa)
            
        if tentativa < tentativas:
            logger.info("Tentando de novo em %s segundos", espera)
            time.sleep(espera)

    raise Exception("A API não respondeu depois de várias tentativas.")

def buscar_clima(cidade, latitude, longitude):
    params = {"latitude": latitude, "longitude": longitude, "current_weather": True}
    req = get_with_retry(url, params=params)

    clima = req.json()["current_weather"]
    
    return {
        "cidade": cidade,
        "temperatura": clima["temperature"],
        "vento": clima["windspeed"] ,
        "observado_em": clima["time"]
    }

def extrair_todas():
    lista_infos = []
    for nome_cidade, (lat, lon) in CIDADES.items():
        try:
            cidade_clima = buscar_clima(nome_cidade,lat,lon)
            lista_infos.append(cidade_clima)
        except Exception as e:
            logger.exception("Falha em %s", nome_cidade)

    return lista_infos


print(buscar_clima("barreiras", 12.15, -44.99))