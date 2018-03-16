

'''DISTRIBUTION OF REVIEW TEXT LEHGTH VS RATINGS - CONTOUR DENSITY PLOT '''
# Plotting density plot for visualizing distribution of review text length v/s rating

# style
plt.style.use('seaborn-darkgrid')
# density plot with shade
sns.kdeplot(dfr[rheader[1]], dfr[rheader[0]], cmap="Reds", shade=True, bw=.15)
#sns.regplot(x=dfr[rheader[1]], y=dfr[rheader[0]], fit_reg=False, scatter_kws={"color":"darkred","alpha":0.05,"s":2} )
# Add legend
blue_line = mlines.Line2D([], [], color='skyblue', alpha=0.9, linewidth=2, label="Frequency of no. of words in review text")
plt.legend(loc=1, ncol=5, handles=[blue_line])
#red_patch = mpatches.Patch(color='red', label="deciding")
#plt.legend(loc=1, ncol=2, handles=[red_patch])
# Add titles
plt.title("distribution of review text length v/s rating", loc='left', fontsize=12, fontweight=0, color='orange')
plt.xlabel("Review text length (in words)")
plt.ylabel("Proportion of reviews")
### <extra code> plt.xticks(df[str(header[0])] , rotation=45 )
plt.show(block=True)


###############################################################################

'''
# Plotting scatter plot for visualizing distribution of review text length v/s rating

# style
plt.style.use('seaborn-darkgrid')
# density plot with shade
sns.kdeplot(df[header[1]], df[header[0]], cmap="Reds", shade=True, bw=.15)
# Add legend
blue_line = mlines.Line2D([], [], color='skyblue', alpha=0.9, linewidth=2, label="Frequency of no. of words in review text")
plt.legend(loc=1, ncol=5, handles=[blue_line])
#red_patch = mpatches.Patch(color='red', label="deciding")
#plt.legend(loc=1, ncol=2, handles=[red_patch])
# Add titles
plt.title("distribution of review text length v/s rating", loc='left', fontsize=12, fontweight=0, color='orange')
plt.xlabel("Review text length (in words)")
plt.ylabel("Proportion of reviews")
### <extra code> plt.xticks(df[str(header[0])] , rotation=45 )
plt.show(block=True)
'''






'''


# horizontal density plot
#sns.kdeplot(df['Length of Review Text'], shade=True, color="skyblue")


# histogram
#sns.distplot(df['Length of Review Text'])





#sns.plt.show()


#plot_line(df,list(df))
'''
###############################################################################


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
