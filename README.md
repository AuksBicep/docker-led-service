[![Build Status](https://travis-ci.org/AuksBicep/docker-led-service.svg?branch=master)](https://travis-ci.org/AuksBicep/docker-led-service) [![Docker Pulls](https://img.shields.io/docker/pulls/auksbicep/docker-led-service.svg)](https://hub.docker.com/r/auksbicep/docker-led-service/)
# docker-led-service

Monitors number of docker containers running on Raspberry Pi, and will light up LED indicators for each container running.

## Details
LED Controller for [Blinkt](https://shop.pimoroni.com/products/blinkt).  The service parses json out of the environmental variables,  and uses compiled regular expressions on order to match image names of running [Docker](https://docs.docker.com/develop/sdk/) containers,  and light up specified colors.  Configuration loaded from Environment in alphabetical order, in the case of overlapping matches, first color match wins.

## Example
The following example will light up a red  led for each running container with the words **scheduler** and **arm** in it's image tags.  Blue for every running container with image tags matching **apiserver**, and purple for every running container with image tags with the word **transaction**.
```bash
docker run -d \
	-v /var/run/docker.sock:/var/run/docker.sock \
	--device /dev/gpiomem \
	-e DOCKER\_API\_VERSION=1.35 \
	-e DLS_IMAGE_COLOR_MATCH='{"match":"^(?=.*scheduler)(?=.*arm).*$", "r":255, "g":0, "b":0}' \
	-e DLS_IMAGE_COLOR_MATCH1='{"match":"apiserver", "r":255, "g":0, "b":255}' \
	-e DLS_IMAGE_COLOR_MATCH2='{"match":"transaction", "r":255, "g":0, "b":255}' \
	auksbicep/docker-led-service:arm
```
