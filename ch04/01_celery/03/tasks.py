# -*- coding: utf-8 -*-

import time
from celery import Celery

broker = 'redis://:pwd123@192.168.2.102:6379/0'
backend = 'redis://:pwd123@192.168.2.102:6379/1'

app = Celery('my_task', broker=broker, backend=backend)

@app.task
def hello(x):
    time.sleep(2)
    return 'hello ' + x

@app.task
def add(x, y):
    time.sleep(5)
    return x + y

@app.task
def minus(x, y):
    time.sleep(2)
    return x - y