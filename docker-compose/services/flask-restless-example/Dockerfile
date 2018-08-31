FROM python:3
# reimplement with supervisor? https://hub.docker.com/r/texastribune/gunicorn/~/dockerfile/

COPY ./src/requirements.txt  /server/requirements.txt
WORKDIR /server
RUN pip install -r requirements.txt

COPY ./src/ /server/
WORKDIR /server

EXPOSE 5000
#CMD gunicorn --bind=dummy:5000 -w 4 dummy:app
