import time

i = 0
while True:
    print("Moni")
    i+=1
    if i == 4:
        print("End of Loop")
        break
    time.sleep(i)
