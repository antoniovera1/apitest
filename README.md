# Tekton test API

API service for a product inventory management web system

## Run the server

You can run this API server through Docker Compose. You need to install docker and docker compose on your computer and run the following commands inside the API's main directory:

```
docker compose build
```
```
docker compose up
```

After your stack is running, you need to run the following one-shot command to migrate the models into the database.

```
docker compose run apiserver python3 manage.py migrate
```

## Documentation

You can find 3 kinds of documentation on this API:

- The OpenAPI Schema of this API at `<API URL>/api/v1/swagger.json`. Or the YAML view at `<API URL>/api/v1/swagger.json`.
- A swagger UI view of this API at `<API URL>/api/v1/swagger`.
- A ReDoc view of this API specification at `<API URL>/api/v1/swagger`.