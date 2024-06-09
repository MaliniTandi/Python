# classify a person age group : child(<13); teenager(13-19); Adult(20-59);senior(60+).
age = int(input("Enter age in numbers"))




if age < 13:
    print("child")

elif age <20:
    print("Teenager")

elif age < 60:
    print("Adult") 

else:
    print("senior")   