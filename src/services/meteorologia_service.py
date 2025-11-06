from dotenv import load_dotenv
import requests
import pandas as pd
import os
from tabulate import tabulate

# Carrega as variáveis do .env
load_dotenv()

class MeteorologiaService:
    def __init__(self):
        self.url_api = os.getenv('URL_API')        
        self.latitude = os.getenv('LATITUDE_PARAM')
        self.longitude = os.getenv('LONGITUDE_PARAM')
        self.hourly = os.getenv('HOURLY_PARAM')
    
    def obter_dados_meteorologia(self):        
        # Construção da URL
        url = f"{self.url_api}forecast?latitude={self.latitude}&longitude={self.longitude}&hourly={self.hourly}"        
        # Requisição
        resposta = requests.get(url)
        # Verifica o status
        if resposta.status_code == 200:
            dados = resposta.json()
            horas = pd.to_datetime(dados["hourly"]["time"])
            probabilidades = dados["hourly"]["precipitation_probability"]
            df = pd.DataFrame({
                "Data": horas.date,
                "Hora": horas,
                "Probabilidade (%)": probabilidades
            })  

            return df
        else:
            print("Erro na requisição:", resposta.status_code)