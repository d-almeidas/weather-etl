from extract import extrair_todas
from transform import transformar

def main():
    infos = extrair_todas()
    dados_prontos = transformar(infos)
    print(dados_prontos)

if __name__ == "__main__":
    main()