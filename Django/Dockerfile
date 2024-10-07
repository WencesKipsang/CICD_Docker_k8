
FROM python:3.12-alpine

WORKDIR /Django_CICD_app

ENV PYTHONUNBUFFERED = 1

COPY ./scripts /scripts
RUN chmod +x /scripts/*

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .
# RUN python3  manage.py collectstatic --noinput
EXPOSE 8999 
 CMD [ "entrypoint.sh"]