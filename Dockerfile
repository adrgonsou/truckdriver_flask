FROM python:3.6

RUN mkdir /application
WORKDIR /application

ADD requirements.txt /application
RUN pip install -r requirements.txt

ADD . /application
RUN python setup.py develop
EXPOSE 8888

CMD ["python", "application/app.py"]