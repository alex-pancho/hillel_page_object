FROM jenkins/jenkins:latest
USER root
### Install app dependencies
# Use apk to add python3 and then start bootstrapping pip
RUN apt-get update
RUN apt-get install -y firefox-esr
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

# To have a clean environment with the typical aliases
# RUN pip3 install --upgrade pip
# RUN pip3 install virtualenv
# change back to user jenkins
USER  jenkins