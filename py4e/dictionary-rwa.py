# Write a program to read through the mbox-short.txt and 
# figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times 
# they appear in the file. After the dictionary is produced,
# the program reads through the dictionary using a maximum loop to find the most prolific committer.

# This code is getting the absolute path of the current script file and then getting the directory
# path of the script file using the `os` module. It then prompts the user to enter a file name to be
# used later in the program.
import os

script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
print(script_directory)
fname = input("Enter file name: ")

# This code is trying to open a file with the name specified by the user and read its contents. It
# then loops through each line in the file and checks if the line starts with the string 'From'. If it
# does, it splits the line into words and extracts the second word, which is assumed to be the email
# address of the sender. The email address is then added to a list called `email_list`.
try:
    with open(fname) as fh:
        email_list = list()
        for line in fh:
            if line.startswith('From'):
                words = line.split()
                email = words[1]
                email_list.append(email)

       # This code is creating a dictionary called `histogram` and looping through each email address
       # in the `email_list`. For each email address, it is adding an entry to the `histogram`
       # dictionary with the email address as the key and the value as the count of how many times
       # that email address appears in the `email_list`. If the email address already exists in the
       # `histogram` dictionary, the count is incremented by 1 using the `get()` method to retrieve
       # the current count and adding 1 to it.
        histogram = dict()
        for email in email_list:
            histogram[email] = histogram.get(email, 0) + 1

        largest = None
        count = None
        for k, v in histogram.items():
            if count is None or v > count:
                count = v
                largest = k

        print(largest, count)

# The `except FileNotFoundError:` block is handling the case where the file specified by the user does
# not exist in the current directory. If the file is not found, it prints the message "File not
# found." to the console.
except FileNotFoundError:
    print("File not found.")