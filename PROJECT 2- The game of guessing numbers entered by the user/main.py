import random 

number = random.randint(1, 10)
attempt = 1
guess = int(input("Guess the number: "))


while True: 

    if guess>number:
        guess = int(input("Guess another number, this one is bigger: "))
        attempt += 1
    elif guess<number:
        guess = int(input("Guess another number, this one is lesser: "))
        attempt += 1

    else:
        print(f"The number that you guessed is right, with {attempt} attempts")
        break