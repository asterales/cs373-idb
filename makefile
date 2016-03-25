FILES :=                              \
    .travis.yml                       \
    apiary.apib   				\
    IDB1.log  					\
    models.html 				\
    models.py  					\
    tests.py                     	\
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