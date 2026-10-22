medical_cause = input("Did you have a medical cause? (Y/N):").strip().upper()

if medical_cause == "Y": 
    print("You are allowed")
else:
    atten = int(input("Enter the attendence of the student: ")) 
    if atten >=75: 
        print("Allowed")
    else:
        print("Not allowed")



units = int(input(" Please enter Number of UNits you Consumed :  "))

if(units < 50):
    amount = units * 2.60
    surcharge = 25

elif(units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35

elif(units <= 100):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 35

elif(units <= 200):
    amount = 130 + 162.50 + 526((units - 200) * 8.45)
    surcharge = 75

else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75

total = amount + surcharge
print("\n Electricity Bill", total)




