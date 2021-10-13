import random
from hangman_art import stages, logo
from hangman_words import word_list
end_of_game = False

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print(f"You have already entered {guess} previously")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
      print(f"{guess} is not in the word, Please try again. Think before you Guess; as you have lost a life")
      lives-=1
      if lives==0:
        end_of_game=True
        print("You lose")
        print(f"The word is {chosen_word}") 

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
