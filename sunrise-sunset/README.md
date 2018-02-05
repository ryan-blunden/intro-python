# Sunrise Sunset

This app is a CLI application that asks the user for a city in Washington state. and will return the sunrise and sunset time.

In class, I live coded the creation of this app to show you what the workflow for developing an application looks like.

## Installation

PipEnv is awesome, and is what will be used to manage the isolated environment for this project.

A Pipfile is part of the source code, so to setup the environment (install the required third party dependencies):

- Open a commandline window.
- Change into the root project folder (sunrise-sunset).
- Run `pipenv install` to install the third party Python dependencies.


## Functional Requirements

- Build a Command Line Application (CLI) that will provide the sunrise and sunset for a given city.
- Only input required is city as state will be initially hard-coded to Washington.
  - Future functionality will require a state input as well, if there are multiple cities in the US with that name.

## Data Requirements

- CSV Import process for an open data set for the cities and their latitude and longitude. 
- For this version, only Washington cities are supported.
- The data consumed by CLI should be in JSON format and available at a REST endpoint.

## Running the Application

### Import the Washington cities from the CSV file

The `locations.json` file in `server/api/v1` is intentionally empty.

You'll need to import the run the `cities_import.py` script first:

- Run `pipenv shell` to activate the Python isolated environment.
- Open a command line window.
- Run `python cities_import.py`.

It will take around 10-15 seconds to complete. The `locations.json` file will now have all the cities from
Washington. Checkout the `cities_import.py` for a simple example of CSV importing and row filtering.

### The REST API Server

THe REST API server is what provides the city, latitude and longitude in JSON format for our CLI to consume.  

To run the server:

- Run `pipenv shell` to activate the Python isolated environment.
- Open a command line window.
- Change into the `server` directory.
- Run `python -m http.server 8080`
- To see the server in action, go to http://localhost:8080

### The CLI Application

- Run `pipenv shell` to activate the Python isolated environment.
- Open a command line window.
- Run `python sunsrise-sunset.py`.

## Next Steps

Extend the application so it can do city lookups in other states.