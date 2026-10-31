vehicle = input("Enter vehicle type: ")
hours = int(input("Enter hours: "))
if vehicle == "bike":
    fee = hours * 10
else:
    fee = hours * 30

print("Parking Fee =", fee)
