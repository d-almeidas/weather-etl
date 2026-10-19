from extract import extrair_todas
from transform import transformar
from load import carregar_dados
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)

def main():
    infos = extrair_todas()
    dados_prontos = transformar(infos)
    total = carregar_dados(dados_prontos)
    logger.info("Rodada finalizada: %s linhas inseridas.", total)
    

if __name__ == "__main__":
    main()