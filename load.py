from dotenv import load_dotenv
import os
import psycopg

def conectar():
    load_dotenv()
    conn = psycopg.connect(
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD")
    )
    return conn

def carregar_dados(dados):
    inseridas = 0
    with conectar() as conn:
        with conn.cursor() as cur:
            for itens in dados:
                cur.execute(
                    """INSERT INTO clima (cidade, temperatura, vento, dthora_coleta, observado_em) 
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (cidade, observado_em) DO NOTHING
                    """,
                    (itens["cidade"], itens["temperatura"], itens["vento"], itens["dthora_coleta"], itens["observado_em"])
                )
                inseridas += cur.rowcount
        return inseridas
    
