def get_nr_items(user_input):
   name_list = user_input.split(',')
   return len(name_list)

print(get_nr_items('Tim, Rick, Arnold'))

def square_side(length):
    area = length ** 2
    return area
print(square_side(7))

def temperature(number):

    if number < 7:
        return 'Cold'
    else:
        return 'Warm'
print(temperature(10))


def password(user_input):
    if len(user_input) < 8:
        return False
    else:
        return True
print (password('MyCatMan5'))