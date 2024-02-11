planet_conversions = {'Sun': 27.01,
                      'Mercury': 0.38,
                      'Venus': 0.91,
                      'Earth': 1,
                      'Moon': 0.166,
                      'Mars': 0.38,
                      'Jupiter': 2.34,
                      'Saturn': 1.06,
                      'Uranus': 0.92,
                      'Neptune': 1.19,
                      'Pluto': 0.06}

user_weight = int(input("What is your Earthly weight? "))
print("-" * 35)

for planet in planet_conversions:
    weight_formula = user_weight * planet_conversions[planet]
    print(f"Your weight on {planet} would be {weight_formula:.2f}")