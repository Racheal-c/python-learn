# Configuration file
loaded_config = """# Rocket Ship Configuration File!
fuel_tanks=4
oxygen_tanks=3
initial_propulsion_level=84
$ End of file"""
# Parse the confuguration info
# Create an empty dictionary to hold the parsed configuration
parsed_config = {}
# for loop to iterate over each line and split it on equals sign
for line in loaded_config.split('\n'):
    try:
        key, value = line.split('=')
        parsed_config[key] = value
    except ValueError:
        print(f'Unable to parse {line}')
print(parsed_config)
# Notes
# parsed_config = {}
# def loaded_config(path):
#     for split('\n') in parsed_config:
#         print("Unable to parse:)")