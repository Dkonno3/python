# importing random library,art and the wordlist
import random
from hangman_art import logo,stages
from wordlist import word_list
#check word function
def check_letter(letter,word,nletters):
    x = 0
    for j in range(0,len(word)):
        if guess==word[j]:
            x += 1
            nletters[j]=guess
    lettersstr="".join(nletters)
    print(lettersstr)
    return(x)
def find_letter(letter, lst):
    return any(letter in word for word in lst)
#Variables
life_counter=6
nletters=''
guess_list=[]
guess=''
#'Main block'
print(logo)
chosen_word = random.choice(word_list)
#print(chosen_word)
y=len(chosen_word)
for _ in range(0,y):
    nletters+='_'
print(f'{nletters} \n')
nletters=list(nletters)
while y > 0 and life_counter > 0:
    guess = input("Guess a letter: ").lower()
    teste=find_letter(guess,guess_list)
    if not teste:
        guess_list += guess
        correct_guess = check_letter(guess, chosen_word, nletters)
        if correct_guess==0:
            print('Lost a life')
            life_counter-=1
        elif correct_guess>0:
            y = y-correct_guess
    print(f'{stages[life_counter]}\n{guess_list}')
if y==0:
    print('Congrats you won')
elif life_counter==0:
    print(f'Game Over, you lose.\nThe word was {chosen_word}')
    print(stages[life_counter])