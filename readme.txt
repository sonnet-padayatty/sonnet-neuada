
Creater : Sonnet Padayatty Reju

Task:
Write a python script, which will convert json files to xml files, encrypt and transfer it in a remote location.

Environment:
Python, Docker

Description:
Solution should be prepared as two Docker images, 1st to send files, and 2nd to receive them.
Deployment of these containers should be automated using docker-compose or shell script.

Python script on container A:
1. convert all json files to xml 
2. encrypt the files
3. Transfer it to a remote location (container B)

Python script on container B:
1. Receive files
2. Decrypt and store files

So, in other words, pipeline should look like:
Json -> XML -> encryption -> transfer -> decryption -> XML

Acceptance criteria:
Any given Json putted to container A appears in XML form on container B using mentioned pipeline.

HOW TO RUN THE SCRIPTS INVOLVED AND AUTOMATE THE DEPLOYMENTS OF DOCKER CONTAINERS

The task is completed on linux environment: ubuntu:18.04

How to run files in linux environment in order to automate the docker container deployments

a. copy all files attached to an ubuntu machine 
b. run the shell script file : "script.sh" using the command: sudo bash script.sh
c. By default, the file test.json will be copied into container1 and the same will be transferred to container2 after encryption
d. The decrypted file which is in xml form can be found in the directory : results under / path.
e. The containers which are running in detached mode can be accessed by using the following command
   docker exec -it Container2 bash
   docker exec -it Container1 bash
f. Please feel free to create new json files/ edit existing json files.
g. The new changes will be reflected in corresponding xml files under "results" directory of container2

If there is any issue in running the files, please connect to my AWS instance - 52.214.74.253 , port: 22 , username : ubuntu
ppk key: "neuda_key" for the same is attached.

Thank You !
 
