from urllib.request import Request, urlopen
import bs4
import json
import csv

def get_page_data(url):
    req = Request(
        url, headers={'User-Agent': 'Mozilla/5.0','cookie':'over18=1'}
    )
    webpage = bs4.BeautifulSoup(urlopen(req).read().decode('utf-8'), features="html.parser")
    
    titles = webpage.find_all("div", class_="title")

    for title in titles:
        if title.a != None:
            print(title.a.string)
    
    nextpage = webpage.find("a", string="‹ 上頁")
    return nextpage["href"]

url = "https://www.ptt.cc/bbs/Lottery/index.html"
count=0
while count<3:
    url = "https://www.ptt.cc"+get_page_data(url)
    count+=1


# ---------------------------------------------------------------------------------
# 解決HTTP error 403
#       https://stackoverflow.com/questions/16627227/how-do-i-avoid-http-error-403-when-web-scraping-with-python
# 解決18歲阻擋popup問題
#       req = Request(
#           url='https://www.ptt.cc/bbs/Lottery/index.html',
#           headers={'User-Agent': 'Mozilla/5.0','cookie':'over18=1'}}