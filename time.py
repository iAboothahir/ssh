from random import seed
from random import randint
import time
from datetime import date
from datetime import datetime
from threading import Timer

seed(1)

for _ in range(100):
	value = randint(0, 100)

today = date.today()
now = datetime.now()
d1 = today.strftime("%d/%m/%Y")
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

def timeout_handler(timeout=1):
    print("Date :", d1)
    print("Time :", dt_string)
    timer = Timer(timeout, timeout_handler)
    timer.start()

timeout_handler()
while True:
    print("Loading...", value, "%")
    time.sleep(1)
