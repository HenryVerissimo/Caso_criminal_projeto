class Suspeito:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def responder_pergunta (self, pergunta: str):
        resposta = str(input(f"{self.nome} {pergunta} (sim/não) ").strip().lower())
        return resposta
        