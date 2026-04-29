date = input("Enter the date (MM-DD-YYYY): ")
mood = input("rate your mood: (1-10): ")
thoughts = input("What are your thoughts? ")

with open(f"../journal/{date}.txt", "w") as file:
    file.write(f"your mood is {mood}" + 2 * '\n')
    file.write(thoughts)


