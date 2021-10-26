import time

for i in range(0,5):
    ptime = time.time()

    time.sleep(5)

    ctime = time.time()
    time1 = ctime-ptime
    print(time1)