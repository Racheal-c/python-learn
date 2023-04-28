#You will use a Jupyter notebook to create your first program. 
#Your senior officer wants you to create code to perform a couple of utilities. 
#You will start by displaying today's date. 
#Then you will add code to convert parsecs to lightyears.

#Creating reusable applications
#Having a program with hard-coded values limits its flexibility. 
#Your first officer likes the program you built to convert parsecs to lightyears, but wants the ability to specify a value for parsecs. She wants you to create a program which can accept user input.

#Display today's date
from datetime import date
print(date.today())

#Converting parsecs to light years
#1 parsec = 3.26 light years
parsecs_input = input(" Input number of parsecs: ")
parsecs = int(parsecs_input)
lightyears = parsecs * 3.26

#Display the result
print(parsecs_input + " parsecs is " + str(lightyears) + " light years. ")