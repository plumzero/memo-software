# -*- coding: utf-8 -*-

import time
from celery import Celery

broker = 'redis://:redispassword@192.168.2.102:6379/0'
backend = 'redis://:redispassword@192.168.2.102:6379/1'

app = Celery('my_task', broker=broker, backend=backend)

@app.task
def add(x, y):
    time.sleep(5)   # 模拟耗时操作
    return x + y