'''
Figuras Geométricas
Um código que manipula diferentes formas geométricas e calcula suas áreas. O erro comum é usar herança para representar formas que não se encaixam perfeitamente.
'''
class Retangulo:
    def __init__(self, largura: float, altura: float):
        self._largura = largura
        self._altura = altura

    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self, valor):
        self._largura = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        self._altura = valor

    def calcular_area(self) -> float:
        return self._largura * self._altura

# Subtipo que viola o contrato do tipo base (Retangulo)
class Quadrado(Retangulo):
    # O quadrado força a alteração da altura quando a largura é alterada
    # (e vice-versa), violando o comportamento esperado do Retangulo.
    @Retangulo.largura.setter
    def largura(self, valor):
        self._largura = valor
        self._altura = valor # VIOLAÇÃO: altera a altura também

    @Retangulo.altura.setter
    def altura(self, valor):
        self._altura = valor
        self._largura = valor # VIOLAÇÃO: altera a largura também

# Função cliente que quebra ao substituir Retangulo por Quadrado
def aumentar_largura_e_checar_area(forma: Retangulo, nova_largura: float):
    print(f"Área Esperada: {nova_largura * forma.altura}")
    forma.largura = nova_largura
    print(f"Área Real: {forma.calcular_area()}")
    # Se for um Retangulo, a altura deve ser a original. Se for Quadrado, quebra.

# Demonstração
print("--- Teste com Retangulo ---")
ret = Retangulo(10, 5)
aumentar_largura_e_checar_area(ret, 12) # OK

print("\n--- Teste com Quadrado (Violação) ---")
qua = Quadrado(10, 10)
# A função espera que a altura seja 10, mas o setter do Quadrado a altera para 12.
aumentar_largura_e_checar_area(qua, 12) # A altura mudou, quebrando o cálculo esperado!