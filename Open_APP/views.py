from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests
import datetime
import urllib.request
import urllib.parse
# Create your views here.

from django.conf import settings
import os
import pandas as pd
import json

def main(request):
    #chart1 data
    excel_path = os.path.join(settings.BASE_DIR, 'excel_files', 'small.xlsx')
    excel_df = pd.read_excel(excel_path, header=4, thousands=',')
    excel_df = excel_df.drop(0)
    excel_df = excel_df.drop([excel_df.columns[4], excel_df.columns[5], excel_df.columns[6]], axis=1)
    excel_df = excel_df.sort_values(by='수출금액', ascending=False).head(3)
    result = excel_df.to_json(orient='records')
    dataset1 = json.loads(result)
    #print('1====================================>')
    #print(json.dumps(dataset1, indent=4, ensure_ascii=False))
    
    #chart2 data
    excel_path = os.path.join(settings.BASE_DIR, 'excel_files', 'country_trade.xls')
    excel_df = pd.read_excel(excel_path, header=4, thousands=',')
    excel_df = excel_df.drop(0)
    excel_df = excel_df.drop([excel_df.columns[2], excel_df.columns[4], excel_df.columns[5], excel_df.columns[6]], axis=1)
    excel_df['총수출금액'] = excel_df.groupby(['기간']).수출금액.transform('sum')
    excel_df = excel_df.sort_values(['기간', '수출금액'], ascending=[True, False]).groupby('기간').head(10)
    result = excel_df.to_json(orient='records')
    dataset2 = json.loads(result)
    #print('2====================================>')
    #print(json.dumps(dataset2, indent=4, ensure_ascii=False))
    
    #chart3 data
    excel_path = os.path.join(settings.BASE_DIR, 'excel_files', 'small3.xlsx')
    excel_df = pd.read_excel(excel_path, header=4, thousands=',')
    excel_df = excel_df.drop(0)
    excel_df = excel_df.drop([excel_df.columns[4], excel_df.columns[5], excel_df.columns[6]], axis=1)
    excel_df = excel_df.sort_values(by='수출금액', ascending=False).head(3)
    result = excel_df.to_json(orient='records')
    dataset3 = json.loads(result)
    #print('3====================================>')
    #print(json.dumps(dataset3, indent=4, ensure_ascii=False))
    
    #chart4 data
    excel_path = os.path.join(settings.BASE_DIR, 'excel_files', 'small4.xlsx')
    excel_df = pd.read_excel(excel_path, header=4, thousands=',')
    excel_df = excel_df.drop(0)
    excel_df = excel_df.drop([excel_df.columns[4], excel_df.columns[5], excel_df.columns[6]], axis=1)
    excel_df = excel_df.sort_values(by='수출금액', ascending=False).head(3)
    result = excel_df.to_json(orient='records')
    dataset4 = json.loads(result)
    #print('4====================================>')
    #print(json.dumps(dataset4, indent=4, ensure_ascii=False))
    
    return render(request,'main.html', {'dataset1':dataset1, 'dataset2':dataset2, 'dataset3':dataset3, 'dataset4':dataset4})
  
   
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
    


