FROM jenkins/jenkins:lts-alpine
USER root
### Install app dependencies
# Use apk to add python3 and then start bootstrapping pip
RUN apk add firefox
RUN apk add python3
RUN apk add py3-pip
RUN mv /usr/lib/python3.11/EXTERNALLY-MANAGED /usr/lib/python3.11/EXTERNALLY-MANAGED.old
# \
#         && curl -O https://bootstrap.pypa.io/get-pip.py \
#         && python3 get-pip.py
        #I needed python&pip for ansible, which itself needs some more stuff.

# To have a clean environment with the typical aliases
RUN pip3 install --upgrade pip
RUN pip3 install virtualenv
# change back to user jenkins
USER  jenkins