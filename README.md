# Data Ingestion and Analysis

## How it Works 
This project uses Python and DynamoDB to ingest data from the provided API. The file get.py contains a function called get(), which works to connect to the 'ds3002project2' table in DynamoDB. It also contains the global variable, 'global minute', which will help set up the code to run once per minute for 60 minutes. Lastly, it calls the function, insert(), which will insert the fields 'factor', 'time', and 'pi'. The last part of code uses the schedule package to run the get() function once per minute, for 60 minutes, 

## Execution
