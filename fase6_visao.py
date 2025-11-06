# Estas são as bibliotecas que sua Fase 6 usa
from ultralytics import YOLO
import cv2 # OpenCV para carregar e desenhar na imagem
import os

# Onde o seu modelo está (copie a pasta "MODELOS_SALVOS")
CAMINHO_MODELO = os.path.join('MODELOS_SALVOS', 'best_60_epocas.pt')

# Onde está sua imagem de teste (crie uma pasta e coloque uma foto lá)
IMAGEM_TESTE = os.path.join('imagens_teste', 'foto_da_lavoura.jpg') 

# Esta é a "ordem" que o chefe (app.py) vai chamar
def rodar_visao_fase6():
    """
    Carrega o modelo YOLO da Fase 6, analisa uma imagem de teste
    e retorna a imagem com as detecções.
    """
    try:
        # 1. Carrega o modelo
        model = YOLO(CAMINHO_MODELO)

        # 2. Carrega a imagem de teste
        # (Verifique se a pasta 'imagens_teste' e a imagem existem!)
        if not os.path.exists(IMAGEM_TESTE):
            return f"Erro: Imagem de teste não encontrada em {IMAGEM_TESTE}"
            
        img = cv2.imread(IMAGEM_TESTE)
        if img is None:
            return "Erro ao carregar imagem. Verifique o caminho."

        # 3. Roda a predição (a "mágica")
        results = model.predict(source=img, conf=0.25)
        
        # 4. Desenha os resultados na imagem
        # O "results[0].plot()" é uma função mágica do YOLO
        # que já desenha os quadrados na imagem!
        img_resultante = results[0].plot() 

        # 5. Devolve a IMAGEM para o "chefe"
        # O Streamlit (app.py) sabe mostrar uma imagem
        return img_resultante

    except Exception as e:
        return f"Ocorreu um erro na Fase 6: {e}. Você instalou 'ultralytics' e 'opencv-python'?"
