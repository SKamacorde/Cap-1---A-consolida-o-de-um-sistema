🚜 FarmTech Solutions - Projeto Consolidado (Fase 7)

Este projeto representa a consolidação de todas as 7 fases da disciplina, integrando um sistema completo de gestão para o agronegócio. O sistema utiliza um dashboard centralizado (Streamlit) para acionar e monitorar diferentes microsserviços, incluindo cálculos de manejo, irrigação inteligente baseada em IoT e análise de saúde da plantação com Visão Computacional.

👥 Integrantes do Grupo

| Nome | RM | |
|---|---|---|
| Daniele Antonieta Garisto Dias | RM565106 |
| Leandro Augusto Jardim da Cunha | RM561395 |
| Luiz Eduardo da Silva | RM561701 |
| João Victor Viana de Sousa | RM565136 |
| Guilherme Ribeiro Slaviero | RM561757 |


🚀 Como Executar o Projeto

Siga os passos abaixo para rodar a aplicação consolidada em seu ambiente local.

1. Pré-requisitos

Python 3.10 (ou superior)

Uma instalação do Anaconda ou um ambiente virtual (venv) é recomendado.

Um arquivo .env na raiz do projeto com as chaves da API de meteorologia (Open-Meteo) e do banco de dados Oracle.

2. Instalação

Clone este repositório e, dentro da pasta principal (FarmTech_Consolidado), instale todas as bibliotecas necessárias:

# Instala todas as dependências do projeto
pip install -r requirements.txt


3. Executando o Dashboard

Com todas as dependências instaladas, inicie o dashboard principal com o Streamlit:

streamlit run app.py


O dashboard será aberto automaticamente no seu navegador padrão (http://localhost:8501).

⚙️ Funcionalidades Integradas

O dashboard principal na Fase 7 permite acionar os seguintes serviços:

Fase 1: Cálculos de Insumos: Executa um cálculo simulado de uso de insumos (adubo, pesticida) com base em dados de cultura e área, retornando um resumo.

Fase 3: Irrigação Inteligente: Conecta-se à API de meteorologia (usando as chaves do .env) e à lógica de sensores (simulada ou real) para decidir se a irrigação deve ou não ser acionada.

Fase 6: Visão Computacional: Carrega um modelo YOLOv8 treinado (best_60_epocas.pt) e o utiliza para analisar uma imagem de teste (imagens_teste/foto_da_lavoura.jpg), exibindo a imagem com as detecções (se houver).

☁️ Fase 5: Serviço de Alerta AWS (SNS)

Para o monitoramento e alerta de eventos críticos (conforme solicitado na Fase 7), foi configurado um serviço de mensageria na AWS utilizando o Simple Notification Service (SNS).

Um Tópico SNS chamado Alertas_FarmTech foi criado.

Uma Assinatura de E-mail foi configurada para este tópico, permitindo que qualquer mensagem publicada no tópico seja enviada como um alerta para os gestores da fazenda.

(SUA TAREFA AQUI: Cole abaixo os screenshots do seu console da AWS mostrando o Tópico e a Assinatura "Confirmada")

Screenshot do Tópico SNS

[COLE AQUI O PRINT DO SEU TÓPICO SNS]

Screenshot da Assinatura de E-mail

[COLE AQUI O PRINT DA SUA ASSINATURA CONFIRMADA]

🎥 Vídeo de Apresentação (YouTube)

Um vídeo de até 10 minutos foi gravado apresentando todas as funcionalidades consolidadas do projeto, desde a Fase 1 até a 7.


Link do Vídeo:

