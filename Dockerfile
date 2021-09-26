# base image
FROM python:3.7-alpine
# copy the all project to main folder
COPY . /opt
# set the main folder as the current working directory
WORKDIR /opt/bin/sh
# get general updates
RUN ["apt-get", "update"]
# install all python libraries in the specific relevant versions
RUN pip install -r requirements.txt
# run project tests
RUN python -m unittest
# run the web application
ENTRYPOINT ["python", "run.py"]