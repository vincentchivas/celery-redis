echo "stoping celery for worker..."
CELERY_LOG_FILE="/home/bhuang/learning/celerydep/proj/log/work.log"
if pgrep -f $CELERY_LOG_FILE > /dev/null 2>&1;
then pkill -9 -f $CELERY_LOG_FILE
fi
