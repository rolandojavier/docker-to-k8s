FROM python:3.10-slim-buster
LABEL MAINTAINER="Rolando Ramos"
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY app/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app/ /code/
CMD bash -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"