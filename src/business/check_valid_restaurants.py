## TO RUN THE PROGRAM:

# $ python check_valid_restaurants.py "valid_restaurants.csv"

################################################################################
# Loading necessary libraries

print("\n LOADING DEPENDENCIES ...",end="")

import sys
import json
import csv


print(" DONE")
################################################################################

filename = sys.argv[1]

# load file into a list
r = []
with open(filename, newline='\n') as f:
     reader = csv.reader(f)
     for row in reader:
         r.append(row[0])

print(" {} Restaurants loaded.".format(len(r)))
