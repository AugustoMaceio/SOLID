from abc import ABC, abstractmethod

# Interfaces segregadas (coesas)
class Impressora(ABC):
    @abstractmethod
    def imprimir(self, documento):
        pass

class Scanner(ABC):
    @abstractmethod
    def scanear(self, documento):
        pass

# 1. O cliente ImpressoraBasica implementa APENAS o que precisa
class ImpressoraBasica(Impressora):
    def imprimir(self, documento):
        print(f"IMPRESSÃO BÁSICA: {documento}")

# 2. O cliente Multifuncional implementa todas as interfaces
class Multifuncional(Impressora, Scanner):
    def imprimir(self, documento):
        print(f"MULTIFUNCIONAL: Imprimindo {documento}")
    
    def scanear(self, documento):
        print(f"MULTIFUNCIONAL: Scaneando {documento}")

# Demonstração
impressora = ImpressoraBasica()
multifuncional = Multifuncional()

impressora.imprimir("Relatório A")
multifuncional.scanear("Documento B")