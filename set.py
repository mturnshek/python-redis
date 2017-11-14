import redis
import numpy as np
import time

r = redis.StrictRedis(host='localhost', port=6379, db=0)

while True:
	r.set('user_input', input('? > '))
	time.sleep(0.25)