import requests

def fetchAndSave(url,path):
    r=requests.get(url)
    with open(path,"w") as f:
        f.write(r.text)

url="https://timesofindia.indiatimes.com/"

fetchAndSave(url,"data/times.html")

