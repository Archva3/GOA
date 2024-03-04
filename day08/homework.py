required_weight, required_height = 50, 170
user_weight = float(input("Enter your weight: "))

print("Weight equality check:", user_weight == required_weight)
print("Height equality check:", input("Enter your height: ") == required_height)

print("\nWeight and height comparison:")
print("User's weight > Required weight:", user_weight > required_weight)
print("User's weight < Required weight:", user_weight < required_weight)
print("User's height > Required height:", float(input("Enter your height: ")) > required_height)
print("User's height < Required height:", float(input("Enter your height: ")) < required_height)




required_pull_ups = 10
required_sit_ups = 15

pull_ups = int(input("Enter the number of pull-ups: "))
sit_ups = int(input("Enter the number of sit-ups: "))

print("Checking if the number of pull-ups or sit-ups matches the required quantity:")
print("Number of pull-ups equals required pull-ups:", pull_ups == required_pull_ups)
print("Number of sit-ups equals required sit-ups:", sit_ups == required_sit_ups)