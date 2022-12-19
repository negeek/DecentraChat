#!/bin/bash
env | while read line ; do echo "export "$line >> /etc/profile ; done
exec /usr/bin/supervisord -n 