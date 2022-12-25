import requests
#r=requests.head('https://www.so.com/s?ie=utf-8&src=hao_isearch2_cube&q=%E5%93%94%E5%93%A9%E5%93%94%E5%93%A9&eci=13220874&nlpv=base645zc1')
#print(r.headers)
r=requests.get("https://image.so.com/i?src=relation_wallpaper_card&q=%E5%8A%A8%E6%BC%AB%E5%A3%81%E7%BA%B8")
#返回状态码200则成功
print(r.status_code)
#r的类型
print(type(r))
print(r.headers)
print(r.text)
#查看编码
print(r.encoding)
print(r.apparent_encoding)
print(r.text)