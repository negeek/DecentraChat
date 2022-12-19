#!/bin/bash
source /chat_env/bin/activate
cd /code

#daphne -u /run/daphne/daphne%(process_num)d.sock --fd 0 --access-log - --proxy-headers chatProj.asgi:application
daphne -b 0.0.0.0 -p 8001 chatProject.asgi:application