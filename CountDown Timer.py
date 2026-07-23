import time
def CountDown():
    timer=float(input("Enter Seconds="))
    while timer>0:
        print(timer)
        time.sleep(1)   #if we Don't put this then all Seconds Will Immediately
        timer-=1
    print("Times Up")
CountDown()