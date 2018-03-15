[![Build Status](https://travis-ci.org/Yelp/dataset-examples.svg)](https://travis-ci.org/Yelp/dataset-examples)

[![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg)]()

[![CocoaPods](https://img.shields.io/cocoapods/l/AFNetworking.svg)]()

[![PyPI](https://img.shields.io/badge/python-3.6-blue.svg)]()

[![PyPI version](https://badge.fury.io/py/numpy.svg)](https://badge.fury.io/py/numpy)

[![PyPI version](https://badge.fury.io/py/pandas.svg)](https://badge.fury.io/py/pandas)

[![PyPI version](https://badge.fury.io/py/statsmodels.svg)](https://badge.fury.io/py/statsmodels)

[![PyPI version](https://badge.fury.io/py/scikit-learn.svg)](https://badge.fury.io/py/scikit-learn)

To install all dependencies: `$ pip install -e .`

Samples
------------

```bash
$ python json_to_csv_converter.py yelp_academic_dataset.json # Creates yelp_academic_dataset.csv
```


```bash
$ python review_autopilot/generate.py Food 'They have the best'
They have the best coffee is good food was delicious cookies and
a few friends i think they make this
```

`positive_category_words`: See the Yelp engineering blog for
details about this example. In short, it generates positivity
scores for words either globally or per-category.

Basic set-up
------------
