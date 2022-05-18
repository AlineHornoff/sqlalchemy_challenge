# SQLAlchemy_challenge

## Introduction
Time to go on a holiday and what better way to prepare than by checking out the weather. This project consists of two parts and explores data of a climate database utilizing SQLAlchemy ORM queries, Pandas and Matplotlib. In part two a Flask API is created to store all the information.

### Part One - Climate Analysis and Exploration

* Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.
* Use SQLAlchemy create_engine to connect to your sqlite database.
* Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.

#### Precipitation Analysis

* Design a query to retrieve the last 12 months of precipitation data.
* Select only the date and prcp values.
* Load the query results into a Pandas DataFrame and set the index to the date column.
* Sort the DataFrame values by date.
* Plot the results using the DataFrame plot method.
* Use Pandas to print the summary statistics for the precipitation data.

#### Station Analysis

* Design a query to calculate the total number of stations.
* Design a query to find the most active stations.
    1. List the stations and observation counts in descending order.
    2. Which station has the highest number of observations?
    3. Hint: You will need to use a function such as func.min, func.max, func.avg, and func.count in your queries.
* Design a query to retrieve the last 12 months of temperature observation data (TOBS).
    1. Filter by the station with the highest number of observations.
    2. Plot the results as a histogram with bins=12.


### Part Two - Climate App

* use flask to create your routes

#### Hints

* You will need to join the station and measurement tables for some of the queries.
* Use Flask jsonify to convert your API data into a valid JSON response object.

## Contents
* Resources - contains CSV files and sqlite file
* Images - contains analysis pngs
