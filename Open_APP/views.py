from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests
import datetime
import urllib.request
import urllib.parse
# Create your views here.

def main(request):
    return render(request,'main.html')
   
def main1(request):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query=경제",headers={'User-Agent':'Mozilla/5.0'})
    html = BeautifulSoup(raw.text, "html.parser")
    articles = html.select("ul.type01 > li")
    time = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    
    newslist=[]
    print("갱신시각:", time)
    raw1 = requests.get("https://search.naver.com/search.naver?where=news&query=통상",headers={'User-Agent':'Mozilla/5.0'})
    html1 = BeautifulSoup(raw1.text, "html.parser")
    articles1 = html1.select("ul.type01 > li")
    time = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    
    newslist1=[]
    print("갱신시각:", time)
    raw2 = requests.get("https://search.naver.com/search.naver?where=news&query=투자",headers={'User-Agent':'Mozilla/5.0'})
    html2 = BeautifulSoup(raw1.text, "html.parser")
    articles2 = html1.select("ul.type01 > li")
    time = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    
    newslist2=[]
    print("갱신시각:", time)

    for ar in articles:
        title = ar.select_one("a._sp_each_title").text  #title
        source = ar.select_one("span._sp_each_source").text #요약
        link = ar.select_one("a").attrs['href'] #하이퍼링크 
        update = ar.select_one("dd.txt_inline").text.split(" ")
        dic ={'title':title,'source':source,'link':link,'update':update}
        newslist.append(dic)
        
        print(dic)
    for ar in articles1:
        title = ar.select_one("a._sp_each_title").text  #title
        source = ar.select_one("span._sp_each_source").text #요약
        link = ar.select_one("a").attrs['href'] #하이퍼링크 
        update = ar.select_one("dd.txt_inline").text.split(" ")
        dic ={'title':title,'source':source,'link':link,'update':update}
        newslist1.append(dic)
        
        print(dic)
    for ar in articles2:
        title = ar.select_one("a._sp_each_title").text  #title
        source = ar.select_one("span._sp_each_source").text #요약
        link = ar.select_one("a").attrs['href'] #하이퍼링크 
        update = ar.select_one("dd.txt_inline").text.split(" ")
        dic ={'title':title,'source':source,'link':link,'update':update}
        newslist2.append(dic)
        
        print(dic)
    return render(request,'main1.html',{'newslist':newslist,'time':time,'newslist1':newslist1,'newslist2':newslist2})
    


