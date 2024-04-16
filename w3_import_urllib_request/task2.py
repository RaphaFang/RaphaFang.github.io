from urllib.request import Request, urlopen
import bs4
import csv

def get_page_title_url(url):
    req = Request(
        url, headers={'User-Agent': 'Mozilla/5.0','cookie':'over18=1'}
    )
    webpage = bs4.BeautifulSoup(urlopen(req).read().decode('utf-8'), features="html.parser")

    blocks = webpage.find_all("div", class_="r-ent")

    for block in blocks:
        sub_webpage_data_list=[]
        title = block.find("div", class_="title")
        number_count = block.find("div", class_="nrec")
        if title.a != None:
            sub_webpage_data_list.append(title.a.string)

            if number_count.span != None:
                sub_webpage_data_list.append(number_count.span.string)
            else:
                sub_webpage_data_list.append(0)

            title_url =  "https://www.ptt.cc"+title.a["href"]
            req = Request(
                title_url, headers={'User-Agent': 'Mozilla/5.0','cookie':'over18=1'}
            )
            sub_webpage = bs4.BeautifulSoup(urlopen(req).read().decode('utf-8'), features="html.parser")
            
            article_meta_value_list = sub_webpage.find_all("span", class_="article-meta-value")
            if article_meta_value_list !=[]:
                sub_webpage_data_list.append(article_meta_value_list[-1].string)

        if sub_webpage_data_list != []:
            webpage_data_list.append(sub_webpage_data_list)

    nextpage = webpage.find("a", string="‹ 上頁")
    return nextpage["href"]

    # for title in titles:
    #     sub_webpage_data_list=[]
    #     if title.a != None:
    #         sub_webpage_data_list.append(title.a.string)

    #         title_url =  "https://www.ptt.cc"+title.a["href"]
    #         req = Request(
    #             title_url, headers={'User-Agent': 'Mozilla/5.0','cookie':'over18=1'}
    #         )
    #         sub_webpage = bs4.BeautifulSoup(urlopen(req).read().decode('utf-8'), features="html.parser")
            

    #         article_meta_value_list = sub_webpage.find_all("span", class_="article-meta-value")
    #         if article_meta_value_list !=[]:
    #             sub_webpage_data_list.append(article_meta_value_list[-1].string)





webpage_data_list=[]
url = "https://www.ptt.cc/bbs/Lottery/index.html"
count=0
while count<3:
    url = "https://www.ptt.cc"+get_page_title_url(url)
    count+=1
# print(webpage_data_list)

with open('RaphaFang.github.io/w3_import_urllib_request/article.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for n in webpage_data_list:
        writer.writerow(n)








# ---------------------------------------------------------------------------------
# 解決HTTP error 403
#       https://stackoverflow.com/questions/16627227/how-do-i-avoid-http-error-403-when-web-scraping-with-python
# 解決18歲阻擋popup問題
#       req = Request(
#           url='https://www.ptt.cc/bbs/Lottery/index.html',
#           headers={'User-Agent': 'Mozilla/5.0','cookie':'over18=1'}}
# 解決本文刪除過長的字串問題