import sys
import os
import random # Para simular a umidade

# --- INÍCIO DA CORREÇÃO DE CAMINHO ---
# (Ensina o Python a achar a pasta "src" e o "aws_alertas.py")
caminho_atual = os.path.dirname(os.path.abspath(__file__))
# (Este é o "FarmTech_Consolidado")
caminho_raiz_do_projeto = os.path.dirname(caminho_atual) 
if caminho_raiz_do_projeto not in sys.path:
    sys.path.append(caminho_raiz_do_projeto)
# --- FIM DA CORREÇÃO DE CAMINHO ---

# 1. Tenta importar as ferramentas da Fase 3 (da pasta src)
try:
    from src.service_factory import get_irrigacao_service
    from src.services.irrigacao_service import IrrigacaoService
    IMPORT_SRC_SUCESSO = True
except ImportError as e:
    print(f"Erro de importação da 'src': {e}")
    IMPORT_SRC_SUCESSO = False
    def get_irrigacao_service():
        return None

# 2. Tenta importar o "carteiro" (o arquivo aws_alertas.py)
try:
    from aws_alertas import enviar_alerta_sns
    IMPORT_ALERTA_SUCESSO = True
except ImportError:
    print("Importação de 'servicos.aws_alertas' falhou, tentando 'aws_alertas'...")
    try:
        from aws_alertas import enviar_alerta_sns
        IMPORT_ALERTA_SUCESSO = True
    except ImportError as e:
        print(f"Erro de importação do 'aws_alertas': {e}")
        IMPORT_ALERTA_SUCESSO = False
        def enviar_alerta_sns(a, b, c, d): # Precisa de 4 argumentos
            return False


# Esta é a "ordem" que o chefe (app.py) vai chamar
def rodar_logica_irrigacao():
    """
    Executa a lógica de irrigação E TAMBÉM o serviço de alerta.
    """
    
    # --- Parte 1: Lógica da Irrigação (o que você já tinha) ---
    if not IMPORT_SRC_SUCESSO:
        return "Erro: Falha ao importar 'src'. Verifique o terminal e o 'oracledb'."
        
    try:
        irrigacao_service = get_irrigacao_service()
        if irrigacao_service is None:
            resultado_irrigacao = "Erro: 'get_irrigacao_service' não encontrado."
        else:
            # Roda a lógica da sua Fase 3 (ver API do tempo, etc.)
            resultado_irrigacao = irrigacao_service.irrigar_plantacao()
            if resultado_irrigacao is None:
                resultado_irrigacao = "Verificação de irrigação concluída. Tudo OK."
    except Exception as e:
        resultado_irrigacao = f"Ocorreu um erro na lógica da Fase 3: {e}"


    # --- Parte 2: Lógica do Alerta (A parte nova!) ---
    if not IMPORT_ALERTA_SUCESSO:
        return f"{resultado_irrigacao}\n\nALERTA: Falha ao importar 'aws_alertas.py'."

    # Simula uma leitura de sensor para disparar o e-mail
    umidade_simulada = random.randint(10, 19) # FORÇANDO umidade baixa
    
    texto_do_alerta = ""
    
    if umidade_simulada < 20:
        # Se a umidade for baixa, chama o "carteiro"!
        print("SIMULAÇÃO: Umidade baixa detectada! Enviando alerta...")
        
        # Chama o "carteiro" com os 4 argumentos
        sucesso_do_envio = enviar_alerta_sns(
            assunto="Umidade do Solo Baixa",
            mensagem_de_alerta=f"Sensores do Setor A detectaram umidade de {umidade_simulada}%. (Abaixo do mínimo de 20%).",
            acao_sugerida="Ligar sistema de irrigação (Bomba 1) por 30 minutos.",
            nivel_risco="MÉDIO" # O novo argumento
        )
        
        if sucesso_do_envio:
            texto_do_alerta = "ALERTA: Umidade baixa detectada! E-mail enviado para os gestores."
        else:
            texto_do_alerta = "ALERTA: Umidade baixa detectada, MAS FALHOU AO ENVIAR E-MAIL. Verifique o terminal."
    else:
        # Se a umidade estivesse OK (não vai acontecer agora)
        texto_do_alerta = f"SIMULAÇÃO: Umidade OK ({umidade_simulada}%)."


    # Devolvemos as DUAS respostas para o "chefe"
    return f"{resultado_irrigacao}\n\n{texto_do_alerta}"

