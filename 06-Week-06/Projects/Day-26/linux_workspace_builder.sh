#!/usr/bin/bash

#
# linux_workspace_builder.sh — a reusable Bash script that prepares a standard 
# 	development workspace and verifies Python and Git availability.  
# Description:
#   This utility automates the creation of standard workspace directories
#   and directory structures required for a fresh local workspace. This also
#   verifies the availability of Python and Git, and displays their versions
#
# Usage:
#   ./linux_workspace_builder.sh [workspace_name] 
#
# Arguments:
#   workspace_name - name of the workspace that the user may supply(optional). 
#   		     This becomes the parent directory of the workspace
#                    If this argument is not supplied, the workspace name defaults
#                    to the value of DEFAULT_WORKSPACE_NAME.
# Assumptions:
#    For the purpose of this mini-project, supplied parameter should be a workspace
#    name that would be created relative to $HOME
#   
#   
#
# Dependencies:
#   bash, git, python3
#
# Author: Glenn J.
# Date: July 2026
# ==============================================================================


#-------------------
# Global Constants
#-------------------
readonly DEFAULT_WORKSPACE_NAME="development-workspace"
readonly REQUIRED_DIRS=(
	"projects"
	"scripts"
	"documentation"
	"data"
	"logs"
)

#------------------
# Local variables
# ----------------
python_status=""
git_status=""
workspace_builder_status=0

# start #
# Evaluate command line paramenters
if (( $# > 1 )); then
    echo "Usage: $0 [workspace_name]" >&2
    exit 2
elif (($# == 1)); then
   # check if we see a path from the first positional parameter
   if [[ "$1" == */* ]]; then
	   echo "[ERROR] Enter a workspace name only, not a path." >&2
	   exit 2
   fi
fi

# A. Display a Start up Message 
echo "Linux Workspace Builder"
echo "Preparing development workspace..."

# B. Determine the target workspace
workspace_name="${1:-$DEFAULT_WORKSPACE_NAME}"

# let's put our workspace_name under the home directory
workspace_path="$HOME/$workspace_name"

# C. Create the workspace directories
echo "--------------------------------"
if mkdir -p "$workspace_path"; then
	echo " [OK] Workspace directory ready: $workspace_path"
else
	echo " [ERROR] Failed to create $workspace_path" >&2
	workspace_builder_status=1
fi
# Create subdirectories
# iterate through list of required directories
for directory in "${REQUIRED_DIRS[@]}"; do
	if mkdir -p "$workspace_path/$directory"; then
		echo " [OK] Directory ready: $workspace_path/$directory"
	else
		echo " [ERROR] Failed to create $workspace_path/$directory" >&2
		workspace_builder_status=1
	fi
done

# D. Verify Python availability
echo "--------------------------------"
if python_path=$(command -v python3); then
    python_ver=$(python3 --version)
    python_status="Available"
    echo " [OK] Python found: $python_path"
    echo "      Version: $python_ver"
else
    echo " [ERROR] Python was not found." >&2
    python_status="Not Found"
    workspace_builder_status=1
fi

# E. Verify Git availability
echo "--------------------------------"
if git_path=$(command -v git); then
    git_ver=$(git --version)
    git_status="Available"
    echo " [OK] Git found: $git_path"
    echo "      Version: $git_ver"
else
    echo " [ERROR] Git was not found." >&2
    git_status="Not Found"
    workspace_builder_status=1
fi



# F. Report environment information
echo "--------------------------------"
echo "Environment Information"
echo "======================="
echo "Linux user: $(whoami)"
echo "Home Directory: $HOME"
echo "Current Working Directory: $(pwd)"
echo "Workspace Location: $workspace_path"
echo "Python status: $python_status" 
echo "Git status: $git_status" 
echo "Kernel Information: $(uname -a)"
echo "Shell: $SHELL"
echo "Hostname: $HOSTNAME"


# G. Display Resulting workspace
echo "--------------------------------"
find "$workspace_path" -maxdepth 1 -type d

# H. Display completion summary
echo "--------------------------------"
echo "Workspace Builder execution complete."
echo ""
echo "Workspace: $workspace_path"
echo "Python: $python_status"
echo "Git: $git_status"
if [[ $workspace_builder_status -eq 0 ]]; then
	echo "Status: SUCCESS"
else
	echo "Status: COMPLETED WITH ERRORS"
fi

exit "$workspace_builder_status"
