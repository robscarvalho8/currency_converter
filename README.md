# Currency Converter
API for currency conversion are:
- USD
- BRL
- EUR
- BTC
- ETH

## Introduction

Description of technologies used and expectations

Python language was used as standard backend technology

To facilitate the work, the framework was used [FastAPI](https://fastapi.tiangolo.com/), the project has another important library [SQLAlchemy](https://www.sqlalchemy.org/), where it is used to store coin data.

For organization and development, the [Flake8](https://flake8.pycqa.org/en/latest/) for better indentation of the code, using the [Docker](https://www.docker.com/) e [Docker-Compose](https://docs.docker.com/compose/), so that the project can be executed on any machine, there is no IDE recommendation to run the application.

## Overview

The application receives 3 query parameters, in its URL, coin_from, coint_to and amout:
    
- coin_from: Coin to be converted
- coin_to: Coin to which the user intends to convert
- amount: Value to be converted


Documentation and details can be found at the following endpoints:

    0.0.0.0:8000/redoc

    0.0.0.0:8000/docs
 

## Requirements

To run the project locally you need the following tools:

- [Git](https://git-scm.com/), to clone the project
- [Docker](https://docs.docker.com/engine/install/ubuntu/)
- [Docker-Compose](https://docs.docker.com/compose/install/)

## Install and Run Project

To run locally, just clone the repository and start docker-compose:
- Clone the project (repository: [https://github.com/robscarvalho8/currency_converter.git](https://github.com/robscarvalho8/currency_converter.git))
- Select project folder

To run locally, just run the command 'docker-compose up --build'

Open the browser and access the url [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs) or [http://0.0.0.0:8000/redoc](http://0.0.0.0:8000/redoc), to view the documentation 

## Directory Structure



    ├── compose                           <- Arquivos usados pelo docker-compose 
    ├── service                           <-  The code of interest
    │   ├── database.py                   <- Database connection code
    │   ├── main.py                       <- Code that launches the application
    │   ├── models.py                     <- Code where the project entities are located
    │   ├── populate_db.py                <- Code for inserting the initial data into the database 
    │   ├── schemas.py                    <- Schemas used in API responses 
    │   ├── validator.py                  <- Code where the business rule is located 
    │   └── views.py                      <- Code where the application endpoints are made available
    ├── Pipfile                           <- Package and distribution management up
    ├── Pipfile.lock                      <- Package and distribution management up
    └ docker-compose.yml                  <-  DockerFile management