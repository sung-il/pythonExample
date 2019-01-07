# -*- coding: utf-8 -*-
 
import requests, bs4
 

def main():
    resp = requests.get('http://finance.naver.com/')
    resp.raise_for_status() # Response 에러 시 프로그램 중단
    
    resp.encoding='euc-kr'
    html = resp.text
    
    bs = bs4.BeautifulSoup(html, 'html.parser')
    tags = bs.select('div.news_area li') # Top 뉴스
    #tags = bs.select('div.news_area a') # Top 뉴스
    for tag in tags:
        title = tag.getText()
        #if '더보기' in title:
        #    break
        print(title)

if __name__ == "__main__":
    main()
