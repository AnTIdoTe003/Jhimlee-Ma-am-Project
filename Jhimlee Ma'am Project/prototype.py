import time

incoming_data = int(input("Enter the amount of ammonia in water "))  # Data to be collected from cloud
# let range of ammonia is set to 5-10ppm
if incoming_data < 5:
    print("Water has less ammonia content ")
elif incoming_data > 10:
    print("Water has more ammonia medicine is to be distributed ")
    print("Machine is starting")
    time.sleep(10)  # the machine is switched on for 10 seconds
    print("Medicine distribution is complete")
elif incoming_data >= 5 & incoming_data <= 10:
    print("Water is okay ")
