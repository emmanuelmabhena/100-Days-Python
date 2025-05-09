print("Welcome to BMI calculator")

Weight = input("What is your weight in Kilograms? ")
Weight = float(Weight)

Height = input("What is your height in Metres? ")
Height = float(Height)

print(f"Your BMI is {Weight/Height**2:.2f}")