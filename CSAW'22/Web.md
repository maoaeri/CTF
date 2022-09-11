# Word Wide Web
Description: Isn't the Word Wide Web a fascinating place to be in? Words.. so many words.. all linked... NOTE: The flag doesn't have a wrapper. It needs to be wrapped with curly brackets and please put CTF in front of the curly brackets.  
http://web.chal.csaw.io:5010  
Author: Anish Agrawal (@roborobo#5025)

---------------------------
code:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request

url = "http://web.chal.csaw.io:5010"

driver = webdriver.Chrome("D:\Downloads\chromedriver_win32 (1)\chromedriver.exe")
driver.get(url+"/stuff")

a_element = driver.find_element(By.XPATH, '/html/body/p/a[contains(@href,"/")]')
print(a_element)
link = a_element.get_attribute('href')
print(link)

while True:
    driver.get(link)

    try:
        a_element = driver.find_element(By.XPATH, '/html/body/p/a[contains(@href,"/")]')
        print(a_element)
        link = a_element.get_attribute('href')
        print(link)
    except:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html)```

