
### Code for Exploratory analysis and Data preprocessing

### How to run ? #####
# Keep review.json in same directory and run the command:
# $ python analyze_review.py "review.json"



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

# Loading nscessary libraries

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

r = [] # valid restaurant business ids
ifilename = sys.argv[1]
ofilename1 = "reviews_restaurants.csv"
ofilename2 = "reviews_restaurants_text.csv"

flag = 200000         # No. of lines to be loaded
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

json_lines = []
f = open(ifilename,encoding = 'utf8')
for i in range(1,flag+1):
    l = f.readline()
    json_lines.append(json.loads( l.strip()))
    pbar.update(1)
#json_lines = [json.loads( l.strip() ) for l in open(ifilename).readlines() ]
pbar.close()
print("\n No. of Reviews loaded            : ",len(json_lines))

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

## loading valid Business IDs
load_restrnt("restaurants_total.csv")

print("\n LOADING COMPLETE.")
print("_________________________________________")

###############################################################################

print("\n WRITING PROCESS STARTED...")

OUT_FILE1 = open(ofilename1, "w")
root1 = csv.writer(OUT_FILE1)
root1.writerow(['review_id','business_id','user_id','text','stars'])
print("\n Column Headers added to "+ofilename1)

OUT_FILE2 = open(ofilename2, "w")
root2 = csv.writer(OUT_FILE2)
root2.writerow(['review_id','business_id','user_id','text','stars'])
print(" Column Headers added to "+ofilename2)

### print(" ",type(json_lines[0]),"\n") # type is dictionary
### print(json_lines[102])
# pprint.pprint(json_lines[101]) ##  type : dictionary
### pprint.pprint(type(json_lines[0]['stars'])) ##  type : dictionary

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
print("_________________________________________")
print("\n  2 Files created\n")
print(" \"",ofilename1,"\"      : Contains review data subset for Las Vegas")
print(" \"",ofilename2,"\" : Contains review data subset for Las Vegas with length 100-200")

#############################################################################

# Plotting Graphs

df = pd.DataFrame(
{'Length of Reviews (words)': list(text_length.keys()),
 'No. of Reviews': list(text_length.values())
})

#plot_line(df,list(df))

print(tabulate(df.head(10), headers=list(df), tablefmt='presto'))

'''
# style
plt.style.use('seaborn-darkgrid')

# density plot with shade
sns.kdeplot(review_length, shade=True, color="skyblue" )

# horizontal density plot
#sns.kdeplot(df['Length of Review Text'], shade=True, color="skyblue")


# histogram
#sns.distplot(df['Length of Review Text'])
# Add legend

red_line = mlines.Line2D([], [], color='blue', alpha=1, linewidth=2, label="Frequency of no. of words in review text")
plt.legend(loc=1, ncol=5, handles=[red_line])
red_patch = mpatches.Patch(color='red', label="deciding")
plt.legend(loc=1, ncol=2, handles=[red_patch])


# Add titles
plt.title("hbsjfhdsgjbgksjbdkjzgnskdn", loc='left', fontsize=12, fontweight=0, color='orange')
plt.xlabel("x")
plt.ylabel("Y")

#plt.xticks(df[str(header[0])] , rotation=45 )
plt.show(block=True)

#sns.plt.show()


#plot_line(df,list(df))
'''
###############################################################################

'''
json_no = 0
for l in json_lines:
 root1.writerow([l['review_id'],l['business_id'],l['user_id'],l['text'].encode("utf-8"),l['stars']])
 json_no += 1
 if(json_no == flag):
     break

print('\n Added {0} lines/reviews to '.format(json_no)+ofilename1)
'''

############################################################################


'''

def categories_vs_reviews():

    count = 0
    categories = dict()      ## value : A category (string)
    for l in json_lines:
     for category in l['categories']:
         if category not in categories:
             categories[category] = l['review_count']
         else:
             categories[category] += l['review_count']

     count += 1
     if(count == flag):
         break
    pprint.pprint(categories,width=2)

    # write dict to csv file

    FILE = open("business-categories-reviews.csv", "w")
     ## use this CSV directly for plotting visuals  on ipyhton notebook
    root = csv.writer(FILE)
    lines = 0
    for category in categories:
        root.writerow([category,categories[category]])
        lines +=1
    print('Finished {0} lines'.format(lines))
    FILE.close()


categories_vs_reviews()

'''
