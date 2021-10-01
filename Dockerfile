FROM python:3.7

# general updates and pip installation
RUN apt-get update -y \
    && apt-get install -y python3-pip

# set a new current working directory
WORKDIR /opt

# add only relevant directories to Docker environment
ADD app /opt/app
ADD calculations /opt/calculations
ADD configs /opt/configs

# add only relevant files to Docker environment
ADD run.py /opt
ADD .gitignore /opt
ADD requirements.txt /opt

# install version specifiers python packages
RUN pip install --no-cache-dir -r requirements.txt

# export app to host's network
# EXPOSE 5000

# run webapp
ENTRYPOINT ["python", "run.py"]