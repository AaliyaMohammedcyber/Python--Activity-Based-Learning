severity = input("Enter severity: ")
frequency = int(input("Enter frequency: "))#The times, the incident ouccured.
if severity == "High" or frequency > 3:
    print("Priority: Urgent")
else:
    print("Priority: Normal")
