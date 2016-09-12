#!/bin/bash
set -e
LOGFILE=/home/ubuntu/{{ project_name }}.logs/{{ project_name }}-dev.log
LOGDIR=$(dirname $LOGFILE)
PROJECT_PATH=/home/ubuntu/{{ gitname }}/{{ project_name }}
NUM_WORKERS=3
ADDRESS=127.0.0.1:5000
# user/group to run as
USER=ubuntu
GROUP=ubuntu
source /home/ubuntu/{{ gitname }}/venv/bin/activate
cd /home/ubuntu/{{ gitname }}
pip install -r requirements.txt
test -d $LOGDIR || mkdir -p $LOGDIR
cd /home/ubuntu/{{ gitname }}/{{ project_name }}
exec envdir /home/ubuntu/.env gunicorn {{ project_name }}.wsgi -w $NUM_WORKERS --bind=$ADDRESS \
--user=$USER --group=$GROUP --log-level=debug --timeout=60 \
--log-file=$LOGFILE 2>>$LOGFILE
