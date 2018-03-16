
### Code for Exploratory analysis and Data preprocessing

## TO RUN THE PROGRAM:

# Keep review.json in same directory and run the command:
# $ python plot_review.py "review.json"

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

flag = 500155      # No. of lines to be loaded
                     # max no. of instances :5261669

################################################################################

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

print("\n LOADING COMPLETE.")
print("__________________________________________________________________________________")

###############################################################################
print("\n CALCULATING ... ")

valid_reviews = 0
valid_small_reviews = 0
text_length = dict()
text_rating = dict()
review_length = []
ratings =[]
print("\n")
pbar = tqdm(total=flag)
for l in json_lines:
    review_length.append(len(l['text']))
    ratings.append(l['stars'])
    if len(l['text']) not in text_length:
        text_length[len(l['text'])] = 1
        text_rating[len(l['text'])] = l['stars']
    else:
        text_length[len(l['text'])] += 1
    pbar.update(1)

pbar.close()
print("\n CACLULATING COMPLETE.")

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
print(tabulate(top30len.head(10), headers=['Review text length','No. of reviews']))
print("\n Total no. of reviews : ",len(review_length))
print(" Review text lengths   :",len(text_length.keys()))
print("__________________________________________________________________________________")

# TOP 100 review Text Lengths

dfr = pd.DataFrame(
{'Length of Review text (words)': list(text_rating.keys()),
 'Rating': list(text_rating.values())
})
###print(df.shape)
#pprint.pprint(df,width=3)
#print(tabulate(df, headers=['States','No. of Reviews'], tablefmt='psql'))
### print(list(df))
title = "Frequency of no. of reviews according to states"
rheader = list(dfr)
#plot_line(df[str(header[1])],df[str(header[0])],str(header[1]),str(header[0]),title,str(header[0]))

top30 = dfr.sort_values(by=['Rating'], ascending=False)
print("\n Top 30 Review Text Lengths (no. of words)\n")
print(tabulate(top30.head(10), headers=['Review text length','Rating']))
print("__________________________________________________________________________________")

# print(len(ratings))
star_ratings = pd.DataFrame(ratings, columns = ["Stars"])
print((star_ratings["Stars"].value_counts()))

# Create data

height = star_ratings["Stars"].value_counts()
bars = ('1-star','2-star','3-star','4-star','5-star')

y_pos = np.arange(len(bars))

plt.style.use('seaborn-darkgrid')
plt.title("Distribution of ratings", loc='left', fontsize=12, fontweight=0, color='orange')
# Create bars
plt.bar(y_pos, height)

# Create names on the x-axis
plt.xticks(y_pos, bars)
plt.xlabel('Ratings', fontweight=1, fontsize='12')
plt.ylabel("Review count")
plt.show(block=True)

###############################################################################
# PLOTTING GRAPHS
###############################################################################

'''DISTRIBUTION OF REVIEW TEXT LEHGTH - DENSITY PLOT '''

def length_density():
    # style
    plt.style.use('seaborn-darkgrid')
    # density plot with shade
    sns.kdeplot(review_length, shade=True, color="skyblue" )
    # Add legend
    blue_line = mlines.Line2D([], [], color='skyblue', alpha=0.9, linewidth=2, label="Frequency of no. of words in review text")
    plt.legend(loc=1, ncol=5, handles=[blue_line])
    #red_patch = mpatches.Patch(color='red', label="deciding")
    #plt.legend(loc=1, ncol=2, handles=[red_patch])
    # Add titles
    plt.title("Frequency of Review text length", loc='left', fontsize=12, fontweight=0, color='orange')
    plt.xlabel("Review text length (in words)")
    plt.ylabel("Proportion of reviews")
    ### <extra code> plt.xticks(df[str(header[0])] , rotation=45 )
    plt.show(block=True)

'''length_density()'''

###############################################################################

'''DISTRIBUTION OF REVIEW TEXT LENGTH VS NO.OF REVIEWS - CONTOUR DENSITY PLOT '''
# Plotting density plot for visualizing distribution of review text length v/s rating

def length_vs_reviews1():
    # style
    plt.style.use('seaborn-darkgrid')
    # density plot with shade
    sns.regplot(x=df[header[0]], y=df[header[1]], fit_reg=False, scatter_kws={"color":"darkred","alpha":0.7,"s":0.03})

    #sns.kdeplot(df[header[0]], df[header[1]], cmap="Blues", shade=True, bw=.15)
    # Add legend
    # blue_line = mlines.Line2D([], [], color='skyblue', alpha=0.9, linewidth=2, label="Frequency of no. of words in review text")
    # plt.legend(loc=1, ncol=5, handles=[blue_line])
    #red_patch = mpatches.Patch(color='red', label="deciding")
    #plt.legend(loc=1, ncol=2, handles=[red_patch])
    # Add titles
    plt.title("Distribution of Review length w.r.t number of reviews", loc='left', fontsize=12, fontweight=0, color='orange')
    plt.xlabel("Review Length (word count)")
    plt.ylabel("Review count (No. of reviews)")
    ### <extra code> plt.xticks(df[str(header[0])] , rotation=45 )
    plt.show(block=True)

