from dotenv import load_dotenv
import os
import psycopg

def conectar():
    load_dotenv()
    conexao = psycopg.connect(
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD")
    )
    return conexao
    
if __name__ == "__main__":
    conex = conectar()
    print("Conectou!")
    for e in conex:
        print(e)
    conex.close()