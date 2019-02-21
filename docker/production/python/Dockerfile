FROM python:3.4

#copy current directory
COPY . /app/

#set current directory
WORKDIR /app

RUN pip install -r requirements/prod.txt

COPY ./docker/production/python/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
