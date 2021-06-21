import time
from datetime import date
from datetime import datetime
from threading import Timer

today = date.today()
now = datetime.now()
d1 = today.strftime("%d/%m/%Y")
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

def timeout_handler(timeout=10):
    print("||||||||||||||||||||")
    print("Today's date :", d1)
    print("Now time :", dt_string)
    print("||||||||||||||||||||")
    timer = Timer(timeout, timeout_handler)
    timer.start()

timeout_handler()
while True:
    print("Loading...")
    time.sleep(1)
