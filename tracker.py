#requests package required
#pip install requests
#pip3 install requests

import requests
import argparse
import json

print( ''' \033[93m
____ __________ _  _   ____  ____  _  _  ___ _   _ 
| __ )___ /___  | || | | __ )|  _ \| || ||_ _| \ | |
|  _ \ |_ \  / /| || |_|  _ \| |_) | || |_| ||  \| |
| |_) |__) |/ / |__   _| |_) |  _ <|__   _| || |\  |
|____/____//_/     |_| |____/|_| \_\  |_||___|_| \_| \033[0m \033[91m
IP Tracker                        CODED BY BETABRAIN        \033[0m  \033[37m                                           

               [run As Admin] \033[0m  
''')

if __name__=="__main__":
    
    parser=argparse.ArgumentParser()

    parser.add_argument("-i","--ipaddress",help="IP address to track")
    args=parser.parse_args()
    ip=args.ipaddress
   
    url="http://ip-api.com/json/"+str(ip)

    #http://ip-api/json/192.168.1.1

    response=requests.get(url)
    data = json.loads(response.content)
    print("\t[+] IP\t\t\t",data["query"])
    print("\t[+] LOC\t\t\t",data["country"])
    print("\t[+] CITY\t\t",data["city"])
    print("\t[+] ISP\t\t\t",data["isp"])
    print("\t[+] REG\t\t\t",data["regionName"])
    print("\t[+] ZIP\t\t\t",data["zip"])
    print("\t[+] LAT\t\t\t",data["lat"])
    print("\t[+] LON\t\t\t",data["lon"])
    print("\t[+] TIME\t\t",data["timezone"])
    print("\n\n")