Score = int(input("Enter marks "))
if Score >= 101:
    print("Verfiy Your grade again")
    exit()


if Score >=90:
    print("Your Grade is A Congrats!")

elif Score >= 80:
    print("Your Grade is B Congrats!")

elif Score >= 70:
    print("Your Grade is C , Can do better!")

elif Score >=60:
    print("Your Grade is D , Need to work hard !")

else:
    print("Sorry better luck next time")
    