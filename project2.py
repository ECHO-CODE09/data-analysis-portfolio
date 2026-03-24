#Temperature Converter 
Temp = float(input("Enter the temperature: "))
unit = input("K or F: ").upper()
def K_to_F(K):
    return (K - 273.15) * 9/5 + 32
def F_to_K(F):
    return (F - 32) * 5/9 + 273.15

if unit == "K":
    print(f"Temperature in Fahrenheit:{K_to_F(Temp):.2f}°F")
elif unit == "F":
    print(f"Temperature in Kelvin:{F_to_K(Temp):.2f}°K")
else:
    print("Invalid unit")
