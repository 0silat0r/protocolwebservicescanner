from http import cookiejar
import socket
import requests
import os
import sys
import time
from pythonping import ping

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket()

try:

    os.system("clear")

    time.sleep(1)
    print("Lütfen Bekleyiniz...")
    time.sleep(1)
    print("Program Açılıyor...")
    time.sleep(1)
    os.system("clear")

    print("-------------------------------------")
    print("ProtocolWebServiceScannerV1")
    print("Programmer: Mfk880")
    print("-------------------------------------")
    time.sleep(3)

    url = input("Hedef URL: ")
    host = input("Hedef Host: ")
    port = input("Hedef Port: ")
    protocol = input("Etkinleştirmek İstediğiniz Protokolü Girin: ")

    os.system("clear")

    #Requests Information
    r = requests.get(url)
    statuscode = r.status_code
    codedbyte = r.encoding
    headers = r.headers["Content-Type"]
    headers2 = r.headers
    history = r.history
    cookies = r.cookies
    apparentencoding = r.apparent_encoding
    elapsed = r.elapsed
    reason = r.reason
    raw = r.raw

    #Socket Information
    ipaddress = socket.gethostbyname(host)
    addressinfo = socket.getaddrinfo(host, port)
    addressinfo2 = socket.getaddrinfo(host, port, family=socket.AF_INET, proto=socket.IPPROTO_TCP)
    addressinfo3 = socket.getaddrinfo(host, port, family=socket.AF_INET, proto=socket.IPPROTO_UDP)
    addressinfo4 = socket.getaddrinfo(host, port, family=socket.AF_INET, proto=socket.INADDR_BROADCAST)
    protocolname = socket.getprotobyname(protocol)

    print("________________________________________________________________")
    print("---------------------- Socket Information ----------------------")
    print(f"Target Host: {host}")
    print(f"Target URL: {url}")
    if port == "80":
        print(f"Target Port: {port} || HTTP Protocol Active")
    if port == "443":
        print(f"Target Port: {port} || HTTPS Protocol Active")
    print()
    print("Other IP Addresses")
    for i in addressinfo:
        print(f"-------------> {i}")
    print()
    for j in addressinfo2:
        print(f"-------------> {j}")
    print()
    for k in addressinfo3:
        print(f"-------------> {k}")
    print()
    for l in addressinfo4:
        print(f"-------------> {l}")
    print()
    if protocolname == "TCP":
        print(f"Protocol Name: TCP || Protocol Number İs {protocolname}")
    if protocolname == "UDP":
        print(f"Protocol Name: UDP || Protocol Number İs {protocolname}")    
    print()
    print()
    print("----------------------------------------------------------------")
    print()
    print("--------------------- Request Information ----------------------")
    print(f"Target URL: {url}")
    if statuscode == "200":
        print(f"Status Code: {statuscode} || HTTP 200 OK")
    if statuscode == "500":
        print(f"Status Code: {statuscode} || HTTP 500 Server Internal Error")
    if statuscode == "404":
        print(f"Status Code: {statuscode} || HTTP 404 Not Found ")
    print(f"Headers: {headers2}")
    print(f"Content-Type: {headers}")
    print(f"Cookies: {cookies}")
    print(f"Cookie Jar: {cookiejar}")
    print(f"Elapsed: {elapsed}")
    print(f"Reason: {reason}")
    print(f"Apparent Encoding: {apparentencoding}")
    print(f"Coding Type: {codedbyte}")
    print(f"Raw: {raw}")
    print(f"Status Codes History: {history}")
    print("----------------------------------------------------------------")   
    print()
    print("Port Information")
    print("----------------------------------------------------------------")
    print(f"Scaning Target: {ipaddress}")
    try:
        for port2 in range(1, 500):
            s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
    
            result = s4.connect_ex((ipaddress, port2))
            if result == 0:
                print("Port {} is open".format(port2))
            s4.close()
    except KeyboardInterrupt:
        print("Port Taramasını Durdurdunuz!")
        sys.exit()
    print("----------------------------------------------------------------")
 
except KeyboardInterrupt:
    print("Programdan Çıkış Yaptınız!")
