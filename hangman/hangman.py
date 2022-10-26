import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words) # letters in the word
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join([ 'a', 'b', 'cd'])--> 'a b cd'
        
        print('You have ', lives,'lives left and you have used these letters: ', ' '.join(used_letters))
        
        #what current word is (ie W - R D)
        word_list = [ letter if  letter in used_letters else '-' for letter in word]
        print('Current word is: ', ' '.join(word_list))
        
        user_letter = input('Enter a letter : ').upper()
        if user_letter in alphabet  - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print|('')

            else :
                lives = lives - 1
                print('Your letter ', used_letters, 'is not in the word.')

        elif user_letter in used_letters:
            print('You have already guessed this character. Please try again.')

        else:
            print('Invalid character. Try Again.')

    if lives == 0:
        print('You could not guess the word. The word was ',word)
    else:
        print('Yay!, You won!! ', word, 'is the correct word.')


hangman()