# IMDB

import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import timeit
import numpy as np
import pandas as pd
import csv

element = []


def fetch_review(*page):

    # replace the movie id (tt1392170) in this url with the movie you want to try
    url = 'http://www.imdb.com/title/tt1392170/reviews?start='

    for i in page:

        try:
            # replace 'path' with the location of your webdriver
            driver = webdriver.Chrome('path/chromedriver')
            driver.get(url+str(i))
            time.sleep(1)
            parent = driver.find_elements_by_css_selector(
                "div[id='tn15content'] > p")
            element.append([i.text for i in parent])
            driver.quit()

        except Exception, e:
            driver.quit()
            print e  # print the error message, so that we know what was wrong.
            element.append('Need Inspect')
            pass

    return(element)


result = []
number = range(0, 1960, 10)
result = fetch_review(*number)

data = pd.DataFrame(result)
data = data.drop(10, axis=1)
review = data.stack().reset_index(drop=True)
review = pd.DataFrame({'ID': review.index, 'review': review.values})
review.to_csv('review.csv', encoding='utf-8', index=False)
