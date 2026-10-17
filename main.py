from extract import extrair_todas
from transform import transformar
from load import carregar_dados

def main():
    infos = extrair_todas()
    dados_prontos = transformar(infos)
    total = carregar_dados(dados_prontos)
    print(f"{total} linhas inseridas.")
    

if __name__ == "__main__":
    main()