'''length_vs_reviews1()'''

###############################################################################

'''DISTRIBUTION OF REVIEW TEXT LENGTH VS NO.OF REVIEWS - CONTOUR DENSITY PLOT '''
# Plotting density plot for visualizing distribution of review text length v/s rating

def length_vs_reviews2():
    # style
    plt.style.use('seaborn-darkgrid')
    # density plot with shade

    sns.kdeplot(df[header[0]], df[header[1]], cmap="Reds", shade=True, bw=.15)

    #sns.kdeplot(df[header[0]], df[header[1]], cmap="Blues", shade=True, bw=.15)
    # Add legend
    # blue_line = mlines.Line2D([], [], color='skyblue', alpha=0.9, linewidth=2, label="Frequency of no. of words in review text")
    # plt.legend(loc=1, ncol=5, handles=[blue_line])
    #red_patch = mpatches.Patch(color='red', label="deciding")
    #plt.legend(loc=1, ncol=2, handles=[red_patch])
    # Add titles
    plt.title("Distribution of Review length w.r.t number of reviews", loc='left', fontsize=12, fontweight=0, color='orange')
    plt.xlabel("Review Length (word count)")
    plt.ylabel("Review count (No. of reviews)")
    ### <extra code> plt.xticks(df[str(header[0])] , rotation=45 )
    plt.show(block=True)

'''length_vs_reviews2()'''

###############################################################################

'''DISTRIBUTION OF REVIEW TEXT LENGTH VS RATINGS - CONTOUR DENSITY PLOT '''
# Plotting density plot for visualizing distribution of review text length v/s rating

def length_vs_ratings():

    # style
    plt.style.use('seaborn-darkgrid')
    # density plot with shade
    #sns.regplot(x=dfr[rheader[0]], y=dfr[rheader[1]], fit_reg=False, scatter_kws={"color":"darkred","alpha":0.7,"s":0.03})
    #sns.jointplot(x=dfr[rheader[0]], y=dfr[rheader[1]], kind='scatter')

    sns.kdeplot(dfr[rheader[0]], dfr[rheader[1]], cmap="Oranges", shade=True, bw=.15, fit_reg=True, alpha=0.75)
    #sns.regplot(x=dfr[rheader[1]], y=dfr[rheader[0]], fit_reg=False, scatter_kws={"color":"darkred","alpha":0.05,"s":2} )

    # Add titles
    plt.title("Distribution of Review Length w.r.t Ratings", loc='left', fontsize=12, fontweight=2, color='Blue')
    plt.xlabel("Review Length")
    plt.ylabel("Rating (No. of Stars)")

    ### <extra code> plt.xticks(df[str(header[0])] , rotation=45 )
    plt.show(block=True)

'''length_vs_ratings()'''

###############################################################################
'''
https://python-graph-gallery.com/pie-plot/
https://python-graph-gallery.com/132-basic-connected-scatterplot/
https://python-graph-gallery.com/132-basic-connected-scatterplot/

# DISTRIBUTION OF RATINGS

# Plotting density plot for visualizing distribution of review text length v/s rating

def ratings2():
    # style
    plt.style.use('seaborn-darkgrid')
    # density plot with shade
    #sns.regplot(x=dfr[rheader[0]], y=dfr[rheader[1]], fit_reg=False, scatter_kws={"color":"darkred","alpha":0.7,"s":0.03})
    #sns.jointplot(x=dfr[rheader[0]], y=dfr[rheader[1]], kind='scatter')

    dfr[rheader[0]].plot(kind='pie', subplots=True, figsize=(8, 8))
    #sns.regplot(x=dfr[rheader[1]], y=dfr[rheader[0]], fit_reg=False, scatter_kws={"color":"darkred","alpha":0.05,"s":2} )

    # Add titles
    plt.title(" Ratings", loc='left', fontsize=12, fontweight=2, color='Blue')
    plt.xlabel("Review Length")
    plt.ylabel("Rating (No. of Stars)")

    ### <extra code> plt.xticks(df[str(header[0])] , rotation=45 )
    plt.show(block=True)

ratings2()

'''

###############################################################################
