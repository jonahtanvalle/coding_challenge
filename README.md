# Coding Challenge

# Flask CSV API with Docker

This project is a Flask API designed to upload CSV data and insert it into a database. It utilizes Docker Compose for local testing of the API and to deploy the database using a Dockerfile.

## Requirements

- Docker
- Docker Compose

## Installation and running

1. Clone this repository:

```bash
git clone https://github.com/jonahtanvalle/coding_challenge.git
cd coding_challenge
```

2. Define enviroment variables (.env file) for rhe following variables:

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
POSTGRES_HOST=postgres

3. Build  and start the Docker containers:

```bash
docker-compose build
docker-compose up
```

## Anotations
If aby doubt please check the evidence.

1. I tested the app using Postman by sending a POST request in a form-data KEY:VALUE as following:

    {file: jobs.csv}
    {file: departments.csv}
    {file: hired_employees.csv}

 I uploaded the data this way beacause of the relations that I develop in the modeling.

 2. In the module utils.py I developed a single function to catch an exception when the employee has no job or department ID, I just assumend this simple logic to null the values that not fit, but obviously is important to know that every type of data has special conditions or bussines rules.

 3. I also added a column to partition the hired_employees data, but is not necessary depending on the ingest frequency or the DB policies to handle the replacements or the new ID.

 TODO: Develop a better Unique ID policy to handle the new additions. 