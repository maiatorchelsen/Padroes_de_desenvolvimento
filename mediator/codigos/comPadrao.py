from abc import ABC, abstractmethod
from typing import Any, Dict

# 1. Interface central do Mediador
class Mediador(ABC):
    @abstractmethod
    def notificar(self, remetente: object, evento: str, dados: Dict[str, Any]) -> None:
        pass

# 2. Classe Base para todos os serviços conhecerem o Mediador
class ComponenteBase:
    def __init__(self) -> None:
        self._mediador: Mediador | None = None

    def set_mediador(self, mediador: Mediador) -> None:
        self._mediador = mediador

# 3. Nossos serviços (Agora eles não se conhecem mais!)
class ServicoLog(ComponenteBase):
    def registrar(self, mensagem: str) -> None:
        print(f"[LOG]: {mensagem}")

class ServicoEmail(ComponenteBase):
    def enviar(self, email_destino: str, mensagem: str) -> None:
        print(f"[EMAIL para {email_destino}]: {mensagem}")

class ServicoConvidados(ComponenteBase):
    def adicionar(self, nome: str, email: str, confirmado: bool) -> None:
        print(f"\nSalvando no banco: {nome}...")
        
        # ✅ Solução: Apenas avisa o mediador, passando os dados
        if self._mediador:
            self._mediador.notificar(
                self, 
                "CONVIDADO_ADICIONADO", 
                {"nome": nome, "email": email, "confirmado": confirmado}
            )

# 4. O Mediador Concreto (A Torre de Controle)
class MediadorSistemaEvento(Mediador):
    def __init__(self, log: ServicoLog, email: ServicoEmail) -> None:
        self.log = log
        self.email = email

    def notificar(self, remetente: object, evento: str, dados: Dict[str, Any]) -> None:
        if evento == "CONVIDADO_ADICIONADO":
            # O mediador decide quem deve ser acionado
            self.log.registrar(f"Novo convidado: {dados['nome']} | Confirmado: {dados['confirmado']}")
            
            if dados['confirmado']:
                self.email.enviar(dados['email'], "Bem-vindo ao nosso evento!")

# --- TESTANDO O CÓDIGO ---
if __name__ == "__main__":
    # Instanciamos as peças separadamente
    servico_log = ServicoLog()
    servico_email = ServicoEmail()
    servico_convidados = ServicoConvidados()

    # Criamos o mediador passando as peças que ele vai orquestrar
    mediador = MediadorSistemaEvento(servico_log, servico_email)

    # Conectamos os serviços ao mediador
    servico_convidados.set_mediador(mediador)
    servico_log.set_mediador(mediador)
    servico_email.set_mediador(mediador)

    # O serviço de convidados faz o seu trabalho isoladamente
    servico_convidados.adicionar("Samuel", "samuel@teste.com", True)