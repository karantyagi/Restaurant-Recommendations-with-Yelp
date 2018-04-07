
### Code for Exploratory analysis and Data preprocessing

## TO RUN THE PROGRAM:

# Keep business.json in same directory and run the command:
# $ python analyze_business.py "business.json"

################################################################################
'''
 BUSINESS
{
  'business_id':            (encrypted business id),
  'name':                   (business name),
  'neighborhoods':          [(hood names)],
  'full_address':           (localized address),
  'city':                   (city),
  'state':                  (state),
  'latitude':               latitude,
  'longitude':              longitude,
  'stars':                  (star rating, rounded to half-stars),
  'review_count':           review count,
  'categories':             [(localized category names)]
  'open':                   1/0 (corresponds to permanently closed, not business hours),
  'attributes':             {"RestaurantsTakeOut": true,
                                "BusinessParking":
                                {   "garage": false,
                                    "street": true,
                                    "validated": false,
                                    "lot": false,
                                    "valet": false }
                            }
'''
################################################################################
# Loading necessary libraries

print("\n LOADING DEPENDENCIES ...",end="")

import sys
import os
import json
import csv
import pprint
from tabulate import tabulate
from tqdm import tqdm
from fig import *
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches

print(" DONE")
################################################################################
restaurants = []  # list to collect valid restaurant business ids

flag = 174567          # No. of lines to be loaded
                      # max no. of instances : 174567

ifilename = sys.argv[1]
ofilename = "business_full_all_attr.csv"
###############################################################################

### LOAD ALL DATA AT ONCE

''' code for complete dataset
json_lines = []
json_lines = [json.loads( l.strip() ) for l in open(ifilename,encoding = 'utf8').readlines() ]
print(" No. of Businesses/intances : ",len(json_lines))
print("\n")
'''
##############################################################################

### LOAD A FIXED NUMBER OF LINES (flag)

print("\n LOADING \"business.json\" DATA (1 LINE AT A TIME)...\n")
pbar = tqdm(total=flag)

msg = False
json_lines = []
f = open(ifilename,encoding = 'utf8')
for i in range(1,flag+1):
    l = f.readline()
    if(i > 174567):
        msg = True
        break
    pbar.update(1)
    json_lines.append(json.loads( l.strip()))
pbar.close()

if msg == True:
    print("\n Overflow, but loading complete.")
print("\n No. of Businesses loaded         : ",len(json_lines))

print("\n LOADING COMPLETE.")
print("__________________________________________________________________________________")

###############################################################################
# code to print types of each attribute
'''
print("\n -----------------------------------------------")
print(" Address         : ",type(json_lines[0]['address']))
print(' business_id     : ',type(json_lines[0]["business_id"]))
print(' name            : ',type(json_lines[0]["name"]))
print(' neighborhoods   : ',type(json_lines[0]["neighborhood"]))
print(' city            : ',type(json_lines[0]["city"]))
print(' state           : ',type(json_lines[0]["state"]))
print(' postal_code     : ',type(json_lines[0]["postal_code"]))
print(' latitude        : ',type(json_lines[0]["latitude"]))
print(' longitude       : ',type(json_lines[0]["longitude"]))
print(' stars           : ',type(json_lines[0]["stars"]))
print(' review_count    : ',type(json_lines[0]["review_count"]))
print(' categories      : ',type(json_lines[0]["categories"]))
print(' is_open         : ',type(json_lines[0]["is_open"]))
print("\n -----------------------------------------------")
'''

print(' attributes         : ',type(json_lines[0]["attributes"]))
###############################################################################

print("\n WRITING PROCESS STARTED...")

os.makedirs(os.path.dirname("output/"+ofilename), exist_ok=True)

OUT_FILE = open("output/"+ofilename, "w")
root = csv.writer(OUT_FILE)
root.writerow((['business_id','categories','name', 'city', 'state',
 'postal_code', 'latitude', 'longitude', 'stars', 'review_count', 'attributes']))
print("\n Column Header added to "+ofilename)

