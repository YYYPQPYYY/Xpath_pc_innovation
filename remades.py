import re
sq=re.finditer(r"\d+", "我的电话10086，我那的电话1010")
#print(sq)
for i in sq:
    #print(i)
    print(i.group())

