
print("Learning python is fun!")

# User name using input function
user_name = input("Please enter your name: ")
print(f"Hello {user_name}!")
user_age = input("Please enter your age: ")

age = int(user_age) 

if age < 18:
    print(f"Sorry {user_name}, you are not eligible to vote. 😢")
else:
    print(f"Congratulations {user_name}, you are eligible to vote! 🎉")