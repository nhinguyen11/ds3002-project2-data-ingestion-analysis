# Data Ingestion and Analysis

## How it Works:
This project uses Python and DynamoDB to ingest data from the provided API. The file get.py contains a function called get(), which works to connect to the 'ds3002project2' table in DynamoDB. It also contains the global variable, 'global minute', which will help set up the code to run once per minute for 60 minutes. Lastly, it calls the function, insert(), which will insert the fields 'factor', 'time', and 'pi'. The last part of code uses the schedule package to run the get() function once per minute, for 60 minutes.The file analysis_viz.py contains the code for making the various visualizations. It uses the csv file api_results.csv, directly downloaded from DynamoDB.

## Execution:

First 6 lines of database.
<img width="1212" alt="Screen Shot 2022-05-11 at 4 40 44 PM" src="https://user-images.githubusercontent.com/98042008/167944064-cce8f527-fe9c-4b3c-9482-e0e73b27607b.png">

Last 6 lines of database.
<img width="1213" alt="Screen Shot 2022-05-11 at 4 41 01 PM" src="https://user-images.githubusercontent.com/98042008/167944237-bccb7708-18bd-4306-8d51-f7c129342a55.png">

## Analysis:

![figure1](https://user-images.githubusercontent.com/98042008/167944449-3b9ee761-2e2c-4f4f-9166-c3cffca74c40.png)

Scatterplot of the relationship between 'time' and 'factor'. There is a strong, positive, and linear relationship between the two variables. The points are fitted precisely along a line. There two outliers near the begining.



![figure2](https://user-images.githubusercontent.com/98042008/167944478-a864eb6c-78ed-404b-8b71-bf15344a228d.png)

Scatterplot of the relationship between 'time' and 'pi'. There is a slight positive relationship at the begining, but the points soon gather to form a horizsontal line. This means that the two variables are not correlated and have no relationship. Once again, the two outliers appear near the beginning.



![figure3](https://user-images.githubusercontent.com/98042008/167944499-fc3e54aa-ade1-49a6-a0a5-4476397d4bd4.png)

Line plot of relationship between 'time' and 'factor'. This one is interesting because the lines create a picture of sail boat. There still appears to be a postiive and linear relationship with the two outliers forming the top of the boat.
