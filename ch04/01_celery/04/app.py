
from celery import Celery
import celeryconfig

# include 表示每个 worker 应该导入的模块列表，以实例创建的模块的目录作为起始路径
app = Celery(__name__, include=["tasks"])

app.config_from_object(celeryconfig)
