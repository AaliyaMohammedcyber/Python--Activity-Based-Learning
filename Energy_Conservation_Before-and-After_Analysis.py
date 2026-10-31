before = int(input("Enter previous usage: "))
after = int(input("Enter current usage: "))
savings = before - after
if savings > 0:
    print("Energy Saved =", savings)
else:
    print("No energy savings")
  
