# Este arquivo define APENAS a classe Cultura.
# Ele NÃO pode ter menus, 'while True' ou 'input()'.

class Cultura:
    # Lista para guardar todas as culturas criadas
    culturas = []

    def __init__(self, codigo, nome):
        self._codigo = codigo
        self._nome = nome
        Cultura.culturas.append(self)
        print(f"Definição de Cultura '{self._nome}' carregada.")

# Criamos as culturas que o sistema conhece UMA VEZ
# Evita criar duplicatas toda vez que o código rodar
if not Cultura.culturas:
    Cultura(codigo='1', nome='Cafe')
    Cultura(codigo='2', nome='Cana de açucar')