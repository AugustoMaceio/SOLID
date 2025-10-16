from abc import ABC, abstractmethod

# 1. Abstração (Contrato) - Deve ser implementada por módulos de baixo nível
class MensagemSender(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass

# 2. Módulos de baixo nível dependem da Abstração
class EmailSender(MensagemSender):
    def enviar(self, mensagem):
        print(f"Implementação Email: Enviando email: {mensagem}")

class SmsSender(MensagemSender):
    def enviar(self, mensagem):
        print(f"Implementação SMS: Enviando SMS: {mensagem}")

# 3. Módulo de alto nível depende da Abstração (Inversão de Dependência)
class ServicoNotificacao:
    # Recebe a dependência no construtor (Injeção de Dependência)
    def __init__(self, sender: MensagemSender):
        self.sender = sender # Depende do CONTRATO, não da classe concreta

    def notificar(self, mensagem):
        """A lógica de notificação é genérica e usa o contrato."""
        self.sender.enviar(mensagem)

# Demonstração
# O código cliente (ou o framework) é quem decide a dependência a ser usada.
notificador_email = ServicoNotificacao(EmailSender())
notificador_email.notificar("Lembrete por Email.")

notificador_sms = ServicoNotificacao(SmsSender())
notificador_sms.notificar("Lembrete por SMS.")