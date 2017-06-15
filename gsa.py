# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 14:37:47 2017

@author: SHUBHAM067
"""
from selenium import webdriver
import lxml.html
from urllib.parse import urljoin
import xlwings as xw

l1=[]
l2=[]
l3=[]
l4=[]
driver = webdriver.Chrome()
driver.get('https://www.gsaadvantage.gov/advantage/s/mfr.do?db=0&searchType=1&q=19:5GS-07F-320AA&q=20:5246+35+1&src=elib&listFor=All')
driver.implicitly_wait(10)
tree = lxml.html.fromstring(driver.page_source)
urls = tree.xpath('//*[@class="black8pt"]//a/@href')
for url in urls:
    u =('https://www.gsaadvantage.gov')
    driver.get(urljoin(u,url))
    tree = lxml.html.fromstring(driver.page_source)
    items_urls = tree.xpath('//a[@class="blue12pt arial no-line"]/@href')
    l1.extend(items_urls)
    break

for l in l1:
    u =('https://www.gsaadvantage.gov')
    driver.get(urljoin(u,l))
    tree = lxml.html.fromstring(driver.page_source)
    item_number = tree.xpath('//*[@id="main"]/table[2]/tbody/tr/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td[3]/table/tbody/tr/td[2]/table[2]/tbody/tr[2]/td[1]/table[1]/tbody/tr[1]/td[2]/text()')
    desc = tree.xpath('//div[@class="TabbedPanelsContentGroup"]//table/tbody/tr/td/div/text()')
    price = tree.xpath('//span[@class="black10pt"]/strong/text()')
    l2.append(item_number)
    l3.append(desc)
    l4.append(price)
    wkb = xw.Book('GSA INDEPENDENDENT ITEMS.xlsx')
    sht = wkb.sheets['Table 1']
    sht.range('A5').value = l2
    sht.range('B5').value = l3
    sht.range('C5').value = l4
    
    
