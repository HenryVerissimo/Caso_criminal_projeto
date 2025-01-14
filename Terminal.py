from sys import stdout

def limpar_terminal():
    for linha in range(0, 50):
        stdout.write("\033[K")
        stdout.write("\033[F")
