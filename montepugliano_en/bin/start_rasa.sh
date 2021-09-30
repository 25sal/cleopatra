#!/bin/sh
cd /home/cleobots/arcotraiano
rasa run -m models --enable-api --cors "*" --debug -p 5000
