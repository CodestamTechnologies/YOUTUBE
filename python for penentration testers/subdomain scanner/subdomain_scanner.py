import requests

domain = input("ENTER THE URL >> ")

file = open("sub.txt")
cont = file.read()

subdomians = cont.splitlines()

for subdomian in subdomians:
    url = f"http://{subdomians}.{domain}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("[+]DISCOVERED DOAMINS >> ",url)