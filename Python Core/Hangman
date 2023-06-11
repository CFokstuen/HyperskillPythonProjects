import random

word_list = ['python', 'java', 'javascript', 'swift']
attempts = 8
guessed_letters = []
wins = 0
losses = 0

while True:
    print("H A N G M A N")
    print("")

    menu_choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit')

    if menu_choice == "play":
        chosen_word = random.choice(word_list)
        hidden_word = '-' * len(chosen_word)
        attempts = 8
        guessed_letters = []

        while attempts > 0:
            print(hidden_word)
            guess = input("Input a letter: ")

            if len(guess) != 1:
                print("Please, input a single letter.")
                continue

            if not guess.isalpha() or not guess.islower():
                print("Please, enter a lowercase letter from the English alphabet.")
                continue

            guess = guess.lower()

            if guess in guessed_letters:
                print("You've already guessed this letter.")
                continue

            guessed_letters.append(guess)

            if guess in chosen_word:
                for i in range(len(chosen_word)):
                    if chosen_word[i] == guess:
                        hidden_word = hidden_word[:i] + guess + hidden_word[i+1:]

                if hidden_word == chosen_word:
                    print(hidden_word)
                    print("You guessed the word", chosen_word + "!")
                    print("You survived!")
                    wins += 1
                    break
            else:
                print("That letter doesn't appear in the word.")
                attempts -= 1

            print("")

        if attempts == 0:
            print("You lost!")
            losses += 1

    elif menu_choice == "results":
        print("You won:", wins, "times")
        print("You lost:", losses, "times")

    elif menu_choice == "exit":
        break

    print("")
