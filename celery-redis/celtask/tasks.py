from __future__ import absolute_import
import time
from celtask.celeryapp import app
from pymongo import Connection


@app.task
def add(x, y):
    time.sleep(5)
    return x + y


@app.task
def mul(x, y):
    time.sleep(10)
    return x * y


@app.task
def xsum():
    numbers = [1, 2, 3]
    conn = Connection('localhost')
    col = conn['test-beat']['beat']
    col.insert({'now': time.time()})
    time.sleep(5)
    return sum(numbers)


@app.task
def cronjob():
    numbers = [1, 2, 3]
    conn = Connection('localhost')
    col = conn['test-beat']['beatcron']
    col.insert({'now': time.time()})
    time.sleep(5)
    return sum(numbers)
