import random
secret = random.randint(1,20)
tries = 0

while True:
    x = int(input("Enter number: "))
    print("Guess: ", x)
    tries += 1

    if secret == x:
        break
    if secret > x:
        print("Too low")
    if secret < x:
        print("Too high")

print(f"Correct! You guessed it in {tries}")

