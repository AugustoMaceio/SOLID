# Módulo de baixo nível (concreto)
class EmailSender:
    def enviar(self, mensagem):
        print(f"BAIXO NÍVEL: Enviando email: {mensagem}")

# Módulo de alto nível que depende diretamente do de baixo nível
class ServicoNotificacao:
    def __init__(self):
        # Dependência CONCRETA: Acoplamento Forte
        self.sender = EmailSender()

    def notificar(self, mensagem):
        """A lógica de notificação está presa ao EmailSender."""
        self.sender.enviar(mensagem)