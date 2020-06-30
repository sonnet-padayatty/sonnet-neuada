# Pulling ubuntu image for container1
FROM ubuntu:18.04
# copy the python script and default json file to the root location of container
COPY test.py /
COPY test.json /
# creates new directory datavolume for mounting 
RUN mkdir /datavolume1
# installing required packages
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install vim -y
RUN apt-get install cron
RUN pip3 install json2xml
# invokes python script
RUN python3 /test.py
# setting cron job for the container1 for the continuity of the tasks
RUN (crontab -l ; echo "* * * * * python3 /test.py")| crontab -
