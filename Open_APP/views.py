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


def main(request, year='2015'):
    #chart1 data
    excel_path = os.path.join(settings.BASE_DIR, 'excel_files', 'by-item_202010305.xls')
    excel_df = pd.read_excel(excel_path, header=4, thousands=',')
    excel_df = excel_df.drop(0)
    excel_df = excel_df.drop([excel_df.columns[3], excel_df.columns[4]], axis=1)
    excel_df = excel_df.sort_values(['기간', '수출금액'], ascending=[True, False]).groupby('기간').head(10)
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
        #---usa data---->
    excel_path = os.path.join(settings.BASE_DIR, 'excel_files', 'usa_trade.xls')
    excel_df = pd.read_excel(excel_path, header=2, thousands=',')
    excel_df = excel_df.drop(0)
    excel_df = excel_df.drop([excel_df.columns[4]], axis=1)
    excel_df.rename(columns = {'년월':'연도', '총무역금액\n(백만불)':'총무역금액', '한국무역금액\n(백만불)':'한국무역금액', '비중\n(%)':'무역비중', '순위':'무역순위'}, inplace = True)
    excel_path = os.path.join(settings.BASE_DIR, 'excel_files', 'usa_import.xls')
    excel_df2 = pd.read_excel(excel_path, header=2, thousands=',')
    excel_df2 = excel_df2.drop(0)
    excel_df2 = excel_df2.drop([excel_df2.columns[0]], axis=1)
    excel_df2.rename(columns = {'총수입금액\n(백만불)':'총수입금액', '한국수입금액\n(백만불)':'한국수입금액', '비중\n(%)':'수입비중', '순위':'수입순위'}, inplace = True)
    excel_path = os.path.join(settings.BASE_DIR, 'excel_files', 'usa_export.xls')
    excel_df3 = pd.read_excel(excel_path, header=2, thousands=',')
    excel_df3 = excel_df3.drop(0)
    excel_df3 = excel_df3.drop([excel_df3.columns[0]], axis=1)
    excel_df3.rename(columns = {'총수출금액\n(백만불)':'총수출금액', '한국수출금액\n(백만불)':'한국수출금액', '비중\n(%)':'수출비중', '순위':'수출순위'}, inplace = True)
    excel_df = pd.concat([excel_df, excel_df2, excel_df3], axis=1, sort=False)
    excel_df = excel_df.head(5)
    excel_df = excel_df.sort_values(['연도'], ascending=True)
    result = excel_df.to_json(orient='records')
    dataset3_usa = json.loads(result)

        #---china data---->
    excel_path = os.path.join(settings.BASE_DIR, 'excel_files', 'china_trade.xls')
    excel_df = pd.read_excel(excel_path, header=2, thousands=',')
    excel_df = excel_df.drop(0)
    excel_df = excel_df.drop([excel_df.columns[4]], axis=1)
    excel_df.rename(columns = {'년월':'연도', '총무역금액\n(백만불)':'총무역금액', '한국무역금액\n(백만불)':'한국무역금액', '비중\n(%)':'무역비중', '순위':'무역순위'}, inplace = True)
    excel_path = os.path.join(settings.BASE_DIR, 'excel_files', 'china_import.xls')
    excel_df2 = pd.read_excel(excel_path, header=2, thousands=',')
    excel_df2 = excel_df2.drop(0)
    excel_df2 = excel_df2.drop([excel_df2.columns[0]], axis=1)
    excel_df2.rename(columns = {'총수입금액\n(백만불)':'총수입금액', '한국수입금액\n(백만불)':'한국수입금액', '비중\n(%)':'수입비중', '순위':'수입순위'}, inplace = True)
    excel_path = os.path.join(settings.BASE_DIR, 'excel_files', 'china_export.xls')
    excel_df3 = pd.read_excel(excel_path, header=2, thousands=',')
    excel_df3 = excel_df3.drop(0)
    excel_df3 = excel_df3.drop([excel_df3.columns[0]], axis=1)
    excel_df3.rename(columns = {'총수출금액\n(백만불)':'총수출금액', '한국수출금액\n(백만불)':'한국수출금액', '비중\n(%)':'수출비중', '순위':'수출순위'}, inplace = True)
    excel_df = pd.concat([excel_df, excel_df2, excel_df3], axis=1, sort=False)
    excel_df = excel_df.head(5)
    excel_df = excel_df.sort_values(['연도'], ascending=True)
    result = excel_df.to_json(orient='records')
    dataset3_china = json.loads(result)

        #---japan data---->
    excel_path = os.path.join(settings.BASE_DIR, 'excel_files', 'japan_trade.xls')
    excel_df = pd.read_excel(excel_path, header=2, thousands=',')
    excel_df = excel_df.drop(0)
    excel_df = excel_df.drop([excel_df.columns[4]], axis=1)
    excel_df.rename(columns = {'년월':'연도', '총무역금액\n(백만￥)':'총무역금액', '한국무역금액\n(백만￥)':'한국무역금액', '비중\n(%)':'무역비중', '순위':'무역순위'}, inplace = True)
    excel_path = os.path.join(settings.BASE_DIR, 'excel_files', 'japan_import.xls')
    excel_df2 = pd.read_excel(excel_path, header=2, thousands=',')
    excel_df2 = excel_df2.drop(0)
    excel_df2 = excel_df2.drop([excel_df2.columns[0]], axis=1)
    excel_df2.rename(columns = {'총수입금액\n(백만￥)':'총수입금액', '한국수입금액\n(백만￥)':'한국수입금액', '비중\n(%)':'수입비중', '순위':'수입순위'}, inplace = True)
    excel_path = os.path.join(settings.BASE_DIR, 'excel_files', 'japan_export.xls')
    excel_df3 = pd.read_excel(excel_path, header=2, thousands=',')
    excel_df3 = excel_df3.drop(0)
    excel_df3 = excel_df3.drop([excel_df3.columns[0]], axis=1)
    excel_df3.rename(columns = {'총수출금액\n(백만￥)':'총수출금액', '한국수출금액\n(백만￥)':'한국수출금액', '비중\n(%)':'수출비중', '순위':'수출순위'}, inplace = True)
    excel_df = pd.concat([excel_df, excel_df2, excel_df3], axis=1, sort=False)
    excel_df = excel_df.head(5)
    excel_df = excel_df.sort_values(['연도'], ascending=True)
    result = excel_df.to_json(orient='records')
    dataset3_japan = json.loads(result)

        #---eu data---->
    excel_path = os.path.join(settings.BASE_DIR, 'excel_files', 'eu_trade.xls')
    excel_df = pd.read_excel(excel_path, header=2, thousands=',')
    excel_df = excel_df.drop(0)
    excel_df = excel_df.drop([excel_df.columns[4]], axis=1)
    excel_df.rename(columns = {'년월':'연도', '총무역금액\n(백만€)':'총무역금액', '한국무역금액\n(백만€)':'한국무역금액', '비중\n(%)':'무역비중', '순위':'무역순위'}, inplace = True)
    excel_path = os.path.join(settings.BASE_DIR, 'excel_files', 'eu_import.xls')
    excel_df2 = pd.read_excel(excel_path, header=2, thousands=',')
    excel_df2 = excel_df2.drop(0)
    excel_df2 = excel_df2.drop([excel_df2.columns[0]], axis=1)
    excel_df2.rename(columns = {'총수입금액\n(백만€)':'총수입금액', '한국수입금액\n(백만€)':'한국수입금액', '비중\n(%)':'수입비중', '순위':'수입순위'}, inplace = True)
    excel_path = os.path.join(settings.BASE_DIR, 'excel_files', 'eu_export.xls')
    excel_df3 = pd.read_excel(excel_path, header=2, thousands=',')
    excel_df3 = excel_df3.drop(0)
    excel_df3 = excel_df3.drop([excel_df3.columns[0]], axis=1)
    excel_df3.rename(columns = {'총수출금액\n(백만€)':'총수출금액', '한국수출금액\n(백만€)':'한국수출금액', '비중\n(%)':'수출비중', '순위':'수출순위'}, inplace = True)
    excel_df = pd.concat([excel_df, excel_df2, excel_df3], axis=1, sort=False)
    excel_df = excel_df.head(5)
    excel_df = excel_df.sort_values(['연도'], ascending=True)
    result = excel_df.to_json(orient='records')
    dataset3_eu = json.loads(result)
    #print('3====================================>')
    #print(json.dumps(dataset3, indent=4, ensure_ascii=False))
    
    #chart4 data
    #chart4 data
    if request.method == "POST":
        year = request.POST['year']
    excel_path = os.path.join(settings.BASE_DIR, 'excel_files', 'small4.xlsx')
    excel_df = pd.read_excel(excel_path, header=4, thousands=',')
    excel_df = excel_df.drop(0)
    excel_df = excel_df.drop(
        [excel_df.columns[4], excel_df.columns[5], excel_df.columns[6]], axis=1)
    excel_df = excel_df.sort_values(by='수출금액', ascending=False).head(3)
    result = excel_df.to_json(orient='records')

    dataset4 = json.loads(result)
    im_path = os.path.join(settings.BASE_DIR, 'excel_files', '성질별수입.xls')
    im_df = pd.read_excel(im_path, header=4, thousands=',')
    im_df.drop(0)
    data = im_df.sort_values(['기간', '국가명', '금액', '성질명'], ascending=[
                             True, True, False, False]).groupby(['기간', '국가명']).head(1)
    data['성질명'] = data['성질명'].str.split('.').str[-1]
    data = data.rename(columns={'금액': '금액(USD 1000$)', '중량': '중량(ton)'})

    ex_path = os.path.join(settings.BASE_DIR, 'excel_files', '성질별수출.xls')
    ex_df = pd.read_excel(ex_path, header=4, thousands=',')
    ex_df.drop(0)
    data2 = ex_df.sort_values(['기간', '국가명', '금액', '성질명'], ascending=[
        True, True, False, False]).groupby(['기간', '국가명']).head(1)
    data2['성질명'] = data2['성질명'].str.split('.').str[-1]
    data2 = data2.rename(columns={'금액': '금액(USD 1000$)', '중량': '중량(ton)'})

    years = data['기간'].unique()
    data = data[data['기간'] == year].drop(['기간', '수출입구분'], axis=1)
    years = data2['기간'].unique()
    data2 = data2[data2['기간'] == year].drop(['기간', '수출입구분'], axis=1)

    dataset41 = data.to_html(index=False, justify='center', classes=[
        "table-bordered", "table-striped", "table-hover"])
    dataset42 = data2.to_html(index=False, justify='center', classes=[
                              "table-bordered", "table-striped", "table-hover"])

    #print('4====================================>')
    #print(json.dumps(dataset4, indent=4, ensure_ascii=False))

    return render(request, 'main.html', {'dataset1': dataset1, 'dataset2': dataset2, 'dataset3_usa': dataset3_usa, 'dataset3_china': dataset3_china, 'dataset3_japan': dataset3_japan, 'dataset3_eu': dataset3_eu, 'dataset4': dataset4, 'dataset41': dataset41, 'dataset42': dataset42, 'year': years})
   
   
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
    


