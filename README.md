# Dime DE Test

## Task
to get the following data from a free financial data API called FMP (
https://site.financialmodelingprep.com/developer/docs/)
- Historical Dividends (https://site.financialmodelingprep.com/developer/docs/#Historical-Dividends)
- Delisted companies ((https://site.financialmodelingprep.com/developer/docs/delisted-companies-api/))
Then store the retrieved data in any database
- 
## Prerequisites

- Docker installed and running
- Docker Compose installed

## Installation

To get started with the deployment:

**clone Source Code:** Unzip the source code to your local machine.
    ```bash
    docker-compose build
    docker-compose up
    ```
   
you can check script at Airflow UI by
```
localhost:8080
```

script will run daily or trigger it manually


Improvements:
- Airflow deployment modularity
- setup connection key
