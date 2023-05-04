# Raise exception
# Creating a utility to convert strings to boolean values
true_values = ['yes', 'y']
false_values = ['no', 'n']

# Create the function to test for true or false
def str_to_bool (value):
    value = value.lower()
    if value in true_values:
        return True
    elif value in false_values:
        return False
    else:
        raise ValueError('Invalid Entry')
    
# Test function here
# Call the function 
str_to_bool('y')