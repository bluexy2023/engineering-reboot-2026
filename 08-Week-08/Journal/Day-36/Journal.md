# Day 36 Journal

# Summary
- learned about inheritance
# Challenges Encountered
- today's exercises and mini-project were straightforward
- I was able to grasp the concepts easily as exercises were limited to inheritance basics
# Solutions Applied
- N/A
# Confidence Assessment
9/10
# Reflection
- "SalariedEmployee IS-A Employee" is a stronger justification that just code reuse alone because SalariedEmployee can be used in the system where Employee is expected without breaking the system.  It allows for modeling domain concepts accurately.
- an example of has-a relationship that should not use inheritance is "Employee" has an Address, but Employee is not an Address. 
- if a subclass needs additional constructor data, it needs to perform super().__init__() and pass original parameters to parent contructor.
  => this results to non-uniform instantiability across the class heirarchy.
# Tomorrow Preparation
- continue to day 37
