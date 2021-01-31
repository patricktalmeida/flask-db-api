VALID_TOKEN="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjEyMTUxNTQ3fQ.vr-Nf5Is-mXPI_J1p2Yivzyw5AMsHn7y-86ezJSslzQ"

.PHONY: build
build:
	docker-compose build

.PHONY: create
create:
	docker-compose up -d

.PHONY: destroy
destroy:
	docker-compose down

.PHONY: migrate
migrate:

	curl --request 'POST' --header "Authorization: Bearer ${VALID_TOKEN}" \
		--header 'Content-Type: application/json' \
		--data '{"author":"John Doe","content":"Poetry is awsome."}' \
		'localhost/api/quotes/'
	curl --request 'POST' --header "Authorization: Bearer ${VALID_TOKEN}" \
		--header 'Content-Type: application/json' \
		--data '{"author":"John Doe","content":"Poetry is pretty awsome."}' \
		'localhost/api/quotes/'
	curl --request 'POST' --header "Authorization: Bearer ${VALID_TOKEN}" \
		--header 'Content-Type: application/json' \
		--data '{"author":"Jane Doe","content":"I love quoting impact phrases."}' \
		'localhost/api/quotes/'
	curl --request 'POST' --header "Authorization: Bearer ${VALID_TOKEN}" \
		--header 'Content-Type: application/json' \
		--data '{"author":"User Name","content":"I love programming."}' \
		'localhost/api/quotes/'
