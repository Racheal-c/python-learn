# Create and modify a Python dictionary
## Managing planet data
### You want to create a program which will store and display information 
### about planets. To start you will use one planet. 
### Create a variable named planet. Store the following values as a dictionary:

planet = {'name': 'Mars', 'moons':'2'}

#Display planet data
## With the variable created, you will now display information. 
## You can retrieve information by either using get or square brackets ([ ]) 
# and the key name. Add the code to display the planet information in the following format: has moon(s)
## If you were working with Earth, the output would be Earth has 1 moon(s)
print(planet['name'] + 'has' + planet['moons'] + 'moons(s)')
#using f' for formatting string literals need to use {} and "" for string
print(f'{planet["name"]} has {planet["moons"]} moons(s)')

#Add circumference information
## You can update existing keys or create new ones by either using the update method or using square brackets ([ ]). When you're using update, you pass in a new dictionary object with the updated or new values. When using square brackets, you specify the key name and assign a new value.
##Add a new value to planet with a key of 'circumference (km)'. 
##This new value should store a dictionary with the planet's two circumferences:
planet['circumference(km)']={
    'polar': 6752,
    'equatorial': 6792
    }
print(f'{planet["name"]} has a polar circumference of {planet["circumference(km)"]["polar"]}')
