import requests
from lxml import etree
import re
#网址，头
url='https://movie.douban.com/chart'
h={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
ps=requests.get(url=url,headers=h)
ps_cog=ps.text
#解析
# html=etree.HTML(ps.cog)
# lis=html.xpath("/html/body/div[3]/div[1]/div/div[1]/div/div/table")
# for table in lis:
#     aaa=table.xpath("./tbody/tr/td[2]/div/a/span/text()")
#     print(aaa)
#解析2
obj=re.compile(r'<table width="100%" class="">.*?<tr class="item">.*? <td width="100" valign="top">.*?<span style="font-size:13px;">(?P<name>.*?)</span>',re.S)
#匹配
result=obj.finditer(ps_cog)
for it in result:
    print(it.group("name"))


#保存
#with open(r"书单","a",encoding="utf-8")as f:
   # f.write("{}".format(aaa))

