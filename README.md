# Whatsapp History Analyis

## Prerequisite to run the application

* Docker

## To start the app

* Add the chat history file

Copy the Whatsapp chat history file into the `/data` directory at the root of the project and rename it `history.txt` 

* Build the docker image

```sh
docker build -t whatsapp-history-analyis .
```
* Start the application 

```sh
docker run -it --rm whatsapp-history-analyis
```

## Functionning

* On startup the whatsapp chat history file is loaded

## Assumptions

* All word comparisons are case incensitive that is `ok = OK = Ok = oK`