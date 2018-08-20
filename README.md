# microservices-boilerplate
Opinionated boilerplate code for setting up a microservices project.

# Getting Started (5 minutes)
Clone the repo:
> 		git clone https://github.com/pope-of-nope/microservices-boilerplate
> 		cd microservices-boilerplate

Install docker and docker-compose (if not already installed):
> 		sh setup/install_docker.sh

Start the server:
>   	make start

Test locally:
>   	make test

Test remotely:
>  		http://<your-hostname-or-ip-address>:8080/ip
>  		http://<your-hostname-or-ip-address>:8080/dummy

Stop the server:
>			make stop
