</Markdown>

# Day 37 Notes

# Concepts Learned
- inheritance, adding new attributes (states in the subclasses), method overriding in the subcclasses
- subclass adding unique states
- subclass implementing an extended version of its parent behavior

# Key Commands
- super(), super().__init__(), super().parent_method() - in the case of extending parent behavior

# Key Observations
- overriding is the act of changing the behavior of a common method (common behavior) from the parent.  It allows for a completely unique behavior, or an extention to the parent behavior (calling super.parent_behavior(), then adding unique subclass behavior)
- super() allows an inherited instance to access the behaviors and states of its parent class of objects
- constructor specialization allows for adding new states in the subclasses.  Without having the peform an assignment in the subclass for all the attributes passed to it as a paremeter, common attributes can be passed to the parent via super().__init__() to delegate the upkeep of the common states to the parent class, and in the subclass, just append new behavior to its own instance, i.e. self._new_attrib = new_attrib in the subclass' __init__() routine
- it's the parent's responsibiity to keep track of the common sates of all types of objects within its domain, while the subclass is only responsible of all the states unique to it.  The parent class doesn't have access to the attributes defined in the subclasses
- replacing behavior in the subclass allows for a completely new and unique behavior in the subclass through overriding a method with the same name in the parent.   Extending inherited behavior, on the other hand, just adds to whatever behavior that was defined in the parent classes.  By access super().some_method() from the parent class, subclass' some_method() implementation can add more code to make the behavior more unique.
- duplicated initializations reqiure a re-assignment of the subclass of all the attributes that are common to its base class.  by calling super().__init__() and passing common attributes, a clear delegation of responsibility is achieved - i.e. the parent initializes states that are common, while the subclass only initializes state unique to it.  This makes the code more clear, and concise.

# Lessons Learned
- see key observations

# Questions For Future Study
- none

