build:
	cd docker-compose && sudo docker-compose build

status:
	cd docker-compose && sudo docker-compose ps

test: status
	curl http://localhost:8080/ip
	curl http://localhost:8080/dummy

start: build
	cd docker-compose && sudo docker-compose up -d
	make status

stop:
	cd docker-compose && sudo docker-compose down

logs:
	cd docker-compose && sudo docker-compose logs

