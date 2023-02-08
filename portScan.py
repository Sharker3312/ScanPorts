import socket, os, time, pyfiglet,sys,urllib
from os import system
from datetime import datetime

DEFAULT_TIMEOUT = 0.5
SUCCESS = 0

def clear():
    if os.name =="nt":
        os.system("cls")
    else:
        os.system("clear")    
        

    

def check_port( *host_port, timeout=DEFAULT_TIMEOUT):
       
    sock = socket.socket()
    sock.settimeout(timeout)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    connected = sock.connect_ex(host_port) 
    
    
    if (connected==0):
        return connected
        sock.close()
    #else:
        #print("CLOSE")    
        
def failed_arguments():
     if len(sys.argv) !=2:
        print("\n[i] Uso: python3 " + " <ip_adress>\n" )
        sys.exit(1)        
        
def menu():
    
    lista_ports=[]
    cant_ports=0
    
   
    ip_adress=sys.argv[1] 
    ip=socket.gethostbyname(ip_adress)
    
    try:
        ip_validation=socket.inet_aton(ip)
        flag_validation=0
        clear()
    except socket.error:
        flag_validation=1
        
    if flag_validation==0:
        ip=socket.gethostbyname(ip_adress)
    
    #banner
        clear()
        ascii_banner= pyfiglet.figlet_format("ScanPort")
        print(ascii_banner)
        print("    made by Sharker3312")
        print("-" *50)
        print("Scanning Target: " + ip )
        print("Scanning Target at: "+str(datetime.now()))
        print("-"*50)
    
    

        for port in range(1,81):
            porc=float(port / 81 ) *100
            porc=round(porc, 1)
            print(porc,"%",end="\r")
            time.sleep(0.5)
        
            imprimir= check_port(ip, port)
        
            if (imprimir==0):
                cant_ports=cant_ports+1
                lista_ports.append(port)   
           
        print("Open Ports ->",lista_ports) 
    if flag_validation==1:
        print("Incorrect ip adress, please verify")    
                
    
  
            
    
    
if __name__== '__main__':
    failed_arguments()
    menu()    



