# 1. Classe de Entidade/Modelo (Apenas dados)
class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base
        
    def __str__(self):
        return f"Nome: {self.nome}, Salário Base: {self.salario_base}"

# 2. Classe de Lógica de Negócio (Calcula Salário)
class CalculadoraSalario:
    def calcular(self, funcionario: Funcionario):
        """Responsável apenas pela regra de cálculo."""
        return funcionario.salario_base * 1.10

# 3. Classe de Persistência (Salva no Banco)
class FuncionarioRepositorio:
    def salvar(self, funcionario: Funcionario):
        """Responsável apenas pela comunicação com o banco de dados."""
        print(f"PERSISTÊNCIA: Salvando {funcionario.nome} no repositório.")

# Demonstração
func = Funcionario("Alice", 3000.0)
salario = CalculadoraSalario().calcular(func)
print(f"O salário final de {func.nome} é: {salario:.2f}")
FuncionarioRepositorio().salvar(func)