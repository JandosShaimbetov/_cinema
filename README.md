# _cinema

This project is heavily inspired by the cinematica.kg website

Heroku [link]()

### Prerequisites	

First clone repository:
```
git clone 'repository'
```
Then you need to build containers with the following command:
```
docker-compose up --build
```
### Create database and user
```
docker exec -it cinema_db bash
su postgres
psql
CREATE DATABASE cinema;
CREATE USER cinema_admin WITH PASSWORD 'admin';
GRANT ALL PRIVILEGES ON DATABASE cinema TO cinema_admin;
```
### Running the migrations
```
docker-compose run --rm _cinema python manage.py migrate
```
### Create a superuser
```
docker-compose run --rm _cinema python manage.py createsuperuser
```
### Running 
```
docker-compose up
```
### Built With

* [Python](https://www.python.org) - an interpreted high-level general-purpose programming language
* [Django](https://docs.djangoproject.com/en/3.2/) - web framework
* [Django Rest Framework](https://www.django-rest-framework.org) - toolkit for building Web APIs
* [PostgreSQL](https://www.postgresql.org) - open source object-relational database system
* [Docker](https://www.docker.com) - Docker is an open platform for developing, shipping, and running applications


## Author

* Jandos Shaimbetov
