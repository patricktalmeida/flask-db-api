## Instructions

1- First create an user and get an auth token by following the [README](../README.md) steps.

2- Change [docker-compose.yml](./docker-compose.yml) `CLIENT_TOKEN` variable for the new token you got. Remember that its valid for 12 hours.

3- Startup locust with the steps above and access its web browser UI on [localhost](http://localhost:8089) to start making requests.

## Boostrap

**Tools needed:**
- docker
- docker-compose
- make

## Create locust environment
```bash
make create
```

## Destroy locust environment

```bash
make destroy
```

### TODO

- Implement more endpoints to locust test
