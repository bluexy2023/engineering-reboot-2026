# decision program to evaluate a range of 
# values.  In this exercise, it is going to 
# evaluate voltage values and determine
# if they are high, low, or normal

voltage = int(input("Enter voltage: "))

if (voltage < 110 ):
    print ("Voltage Low")
elif (voltage > 120):
    print ("Voltage High")
else:
    print ("Voltage Normal")