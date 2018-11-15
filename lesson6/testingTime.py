from classTime import Time

myTime = Time()

myTime.set_time( 38, 59, 45)

for i in range(20):
    myTime.print_time()
    myTime.tick()