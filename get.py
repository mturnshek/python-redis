import redis
import numpy as np
import time

r = redis.StrictRedis(host='localhost', port=6379, db=0)

while True:
	print((r.get('user_input').decode('utf-8')))
	time.sleep(0.25)