pbar = tqdm(total=flag)
json_no = 0
for l in json_lines:
 root.writerow(([l['business_id'].encode("utf-8"),l['categories'],
 l['name'].encode("utf-8"), l['city'].encode("utf-8"),
 l['state'].encode("utf-8"), l['postal_code'].encode("utf-8"),
 l['latitude'], l['longitude'], l['stars'], l['review_count'],
 l['attributes']]))
 pbar.update(1)
 json_no += 1
 if(json_no == flag):
     break

pbar.close()
print('\n Added {0} lines/businesses to csv'.format(json_no))
OUT_FILE.close()

print(" "+ofilename+" completed.")
print("\n WRITING COMPLETE.")
print("__________________________________________________________________________________")

###############################################################################

# Print Top 10 categories and plot the result

def categories_vs_reviews():
    f1 = open("output/valid_restaurants.csv", "w")
    f1_root = csv.writer(f1)
    global restaurants
    count = 0
    categories = dict()      ## value : A category (string)
    for l in json_lines:
     for category in l['categories']:
         if (str(category) == "Restaurants"
         and l['city'] == "Las Vegas"
         and l['business_id'] not in restaurants):
             restaurants.append(l['business_id'])
             f1_root.writerow([l['business_id']])
             print(" {} found: {}".format(category,len(restaurants)),end="\r", flush=True)
         if category not in categories:
             categories[category] = l['review_count']
         else:
             categories[category] += l['review_count']
     count += 1
     if(count == flag):
         break
    print("\n Unique business categories : {} found among {} businesses/instances.".format(len(categories),count))

    # write dict to csv file

    FILE = open("output/business-categories-reviews.csv", "w")
     ## use this CSV directly for plotting visuals  on ipyhton notebook
    root = csv.writer(FILE)
    lines = 0
    reviews = []
    result_array = np.array([])
    for category in categories:
        root.writerow([category,categories[category]])
        reviews.append(categories[category])
        lines +=1
        result_array = np.append(result_array,[lines,categories[category]])


    print(" Completed writing to business-categories-reviews.csv.")
    print(" Wrote {0} categories to file.".format(lines))
    FILE.close()
    f1.close()

    ## PLOTTING Data

    df = pd.DataFrame(
    {'Business Categories': list(range(1,len(categories)+1)),
     'No. of Reviews': reviews
    })

    ###print(df.shape)
    #pprint.pprint(df,width=3)
    #print(tabulate(df, headers=['Business categories','No.of Reviews'], tablefmt='psql'))
    ### print(list(df))

    header = list(df)
    title = "Frequency of no. of reviews according to business categories"
    plot_line(df[str(header[0])],df[str(header[1])],str(header[0]),str(header[1]),title,str(header[1]))

    top10 = df.sort_values(by=['No. of Reviews'], ascending=False)
    print("\n Top 10 Business Categories\n")
    print(tabulate(top10.head(5), headers=['Business Category','No.of Reviews'], tablefmt='presto'))

print("\n BUSINESS CATEGORIES v/s NO. OF REVIEWS\n")
categories_vs_reviews()
print("__________________________________________________________________________________")

########################################################################################################


def state_vs_reviews():
    count = 0
    states = dict()      ## value : A category (string)
    for l in json_lines:
        if l['state'] not in states:
            states[l['state']] = l['review_count']
        else:
            states[l['state']] += l['review_count']
        count += 1
        if(count == flag):
            break
    ## pprint.pprint(categories,width=2)
    #print("\n No. of States : {} found in {} instances/lines.".format(len(states),count))
    print(" No. of States : {} ".format(len(states)))
    # write dict to csv file

    FILE = open("output/states-reviews.csv", "w")
     ## use this CSV directly for plotting visuals  on ipyhton notebook
    root = csv.writer(FILE)
    lines = 0
    reviews = []

    for state in states:
        root.writerow([state,states[state]])
        reviews.append(states[state])
        lines +=1


    print(" states-reviews.csv created.")
    print(" Wrote {0} states to file.".format(lines))
    FILE.close()

    ## PLOTTING Data
    df = pd.DataFrame(
    {'No. of Reviews': reviews,
     'States': list(range(1,len(states)+1))
    })

    ###print(df.shape)
    #pprint.pprint(df,width=3)
    #print(tabulate(df, headers=['States','No. of Reviews'], tablefmt='psql'))
    ### print(list(df))
    title = "Frequency of no. of reviews according to states"
    header = list(df)
    plot_line(df[str(header[1])],df[str(header[0])],str(header[1]),str(header[0]),title,str(header[0]))

    top10states = df.sort_values(by=['No. of Reviews'], ascending=False)
    print("\n Top 10 States\n")
    print(tabulate(top10states.head(10), headers=['No. of Reviews','State'], tablefmt='presto'))
    #### making data frame

    ### print(" Type categories : ",type(categories))
    ### pprint.pprint(reviews,width=2)

