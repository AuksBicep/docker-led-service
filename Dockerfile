FROM auksbicep/python2-docker-blinkt:arm

ADD ./scripts ./scripts

CMD python ./scripts/docker-led-service.py

