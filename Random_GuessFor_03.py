import random
secret = random.randint(1,20)
tries = 0

for attempt in range(7):
    x = int(input("Enter number: "))
    print("Guess: ", x)
    tries += 1

    if secret == x:
        print(f"Correct! You guessed it in {tries}")
    elif secret > x:
        print("Too low")
    elif secret < x:
        print("Too high")
else:
    print("Out of tries! The number was", tries)


