'''
Uma aplicação de logística tem uma classe que calcula o custo do 
frete com base no tipo de entrega (correio, transportadora, etc.).
'''

class CalculadoraFrete:
    def calcular(self, tipo_entrega: str, peso: float):
        if tipo_entrega == "CORREIO":
            return 10.0 + peso * 2.0
        elif tipo_entrega == "TRANSPORTADORA":
            return 25.0 + peso * 1.5
        # SE FOR ADICIONADO UM NOVO TIPO (EX: RETIRADA), 
        # ESTE MÉTODO TERÁ QUE SER MODIFICADO (VIOLAÇÃO DO OCP).
        else:
            raise ValueError("Tipo de entrega não suportado.")

# Demonstração
print(f"Frete Correio: {CalculadoraFrete().calcular('CORREIO', 5.0)}")