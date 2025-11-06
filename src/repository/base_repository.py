import oracledb as db
import os
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

class BaseRepository:
    def __init__(self):
        self.username = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.dsn = os.getenv('DB_SERVER')

    def get_connection(self):
        try:
            connection = db.connect(
                user=self.username,
                password=self.password,
                dsn=self.dsn
            )
            return connection
        except db.Error as e:
            print("❌ Erro ao conectar ao Oracle:")
            print(e)