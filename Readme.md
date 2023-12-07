# Get start with Great expectations

## Initial precondition:
- An installation of [Python](https://www.python.org/downloads/), version 3.8 to 3.11
- pip
- An internet browser

## Installation of Great Expectations

- Run the command in the terminal: 
``` 
pip install great_expectations
```

## DB connection configuration

Initial connection string looks like:
```
CONNECTION_STRING = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
```

To configure it properly for your local machine please edit data in variables.py file:
```
# fill in proper value for the next variables:
DATASOURCE_NAME 
HOST 
PORT
USERNAME 
PASSWORD 
DATABASE 
ADDRESS_TABLE_NAME 
```

## Run existed validations for the checkpoint:
Run the project file gr_exp.py to create a checkpoint 

Next time run of the existed checkpoint can be triggered by:
```
# Run next command in the terminal 
great_expectations checkpoint run my_sql_checkpoint
```