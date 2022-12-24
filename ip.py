from os import system as sys
from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup as BS

sys('clear')

class ip:
    def banner(self):
        print ('''
   ________        __            .___        
  /  _____/  _____/  |_          |   |_____  
 /   \  ____/ __ \   __\  ______ |   \____ \ 
 \    \_\  \  ___/|  |   /_____/ |   |  |_> >
  \______  /\___  >__|           |___|   __/ 
         \/     \/                   |__|    
         
         scapy01
______________________________________________
''')
    def public_ip(self):
        headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"}
        url = Request('https://www.myip.com/',headers=headers)
        openurl = urlopen(url).read(99999)
        soup = BS(openurl , 'html.parser')
        for i in soup.findAll('span',{'id':'ip'}):
            print (f' [+] Public Ip > {i.text}')

    def privet_ip(self):
        sys("printf ' [+] Privet Ip > ';ifconfig wlan0 | grep 'netmask' | awk -F ' ' '{print $2}'")

    def localhost(self):
        print(" [+] LocalHost > 127.0.0.1\n")

ip = ip()
ip.banner()
ip.public_ip()
ip.privet_ip()
ip.localhost()
