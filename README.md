# Movie-Review-Scraper

This scraper can be used to scrap data from IMDB  , currently i have made this to scrap movie reviews and ratings of Avengers Endgame movie but with simple modification it can be exteded to scrap reviews and rantings of any movie.

## Getting Started

To use this scraper clone this repo and run below commands in your command promt.
This command will store data in review.json file
```
scrapy crawl laptop_review -o review.json
```
This command will store data in review.csv file
```
scrapy crawl laptop_review -o review.csv
```

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

In this project I have used scrapy to scrap reviews. scrapy can be installed fron pip using below command
```
!pip install scrapy
```


