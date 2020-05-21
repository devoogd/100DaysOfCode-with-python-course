import datetime
import time


def run_the_loop(dt):
    t1 = datetime.datetime.now()
    t2 = datetime.datetime.now()
    while int((t2 - t1).seconds) < dt:
        t2 = datetime.datetime.now()
        time.sleep(1)
        print(f'{t2 - t1} seconds')

dt = int(input('How many seconds does the loop need to count: '))

run_the_loop(dt)

print('done!')

