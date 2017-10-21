# -*- coding: utf-8 -*-
#读取pdf文档
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
import pdfminer.pdfinterp


#获取文档对象
fp = open("../res/b.pdf","rb")
#创建一个与文档关联的解释器
parser=PDFParser(fp)
#PDF文档对象
doc = PDFDocument()
#链接解释器和文档对象
parser.set_document(doc)
doc.set_parser(parser)
#初始化文档
doc.initialize("")
#创建pdf资源管理器
resource = PDFResourceManager()
#创建一个聚合器
device = PDFPageAggregator(resource,laparams=LAParams())
#创建PDF页面解释器
interpreter=PDFPageInterpreter(resource,device)


#使用文档对象得到页面的集合
for page in doc.get_pages():
    #使用页面解释器来读取
    interpreter.process_page(page)

    #使用聚合器来获取内容
    layout=  device.get_result()

    for out in layout:
        if hasattr(out,"get_text"):
            print(out.get_text())
