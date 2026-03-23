











name = input("Enter your name: ")
age = input("Enter your age: ")
color = input("Enter your favorite color: ")
food = input("Enter your favorite food: ")

# Saving the data to a text file

try:
    with open("user_info.txt", "w") as file:
        file.write(f"{name}\n")
        file.write(f"{age}\n")
        file.write(f"{color}\n")
        file.write(f"{food}\n")
    print("\nSuccess! Your information has been saved to 'user_info.txt'.")
except Exception as e:
    print(f"An error occurred while saving the file: {e}")
