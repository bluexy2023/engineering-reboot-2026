# Eligibility checker for a person to be able to 
# avail of a service

# Requirements:
# Processing Rule
# ---------------
# Eligible when:
# Age >= 18
# AND
# Age <= 65
# Outputs
# -------
# Eligible
# Not Eligible

age = int(input("Enter age: "))
if ( age >= 18 and age <= 65 ):
    print ("Eligible")
else:
    print ("Not Eligible")
