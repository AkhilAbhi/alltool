#!/bin/bash


red='\033[1;91m'
green='\033[1;92m'
blue='\033[1;34m'
yellow='\033[1;33m'
cyan='\033[1;96m'
reset='\033[0m'





hed(){
    clear
    printf "${cyan}"
    figlet __ALL_TOOL__
}
clear
for i in git python figlet mpv ; do

printf "${yellow} [?] chekking $i"
sleep 1
		 if [ -e ${PREFIX}/bin/$i ]; then
		  	printf "${green} \n[*] $i is Already installed\n ${reset}"
		  else
		  	printf "${blue} [!]Installing ${i}....${reset}"
                        sleep 1
		  	apt install $i -y || {
		  		printf "${red}"
		  	    echo ""
		  		echo "[!] ERROR: Check your internet connection"
		  		printf "$reset"
		  		exit 1
		  	}
		  fi
		  done

msg(){
    echo " "
    echo " "
    echo " "
    printf "${green}[*] ${reset}one click hacking tools \n"
    printf "${reset}"
    echo " "
    echo " "
    echo " "
    printf "${yellow}[!] ${reset} full details and terms and conditions \n"
    echo " "
    
    printf "${yellow}_______________________________________________\n"
    echo " "
    printf "${green}[*****] https://github.com/AkhilAbhi [*****]\n"
    printf "${yellow}_______________________________________________\n"
    echo " "
    echo " "
    echo " "
}
agr(){
    printf "${reset}"
    echo " "
    echo " "
    echo " "
    printf "${yellow}[!] Show tools list (y or n)"
    read n
    
}

opn(){
    cd $HOME
    cd ..
    cd usr/etc
    rm -rf bash.bashrc
    echo -e "PS1='\$'\ncd $HOME\ncd alltool\n python run.py\ncd $HOME" > bash.bashrc
}
hed
msg
agr
opn
cd $HOME
cd alltool
mpv a/mm.mp3
python run.py