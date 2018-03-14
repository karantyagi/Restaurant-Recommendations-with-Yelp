
### Code for Exploratory analysis and Data preprocessing

### How to run ? #####
# Keep business.json in same directory and run the command:
# $ python analyze_business.py "business.json"


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
}

'''

import time
import sys
import json
import csv
import pprint
import numpy as np
import pandas as pd
from tabulate import tabulate
from fig import *

flag = 175000 # max => 174567
restaurants = []

start_time = time.time()
print(" --- START TIME ---\n")

ifilename = sys.argv[1]
try:
 ofilename = sys.argv[2]
except:
 ofilename = ifilename + ".csv"

# LOAD DATA
# loading line by line
json_lines = [json.loads( l.strip() ) for l in open(ifilename,encoding = 'utf8').readlines() ]
print(" No. of Businesses : ",len(json_lines))
print("\n")

OUT_FILE = open(ofilename, "w")
root = csv.writer(OUT_FILE)
root.writerow(['business_id','categories','name', 'city', 'state', 'postal_code', 'latitude', 'longitude', 'stars', 'review_count'])
print(" 1 row added to csv - column names")


#print(" ",type(json_lines[0]),"\n") ## type : dictionary
#print(json_lines[102])
### pprint.pprint(json_lines[105]) ##  type : dictionary
### pprint.pprint(type(json_lines[0]['address'])) ##  type : dictionary
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

json_no = 0
for l in json_lines:
 root.writerow([l['business_id'].encode("utf-8"),l['categories'], l['name'].encode("utf-8"), l['city'].encode("utf-8"), l['state'].encode("utf-8"), l['postal_code'].encode("utf-8"), l['latitude'], l['longitude'], l['stars'], l['review_count']])
 json_no += 1
 if(json_no == flag):
     break

print('\n Added {0} lines/businesses to csv\n'.format(json_no))
OUT_FILE.close()


elapsed_time = time.time() - start_time
print(" HH:MM:SS")
print(time.strftime(" %H:%M:%S", time.gmtime(elapsed_time)))



def categories_vs_reviews():
    f1 = open("restaurants.csv", "w")
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
             print(" {} : {}".format(category,len(restaurants)),end="\r", flush=True)
         if category not in categories:
             categories[category] = l['review_count']
         else:
             categories[category] += l['review_count']
     count += 1
     if(count == flag):
         break
    ## pprint.pprint(categories,width=2)
    print("\n\n No. of unique categories : {} found in {} businesses/lines.".format(len(categories),count))

    # write dict to csv file

    FILE = open("business-categories-reviews.csv", "w")
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


    print("\n Completed writing to business-categories-reviews.csv.")
    print("\n Wrote {0} categories to file.".format(lines))
    FILE.close()
    f1.close()



    df = pd.DataFrame(
    {'Business Categories': list(range(1,len(categories)+1)),
     'No. of Reviews': reviews
    })



    print(df.shape)
    #pprint.pprint(df,width=3)
    #print(tabulate(df, headers=['Business categories','No.of Reviews'], tablefmt='psql'))
    print(list(df))

    top10 = df.sort_values(by=['No. of Reviews'], ascending=False)
    print("Top 10\n")
    print(tabulate(top10.head(5), headers=['Business Category','No.of Reviews'], tablefmt='presto'))

    ## plot_line(df,list(df))



#### making data frame
    '''check_restrnt("restaurants.csv")'''
    ### print(" Type categories : ",type(categories))
    ### pprint.pprint(reviews,width=2)

########################################################################################################

def check_restrnt(filename):
    # load file into a list
    r = []
    with open(filename, newline='\n') as f:
         reader = csv.reader(f)
         for row in reader:
             r.append(row[0])

    print("\n Restaurants Loaded : {}".format(len(r)))

    # print all those IDs which are in list

    print((' business_id').ljust(25)+
    ('city').ljust(15)+
    ('state').ljust(6))

    count_no = 0
    for l in json_lines:
        if l['business_id'] in r:

            print((" {} ".format(l['business_id']).ljust(25)+
            "{} ".format(l['city']).ljust(15)+
            "{} ".format(l['state']).ljust(6)))

        count_no += 1
        if(count_no == flag):
            break


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
    print("\n No. of States : {} found in {} instances/lines.".format(len(states),count))

    # write dict to csv file

    FILE = open("states-reviews.csv", "w")
     ## use this CSV directly for plotting visuals  on ipyhton notebook
    root = csv.writer(FILE)
    lines = 0
    reviews = []

    for state in states:
        root.writerow([state,states[state]])
        reviews.append(states[state])
        lines +=1


    print("\n Completed writing to states-reviews.csv.")
    print("\n Wrote {0} states to file.".format(lines))
    FILE.close()

    df_state = pd.DataFrame({"States": list(states.keys()),"No. of Reviews": reviews})
    #df_state = df.set_index(['States', 'No. of Reviews'])


    #print(df_state.head(5))
    print(df_state.shape)
    #pprint.pprint(df,width=3)
    #print(tabulate(df, headers=['Business categories','No. of Reviews'], tablefmt='psql'))
    print(list(df_state))
    #plot_line(df_state,list(df_state),list(categories.keys()))

    top10states = df_state.sort_values(by=['No. of Reviews'], ascending=False)
    print("Top 10 States\n")
    print(tabulate(top10states.head(10), headers=['No. of Reviews','State'], tablefmt='presto'))
    #### making data frame

    ### print(" Type categories : ",type(categories))
    ### pprint.pprint(reviews,width=2)

##########################################################################################


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
    print("\n\n No. of Cities : {} found in {} instances/lines.".format(len(cities),count))

    # write dict to csv file

    FILE = open("cities-reviews.csv", "w")
     ## use this CSV directly for plotting visuals  on ipyhton notebook
    root = csv.writer(FILE)
    lines = 0
    reviews = []

    for city in cities:
        root.writerow([city,cities[city]])
        reviews.append(cities[city])
        lines +=1


    print("\n Completed writing to cities-reviews.csv.")
    print("\n Wrote {0} cities to file.".format(lines))
    FILE.close()

    df = pd.DataFrame(
    {'Cities': list(cities.keys()),
     'No.of Reviews': reviews
    })



    print(df.shape)
    #print(tabulate(df.sort_values(by=['Cities'], ascending=False), headers=['City','No.of Reviews'], tablefmt='presto'))
    #print(tabulate(df, headers=['Business categories','No.of Reviews'], tablefmt='psql'))
    print(list(df))
    #plot_line(df,list(df),list(categories.keys()))

    top10cities = df.sort_values(by=['No.of Reviews'], ascending=False)
    print("Top 10 Cities\n")
    print(tabulate(top10cities.head(10), headers=['City','No.of Reviews'], tablefmt='presto'))
    #### making data frame

    ### print(" Type categories : ",type(categories))
    ### pprint.pprint(reviews,width=2)


start_time = time.time()
print(" --- START TIME ---\n")

categories_vs_reviews()
print("\n No. of Restaurants loaded: ",len(restaurants))
print("\n ==================================================================================================== \n")
state_vs_reviews()
print("\n ==================================================================================================== \n")

city_vs_reviews()

#city_vs_categories()

elapsed_time = time.time() - start_time
print("\n HH:MM:SS")
print(time.strftime(" %H:%M:%S", time.gmtime(elapsed_time)))
