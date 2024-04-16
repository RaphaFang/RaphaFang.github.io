from urllib.request import Request, urlopen
import bs4
import json
import csv

def get_page_title_url(url):
    req = Request(
        url, headers={'User-Agent': 'Mozilla/5.0','cookie':'over18=1'}
    )
    webpage = bs4.BeautifulSoup(urlopen(req).read().decode('utf-8'), features="html.parser")
    titles = webpage.find_all("div", class_="title")

    for title in titles:
        sub_webpage_data_list=[]
        if title.a != None:
            sub_webpage_data_list.append(title.a.string)
            title_url =  "https://www.ptt.cc"+title.a["href"]
            sub_webpage_data_list.append(title_url)
            req = Request(
                title_url, headers={'User-Agent': 'Mozilla/5.0','cookie':'over18=1'}
            )
            sub_webpage = bs4.BeautifulSoup(urlopen(req).read().decode('utf-8'), features="html.parser")
            push_count = len(sub_webpage.find_all('span', string = '推 '))
            dispush_count = len(sub_webpage.find_all('span', string = '噓 '))

        else:
            title_name = title.string[title.string.find("("):title.string.find("]")+1]
            title_url = []

        # title_url_dict[title_name]=title_url
        webpage_data_list.append(sub_webpage_data_list)

    # title_url = "https://www.ptt.cc"+title.a["href"]
    # push_count = title.find('span', string = '推 ').count()
    
    nextpage = webpage.find("a", string="‹ 上頁")
    return nextpage["href"]

# def get_like_count_publish_time():
#     req = Request(
#         url, headers={'User-Agent': 'Mozilla/5.0','cookie':'over18=1'}
#     )
#     webpage = bs4.BeautifulSoup(urlopen(req).read().decode('utf-8'), features="html.parser")
#     titles = webpage.find_all("div", class_="title")



title_url_dict = {}
webpage_data_list=[]
url = "https://www.ptt.cc/bbs/Lottery/index.html"
count=0
while count<3:
    url = "https://www.ptt.cc"+get_page_title_url(url)
    count+=1

print(title_url_dict)

# get_like_count_publish_time()






# ---------------------------------------------------------------------------------
# 解決HTTP error 403
#       https://stackoverflow.com/questions/16627227/how-do-i-avoid-http-error-403-when-web-scraping-with-python
# 解決18歲阻擋popup問題
#       req = Request(
#           url='https://www.ptt.cc/bbs/Lottery/index.html',
#           headers={'User-Agent': 'Mozilla/5.0','cookie':'over18=1'}}
# 解決本文刪除過長的字串問題