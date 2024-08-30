isHelmetOn = True
isDrivingLicense = True
totalFineAmount = 0 
helmetFine = 450.50
licenseFine = 700 

print("Program to Calculate the Challan")
countWheels = int(input("Enter the no of wheels: "))
if countWheels == 2:
    if input("Is helmet on? ") == "No":
        isHelmetOn = False
        totalFineAmount = totalFineAmount + helmetFine

if input("Do you have driving license? ") == "No":
    isDrivingLicense = False
    totalFineAmount = totalFineAmount + licenseFine

if totalFineAmount > 0:
    print("Fine Receipt")
    if not isHelmetOn:
        print("Helmet Fine: Rs.",helmetFine)
    
    if not isDrivingLicense:
        print("License Fine: Rs.",licenseFine)
    
    print("Total fine Charged is Rs.",totalFineAmount)
else:
    print("No Violation")






        
