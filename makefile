FILES :=                              \
    .travis.yml                       \
    apiary.apib   				\
    IDB1.log  					\
    models.html 				\
    models.py  					\
    app/tests.py                     	\
    UML.pdf  

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
	echo "success";


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
	docker login
	docker build -t nathanbain314/sweography_app app
	docker push nathanbain314/sweography_app
	docker build -t nathanbain314/sweography_lb lb
	docker push nathanbain314/sweography_lb
	docker build -t nathanbain314/sweography_db db
	docker push nathanbain314/sweography_db
	docker-compose --file docker-compose-prod.yml up -d
	docker port sweography_lb 80

build_master_db:
	source docker_source/master/docker.env && make build_db

build_dev_db:
	source docker_source/dev/docker.env && make build_db

build_db:
	docker-compose --file docker-compose-prod.yml run -d --rm --no-deps app python models.py create_db

master_ip:
	source docker_source/master/docker.env && docker port sweography_lb 80

dev_ip:
	source docker_source/dev/docker.env && docker port sweography_lb 80
