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
    
    print()
    print("Turkish Language")
    print("-------------------------------------")
    print("Kullanım Kılavuzu")
    print("Hedef URL: http://example.org")
    print("Hedef Host: example.org")
    print("Hedef Port: 443 or (ya da) 80")
    print("Not: Eğer 443 kullanılacak ise Hedef URL Tarafında https kullanılması önerilir.\n80 Portu için ise http kullanılması önerilir.")
    print("Etkinleştirmek İstediğiniz Protokolü Girin: TCP")
    print("Not: Genel olarak internet üzerinde çalışan bir çok site TCP mantığıyla çalışır. \nBurda TCP'nin protokol sıra numarası alınmakta.")
    print("-------------------------------------")
    print()
    print("English Language")
    print("-------------------------------------")
    print("User Manual")
    print("Destination URL: http://example.org")
    print("Target Host: example.org")
    print("Destination Port: 443 or (or) 80")
    print("Note: If 443 is to be used, https on the Destination URL Side It is recommended to use http.\nFor port 80, it is recommended to use http.")
    print("Enter the Protocol you want to enable: TCP")
    print("Note: In general, many sites on the internet work with TCP logic. \nHere is the protocol sequence number of TCP.") 
    print("-------------------------------------")
    print()
    
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
    print("Address Information")
    for i in addressinfo:
        print(f"-------------> {i}")
    print()
    print("TCP/IP Protocol Information")
    for j in addressinfo2:
        print(f"-------------> {j}")
    print()
    print("UDP Protocol Information")
    for k in addressinfo3:
        print(f"-------------> {k}")
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
    print("PING Information")
    print("----------------------------------------------------------------")   
    response = os.system(f"ping -c 4 {host}")
    print(response)
    print("----------------------------------------------------------------")
    print()
    print("Port Information")
    print("----------------------------------------------------------------")
    print(f"Scaning Target: {ipaddress}")
    try:
        for port2 in range(1, 65535):
            s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
    
            result = s4.connect_ex((ipaddress, port2))
            if result == 0:
                print("Port {} is open".format(port2))
            s4.close()
    except KeyboardInterrupt:
        print("Port Taramasını Durdurdunuz!")
print("----------------------------------------------------------------")
    
except KeyboardInterrupt:
    print("Programdan Çıkış Yaptınız!")
