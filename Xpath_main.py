from lxml import  etree

text = '''
<book>
    <id>1</id>
    <name>可可树了</name>
    <author>
        <nice>直走到</nice>
        <nice>司法局</nice>
        <div>
            <nice>奥利弗1</nice>
        </div>
            <div>
                <nice>奥利弗2</nice>
            </div>
        <div>
            <nice>奥利弗3</nice>
        </div>
         <n>
            <nice>这里标签为n包围的nice</nice>
        </n>
    </author>
 </book>
'''
tree = etree.XML(text)
# result = tree.xpath("/BOOK")
# result=tree.xpath("/book/name")
# result=tree.xpath("/book/name/text()")#拿文本
# result=tree.xpath("/book/author/nice/text()")#['直走到', '司法局']
# result=tree.xpath("/book/author/div/nice/text()")#['奥利弗1']
# result=tree.xpath("/book/author//nice/text()")#['直走到', '司法局', '奥利弗1']
# result=tree.xpath("/book/author//nice/text()")#['直走到', '司法局', '奥利弗1', '奥利弗2', '奥利弗3']
result=tree.xpath("/book/author/*/nice/text()")#['奥利弗1', '奥利弗2', '奥利弗3', '这里标签为n包围的nice']    *任意节点，通配符
print(result)

