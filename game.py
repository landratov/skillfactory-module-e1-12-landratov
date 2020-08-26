import random, re


class Game:

    words = ["skillfactory", "testing", "blackbox", "pytest", "unittest", "coverage"]
    max_guesses = 4

    def __init__(self):
        self.word = random.choice(self.words)
        self.error_count = 0
        self.guessed_letters = set()

    def get_current_state(self):
        state = ""
        for char in self.word:
            if char in self.guessed_letters:
                state += char
            else:
                state += '_'
        return state

    def guess(self):
        while True:
            input_char = input("Введите букву: ")
            if not re.match("^[a-z]*$", input_char):
                print("Вводить можно только буквы a-z")
            if len(input_char) > 1:
                print("Вводить можно не более одной буквы")
            else:
                self.guessed_letters.add(input_char)
                if input_char not in self.word:
                    self.error_count += 1
                break

    def is_finished(self):
        for char in self.word:
            if char not in self.guessed_letters:
                return False
        return True


if __name__ == '__main__':
    word_game = Game()
    print("Добро пожаловать в игру!\n")

    while not word_game.is_finished() and word_game.error_count < word_game.max_guesses:
        print(f"Слово: {word_game.get_current_state()}\nШтрафные очки: {word_game.error_count} / {word_game.max_guesses}")
        word_game.guess()
        print()

    if word_game.error_count >= word_game.max_guesses:
        print(f"Вы проиграли! Правильный ответ: {word_game.word}")
        exit()

    if word_game.is_finished():
        print("Поздравляю! Вы выиграли!")
        exit()
