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