print("\n STATES v/s NO. OF REVIEWS\n")
state_vs_reviews()
print("__________________________________________________________________________________")
##########################################################################################

# Function to
def city_vs_reviews():
    count = 0
    cities = dict()      ## value : A category (string)
    for l in json_lines:
        if l['city'] not in cities:
            cities[l['city']] = l['review_count']
        else:
            cities[l['city']] += l['review_count']
        count += 1
        if(count == flag):
            break
    ## pprint.pprint(categories,width=2)
    print(" No. of Cities : {}.".format(len(cities),count))

    # write dict to csv file

    FILE = open("output/cities-reviews.csv", "w")
     ## use this CSV directly for plotting visuals  on ipyhton notebook
    root = csv.writer(FILE)
    lines = 0
    reviews = []

    for city in cities:
        root.writerow([city,cities[city]])
        reviews.append(cities[city])
        lines +=1


    print(" cities-reviews.csv created.")
    print(" Wrote {0} cities to file.".format(lines))
    FILE.close()

    ## PLOTTING Data
    df = pd.DataFrame(
    {'No. of Reviews': reviews,
     'Cities': list(range(1,len(cities)+1))
    })

    ###print(df.shape)
    #pprint.pprint(df,width=3)
    #print(tabulate(df, headers=['States','No. of Reviews'], tablefmt='psql'))
    ### print(list(df))
    title = "Frequency of no. of reviews according to Cities"
    header = list(df)
    plot_line(df[str(header[0])],df[str(header[1])],str(header[0]),str(header[1]),title,str(header[1]))

    top10cities = df.sort_values(by=['No. of Reviews'], ascending=False)
    print("\n Top 10 Cities\n")
    print(tabulate(top10cities.head(10), headers=['City','No. of Reviews'], tablefmt='presto'))
    #### making data frame
    ### print(" Type categories : ",type(categories))
    ### pprint.pprint(reviews,width=2)

print("\n CITIES v/s NO. OF REVIEWS\n")
city_vs_reviews()
print("__________________________________________________________________________________")
##########################################################################################

print("\n SUMMARY")
print(" No. of Businesses(restaurants) in Las Vegas : ",len(restaurants))
print("\n OUTPUT : 5 new files created in \'output\' folder\n")
print(" valid_restaurants.csv            : business_ids of all valid restaurants, contains 1 column")
print(" busines_full.csv                 :  Business.json in csv format")
print(" business-categories-reviews.csv  : Contains 2 columns - business category, no. of reviews")
print(" states-reviews.csv               : Contains 2 columns - state, no. of reviews")
print(" cities-reviews.csv               : Contains 2 columns - city, no. of reviews")
print("__________________________________________________________________________________")

###############################################################################
#  CHECK ALL VALID RESTAURANTS
'''
print("\n Restaurants : {} \n".format(len(restaurants)))

print((' business_id').ljust(25)+
('city').ljust(15)+
('state').ljust(6)+" Category\n")

count_no = 0
for l in json_lines:
    if l['business_id'] in restaurants:
        for category in l['categories']:
            if str(category) == "Restaurants" :
                print((" {} ".format(l['business_id']).ljust(25)+
                "{} ".format(l['city']).ljust(15)+
                "{} ".format(l['state']).ljust(6)+
                " Restaurants"))
    count_no += 1
    if(count_no == flag):
        break
'''
###############################################################################
