</MARKDOWN>
Readme.md

This project is to demonstrate a developer workflow of 
preparing a python virtual environment to be able to run a python
script with all its dependencies

Files:
   .venv             - virtual environment 
 - ./requirement.txt - this is a listing of all dependencies that must be installed in-order to 
                       run the python code properly
   ./using_colorama.py - the actual python code to be executed
   ./bootstrap.sh - performs automated preparation of the virtual environment, which perform 
                    the following steps:
                        a. if .venv does not exist, perform python3 -m venv .venv
                        b. activates the virtual environment via "source .venv/bin/activate"
                        c. installs the module colorama via pip install colorama
                        d. runs the python program "using_colorama.py"
                        e. freezes the depencies through pip freeze > requirements.txt
   
