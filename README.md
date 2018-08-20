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
>>     ...
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
>   	$ make test
>>     ...
>>     cd docker-compose && sudo docker-compose ps
>>               Name                        Command               State           Ports
>>     ------------------------------------------------------------------------------------------
>>     docker-compose_dummy_1     gunicorn --bind=dummy:5000 ...   Up      5000/tcp
>>     docker-compose_gateway_1   npm start                        Up      0.0.0.0:8080->8080/tcp
>>     curl http://localhost:8080/ip
>>     {
>>       "origin": "34.193.26.96"
>>     }
>>     curl http://localhost:8080/dummy
>>     {"status":"okay"}

Test remotely:
>  		http://<your-hostname-or-ip-address>:8080/ip
>  		http://<your-hostname-or-ip-address>:8080/dummy

Check server logs:
>   	$ make logs
>>     ...
>>     cd docker-compose && sudo docker-compose logs
>>     Attaching to docker-compose_gateway_1, docker-compose_dummy_1
>>     gateway_1  |
>>     gateway_1  | > Gateway@1.0.0 start /home/node/Gateway
>>     gateway_1  | > node server.js
>>     gateway_1  |
>>     gateway_1  | [EG:gateway] warn: rewrite plugin hasn't provided a schema. Validation for this plugin will be skipped.
>>     gateway_1  | gateway http server listening on :::8080
>>     gateway_1  | admin http server listening on 127.0.0.1:9876
>>     dummy_1    | [2018-08-20 18:14:10 +0000] [1] [INFO] Starting gunicorn 19.9.0
>>     dummy_1    | [2018-08-20 18:14:10 +0000] [1] [INFO] Listening at: http://192.168.48.2:5000 (1)
>>     dummy_1    | [2018-08-20 18:14:10 +0000] [1] [INFO] Using worker: sync
>>     dummy_1    | [2018-08-20 18:14:10 +0000] [10] [INFO] Booting worker with pid: 10
>>     dummy_1    | [2018-08-20 18:14:10 +0000] [11] [INFO] Booting worker with pid: 11
>>     dummy_1    | [2018-08-20 18:14:10 +0000] [12] [INFO] Booting worker with pid: 12
>>     dummy_1    | [2018-08-20 18:14:10 +0000] [13] [INFO] Booting worker with pid: 13

Stop the server:
>   	$ make stop
>>     ...
>>     cd docker-compose && sudo docker-compose down
>>     Stopping docker-compose_dummy_1   ... done
>>     Stopping docker-compose_gateway_1 ... done
>>     Removing docker-compose_dummy_1   ... done
>>     Removing docker-compose_gateway_1 ... done
>>     Removing network docker-compose_main

# Technologies involved:
Docker - a technology for managing virtual machines. Terms: container = VM; image = the initial state of the container before it's run; Dockerfile = a file that defines the image; Volume = a directory on the host OS which can be exposed to containers (without including it in the docker image.)
Docker Compose - a technology for managing interdependent docker containers. Terms: service = an abstraction layer that wraps around a Dockerfile to define anything unusual the docker daemon needs to know when operating on that Dockerfile.
Express-Gateway - a very well-designed and fully featured node.js project for configuring microservice gateways. The implementation runs on Express, a web server framework for node.js which serves requests through a very efficient event loop architecture. Express-Gateway uses configuration files to control behavior (which means you can use this project without knowing a lick of node.js--just read their documentation here: https://www.express-gateway.io/docs/configuration/gateway.config.yml/)

# How to expose your own microservices (using the "dummy.py" example.)
The "dummy.py" is a simple python webserver written using Flask, but it also stands in for whatever microservice you want to write, in whatever language you want to use. 

In order to use your own microservice code, you'll need to do 3 things:
- 1. "Dockerize" your code by creating a Dockerfile. The Dockerfile's responsibility is to ensure a working runtime environment.
- 2. Wrap a Docker "Service" around your Dockerfile by editing the "docker-compose.yml" file. A Service's responsibility is to ensure dependencies at a higher level than writing them in the Dockerfile. It's highly recommended you configure as much as possible through the Service rather than the Dockerfile, including: network aliases and port forwarding, environment variables, start-up order, or shared directories.
- 3. Edit the gateway configuration under "dockerized-config". In this file, you define publically accessible API endpoints, which receive requests from end-users. When the API endpoint gets a request, it checks for any applicable pipelines. The most important pipeline is the proxy, which defines the appropriate backend (service endpoint) and optionally allows you to transform the original request before it hits the microservice.

Let's see how those three steps work for the example "dummy.py" microservice. 

First, take a look at the "dummy.py" code itself. There is only one endpoint (GET "/") which returns a simple JSON response. The server is written in Python using the Flask web server framework. If you're familiar with Python, you could run this code yourself easily. If not, don't worry about getting it to run (that's what Docker does for us.)

Next look at the Dockerfile. Whoever wrote the "dummy.py" file should take the time to define this Dockerfile, because it guarantees anyone else (including the docker daemon) can run their code with no problem, without having any familiarity with Python.

Next, look at the Compose file ("docker-compose.yml"), specifically the "dummy" service. The biggest thing this does is override the default behaviors of the docker-daemon whenever performing a docker operation such as building the image or starting the container (which happens every time you type the "make start" command.)

Finally, the "gateway.yml" file configures the API endpoint, Service endpoint, and a proxy pipeline connecting the API and Service endpoints.
