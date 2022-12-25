import requests
p=input("输入")
url=f'https://{p}.html'
dic={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 QIHU 360SE/13.1.6290.0"
}
r=requests.get(url,headers=dic)
print(r.text)
r.close()

