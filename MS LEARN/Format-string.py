# Create the variables
## Start by creating three variables, name, gravity, and planet, and set them to the following values:

name = 'Ganymede'
planet = 'Mars'
gravity = '1.43'
# Create the template
## Now you will create the template to display the information about the moon.
template = """Gravity Facts about {name}
--------------------------
Planet Name = {planet}
Gravity on {name} = {gravity} m/s2"""
# Use the template
## With the template created, it's time to use it to display information about the moon! Use the format function on template to use the template and print the information. Set name, planet, and gravity to the appropriate values.
print(template.format(name=name, planet=planet, gravity=gravity))

#1. can leads to more erroe as it has the symbol and not flexible
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth" % mass_percentage)
#2. reduce error and increase clarity with the format dunction (.format)
print("On the Moon, you would weigh about {} of your weight on Earth"  .format(mass_percentage))
