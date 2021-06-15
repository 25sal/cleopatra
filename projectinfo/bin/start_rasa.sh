#!/bin/sh
cd /home/cleobots/projectinfo
rasa run -m models --enable-api --cors "*" --debug -p 5005
