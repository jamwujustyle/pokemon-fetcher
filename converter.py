weight = float(input("enter your weight: "))
unit = input("Kilograms or Pounds? (l or k)").lower()

if unit == "k":
    weight *= 2.205
    unit = "lbs"
elif unit == "l":
    weight / 2.205
    unit = "kgs"
else:
    print(f"{unit} was not valid")

print(f"{round(weight, 1)} {unit}")
