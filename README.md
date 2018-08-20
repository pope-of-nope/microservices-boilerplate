# microservices-boilerplate
Opinionated boilerplate code for setting up a microservices project.

# Getting Started (5 minutes)
Clone the repo:
> 		$ git clone https://github.com/pope-of-nope/microservices-boilerplate
> 		$ cd microservices-boilerplate

Install docker and docker-compose (if not already installed):
> 		$ sudo sh setup/install_docker.sh

Start the server:
>   	$ make start

>     Result:
>>     cd docker-compose && sudo docker-compose build > build.out && rm build.out
>>     Building gateway
>>     Building dummy
>>     cd docker-compose && sudo docker-compose up -d
>>     Creating network "docker-compose_main" with the default driver
>>     Creating docker-compose_gateway_1 ... done
>>     Creating docker-compose_dummy_1   ... done
>>     make status
>>     make[1]: Entering directory '~/microservices-boilerplate'
>>     cd docker-compose && sudo docker-compose ps
>>               Name                        Command               State           Ports
>>     ------------------------------------------------------------------------------------------
>>     docker-compose_dummy_1     gunicorn --bind=dummy:5000 ...   Up      5000/tcp
>>     docker-compose_gateway_1   npm start                        Up      0.0.0.0:8080->8080/tcp
>>     make[1]: Leaving directory '~/microservices-boilerplate'

Test locally:
>   	make test

Test remotely:
>  		http://<your-hostname-or-ip-address>:8080/ip
>  		http://<your-hostname-or-ip-address>:8080/dummy

Stop the server:
>			make stop
