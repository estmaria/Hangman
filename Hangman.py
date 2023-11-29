import random

#Maria Esteban
#10/15/2023
#A simulation of the hangman game


print(f'Welcome to hangman!')
print("First choose a mode")
print("The program will randomly select a word for you to guess.")
print("Introduce letters (upper or lower case) to guess the word. You have 6 attemps.")
print("Good luck!")

# Initialize an empty list to store words
word_list = []

while True:
    mode = input("Choose a mode e (easy), m (medium), h (hard) or c (choose your own words):")
    if mode=="e":
        word_list=["cat", "sun", "hat", "moon", "fish", "pen", "blue", "taxi"]
        break
    elif mode=="m":
        word_list=["table", "happy", "music", "apple", "puzzle", "banana", "river"]
        break
    elif mode=="h":
        word_list=["symphony", "cryptocurrency", "xylophone", "mathematics", "hippopotamus", "platypus"]
        break
    elif mode=="c":
        # Ask the user for words 
        while True:
            word = input("Enter words/senteces or type 'play' to start the game: ")
            if word.isdigit():
                print(f'Error')
            if word=="play":
                if len(word_list)==0:
                    print("You have not entered any word. Introduce at least one word to play")
                    continue
                else:
                    break
            else:
                word_list.append(word)
    else:
        print("That does not correspond to anything. Try again!")


    
    
# Choose a random word from the list
random_word = random.choice(word_list)



# Define characters that should not be replaced with underscores
allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
guessed_word=""

# Iterate through the random word and replace characters as necessary
for char in random_word:
    if char in allowed_chars:
        guessed_word+= '_'
    else:
        guessed_word+=char
for char in guessed_word:
    print(char, end=" ")
print('')
    
missed_letters=""        
guessed_letters=""
attempts=0
max_attempts=6
completed=False


def print_hangman(attempts):
    if attempts==0:
        print("------")
        print("|    |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("------------")
    if attempts==1:
        print("------")
        print("|    |")
        print("|    O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("------------")
    if attempts==2:
        print("------")
        print("|    |")
        print("|    O")
        print("|    |")
        print("|    |")
        print("|")
        print("|")
        print("------------")
    if attempts==3:
        print("------")
        print("|    |")
        print("|    O")
        print("|    |")
        print("|    |")
        print("|   /")
        print("|")
        print("------------")
    if attempts==4:
        print("------")
        print("|    |")
        print("|    O")
        print("|    |")
        print("|    |")
        print("|   / \\")
        print("|")
        print("------------")
    if attempts==5:
        print("------")
        print("|    |")
        print("|    O")
        print("|  --|")
        print("|    |")
        print("|   / \\")
        print("|")
        print("------------")
    if attempts==6:
        print("------")
        print("|    |")
        print("|    O")
        print("|  --|--")
        print("|    |")
        print("|   / \\")
        print("|")
        print("------------")
    



while(attempts<max_attempts and completed==False):
    letter=input("Enter a guess (letters only): ")


    if (letter in guessed_letters) or (letter not in allowed_chars):
                 
            if letter in guessed_letters:
                         print(f"You've alredy tried this letter")
                         
            if letter not in allowed_chars:
                         print(f'Not a valid letter')
    else:

        if letter in random_word:
                     #buscar cuantas veces se repite esa letra y donde
                     #reemplazar las letras en guessed word y display
                     print(f'Good guess! The letter {letter} is in the word')
                     guessed_letters+=letter
                     index_list=[]
                     last_index=0
                     count=random_word.count(letter)
                     for i in range(0,count):
                         index=random_word.find(letter,last_index)
                         last_index=index+1
                         index_list.append(index)

                     #replace the underscores with the letter
                     for i in range(0,len(index_list)):
                         index2=index_list[i]
                         guessed_word=guessed_word[0:index2]+letter+guessed_word[index2+1:]
                    
        else:
            print(f'The letter {letter} was not in the word')
            guessed_letters+=letter
            missed_letters+=letter
            attempts+=1

        print_hangman(attempts)
            
        for char in guessed_word:
            print(char, end=" ")
        print('')


        
        print(f'Attempts remaining: {max_attempts-attempts}')
        if len(missed_letters)==0:
            print(f'Missed letters: None')
        else:
            print(f'Missed letters: {missed_letters}')




        if guessed_word.count('_')==0:
            print('You guessed the word/sentence!')
            completed=True

        if attempts==6:
            print(f"You've run out of attemps. The word/sentence was {random_word}")
    





    





    
