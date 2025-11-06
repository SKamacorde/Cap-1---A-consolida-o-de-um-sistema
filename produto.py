from random import randint
# Importa 'Cultura' (está na mesma pasta)
import cultura

class Produto:
    # Lista para guardar todos os produtos criados
    produtos = []

    def __init__(self, codigo_cultura, nome_produto, quantidade, comprimento, rua):
        self._codigo = randint(1,100) # Código aleatório
        self._nome_produto = nome_produto.title()
        self._quantidade = quantidade
        self._comprimento = comprimento
        self._rua = rua
        
        # Encontra o objeto 'Cultura' com base no código
        self._cultura_obj = self.encontrar_cultura(codigo_cultura)
        
        Produto.produtos.append(self)
        print(f"Definição de Produto '{self._nome_produto}' carregada.")

    def encontrar_cultura(self, cultura_codigo):
        """ Encontra e retorna o objeto Cultura pelo código. """
        # Agora o "cultura.Cultura.culturas" é o caminho
        for c in cultura.Cultura.culturas:
            if c._codigo == cultura_codigo:
                return c
        return None # Se não achar
    
    @staticmethod
    def is_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False
