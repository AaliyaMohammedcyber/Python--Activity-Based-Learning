capacity = int(input("Enter bus capacity: "))
stops = int(input("Enter number of stops: "))
passengers = 0
for i in range(1, stops + 1):
    boarded = int(input("Passengers boarded: "))
    left = int(input("Passengers left: "))
    passengers = passengers + boarded - left
    if passengers > capacity:
        print("Capacity exceeded!")
    else:
        print("Current passengers:", passengers)
