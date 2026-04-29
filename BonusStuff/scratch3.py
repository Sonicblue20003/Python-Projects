def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    min_max = {'Max': maximum, 'Min': minimum}
    minmax_string = str(min_max)
    return minmax_string

total = str(get_max())
print(total)