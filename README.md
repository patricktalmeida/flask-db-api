## Boostrap

**Tools needed:**
- docker
- docker-compose
- make
- curl

```bash
make build
make create
```
## Input example data

```bash
make migrate
```
## Destroy environment

```bash
make destroy
```

## Instructions

To make requests authentications is needed. How to authenticate:

- First create a new user
```bash
curl --request 'POST' \
    --header 'Content-Type: application/json' \
    --data '{"username":"User Name","email":"email@email.com","password":"12345"}' \
    'localhost/api/register'
```

- After creating an user you need to get a new valid token, it lasts for 12 hours.
```bash
curl --request 'POST' \
    --header 'Content-Type: application/json' \
    --data '{"email":"email@email.com","password":"12345"}' \
    'localhost/auth/login'
```

- After getting a new token change [Makefile](./Makefile) variable `VALID_TOKEN` on the top of the file to make your life easier when creating some new data.

### New post

```bash
curl --request 'POST' --header "Authorization: Bearer ${VALID_TOKEN}" \
	--header 'Content-Type: application/json' \
	--data '{"author":"User Name","content":"I love programming."}' \
	'localhost/api/quotes/'
```

### Getting data

- Get all posts from a single author:
```bash
curl 'localhost/api/authors/1'
```

- Get all posts:
```bash
curl 'localhost/api/quotes'
```

### Endpoints

- **GET endpoints**
 - `/api/authors/<id>` (needs authentication)
 - `/api/quotes/<id>` (needs authentication)
 - `/api/quotes/` (needs authentication)
 - `/api/healthcheck`
 - `/auth/healthcheck`
- **POST endpoits**
 - `/api/quotes/` (needs authentication)
 - `/api/register`
 - `/auth/login`

## How to run Unit Tests

```bash
./run_tests.sh
```

### TODO

- Add queue on `/api/register` and `/api/quotes`.
