#! python3
# stopwatch.py - A simple stopwatch program

import time

# Display the program's instruction
print('Press ENTER to begin. Afterwards, press ENTER to click stopwatch. Press Ctrl + C to quit.!')
input()
print('Started')
startTime = time.time()
lastTime = startTime
lapNum = 1

     
# start tracking the lap time.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    # Handle the Ctrl + C
    print("\nDone!")
