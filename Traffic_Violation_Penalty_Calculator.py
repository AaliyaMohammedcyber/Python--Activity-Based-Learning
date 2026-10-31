vehicle = input("Enter vehicle type: ")
offense = input("Enter offense: ")
if vehicle == "car":
    if offense == "speeding":
        fine = 100
    else:
        fine = 150
else:
    if offense == "speeding":
        fine = 50
    else:
        fine = 80

print("Fine =", fine)
