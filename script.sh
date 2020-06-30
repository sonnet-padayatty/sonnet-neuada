#!/bin/bash

# do the docker installation and starting the service
apt-get update -y
apt-get install docker -y
apt-get install docker.io -y
service docker start
# create two seperste directories to run dockerfiles that deploy containers
mkdir ./container1
mkdir ./container2
# copy required files for each container into their corresponding directory
cp ./{Dockerfile,test.json,test.py} ./container1
cp ./{Dockerfile2,test2.py} ./container2
mv ./container2/Dockerfile2 ./container2/Dockerfile
# create datavolume for the containers 
docker volume create --name DataVolume1
# build the image for container1
docker build -t imageone ./container1
# running docker in detached mode after attaching datavolume
docker run -tid --name=Container1 -v DataVolume1:/datavolume1 imageone
# build image for container2
docker build -t imagetwo ./container2
# running docker in detached mode after attaching datavolume from container1
docker run -tid --name=Container2 --volumes-from Container1 imagetwo
# stating services for cron jobs
docker exec -d Container1 service cron start
docker exec -d Container2 service cron start
# making the python script executable by changing the permissions
docker exec -d Container1 chmod 777 /test.py
docker exec -d Container2 chmod 777 /test2.py

