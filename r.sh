#!/bin/bash


red='\033[1;91m'
green='\033[1;92m'
blue='\033[1;34m'
yellow='\033[1;33m'
cyan='\033[1;96m'
reset='\033[0m'



clear

cd /data/data/com.termux/files/usr/etc
rm -rf bash.bashrc
echo -e "PS1='\$' " > bash.bashrc
printf "${green}"
figlet unlock
printf "${reset}"