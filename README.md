# Flask docker dev bootstrap environment

This repo serves as a foundation for flask project using docker containers.
It's bundled to support different implementation scenarios.
Feel free to strip out the components that you won't use.

The following containers are available:
* app service - Python with Flask and GraphQl
* postgres service
* neo4j service

Technology stack:
* GraphQl - graphene
* REST API - flask-restx

# Dev environment

Spin up dev containers
```
docker-compose up --build
```
Attach to postgres container and psql cli
```
docker-compose exec postgres psql --username=postgres --dbname=app
```

Database setup
```
docker-compose exec app python manage.py create_db
docker-compose exec app python manage.py seed_db
```