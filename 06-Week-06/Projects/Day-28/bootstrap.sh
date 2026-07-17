#!/usr/bin/env bash

run_python_program()
{
	echo "Running Python Program..."
	python using_colorama.py
}

# Let's create our virtual environment called ".venv"
if [[ ! -d ".venv" ]]; then
	python3 -m venv .venv
fi

# let's activate our virtual environment
source .venv/bin/activate

# let's install our dependencies inside this virtual environment
python -m pip install -r requirements.txt

# let's run our python program
run_python_program

