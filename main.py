import json
import random
from datetime import datetime
with open("tips.json", "r") as file:
    data = json.load(file)

study_tips = data["study_tips"]
motivation_quotes = data["motivation_quotes"]
name = input("Enter your name: ")

print("\nWelcome,", name + "!")
print("Smart Student Assistant")
print("--------------------------")

while True:
    print("\nMenu")
    print("1. Generate Study Tip")
    print("2. Generate Motivation Quote")
    print("3. Display Current Date & Time")
    print("4. Exit")

    choice = input("Enter your choice: ")

    output = ""

    if choice == "1":
        tip = random.choice(study_tips)
        output = f"Study Tip: {tip}"
        print(output)

    elif choice == "2":
        quote = random.choice(motivation_quotes)
        output = f"Motivation Quote: {quote}"
        print(output)

    elif choice == "3":
        now = datetime.now()
        output = "Current Date & Time: " + now.strftime("%d-%m-%Y %H:%M:%S")
        print(output)

    elif choice == "4":
        print("Thank you for using Smart Student Assistant!")
        break

    else:
        print("Invalid choice! Please try again.")
        continue
    with open("output.txt", "a") as out_file:
        out_file.write(output + "\n")