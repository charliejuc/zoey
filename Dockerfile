FROM python:3.7

RUN mkdir /zoey/ 
COPY ./* /zoey/
WORKDIR /zoey/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt