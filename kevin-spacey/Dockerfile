FROM ubuntu:latest
MAINTAINER Srini Karlekar "skarlekar@yahoo.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install flask-restful
RUN pip install -U spacy
RUN python -m spacy download en
ENTRYPOINT ["python"]
CMD ["app.py"]
