tax = 8.75

# User input
meal_cost = float(input("What was the meal cost? "))
meal_tip = float(input("What was the tip? (Press ENTER for 18%) ") or "18")

# Calculations
tip_perc = meal_tip / 100
tip_cost = meal_cost * tip_perc
meal_tax = meal_cost * (tax / 100)
meal_total = round(meal_cost + tip_cost + meal_tax, 2)

# Output
print("\n------- OUTPUT ---------")
print(f"Meal Cost: ${meal_cost}")
print(f"Tax amount: ${meal_tax:.2f}")
print(f"Tip amount: ${tip_cost:.2f}")
print(f"Meal Total: ${meal_total}")