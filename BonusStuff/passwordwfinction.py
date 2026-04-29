def strength(password):
    user_password = {}
    if len(password) >= 8:
        user_password["length"] = True
    else:
        user_password['length'] = False

    digit = False
    for i in password:
        if i.isdigit():
            digit = True
    user_password['digit'] = digit

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True
    user_password[uppercase] = uppercase

    if all(user_password.values()):
        results = 'Strong Password'
    else:
        results = 'Weak Password'

    return results


print(strength('Tomato1'))