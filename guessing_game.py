import random

numofguesses = 0

print("Hallo!, wat is je naam?")
name = input()

number = random.randint(1,20)
print("Kies een nummer tussen de 1 en 20")

while numofguesses < 5:
    print("Gok een nummer")
    guess = input()
    guess = int(guess)

    numofguesses = numofguesses + 1
    if guess < number:
        print("nummer is te laag")
    if guess > number:
        print("nummer is te hoog")
    if guess == number:
        break
if guess == number:
    numofguesses = str(numofguesses)
    print("Goed gedaan", name , "je hebt het getal in:",numofguesses ,"keer geraden!")

if guess != number:
    number = str(number)
    print("Helaas je bent af, het nummer was:",number)

