build:
	cd docker-compose && sudo docker-compose build

start: build
	cd docker-compose && sudo docker-compose up -d

stop:
	cd docker-compose && sudo docker-compose down

logs:
	cd docker-compose && sudo docker-compose logs

