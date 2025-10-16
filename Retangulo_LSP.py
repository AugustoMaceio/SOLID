from abc import ABC, abstractmethod

# Abstração base: O que importa para o cliente é a área
class Forma(ABC):
    @abstractmethod
    def calcular_area(self) -> float:
        pass

# 1. Implementação Retangulo
class Retangulo(Forma):
    def __init__(self, largura: float, altura: float):
        self._largura = largura
        self._altura = altura

    def calcular_area(self) -> float:
        return self._largura * self._altura

# 2. Implementação Quadrado
class Quadrado(Forma):
    def __init__(self, lado: float):
        self._lado = lado

    def calcular_area(self) -> float:
        return self._lado * self._lado

# Função cliente que respeita o LSP (só depende do contrato calcular_area)
def imprimir_area(forma: Forma):
    print(f"A área da forma é: {forma.calcular_area()}")

# Demonstração (Substituição funciona perfeitamente)
imprimir_area(Retangulo(10, 5))
imprimir_area(Quadrado(10))