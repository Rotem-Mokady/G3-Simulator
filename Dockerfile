FROM python:3.7
# updates and pip installation
RUN apt-get update -y \
    && apt-get install -y python3-pip
# set a new current working directory
WORKDIR /opt
COPY . /opt
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# provide port to the outside network
EXPOSE 5000
# run app
ENTRYPOINT ["python", "run.py"]