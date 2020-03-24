my_name = 'Dale C. Schulz'
my_age = 58 # not a lie
my_height = 71 # inches
my_weight = 153 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Blonde'
my_kg_weight = my_weight * .453592
my_cm_height = my_height * 2.54

print()
print()
print(f"Let's talk about {my_name}.")
print(f"He is {my_age} years old.")
print(f"He's {my_height} inches tall.")
print(f"That is {my_cm_height} centimeters.")
print(f"He's {my_weight} pounds heavy.")
print(f"That is {my_kg_weight} kilograms.")
print("He needs to lose about 5 pounds.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
print()
print()