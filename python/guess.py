from random import *
guess=""
password=input("password:")
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
while (guess!=password):
    guess= ""
    for letter in password:
        guess_letter=letters[randint(0,25)]
        guess=str(guess_letter)+str(guess)
    print(guess)
print("password guessed")
input("")