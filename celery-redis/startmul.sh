if pgrep -f /home/bhuang/learning/celerydep/proj/log/work.log > /dev/null 2>&1;  
then echo "celery work is already running"
else
    echo "start to run celery for proj"
    celery multi start 3 -Q:1 add_queue -Q:2 mul_queue -Q:3 default --app=celtask.celeryapp:app  --loglevel=info --logfile=/home/bhuang/learning/celerydep/proj/log/work.log
fi
