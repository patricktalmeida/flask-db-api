.PHONY: create
create:
	docker-compose up -d

.PHONY: destroy
destroy:
	docker-compose down

.PHONY: migrate
migrate:
	curl --request 'POST' --header 'Content-Type: application/json' --data '{"author":"John Doe","content":"Poetry is awsome."}' 'localhost:5000/quotes/'
	curl --request 'POST' --header 'Content-Type: application/json' --data '{"author":"John Doe","content":"Poetry is pretty awsome."}' 'localhost:5000/quotes/'
	curl --request 'POST' --header 'Content-Type: application/json' --data '{"author":"Jane Doe","content":"I love quoting impact phrases."}' 'localhost:5000/quotes/'
	curl --request 'POST' --header 'Content-Type: application/json' --data '{"author":"Patrick Almeida","content":"I love programming."}' 'localhost:5000/quotes/'
