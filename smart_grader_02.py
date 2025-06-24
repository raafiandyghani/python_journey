name = input("What is your name?: ")
grade = int(input("Put the score!: "))



if grade >= 90:
    score = "Grade A"
elif grade >= 80:
    score = "Grade B"
elif grade >= 70:
    score = "Grade C"
else:
    score = "Grade D"

print("Name: ", name)
print("Score: ", grade)
print(f"Hello {name}! You got {score}. Congrats!")