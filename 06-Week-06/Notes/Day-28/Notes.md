</Markdown>

# Day 28 Notes

# Concepts Learned
new commands learned
- python -m venv .venv (to create a new python virtual environment)
- pip install
- pip install -r <dependency file>
observations about venv structure
- symlinks to actual commands like python and pip
- all packages installed for python are gathered in the virtual environment filesystem
differences between global and isolated environments
- inherits parent variables like PATH among others, but keep packages separate
package management workflow
  - create virtual enviroment
  - activate enviroment
  - perform operation on the new enviroment
  - deactivate virtual enviroment
engineering insights
  - creating slef-contained virtual environements allow for sandbox development
    where only packages needed for the performance of the task is installed.  This protects
    the system-wide configurations and thereby maintains the integrity of the system

# Key Commands
   - python -m venv .venv
     python -m pip install <module>
     source ./venv/bin/activate
     deactivate

# Key Observations
     python and bash can be executed alongside each other through the use of virtual environments

# Lessons Learned
    - learned about automating an engineering workflow and package management through isolated virtual environment

# Questions For Future Study

