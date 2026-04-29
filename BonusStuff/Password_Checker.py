password = input("Enter your password: ")
result={}
if len(password) >= 8:
     result["length"] = (True)

else:
    result["length"] = (False)
    print("Password is too short")

digit = False

for i in password:
    if i.isdigit():
        digit = True
result['digit'] = digit
if not digit:
    print("Password must contain at least one digit")

uppercase = False
for c in password:
    if c.isupper():
        uppercase = True
result[uppercase] = uppercase
if not uppercase:
    print("Password must contain at least one uppercase letter")

if (all(result.values())):
    print("Password is strong")
else:
    print("Password is weak")

