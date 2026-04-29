feet_inches = input ("Enter feet and inches: ")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches

def convert(feet, inches):
   meters = feet * 0.3048 + inches * 0.0254
   return meters

f, i = parse(feet_inches)
results = (convert(f, i))

if results < 1:
    print('kid is too small to ride')
else:
    print('kid can ride')