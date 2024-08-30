## Film Suggestion

## Description
This project is a **Film Suggestion**.
This app takes a list of popular movies, sorts them in descending order by rating. Then it starts from the beginning
of the list and asks the user if he has seen the movie. If the user has not seen the movie,
the user is suggested to watch the movie and the name of the movie is googled for the user to choose his site to watch.

## How to run
run following:
```bash
python -m venv env
. env/bin/activate
pip install -r requirements.txt
python main.py
```
## How to deploy

You need to have docker installed on your machine. you can easily deploy the service with executing
the following command in your terminal:

```bash
docker-compose up
```
