'''
Uma aplicação de RH tem uma classe que gerencia os dados de um 
funcionário e é responsável tanto pelo cálculo do salário quanto 
pela persistência dos dados.
Isso viola o Princípio da Responsabilidade Única (SRP) porque a
classe tem mais de uma razão para mudar.'''

class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    # Responsabilidade 1: Lógica de Negócio
    def calcular_salario(self):
        """Calcula o salário final com 10% de bônus."""
        return self.salario_base * 1.10

    # Responsabilidade 2: Persistência de Dados
    def salvar_no_banco(self):
        """Simula a persistência dos dados do funcionário."""
        print(f"SALVANDO: Funcionário {self.nome} (Base: {self.salario_base}) no banco de dados.")
        # Lógica real de acesso a banco de dados estaria aqui