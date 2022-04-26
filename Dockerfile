FROM python:3.10

WORKDIR /app
ADD main.py .

RUN pip install redis

CMD [ "python", "main.py" ]
