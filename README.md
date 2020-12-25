
[![pipeline status](https://gitlab.com/cyberdroidmann/museumwiki/badges/main/pipeline.svg)](https://gitlab.com/cyberdroidmann/museumwiki/-/commits/main)


# Museum Wiki

**Description**:  
Museum Wiki is an open API that serves resources onf basic information about Museums around the world, in an API ready way.
Currently there are no official Wiki for museums (Still being discussed), this is a trivial project to fill the gap. 



**Technology stack**:
- Python
- Django
- Django Rest-Framework
- Docker

**Status**:
This project is still heavily under developent, but I have released a trivial version 1.0, that is feature complete :)

**Links to API Documentation**
- [CoreAPI Documentation]()
- [Swagger Documentation]()


## Setup

**Dependencies**
Just Docker :). If you have docker installed, you are good to go!
Docker installation for your operating system [here](https://docs.docker.com/get-docker/)


**Build the images:**

```$ docker-compose build ```

**Run the containers:**

```$ docker-compose up -d ```

**Create migrations:**

```$ docker-compose exec wiki python manage.py makemigrations```

**Apply the migrations:**

```$ docker-compose exec wiki python manage.py migrate```

**Seed the database:**

```$ docker-compose exec wiki python manage.py loaddata movies.json```

## Running Tests & Checks

**Run tests:**

``` $ docker-compose exec wiki pytest -p no:warnings ```

**Run the tests with coverage:**

``` $ docker-compose exec wiki pytest -p no:warnings --cov=. ```

**Check lint:**

``` $ docker-compose exec wiki flake8 . ```

**Run Black and isort with check options:**

``` $ docker-compose exec wiki black --check . ```
``` $ docker-compose exec wiki /bin/sh -c "isort ./*/*.py --check-only" ```

**Make code changes with Black and isort:**

``` $ docker-compose exec wiki black  . ```
``` $ docker-compose exec wiki /bin/sh -c "isort ./*/*.py" ```


------

## Credits

- Inspired by [Glamkit](https://github.com/ic-labs/django-icekit)
