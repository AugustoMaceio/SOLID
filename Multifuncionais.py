'''
Princípio da Segregação de Interfaces (ISP - Interface Segregation Principle)
Nenhum cliente deve ser forçado a depender de métodos que ele não usa.

Dispositivos de Escritório Multifuncionais
Uma empresa usa diferentes dispositivos (impressora simples, 
scanner, máquina multifuncional).
'''
from abc import ABC, abstractmethod

# Interface "Gorda"
class DispositivoMultifuncional(ABC):
    @abstractmethod
    def imprimir(self, documento):
        pass
    @abstractmethod
    def scanear(self, documento):
        pass
    @abstractmethod
    def fax(self, documento):
        pass

# O cliente (ImpressoraBasica) é forçado a implementar métodos inúteis
class ImpressoraBasica(DispositivoMultifuncional):
    def imprimir(self, documento):
        print(f"IMPRESSÃO: {documento}")

    def scanear(self, documento):
        # VIOLAÇÃO: Implementação forçada que não faz sentido para a impressora
        raise NotImplementedError("Scanner não suportado nesta impressora.")

    def fax(self, documento):
        # VIOLAÇÃO: Implementação forçada que não faz sentido
        raise NotImplementedError("Fax não suportado.")