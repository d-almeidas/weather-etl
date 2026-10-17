from extract import extrair_todas
from datetime import datetime

def transformar(dados):
    resultado = []
    agora = datetime.now().isoformat()

    for itens in dados:
        if itens["temperatura"] > 60 or itens["temperatura"] < -50:
            print(f"Descartado: {itens['cidade']} com temperatura fora do intervalo ({itens['temperatura']})")
            continue
        resultado.append ({
        "cidade": itens["cidade"],
        "temperatura": round(itens["temperatura"], 1),
        "vento": round(itens["vento"], 1),
        "dthora_coleta": agora
        })
    return resultado
