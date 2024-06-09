#  movie ticketts are priced based on age :12$ for adult (18 and over), $8 for childern. Everyone gets $2 discount on wednesday
age = int(input("enter age"))
day = "Wednesday"


price = 12 if age>= 18 else 8
if day == "Wednesday":
    price = price - 2

print( "Ticket price for you is $ ", price)