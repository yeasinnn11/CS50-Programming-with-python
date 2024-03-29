import random
while True:
    try:
        n=int(input("Level1: "))
        num=random.randint(1,n)
        guess=int(input("Guess: "))
        if guess < num:
            print("Too small!")
            continue
        elif guess > num:
            print("Too large!")
            continue
        else:
            print("Just right!")
    except ValueError:
        continue
    break
