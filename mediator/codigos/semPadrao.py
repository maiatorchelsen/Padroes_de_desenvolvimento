# Serviços de infraestrutura
class ServicoLog:
    def registrar(self, mensagem: str) -> None:
        print(f"[LOG]: {mensagem}")

class ServicoEmail:
    def enviar(self, email_destino: str, mensagem: str) -> None:
        print(f"[EMAIL para {email_destino}]: {mensagem}")

# Serviço principal de negócio (Altamente acoplado)
class ServicoConvidados:
    def __init__(self) -> None:
        # ❌ Problema: A classe cria as dependências diretamente
        self.log = ServicoLog()
        self.email = ServicoEmail()

    def adicionar(self, nome: str, email: str, confirmado: bool) -> None:
        print(f"\nSalvando no banco: {nome}...")
        
        # Chamadas diretas amarrando o código
        self.log.registrar(f"Novo convidado: {nome} | Confirmado: {confirmado}")
        
        if confirmado:
            self.email.enviar(email, "Bem-vindo ao nosso evento!")

# --- TESTANDO O CÓDIGO ---
if __name__ == "__main__":
    sistema = ServicoConvidados()
    sistema.adicionar("Samuel", "samuel@teste.com", True)