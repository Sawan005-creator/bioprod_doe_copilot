from itertools import product


def generate_combinations(variables):
    names = list(variables.keys())
    levels = list(variables.values())

    combinations = product(*levels)

    for combination in combinations:
        result = []

        for i in range(len(names)):
            result.append(f"{names[i]}={combination[i]}")

        print(", ".join(result))


# Ask how many variables
n = int(input("Enter number of variables (2 or 3): "))

variables = {}

for i in range(n):
    name = input(f"\nEnter name of variable {i + 1}: ")
    low = input(f"Enter LOW value for {name}: ")
    high = input(f"Enter HIGH value for {name}: ")

    variables[name] = [low, high]


print("\nFactorial combinations:")
generate_combinations(variables)