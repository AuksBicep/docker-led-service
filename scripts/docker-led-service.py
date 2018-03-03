#!/usr/bin/env python

import os
import json
import colorsys
import time
import itertools
import sys
import re

import docker
import blinkt

docker_client = docker.from_env()
blinkt.set_clear_on_exit()
blinkt.set_brightness(0.034)

match_color = reduce(
        lambda acc, cur: dict(itertools.chain(acc.items(), { re.compile(cur['match']):cur }.items())),
        [json.loads(v) for k, v in os.environ.items() if k.startswith('DLI_CONTAINER')],
        {})

while True:
    pixel = -1
    for x in (docker_client.containers.list()):
        for reg_ex in match_color.keys():
            if reg_ex.search(''.join(map(str,x.image.tags))):
                pixel += 1
                blinkt.set_pixel(
                        pixel, 
                        match_color[reg_ex]['r'], 
                        match_color[reg_ex]['g'], 
                        match_color[reg_ex]['b'])
                time.sleep(0.1)
                blinkt.show()
                break
    for x in range(blinkt.NUM_PIXELS-1, pixel, -1):
        blinkt.set_pixel(x, 0,0,0)
    blinkt.show()
    time.sleep(5)

