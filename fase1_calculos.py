# Importa os arquivos (estão na mesma pasta)
import produto
import cultura

# Função auxiliar que você já tinha
def calcular_area(comprimento, largura):
    return comprimento * largura

# Esta é a "ordem" que o chefe (app.py) vai chamar
def rodar_calculos_fase1():
    """
    Executa os cálculos da Fase 1 e retorna uma string formatada com os resultados.
    """
    
    # Limpamos a lista de produtos antes de criar novos
    produto.Produto.produtos.clear()
    
    # Criamos alguns produtos de exemplo para o cálculo
    print("Criando produtos de exemplo para cálculo...")
    produto.Produto(codigo_cultura='1', nome_produto='Adubo XPTO', quantidade=500, comprimento=100, rua=2)
    produto.Produto(codigo_cultura='2', nome_produto='Pesticida Y', quantidade=300, comprimento=200, rua=3)
    
    texto_de_retorno = ""

    if not produto.Produto.produtos:
        return "Nenhum produto encontrado para calcular."

    for item in produto.Produto.produtos:
        
        cultura_str = "Cultura Desconhecida"
        if item._cultura_obj: # Verifica se a cultura foi encontrada
            cultura_str = item._cultura_obj._nome
        
        texto_de_retorno += f"Cultura: {cultura_str}, Produto: {item._nome_produto}\n"
        
        largura_total = calcular_area(item._comprimento, item._rua)
        aplicacao_por_metro = item._quantidade / 1000
        quantidade_ruas = largura_total / item._rua
        litros_necessarios = quantidade_ruas * item._comprimento * aplicacao_por_metro

        texto_de_retorno += f"  - A lavoura possui {largura_total:.2f} (em metros) de area total.\n"
        texto_de_retorno += f"  - A lavoura possui aproximadamente {quantidade_ruas:.2f} ruas.\n"
        texto_de_retorno += f"  - Serão necessários cerca de {litros_necessarios:.4f} litros de {item._nome_produto}.\n\n"

    return texto_de_retorno
