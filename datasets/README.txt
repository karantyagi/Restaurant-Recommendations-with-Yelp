
Dataset Descriptions
_____________________________________________________________________________________________________________________________________

valid_restaurants.csv           	  :  Contains business_ids of all Restaurants in Las Vegas
reviews_restaurants.csv			  :  Contains review data subset for Restaurants in Las Vegas
reviews_restaurants_text.csv		  :  Contains review data subset for Restaurants in Las Vegas with review length 100-200 words
reviews_restaurants_text_unbiased_svm.csv :  Contains review data subset for Restaurants in Las Vegas
					     with review length 100-200 words, with unbiased(predicted from review text)
					     ratings, using SVM model
reviews_restaurants_text_unbiased_nb.csv  :  Contains review data subset for Restaurants in Las Vegas
					     with review length 100-200 words, with unbiased(predicted from review text)
					     ratings, using Naive Bayes model
business_full_all_attr.csv		  :  Contains complete business.json dataset with all columns
business-categories-reviews		  :  Contains 2 columns, categories and reviews in each category
cities_reviews				  :  Contains 2 columns, city and reviews in each city
states-reviews				  :  Contains 2 columns, state and reviews in each state

______________________________________________________________________________________________________________________________________

business_full_all_attr.csv : DESCRIPTION (with example)

{
    // string, 22 character unique string business id
    "business_id": "tnhfDv5Il8EaGSXZGiuQGg",

   // an array of strings of business categories
    "categories": [
        "Mexican",
        "Burgers",
        "Gastropubs"
    ],

    // string, the business's name
    "name": "Garaje",

    // string, the city
    "city": "San Francisco",

    // string, 2 character state code, if applicable
    "state": "CA",

    // string, the postal code
    "postal code": "94107",

    // float, latitude
    "latitude": 37.7817529521,

    // float, longitude
    "longitude": -122.39612197,

    // float, star rating, rounded to half-stars
    "stars": 4.5,

    // interger, number of reviews
    "review_count": 1198,

    // object, business attributes to values. note: some attribute values might be objects
    "attributes": {
        "RestaurantsTakeOut": true,
        "BusinessParking": {
            "garage": false,
            "street": true,
            "validated": false,
            "lot": false,
            "valet": false
        },
    }

}
