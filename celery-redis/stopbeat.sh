echo "stoping celery for beat..."
CELERY_LOG_FILE="/home/bhuang/learning/celerydep/proj/log/beat.log"
if pgrep -f $CELERY_LOG_FILE > /dev/null 2>&1;
then pkill -9 -f $CELERY_LOG_FILE
fi
