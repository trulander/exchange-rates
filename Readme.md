# django(DRF) + celery + unit tests + docker + docker-compose

[Link to documentation in Russian](https://github.com/trulander/exchange-rates/blob/master/ReadmeRu.md)

The project based on the task:
```team foundation
1)  Servise goes by API ones in 5-10-15 minutes (set via .env) and gets the data about 
    cryptocurrency BTC (for example curl -H "X-CMC_PRO_API_KEY: d61bca4c-e9d3-40b9-8d82-abf9b057ffbd" -H "Accept: application/json" -d "id=1" -G https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest)
    and save the data to the databases, the exchange rate, the time the data was received, and whatever else you whant.
2) Service that show informarion from the database about exchange rate(last and list)
    *   if it possible, if i want to get the latest exchange rate, i go by a special endpoint and worker gets the latest data
    *   Wrap everythink in a Docker + docker-compose
3)  share on the Github
    *   And the best if it async(if not django)
```



## List of enpoinds API:
```team foundation
/api/ratescurrency/    - Outputs a list of all records with exchange rates
/api/ratescurrency/{id}/  - Outputs a list of rates sorted by currency id

/api/ratecurrency/{id}/  - Outputs 1 course record by its id in the table of DB

/api/lastrate/{id}/    - Outputs the last record of the currency rate from the DB by its id

/api/latestrate/{id}/   - Creates a task for celery to request a fresh currency rate by its id through a service to a third-party api.
                    Expects celery to perform the task and returns the result in response.
                    
/api/currencies/     - Outputs a list of currencies stored in the DB
/api/currencies/{id}/  - Outputs detailed information about the currency from the DB by its id
```

## List of endpoints services:
```team foundation
 /services/requestcurrency/{id}/ - 
        Makes a request directly to a third-party api for a currency rate by id on a third-party service.
        Saves the result to the database and responds with the currency model.
        Available only by authorization
```


The project contains a Core module which contains common classes for all django applications

The api application is responsible for presenting the API to the end user of the project, providing the endpoints
to work with the data in the database.

The services application is responsible for business logic and contains 1 service endpoint for direct request to third-party api without celery.<br>
BusinessLogic folder contains business logic class of service which is responsible for third-party api requests.

The project out of the box works with the database this sqlite, but is designed to work with postgreSQL, to switch to work with it there is a 
environment variable DATABASE_TYPE which will work with the database if you set it to sqlite, otherwise it will work with postgresql.


## Commands to set up the project
```shell
    git clone https://github.com/trulander/exchange-rates
    cd exchange-rates
    docker-compose up
```
After that you'll get a working project out of the box

Asynchronus realisation of the project: [https://github.com/trulander/exchange-rates-async](https://github.com/trulander/exchange-rates-async)
