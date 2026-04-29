
try:
    total_value = float(input('Input the total value:'))
    value = float(input('input the value: '))

    result = value / total_value * 100
    print(f'The result is {result}%')

except ValueError:
    print('You must enter a number')
except ZeroDivisionError:
    print('your total value can not be zero')