from BonusStuff.converters13 import convert
from BonusStuff.parsers13 import parse


feet_inches = input ("Enter feet and inches: ")

f, i = parse(feet_inches)
results = (convert(f, i))

if results < 1:
    print('kid is too small to ride')
else:
    print('kid can ride')