FROM python:3.7

# general updates and pip installation
RUN apt-get update -y \
    && apt-get install -y python3-pip

# set a new current working directory
WORKDIR /opt

# add only relevant directories to Docker environment
ADD app ./app/
ADD calculations ./calculations/
ADD configs ./configs/

# add only relevant files to Docker environment
ADD run.py ./
ADD .gitignore ./
ADD requirements.txt ./

# install version specifiers python packages
RUN pip install --no-cache-dir -r requirements.txt

# no more need for requirements after packages installation
RUN rm -rf ./requirements.txt

# export app to host's network
# EXPOSE 5000

# run webapp
ENTRYPOINT ["python", "run.py"]