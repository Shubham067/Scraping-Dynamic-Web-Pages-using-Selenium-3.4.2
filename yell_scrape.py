# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 03:32:30 2017

@author: SHUBHAM067
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import lxml.html
from urllib.parse import urljoin
from selenium.common.exceptions import NoSuchElementException

l1 = []
l2 = []
driver = webdriver.Chrome()
driver.get('https://www.yell.com/')
driver.implicitly_wait(10)
search_keyword = driver.find_element_by_id("search_keyword")
search_keyword.send_keys("Personal Trainers")
search_location = driver.find_element_by_id("search_location")
search_location.send_keys("UK")
search_location.send_keys(Keys.RETURN)
#driver.close()
url = driver.current_url
l1.append(url)
while True:
    try:
        driver.find_element_by_xpath("//div[@class=\"row pagination\"]//a[contains(text(), 'Next')]").click()
    except NoSuchElementException:
        break
    url = driver.current_url
    l1.append(url)
l1 = list(set(l1))

for l in l1:
    driver.get(l)
    tree = lxml.html.fromstring(driver.page_source)
    urls = tree.xpath('//div[@class=\"row businessCapsule--title\"]//@href')
    u = 'https://www.yell.com'
    for url in urls:
        l2.append(urljoin(u,url))

for l in l2[2]:
    driver.get(l)
    tree = lxml.html.fromstring(driver.page_source)
    Business_Name = tree.xpath('//div[@class=\"row businessCapsule--title\"]//h2//text()')
    Phone_Number = tree.xpath('//div[@class=\"col-sm-12 businessCapsule--telephone\"]/ul/li/strong/text()')
    Website = tree.xpath('//div[@class=\"col-sm-19 businessCapsule--callToAction\"]/a[1]/@href')
    Email = urljoin(u,tree.xpath('//div[@class=\"col-sm-19 businessCapsule--callToAction\"]/a[2]/@href'))
    Business_Overview = tree.xpath('//div[@id=\"aboutUs\"]/p/text()')
    
print(Business_Name)
print(Phone_Number)
print(Website)
print(Email)
print(Business_Overview)
    



