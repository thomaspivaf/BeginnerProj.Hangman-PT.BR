# Hangman Game (Jogo da Forca)

# Import
import random
import os

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

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

tentativa = []
letras = []
contador = 0
letrascertas = []
letraserradas = []

# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word

    # Método para adivinhar a letra
    def guess(self, letter):
        self.letter = letter
        global letras
        global tentativa
        global contador
        global letrascertas
        global letraserradas

        for i in range(0, len(letras)):
            if (letter == letras[i]):
                tentativa[i] = letter

        if (letter not in letras):
            contador += 1
            letraserradas.append(letter)
        elif (letter in letras):
            letrascertas.append(letter)

        return letras and tentativa

    def hangman_over(self):
        global contador
        global tentativa
        if contador == 6:
            return False

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if tentativa == letras:
            return True


    def hide_word(self):
        global tentativa
        global letras
        for i in letras:
            tentativa += "-"
        return tentativa

        # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        global contador
        global board
        global letrascertas
        global letraserradas
        global tentativa

        print(board[contador])
        print('Palavra: ' + ''.join(tentativa))
        print(" ")
        print('Letras erradas:')
        print(' '.join(letraserradas))
        print('Letras corretas:')
        print(' '.join(letrascertas))




# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa

def main():
    # Objeto
    game = Hangman(rand_word())

    for i in game.word:
        letras.append(i)
    game.hide_word()

    while tentativa != letras and contador < 6:

        game.print_game_status()
        chute = input(('Digite uma letra: '))
        game.guess(chute)
        print('Palavra: ' + ''.join(tentativa))
    else:
        game.print_game_status()
        if game.hangman_won():
            print('\nParabéns! Você venceu!!')
        else:
            print('\nGame over! Você perdeu.')
            print('A palavra era ' + game.word)

        print('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa
if __name__ == "__main__":
    main()
