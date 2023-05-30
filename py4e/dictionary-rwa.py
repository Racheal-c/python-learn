# Write a program to read through the mbox-short.txt and 
# figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times 
# they appear in the file. After the dictionary is produced,
# the program reads through the dictionary using a maximum loop to find the most prolific committer.
import os

script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
print(script_directory)
fname = input("Enter file name: ")

try:
    with open(fname) as fh:
        email_list = list()
        for line in fh:
            if line.startswith('From'):
                words = line.split()
                email = words[1]
                email_list.append(email)

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

except FileNotFoundError:
    print("File not found.")