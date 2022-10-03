from math import pi

first_radius = (float(input("Sat the first planet's radius: "))) * 10**6
second_radius = (float(input("Sat the second planet's radius: "))) * 10**6

first_planet_speed = float(input("Sat the first planet's speed: "))
second_planet_speed = float(input("Sat the first planet's speed: "))

first_planet_year = (2 * first_radius * pi) / first_planet_speed
second_planet_year = (2 * second_radius * pi) / second_planet_speed

print("Year length on the first planet:", first_planet_year)
print("Year length on the second planet:", second_planet_year)


print("Is that right: the year on the first planet is longer?")
print(first_planet_year > second_planet_year)
