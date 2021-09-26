# base image
FROM python:3.7-alpine
WORKDIR /opt
COPY . /opt
# install all python libraries in the specific relevant versions
RUN pip install -r requirements.txt
# get general updates
RUN ["apt-get", "update"]

# run project tests
RUN python -m unittest
# run the web application
ENTRYPOINT ["python", "run.py"]