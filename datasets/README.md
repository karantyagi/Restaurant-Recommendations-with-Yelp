## `Dataset Descriptions`

exploratory analysis/reviews analysis/plot_reviews.py

| __Dataset__ | __DESCRIPTION__ |
| ------ | ------ |
| business-categories-reviews.csv | Contains 2 columns, categories and reviews in each category |
| business_full_all_attr.csv | Contains complete business.json dataset with all columns |
| valid_restaurants.csv | Contains business_ids of all Restaurants in Las Vegas |
| states-reviews.csv | Contains 2 columns, state and reviews in each state |
| cities-reviews.csv| Contains 2 columns, city and reviews in each city |
| reviews_restaurants.csv | Contains review data subset for Restaurants in Las Vegas |
| reviews_restaurants_text.csv | Contains review data subset for Restaurants in Las Vegas with review length 100-200 words |
| reviews_restaurants_text_unbiased_svm.csv | Contains review data subset for Restaurants in Las Vegas with review length 100-200 words, with unbiased(predicted from review text) ratings, using SVM model |
| reviews_restaurants_text_unbiased_nb.csv | Contains review data subset for Restaurants in Las Vegas with review length 100-200 words, with unbiased(predicted from review text) ratings, using Naive Bayes model |

---
### `Yelp Datasets (json format)`
Download `business.json`, `user.json` and `review.json` from https://www.yelp.com/dataset

---
### `Building remaining datasets`

__All datasets can be created using the above yelp datasets by running:__
- [`analyze_business.py`](https://github.com/karantyagi/Restaurant-Recommendations-with-Yelp/tree/master/exploratory%20analysis/business%20anaysis/src)
- [`plot_reviews.py`](https://github.com/karantyagi/Restaurant-Recommendations-with-Yelp/tree/master/exploratory%20analysis/reviews%20analysis)

---
