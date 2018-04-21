# `Analyzing business dataset`


### Python code for:
- loading the business.json dataset
- converting it to business.json.csv
- anlayzing and plotting graphs

---
### Dependencies:

- Download `business.json` from https://www.yelp.com/dataset
- Keep `business.json` in the same folder as `analyze_business.py` 

---
### How to run the files:

```bash
$ python analyze_business.py "business.json"
```
---
### Expected Output:
`output` folder created with the following files:
- business-categories-reviews.csv
- business_full_all_attr.csv
- valid_restaurants.csv
- states-reviews.csv
- cities-reviews.csv

| __Dataset__ | __DESCRIPTION__ |
| ------ | ------ |
| business-categories-reviews.csv | Contains 2 columns, categories and reviews in each category |
| business_full_all_attr.csv | Contains complete business.json dataset with all columns |
| valid_restaurants.csv | Contains business_ids of all Restaurants in Las Vegas |
| states-reviews.csv | Contains 2 columns, state and reviews in each state |
| cities-reviews.csv| Contains 2 columns, city and reviews in each city |

---
