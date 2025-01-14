from Erros import ErroPrevisto
from Suspeito_crime import Suspeito
from Terminal import limpar_terminal
from time import sleep

class CasoCriminal:

    def __init__(self):
        self.__suspeito = None
        self.__nome_caso = None
        self.__respostas_afirmativas = 0
        self.__perguntas = [
            "telefonou para a vítima?",
            "esteve no local do crime?",
            "mora perto da vítima?",
            "devia para a vítima?",
            "já trabalhou para a vítima?"
        ]


    def comecar_investigacao(self) -> None:
        limpar_terminal()
        self.__cadastrar_crime()

        for pergunta in self.__perguntas:

            while True:
                limpar_terminal()
                resposta = self.__suspeito.responder_pergunta(pergunta)

                if self.__verificar_resposta(resposta):
                    if self.__confirmar_resposta(resposta):

                        self.__incrementar_respostas_afirmativas(resposta)
                        break

                    else:
                        ErroPrevisto.informacao_errada()
                        sleep(3)
                else:
                    ErroPrevisto.resposta_invalida()
                    sleep(3)
                
                limpar_terminal()

        self.__printar_veredito()


    def __cadastrar_crime(self) -> None:
        while True:
            nome_crime = str(input("Digite o nome do caso criminal: ").strip())
            if self.__confirmar_resposta(nome_crime):
                self.__nome_caso = nome_crime
                limpar_terminal()
                self.__cadastrar_suspeito()
                break
            else:
                ErroPrevisto.informacao_errada()
                sleep(3)
                limpar_terminal()


    def __cadastrar_suspeito(self) -> None:
        while True:
            nome = str(input("Digite o nome do suspeito: ").strip())
            if self.__confirmar_resposta(nome):
                limpar_terminal()
                suspeito = Suspeito(nome)
                self.__suspeito = suspeito
                break
            else:
                ErroPrevisto.informacao_errada()
                sleep(3)
                limpar_terminal()
    

    def __verificar_resposta(self, resposta: str) -> bool:
        if resposta in ["sim", "não", "nao"]:
            return True
        else:
            return False


    def __confirmar_resposta(self, resposta: str) -> bool:
        while True:
            confirmacao = str(input(f'Você respondeu \033[1;34m"{resposta}"\033[m para a pergunta, está certo? (sim/não) ').strip().lower())
            if confirmacao == "sim":
                return True
            elif confirmacao in ["não", "nao"]:
                return False
            else:
                ErroPrevisto.confirmacao_invalida()
                sleep(2)
            limpar_terminal()


    def __incrementar_respostas_afirmativas(self, resposta: str) -> None:
        if resposta == "sim":
            self.__respostas_afirmativas += 1


    def __printar_veredito(self) -> None:
        limpar_terminal()
        print(f"Informações sobre o caso \033[1;34m{self.__nome_caso}\033[m:")

        if self.__respostas_afirmativas <= 1:
            print(f"o suspeito {self.__suspeito.nome} é \033[1;32minocente!\033[m")

        elif self.__respostas_afirmativas == 2:
            print(f"o suspeito {self.__suspeito.nome} ainda é \033[1;33msuspeito!\033[m")

        elif self.__respostas_afirmativas <= 4:
            print(f"o suspeito {self.__suspeito.nome} foi um \033[1;31mcúmplice!\033[m")

        else:
            print(f"o suspeito {self.__suspeito.nome} é o \033[1;31massassino!\033[m")
        sleep(10)