FROM jenkins/jenkins:lts
USER root
RUN mkdir /my_app
WORKDIR /my_app
RUN apt-get update -y
RUN apt-get install software-properties-common -y
# RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get update -y
RUN apt-get install python3
RUN apt-get install python3-pip -y
