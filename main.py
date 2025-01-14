from Caso_criminal import CasoCriminal
from Erros import ErroPrevisto
from Terminal import limpar_terminal
from time import sleep


if __name__ == "__main__":

    while True:
        sleep(1)
        limpar_terminal()
        pergunta = (input("Deseja começar a investigação de um caso criminal? (sim/não) ").strip().lower())

        if pergunta == "sim":
            
            crime01 = CasoCriminal()
            crime01.comecar_investigacao()

        elif pergunta in ["não", "nao"]:
            break

        else:
            ErroPrevisto.resposta_invalida()

    limpar_terminal()
    print("Programa finalizado!")