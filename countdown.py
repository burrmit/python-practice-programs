import time
def countdown(mins,secs):
    i=mins
    j=secs
    k=0
    while True:
        if(j==-1):
            j=59
            i -=1
        if(j > 9):
            print(str(k)+str(i)+":"+str(j),end="\r")
        else:
            print(str(k)+str(i)+":"+str(k)+str(j),end="\r")
        time.sleep(1)
        j -= 1
        if(i==0 and j==-1):
            break
    if(i==0 and j==-1):
        print("Goodbye!", end="\r")
        time.sleep(1)
# countdown(int(input("Enter minutes: ")),int(input("Enter seconds: "))) # User Input
countdown(10,0) # countdown(mins, sec)
