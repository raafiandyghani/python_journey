name = input(f"What is your name? ")
age = input(f"How old are you? ")
city = input (f"Where do you live? ")
hobby = input (f"What is your hobby? ")
student_status = input(f"Are you a student? (yes/no) ").lower() == "yes"

print("\n🛠️  Generating Bio...\n")
print(f"Hello my name is {name}")
print(f"I'm {int(age)} years old and I live in {city}")
print(f"My favorite hobby is {hobby}")
print("Status:", "Student" if student_status else "Not a student")
