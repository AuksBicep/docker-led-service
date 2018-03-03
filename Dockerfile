FROM arm32v7/python:2.7.14-slim-stretch

RUN apt-get update && \
    apt-get install -y --no-install-recommends g++ && \
    apt-get clean

ADD ./requirements.txt .

RUN pip install -r requirements.txt

ADD ./scripts ./scripts

CMD python ./scripts/docker-led-service.py

