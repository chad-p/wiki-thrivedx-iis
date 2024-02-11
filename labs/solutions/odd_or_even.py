user_choice = input("Give me a number: ")
user_choice = int(user_choice)

if user_choice % 2 == 0:  # % = modulus. Any value that is used on function will be put into modulus operation.
    print(f"Your number {user_choice} is an even number.")  # Result 0 means it's even.
else:
    print(f"Your number {user_choice} is an odd number.")  # Other than 0 means it's odd..