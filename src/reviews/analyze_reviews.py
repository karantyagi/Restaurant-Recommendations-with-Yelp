
### Code for Exploratory analysis and Data preprocessing

## TO RUN THE PROGRAM:

# Keep review.json in same directory and run the command:
# $ python analyze_review.py "review.json"

################################################################################
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

import os
import sys
import json
import csv
import pprint
import time
from tabulate import tabulate
from tqdm import tqdm
from fig import *
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches

print(" DONE")
################################################################################

r = [] # valid restaurant business ids
ifilename = sys.argv[1]
ofilename1 = "reviews_restaurants.csv"
ofilename2 = "reviews_restaurants_text.csv"

flag = 60000       # No. of lines to be loaded
                     # max no. of instances :5261669

################################################################################

# Function to load all valid restaurant business_ids
# Valid business-ids are Catergoy :Reastaurants, City : Las Vegas

def load_restrnt(filename):
    global r
    with open(filename, newline='\n') as f:
         reader = csv.reader(f)
         for row in reader:
             r.append(row[0])
    print(" Restaurants (business_ids) Loaded : {}".format(len(r)))

###############################################################################

### LOAD ALL DATA AT ONCE

''' code for complete dataset
json_lines = [json.loads( l.strip() ) for l in open(ifilename,encoding = 'utf8').readlines() ]
print(" No. of Reviews: ",len(json_lines))
print("\n")
'''
##############################################################################

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
    json_lines.append(json.loads( l.strip()))
    pbar.update(1)
pbar.close()
if msg == True:
    print("\n Overflow, but loading complete.")
print("\n No. of Reviews loaded            : ",len(json_lines))

## loading valid Business IDs
load_restrnt("valid_restaurants.csv")

print("\n LOADING COMPLETE.")
print("__________________________________________________________________________________")

###############################################################################
# code to print types of each attribute
'''
print("\n --------------------------------")
print(' business_id     : ',type(json_lines[0]["business_id"]))
print(' review_id       : ',type(json_lines[0]["review_id"]))
print(' user_id         : ',type(json_lines[0]["user_id"]))
print(' text            : ',type(json_lines[0]["text"]))
print(' stars           : ',type(json_lines[0]["stars"]))
print(' useful          : ',type(json_lines[0]["useful"]))
print(' cool            : ',type(json_lines[0]["cool"]))
print(' funny           : ',type(json_lines[0]["funny"]))
print(" --------------------------------- \n")
'''
###############################################################################

print("\n WRITING PROCESS STARTED...")

os.makedirs(os.path.dirname("output/"+ofilename1), exist_ok=True)
os.makedirs(os.path.dirname("output/"+ofilename2), exist_ok=True)

OUT_FILE1 = open("output/"+ofilename1, "w")
root1 = csv.writer(OUT_FILE1)
root1.writerow(['review_id','business_id','user_id','text','stars'])
print("\n Column Header added to "+ofilename1)

OUT_FILE2 = open("output/"+ofilename2, "w")
root2 = csv.writer(OUT_FILE2)
root2.writerow(['review_id','business_id','user_id','text','stars'])
print(" Column Header added to "+ofilename2)

valid_reviews = 0
valid_small_reviews = 0
text_length = dict()
review_length = []
print("\n")
pbar = tqdm(total=flag)
for l in json_lines:
    review_length.append(len(l['text']))
    if len(l['text']) not in text_length:
        text_length[len(l['text'])] = 1
    else:
        text_length[len(l['text'])] += 1

    if l['business_id'] in r:
        root1.writerow([l['review_id'],l['business_id'],l['user_id'],l['text'].encode("utf-8"),l['stars']])
        #print(" Text length : ",len(l['text']))
        if len(l['text']) >=100 and len(l['text']) <= 200:
            #print(" Text length : ",len(l['text']))
            root2.writerow([l['review_id'],l['business_id'],l['user_id'],l['text'].encode("utf-8"),l['stars']])
            valid_small_reviews += 1
        valid_reviews +=1
    pbar.update(1)

pbar.close()
print("\n")
print(" No. of Restaurant Reviews in Las Vegas        : ",valid_reviews)
print(" No. of Restaurant Reviews with length 100-200 : ",valid_small_reviews)
print(" text_length list created, size : ",len(text_length))

OUT_FILE1.close()
OUT_FILE2.close()

print("\n WRITING COMPLETE.")
print("__________________________________________________________________________________")
print("\n OUTPUT : 2 new files\n")
print(" \"",ofilename1,"\"      : Contains review data subset for Las Vegas")
print(" \"",ofilename2,"\" : Contains review data subset for Las Vegas with length 100-200")
print("__________________________________________________________________________________")

#############################################################################

# TOP 100 review Text Lengths

df = pd.DataFrame(
{'Length of Review text (words)': list(text_length.keys()),
 'No. of Reviews': list(text_length.values())
})
###print(df.shape)
#pprint.pprint(df,width=3)
#print(tabulate(df, headers=['States','No. of Reviews'], tablefmt='psql'))
### print(list(df))
title = "Frequency of no. of reviews according to states"
header = list(df)
#plot_line(df[str(header[1])],df[str(header[0])],str(header[1]),str(header[0]),title,str(header[0]))

top30len = df.sort_values(by=['No. of Reviews'], ascending=False)
print("\n Top 30 Review Text Lengths (no. of words)\n")
print(tabulate(top30len.head(100), headers=['Review text length','No. of reviews']))
print("\n Total no. of reviews : ",len(review_length))
print(" Review text lengths   :",len(text_length.keys()))
print("__________________________________________________________________________________")
