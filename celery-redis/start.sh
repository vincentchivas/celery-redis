if pgrep -f /home/bhuang/learning/celerydep/proj/log/work.log > /dev/null 2>&1;  
then echo "celery work is already running"
else
    echo "start to run celery for proj"
    nohup celery --app=celtask.celeryapp:app worker --loglevel=info --logfile=/home/bhuang/learning/celerydep/proj/log/work.log > /dev/null 2>&1 &
fi
