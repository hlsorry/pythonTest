#!/usr/bin/python
# coding:utf-8
 
import requests
from bs4 import BeautifulSoup
# 设置自己的名字
test_url = 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=海龙'
 
def download_page(url):
    data = requests.get(url).content
    return data
 
name_list = []
def parse_html(html):
    soup = BeautifulSoup(html)
    name_list_soup = soup.find('div', attrs={'id': 'content_left'})
    if name_list_soup != None:
        for name_item in name_list_soup.find_all('div', attrs={'class': 'c-container'}):
            h3 = name_item.find('h3', attrs={'class': 't'})
            link = h3.find('a')
            print(link.getText())
            print(link['href'])
 
def main():
    parse_html(download_page(test_url))
 
if __name__ == '__main__':
    main()
