# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Importação de pacotes
import random

# Board (tabuleiro), do tipo lista 6 tentativas
tabuleiro = ['''

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Forca:
    ### ----- ATRIBUTOS (Construtor)-------

    # Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letra_errada = []
        self.letra_certa = []
        print(">>>>>>>>>>FORCA<<<<<<<<<<")
        print("Versão v1 by Dolly")
        print("REGRA: Você tem que adivinhar a palavra secreta, só pode erra 6 vezes")

    ### ------ FUNÇÕES (operações) que a classe Hangman pode executar ------

    # Método para checar o status do game e imprimir o board na tela
    def print_jogo_status(self):
        # Imprime o tabuleiro de acordo com a quantidade de letras na lista letra_errada
        print(tabuleiro[len(
            self.letra_errada)])
        print(
            "Palavra Secreta:" + self.atualiza_palavra_tabuleiro())
        # Imprime a palavra secreta de acordo com o metodo "atualiza_palavra_tabuleiro"

        print('Letras corretas: ', )
        for letra in self.letra_certa:
            print(letra, )
        print()

        print('\nLetras erradas: ', )
        for letra in self.letra_errada:
            print(letra, )
        print()

    # Método para alocar a letra capturada e atualizar as listas (certa e errada)
    def aloca_letra(self, letra):

        if letra in self.palavra and letra not in self.letra_certa:  # Se a letra estiver na palavra secreta
            self.letra_certa.append(letra)
        elif letra not in self.palavra and letra not in self.letra_errada:  # Se a letra não estiver na palavra secreta
            self.letra_errada.append(letra)
        else:
            return False
        return True

    # Método para atualizar a letra no board
    def atualiza_palavra_tabuleiro(self):
        atualiza = ''
        for letra in self.palavra:
            if letra not in self.letra_certa:
                atualiza += '*'
            else:
                atualiza += letra
        return atualiza

    # Método para DEFINIR perda do jogo. Queira fazer um contador, mas ...
    def forca_perde(self):
        return self.forca_ganha() or (len(self.letra_errada) == 6)

    # Método para DEFINIR ganho do jogo - !GENIAL!
    def forca_ganha(self):
        if "*" not in self.atualiza_palavra_tabuleiro():
            return True
        else:
            return False

    # Função para ler uma palavra de forma aleatória do banco de palavras


def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main ----- Execução do Programa---
def main():
    # Objeto - NASCIMENTO DO JOGO--- FAZER ELE RODAR
    game = Forca(rand_word())

    # Verifica o status do jogo
    game.print_jogo_status()

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.forca_perde():
        game.print_jogo_status()
        letra = input('\nDigite uma letra: ')
        game.aloca_letra(letra)

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.forca_ganha():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.palavra)

    print('\nAgora vá comemorar! Você conseguiu programar em Python!\n')


# Executa o programa		
if __name__ == "__main__":
    main()
