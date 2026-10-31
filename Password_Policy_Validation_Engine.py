password = input("Enter password: ")
length_ok = False
has_digit = False
if len(password) >= 8:
    length_ok = True

for ch in password:
    if ch >= '0' and ch <= '9':
        has_digit = True
if length_ok and has_digit:
    print("Valid Password")
else:
    print("Invalid Password")
