# Day 37 Journal

# Summary
- learned about inheritance, super() for subclass __init__ to call parent initialization, and extending parent behavior by using super() in conjuntion with common method overriding
# Challenges Encountered
- concept was easy to follow 
# Solutions Applied
- none
# Confidence Assessment
- 9/10
# Reflection
- today's implementation changed my understanding of inheritance compared to Day 36 in that it illustrated that to allow for addition of states in the subclass, subclass initialization should call super().__init__ to pass common states with the parent subclass, and accommodate the new state under its own domain, i.e self.new_attrib = new_attrib in the subclass.  As well as that, common methods can be overriden by redefining the "public" method or behavior from the base class.  One must not mechanically just use super().common_method in the base class, if the common behavior is needed, the subclass can implement its own completely unit behavior.
# Tomorrow Preparation
- continue to polymorphism
