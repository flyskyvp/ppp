#-*-coding:utf-8-*-

import urllib
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import re
import sys
import os
reload(sys)
sys.setdefaultencoding('utf8')

#判断目录是否存在，不存在则创建
def creatPath(path):
    path=path.decode("UTF-8")
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)

#通过url获取html内容
def getContent(url):
    html = urllib.urlopen(url)

    content = html.read().decode('gbk').encode('utf-8')
    html.close()
    return content

#获取书名
def getBookName(content):
    soup = BeautifulSoup(content, 'html.parser')
    return soup.h1.string

##通过书名、章节名称 获取章节内容
def getText(content, bookName, chapterName):
    regex = r'(&nbsp;&nbsp;&nbsp;&nbsp;)(.*?)(<br /><br />)'
    pat = re.compile(regex)

    texts = re.findall(pat, content)

    path = "E:\\src\\myBook\\data\\" + bookName.decode("UTF-8") 

    creatPath(path)

    fileName = path + "\\" + chapterName.decode("UTF-8") + ".txt"

    f = open(fileName.decode('utf-8').encode('gbk'), 'a')
    f.truncate()
    i = 0
    for text in texts:
        conv_text = map(lambda x: x.decode("UTF-8"), text)
        i += 1
        print conv_text[1]
        f.write(conv_text[1].encode('utf-8'))  # 写文件时需要再次转码
        f.write('\n')

    f.close()

#获取所有章节
def getChapterNameList(url):
    content = getContent(url)
    soup = BeautifulSoup(content, 'html.parser', parse_only=SoupStrainer("dd"))
    bookName = str(getBookName(content))
    lists = soup.find_all('a')
    for list in lists:
        chapterName = list.string.encode('utf-8')
        url_c = url + list.get('href')
        content0 = getContent(url_c)
        getText(content0, bookName, chapterName)


##获取最新章节
def getNewetChapter(url):
    content = getContent(url)
    bookName = str(getBookName(content))
    print bookName
    soup = BeautifulSoup(content, 'html.parser', parse_only=SoupStrainer(id="info"))
    
    for i in soup.find_all('p'):
        str1=str(i.encode('utf-8'))
        pat =re.compile(r'<p>最新章节：.*</p>')
        if pat.search(str1):            
            url_c = url + i.a['href']
            content0 = getContent(url_c)
            chapterName = i.a.string.encode('utf-8')
            print bookName, chapterName
            getText(content0, bookName, chapterName)


def main():
    url0 = 'http://www.biquge.la/book/903/'
    # print getChapterNameList(url0)
    getNewetChapter(url0)

if __name__ == '__main__':
        main()
