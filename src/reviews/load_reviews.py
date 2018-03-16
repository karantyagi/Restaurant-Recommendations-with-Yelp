
### Code for Exploratory analysis and Data preprocessing

### How to run ? #####
# Keep review.json in same directory and run the command:
# $ python load_reviews.py "review.json"

'''
 REVIEW

{
  'business_id':        string, 22 character business id, maps to business in business.json
  'review_id':          string, 22 character unique review id
  'user_id':            string, 22 character unique user id, maps to the user in user.json
  'stars':              integer (star rating 1-5)
  'date':               string (date formatted YYYY-MM-DD)
  'text':               string (review text)
  'useful':             integer
  'funny':              integer
  'cool':               integer
}

'''

################################################################################

# Loading necessary libraries

print("\n LOADING DEPENDENCIES ...",end="")
import sys
import json
import csv
import pprint
from tqdm import tqdm
print(" DONE")
################################################################################

r = [] # valid restaurant business ids
ifilename = sys.argv[1]
ofilename1 = "reviews_restaurants.csv"
ofilename2 = "reviews_restaurants_text.csv"

flag = 50000      # No. of lines to be loaded
                     # max no. of instances :5261669

###############################################################################

### LOAD A FIXED NUMBER OF LINES (flag)

print("\n LOADING \"review.json\" DATA (1 LINE AT A TIME)...\n")
pbar = tqdm(total=flag)

msg = False
json_lines = []
f = open(ifilename,encoding = 'utf8')
for i in range(1,flag+1):
    l = f.readline()
    if(i > 5261669):
        msg = True
        break
    pbar.update(1)
    json_lines.append(json.loads( l.strip()))

pbar.close()
if msg == True:
    print("\n Overflow, but loading complete.")
print("\n No. of Reviews loaded            : ",len(json_lines))

print("\n LOADING COMPLETE.")
print("_________________________________________")

###############################################################################
