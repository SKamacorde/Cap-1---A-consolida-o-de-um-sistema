import boto3
import os
from dotenv import load_dotenv
from datetime import datetime # Para adicionar data e hora no e-mail

# Carrega as variáveis do arquivo .env
load_dotenv()

# --- PREENCHA ESTAS DUAS LINHAS! ---
# Lembre-se de colar seu ARN real que você copiou do console da AWS
# (O ARN se parece com: arn:aws:sns:sa-east-1:123456789012:Alertas_FarmTech)
TOPIC_ARN = "COLE_O_SEU_TOPIC_ARN_AQUI" 

# Região de São Paulo
AWS_REGION = "sa-east-1" 
# --- FIM DO PREENCHIMENTO ---

# Tenta configurar o "carteiro"
try:
    sns_client = boto3.client('sns', region_name=AWS_REGION)
except Exception as e:
    print(f"Erro ao criar o cliente Boto3 (Boto3): {e}")
    sns_client = None

# A função que formata e envia o e-mail
def enviar_alerta_sns(assunto, mensagem_de_alerta, acao_sugerida, nivel_risco="PADRÃO"):
    """
    Envia uma mensagem formatada para o Tópico SNS.
    """
    if sns_client is None:
        print("ERRO DE ALERTA: O cliente SNS (Boto3) não foi inicializado.")
        return False
        
    if "COLE_O_SEU_TOPIC_ARN_AQUI" in TOPIC_ARN:
        print("ERRO DE ALERTA: O TOPIC_ARN não foi configurado em 'aws_alertas.py'.")
        return False

    try:
        # Pega a data e hora atual
        agora = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")

        # --- ESTA É A MENSAGEM DO E-MAIL ---
        mensagem_completa = f"""
        ========================================
        ALERTA DO SISTEMA DE GESTÃO FARMTECH
        ========================================
        
        Um novo evento foi detectado pelo sistema e requer sua atenção.

        NÍVEL DE RISCO: {nivel_risco}
        
        ASSUNTO: {assunto}
        
        PROBLEMA DETECTADO:
        {mensagem_de_alerta}
        
        ----------------------------------------
        
        AÇÃO CORRETIVA SUGERIDA:
        {acao_sugerida}
        
        ----------------------------------------
        
        Data/Hora da Detecção: {agora}
        Sistema: FarmTech Consolidado (Fase 7)
        """
        # --- FIM DA MENSAGEM DO E-MAIL ---
        
        # Publica a mensagem no "grupo" (Tópico)
        response = sns_client.publish(
            TopicArn=TOPIC_ARN,
            Message=mensagem_completa,
            Subject=f"FarmTech Alerta ({nivel_risco}): {assunto}" # Este é o Assunto do e-mail
        )
        
        print(f"ALERTA ENVIADO COM SUCESSO! Nível: {nivel_risco}, Assunto: {assunto}")
        return True

    except Exception as e:
        print(f"ERRO AO ENVIAR ALERTA SNS: {e}")
        return False

