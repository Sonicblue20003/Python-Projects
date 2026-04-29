filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]
for f in filenames:
    f = f[:-4].capitalize()
    print(f)

#These are different problems

try:
    waiting_list = ["john", "marry"]
    name = input("Enter name: ")

    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    print(f"{name} is not in list")