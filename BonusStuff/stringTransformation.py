filenames = ['1.doc', '1.report', '1.spreadsheet' ]
filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]
print (filenames)

numbers = [10.1, 12.3, 14.7]
numbers = [int(number) for number in numbers]
print(numbers)

temperatures = [10, 12, 14]
file = open("file.txt", 'w')
temperatures = [str(temperature) + '\n' for temperature in temperatures]
file.writelines(temperatures)
print(temperatures)