number_1 = int(input("What is your first number?"))
number_2 = int(input("What is your second number?"))

if number_1 > number_2:
    print("Your frst number is greater.")
else:
    print("Your second number is greater.")




percent = int(input("What is your percentage?"))

if percent >= 90 or percent <= 100:
    print("Grade A")
elif percent >= 80 or percent <= 89:
    print("Grade B")
elif percent >= 70 or percent <= 79:
    print("Grade C")
else :
    print("Grade D/Needs improvment.")



age = int(input("How old are you?"))
is_student = bool(input("Are you a student"))

if age < 18:
    if is_student:
        print("The price is $8.")

    else:
        print("The price is $10.")

else:
    if is_student:
        print("The price is $12")
    else:
        print("The price is $15.")

    

