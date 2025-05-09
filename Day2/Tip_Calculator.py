print("Welcome to the tip calculator!")

Total_Amount = input("What was the total bill? ")
Total_Amount = float(Total_Amount)

Tip = input("How much tip would you like to give? 12, 10 or 15 ")
Tip = float(Tip)

People_Paying = input("How many people to split the bill ")
People_Paying = float(People_Paying)

print(f"Each person should pay ${(Total_Amount * Tip / 100) / People_Paying:.2f}")