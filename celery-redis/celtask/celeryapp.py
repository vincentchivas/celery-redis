from __future__ import absolute_import
from datetime import timedelta
from celery.schedules import crontab
from celery import Celery
from kombu import Queue, Exchange

app = Celery(
    'celtask',
    backend='redis://localhost:6379/8',
    broker='redis://localhost:6379/9',
    include=['celtask.tasks'])

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,)


class MyRouter(object):
    '''rount for tasks'''
    def route_for_task(self, task, *args, **kwargs):
        if task == 'celtask.tasks.add':
            return {'queue': 'add_queue', 'routing_key': 'add_queue'}
        elif task == 'celtask.tasks.mul':
            return {'queue': 'mul_queue', 'routing_key': 'mul_queue'}
        else:
            return {'queue': 'default', 'routing_key': 'default'}

QUEUES = (
    Queue('add_queue', Exchange('add_queue'), routing_key='add_queue'),
    Queue('mul_queue', Exchange('mul_queue'), routing_key='mul_queue'),
    Queue('default', Exchange('default'), routing_key='default'),)

app.conf.update(
    CELERYBEAT_SCHEDULE={
        "test_xsum": {
            "task": "celtask.tasks.xsum",
            "schedule": timedelta(seconds=30),
            "args": (),
        },
        "test_crontab": {
            # ececutes every monday morning at 7:30
            "task": "celtask.tasks.cronjob",
            "schedule": crontab(hour=7, minute=30, day_of_week=1),
            "args": (),
        },
    },
    CELERY_QUEUES=QUEUES,
    CELERY_ROUTES=(MyRouter(),),
)


if __name__ == '__main__':
    app.start()
