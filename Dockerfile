FROM python:3.7
# updates and pip installation
RUN apt-get update -y \
    && apt-get install -y python3-pip
# set a new current working directory
WORKDIR /opt
COPY . /opt
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# export app to host's network
EXPOSE 5000
# run webapp
ENTRYPOINT ["python", "run.py"]