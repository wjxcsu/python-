# -*- coding: utf-8 -*-
import requests
import codecs
import os
import re
from bs4 import BeautifulSoup
url = "http://www.qiushibaike.com/hot/page/"
f = codecs.open(u"糗事百科.txt", "w", "utf-8")
count=0
try:
    max = raw_input(u"请输入需要爬取的总页数：")
    while re.match(r"\d+", max)==None:
         max = raw_input(u"请输入正确的页数：")
    print u"爬取中。。。"
    for index in range(1, int(max)):
        req = requests.get(url+str(index))
        soup = BeautifulSoup(req.text, "html.parser")
        for item in soup.find_all("div", class_='article block untagged mb15'):
             item_thumb = item.find(class_="thumb")
             item_video = item.find(class_="video_holder")
             if item_thumb==None and item_video==None:
                item_author = item.find(class_="author clearfix")
                if item_author != None:
                    f.write(u"用户名："+item_author.h2.string+"\r\n")
                item_content = item.find(class_="content")
                f.write(u"   说："+item_content.text.strip()+"\r\n")
                item_vote = item.find(class_="stats-vote")
                f.write(u"  共有"+item_vote.i.string+u"人赞"+"\r\n\r\n")
                count+=1
    f.close()
    print u"爬取已经完成,共爬取%s条。\r\n在当前文件夹的\"糗事百科.txt\"中。"%count
except requests.exceptions.RequestException:
    print u"网络连接异常"
os.system("pause")
print 'wjx'
