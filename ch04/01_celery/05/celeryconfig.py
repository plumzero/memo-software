
broker_url = 'redis://:pwd123@192.168.2.102:6379/0'
result_backend = 'redis://:pwd123@192.168.2.102:6379/1'
task_serializer = 'json'
result_serializer = 'json'
result_expires = 60 * 60 * 24
