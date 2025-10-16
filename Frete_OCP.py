from abc import ABC, abstractmethod

# Contrato Base (Fechado para Modificação)
class TipoFrete(ABC):
    @abstractmethod
    def calcular(self, peso: float) -> float:
        """Define o método que todo tipo de frete deve ter."""
        pass

# 1. Extensão para Correio (Aberto para Extensão)
class FreteCorreio(TipoFrete):
    def calcular(self, peso: float) -> float:
        return 10.0 + peso * 2.0

# 2. Extensão para Retirada (Novo, sem modificar o código existente)
class FreteRetiradaLoja(TipoFrete):
    def calcular(self, peso: float) -> float:
        return 0.0 # Frete grátis

# Classe central (Fechada para Modificação)
class CalculadoraFrete:
    def calcular(self, tipo_frete: TipoFrete, peso: float):
        """Aceita qualquer objeto que satisfaça o contrato TipoFrete."""
        return tipo_frete.calcular(peso)

# Demonstração
calc = CalculadoraFrete()
print(f"Frete Correio: {calc.calcular(FreteCorreio(), 5.0)}")
print(f"Frete Retirada: {calc.calcular(FreteRetiradaLoja(), 5.0)}")