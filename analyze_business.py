
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


import sys
import json
import csv
import pprint

flag = 100

ifilename = sys.argv[1]
try:
 ofilename = sys.argv[2]
except:
 ofilename = ifilename + ".csv"

# LOAD DATA
# loading line by line
json_lines = [json.loads( l.strip() ) for l in open(ifilename).readlines() ]

print(len(json_lines))

OUT_FILE = open(ofilename, "w")
root = csv.writer(OUT_FILE)
root.writerow(['business_id','categories','name'])



print(" ",type(json_lines[0]),"\n")
#print(json_lines[102])
pprint.pprint(json_lines[105]) ##  type : dictionary
pprint.pprint(type(json_lines[0]['address'])) ##  type : dictionary
print("\n -----------------------------------------------")
print("Address         : ",type(json_lines[0]['address']))
print('business_id     : ',type(json_lines[0]["business_id"]))
print('name            : ',type(json_lines[0]["name"]))
print('neighborhoods   : ',type(json_lines[0]["neighborhood"]))
print('city            : ',type(json_lines[0]["city"]))
print('state           : ',type(json_lines[0]["state"]))
print('postal_code     : ',type(json_lines[0]["postal_code"]))
print('latitude        : ',type(json_lines[0]["latitude"]))
print('longitude       : ',type(json_lines[0]["longitude"]))
print('stars           : ',type(json_lines[0]["stars"]))
print('review_count    : ',type(json_lines[0]["review_count"]))
print('categories      : ',type(json_lines[0]["categories"]))
print('is_open         : ',type(json_lines[0]["is_open"]))
print("\n -----------------------------------------------")

json_no = 0
for l in json_lines:
 root.writerow([l['business_id'],l['categories'], l['name']])
 json_no += 1
 if(json_no == flag):
     break

print('Finished {0} lines'.format(json_no))
OUT_FILE.close()


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
