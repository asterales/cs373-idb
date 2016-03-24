models.html:
	pydoc3 -w models

IDB1.log:
	git log > IDB1.log

retrieve_sha:
	git rev-parse HEAD

build_master:
	source docker_source/master/docker.env && make build

build_dev:
	source docker_source/dev/docker.env && make build

build:
	docker build -t nathanbain314/sweography_app app
	docker push nathanbain314/sweography_app
	docker build -t nathanbain314/sweography_lb lb
	docker push nathanbain314/sweography_lb
	docker-compose --file docker-compose-prod.yml up -d
	docker port sweography_lb 80
