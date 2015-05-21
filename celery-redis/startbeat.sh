if pgrep -f /home/bhuang/learning/celerydep/proj/log/beat.log > /dev/null 2>&1;  
then echo "celery beat is already running"
else
    echo "start to run celery beat for proj"
    nohup celery beat --app=celtask.celeryapp:app  --loglevel=info --logfile=/home/bhuang/learning/celerydep/proj/log/beat.log > /dev/null 2>&1 &
fi
