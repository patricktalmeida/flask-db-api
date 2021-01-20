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

### New post

```bash
curl --request 'POST' --header 'Content-Type: application/json' --data '{"author":"Peter Hintjens","content":"Simplicity is always better than functionality."}' 'localhost:5000/quotes/'
```

### Getting data

- Get all posts from a single author:
```bash
curl 'localhost:5000/authors/1'
```

- Get all posts:
```bash
curl 'localhost:5000/quotes'
```

### Endpoints

- **GET endpoints**
 - `/authors/<id>`
 - `/quotes/<id>`
 - `/quotes/`
- **POST endpoits**
 - `/quotes/`
