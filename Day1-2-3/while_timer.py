import datetime
import time

t = datetime.datetime.now()
loops = 20 # seconds

while loops > 0:
    print(f'{loops} seconds')
    time.sleep(1)
    loops -= 1
    t2 = datetime.datetime.now()

print(f'{(t2-t).seconds} seconds')
print(f'{((t2-t).seconds)/60} minutes')