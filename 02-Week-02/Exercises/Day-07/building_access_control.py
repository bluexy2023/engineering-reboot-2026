# building access control system
# this exercise is to create an python program to evaluate
# the conditions for a person to be granted access to a building or not

##### Requirements #####
# Only employees are allowed to enter the building
# within 8AM to 5PM
# hours are expressed in a 24-hour format

emp_status = input("Are you an employee? (Y/N): ")
hour_of_the_day = int(input("Hour of the day: (0-23): "))

if ( emp_status == "Y" and ( hour_of_the_day >= 8 ) 
    and (hour_of_the_day <= 17) ):
    print ("Access Granted")
else:
    print ("Access Denied")
