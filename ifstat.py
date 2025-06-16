weight=float(input("enter weight: "))
metric= input("(k)g or (l)bs: ")

if metric=="l" or metric =="L":
    print(str(weight/2.20462) + " Kgs") 
elif metric=="k" or metric=="K":
    print(str(weight*2.20462) + " lbs")
else:
    print("Invalid Input")
