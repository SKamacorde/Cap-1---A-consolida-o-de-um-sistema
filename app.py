import streamlit as st
import pandas as pd
# Importe outras coisas que sua Fase 4 usa (sklearn, etc.)

# --- IMPORTA OS "FUNCIONÁRIOS" ---
# (Agora eles estão na mesma pasta, é mais fácil!)
import fase1_calculos
import fase3_iot
import fase6_visao

# --- COMEÇO DO SEU DASHBOARD DA FASE 4 ---
st.set_page_config(layout="wide")
st.title("🚜 FarmTech Solutions - Painel de Gestão Consolidado")

st.info("Este é o dashboard principal que integra todos os serviços das Fases 1 a 6.")

# ... (seu código da Fase 4) ...
st.markdown("---")


# --- NOVA PARTE (Fase 7) ---
st.header("Serviços Consolidados (Fase 7)")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Fase 1: Cálculos de Insumos")
    if st.button("Rodar Cálculos de Manejo"):
        with st.spinner("Calculando..."):
            # 1. Chama o "funcionário" da Fase 1
            resultado_f1 = fase1_calculos.rodar_calculos_fase1()
            # Mostra o texto que o funcionário "devolveu"
            st.text_area("Resultado dos Cálculos", resultado_f1, height=200)
            st.success("Cálculos da Fase 1 concluídos!")

with col2:
    st.subheader("Fase 3: Irrigação Inteligente")
    if st.button("Verificar Sensores de Irrigação"):
        with st.spinner("Verificando API de clima e sensores..."):
            # 2. Chama o "funcionário" da Fase 3
            # A função "from src..." DENTRO de fase3_iot.py
            # agora vai funcionar!
            resultado_f3 = fase3_iot.rodar_logica_irrigacao()
            # Mostra o texto que o funcionário "devolveu"
            st.info(resultado_f3)
            st.success("Verificação da Fase 3 concluída!")

with col3:
    st.subheader("Fase 6: Visão Computacional")
    if st.button("Analisar Saúde da Plantação"):
        with st.spinner("Carregando modelo YOLO e analisando imagem..."):
            # 3. Chama o "funcionário" da Fase 6
            resultado_f6 = fase6_visao.rodar_visao_fase6()
            
            # Verificamos se ele "devolveu" uma imagem ou um texto de erro
            if isinstance(resultado_f6, str):
                # Se for texto, é um erro
                st.error(resultado_f6)
            else:
                # Se for uma imagem, mostramos!
                st.image(resultado_f6, channels="BGR", caption="Imagem Analisada pelo Modelo")
                st.success("Análise da Fase 6 concluída!")

