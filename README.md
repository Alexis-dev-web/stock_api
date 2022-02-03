# stock-core-server

## Requirements

1. Docker version 19.03.8 or greater.
2. Python 3.
3. Favorite code editor.

## Local Development

1. Rename `.env.dev.template` to `.env.dev`.


2. Build development container (run on terminal):

    ```
       # NOT PGADMIN
       $ docker-compose -f docker-compose.dev.yml up -d --build
    ```


    ```
       # WITH PGADMIN
       $ docker-compose -f docker-compose-pgadmin.yml up -d --build
    ```
3. Create tables:
    ```
       # NOT PGADMIN
       $ docker-compose -f docker-compose.dev.yml exec web python manage.py create_db
    ```


    ```
       # WITH PGADMIN
       $ docker-compose -f docker-compose-pgadmin.dev.yml exec web python manage.py create_db
    ```
4. DB Manage:
    ```
        # NOT PGADMIN
        $ docker-compose -f docker-compose.dev.yml exec db psql --username=stock --dbname=stock_server
    ```


    ```
        # WITH PGADMIN
        $ docker-compose -f docker-compose-pgadmin.dev.yml exec db psql --username=stock --dbname=stock_server
    ```
    
The project is running on http://127.0.0.1:5000

## Dev Guide

### Logs

1. Follow the next pattern:
    ```python
        logging.info(f"ClassName#methodName (START, FAILURE, SUCESS, INFO) <what_you_want> parameter={value}")

        logging.error(f"ClassName#methodName FAILURE <what_you_want> exception={exception}")
    ```

> **Remember:** Write automated tests for every critical method you write.

1. Running tests:
    ```shell
        $ pip install pytest
        $ pytest -v
    ```
2. Check code coverage:
    ```shell
        $ pip install coverage
        $ coverage run -m pytest
        $ coverage report
    ```