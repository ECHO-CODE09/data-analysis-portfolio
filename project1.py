#weight converter

weight = float(input("Enter weight: "))
unit = input("(K)g or (L)bs: ").upper()

def kg_to_lbs(kg):
    return kg * 2.20462

def lbs_to_kg(lbs):
    return lbs / 2.20462

if unit == "K":
    print("Weight in lbs:", kg_to_lbs(weight))
elif unit == "L":
    print("Weight in kg:", lbs_to_kg(weight))
else:
    print("Invalid unit")
