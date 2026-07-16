#!/usr/bin/env bash

#
# system_reporter.sh — a reusable bash script that produces an engineering system report  
# Description:
#   This utility gathers and displays the following information:
#      - Current user
#      - Current date/time
#      - Hostname
#      - Working directory
#      - Home directory
#      - Linux kernel
#      - Distribution information (if available)
#      - Bash version
#      - Python version
#      - Git version
#      - Disk usage
#      - Memory information
#      - System uptime
#
# Usage:
#   ./system_reporter.sh 
#
# Arguments:
#   None
# 
# Assumptions:
#    For the purpose of this mini-project, system reports are stored
#    under $HOME/system_reports/ directory
#   
#   
#
# Dependencies:
#   bash, git, python3
#
# Author: Glenn J.
# Date: July 2026
# ==============================================================================
system_reports_dir="$HOME/system_reports"
system_reports_time_stamp=$(date +%Y%m%d_%H%M%S)
system_reports_filename="system_reports_$system_reports_time_stamp.txt"
system_reports_destination_file="$system_reports_dir/$system_reports_filename"

if (($# > 0)); then
    echo "Usage: $0" >&2
    exit 2
fi

# Let's Prepare our output directory and initialize
#   the system report destination file
if mkdir -p "$system_reports_dir"; then
	touch "$system_reports_destination_file"
else
	echo "Failed to create $system_reports_dir" >&2
	exit 1
fi

# Start-up Display 
echo "====================================" | tee -a "$system_reports_destination_file"
echo "Engineering Reboot 2026"| tee -a "$system_reports_destination_file"
echo "Day 27 System Reporter" | tee -a "$system_reports_destination_file"
echo "====================================" | tee -a "$system_reports_destination_file"

# Current User
current_user=$(whoami)
echo -e "\nCurrent User" | tee -a "$system_reports_destination_file"
echo "--------------------" | tee -a "$system_reports_destination_file"
echo "$current_user" | tee -a "$system_reports_destination_file"
# Hostname
echo -e "\nHostname" | tee -a "$system_reports_destination_file"
echo "--------------------" | tee -a "$system_reports_destination_file"
echo "$HOSTNAME"| tee -a "$system_reports_destination_file"

# Working Directory
working_directory=$(pwd)
echo -e "\nWorking Directory" | tee -a "$system_reports_destination_file"
echo "--------------------" | tee -a "$system_reports_destination_file"
echo "$working_directory" | tee -a "$system_reports_destination_file"

# Home Directory
echo -e "\nHome Directory" | tee -a "$system_reports_destination_file"
echo "--------------------" | tee -a "$system_reports_destination_file"
echo "$HOME" | tee -a "$system_reports_destination_file"

# Kernel Information
linux_kernel=$(uname -r)
echo -e "\nLinux Kernel" | tee -a "$system_reports_destination_file"
echo "--------------------" | tee -a "$system_reports_destination_file"
echo "$linux_kernel" | tee -a "$system_reports_destination_file"

# Linux Distribution
echo -e "\nDistribution Information" | tee -a "$system_reports_destination_file"
echo "--------------------" | tee -a "$system_reports_destination_file"
if linux_distribution_info=$(source /etc/os-release && echo "$PRETTY_NAME"); then
    echo "$linux_distribution_info" | tee -a "$system_reports_destination_file"
else
    echo "Not available" | tee -a "$system_reports_destination_file"
fi

# Bash Version
echo -e "\nBash" | tee -a "$system_reports_destination_file"
echo "--------------------" | tee -a "$system_reports_destination_file"
if command -v bash > /dev/null; then
    echo "$(bash --version | head -1)" | tee -a "$system_reports_destination_file"
else
    echo "Not Available" | tee -a "$system_reports_destination_file"
fi

# Python
echo -e "\nPython" | tee -a "$system_reports_destination_file"
echo "--------------------" | tee -a "$system_reports_destination_file"
if command -v python3 >/dev/null; then
    echo "$(python3 --version)" | tee -a "$system_reports_destination_file"
else
    echo "Not Available" | tee -a "$system_reports_destination_file"
fi

# Git Version
echo -e "\nGit" | tee -a "$system_reports_destination_file"
echo "--------------------" | tee -a "$system_reports_destination_file"
if command -v git >/dev/null; then
    echo "$(git --version)" | tee -a "$system_reports_destination_file"
else
    echo "Not Available" | tee -a "$system_reports_destination_file"
fi

# Disk Usage
# let's limit it to the top 10 lines
echo -e "\nDisk Usage" | tee -a "$system_reports_destination_file"
echo "--------------------" | tee -a "$system_reports_destination_file"
df -h | head -10 | tee -a "$system_reports_destination_file"

# Memory Information
echo -e "\nMemory Information" | tee -a "$system_reports_destination_file"
echo "--------------------" | tee -a "$system_reports_destination_file"
free -h | tee -a "$system_reports_destination_file"

# System Uptime
echo -e "\nSystem Uptime" | tee -a "$system_reports_destination_file"
echo "--------------------" | tee -a "$system_reports_destination_file"
uptime | tee -a "$system_reports_destination_file"

# Execution completed
echo -e "\nReport successfully generated."
echo "=============================="
echo -e "\tFilename: \t$system_reports_filename"
echo -e "\tLocation: \t$system_reports_dir"


