FROM python:3.10

WORKDIR /app
ADD inserter.py settings.py webserver.py ./

RUN pip install redis falcon

CMD [ "python", "inserter.py" ]
