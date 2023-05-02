# Learning module: https://learn.microsoft.com/en-us/training/modules/functions-python/6-variable-arguments
#using variable keyword arguments (**)in the function named fuel_report
def fuel_report(**fuel_tanks):
    # Use for loop to print the output
    for name, value in fuel_tanks.items():
        output = f"{name}: {value}"
        print(output)

fuel_report(main=50, external=100, emergency=60)