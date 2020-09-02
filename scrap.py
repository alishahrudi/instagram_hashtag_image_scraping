#  instagram_scrap  Copyright (C) 2020  Ali Shahrudi
#  This program comes with ABSOLUTELY NO WARRANTY. 
#  his is free software, and you are welcome to redistribute it
#  under certain conditions.

# import necessary libs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import argparse
import requests
from selenium.webdriver.firefox.options import Options
from termcolor import colored

# argument parsing for command line 
ap = argparse.ArgumentParser()
ap.add_argument("--hashtag",required=True,
                help="hashtag name")

ap.add_argument("--numb",required=True,
                help="number of scrooling")

arg = vars(ap.parse_args())
num = arg["numb"]
name = arg["hashtag"]

def scrap(hashtag_name , scrool):
    """this function will give hashtag name and number of scrool you want to 
        each scrool will return 10 pic 

    Args:
        hashtag_name ([str]): the hashtag toy want to scrap
        scrool ([int]): number of scrolling

    Returns:
        [txt file]: the txt file of picture's url 
    """
    try :
        # using selenuin in headless option
        options = Options()
        options.headless = True
        
        #show the instagram image
        with open ('instagram_pic.txt','r')as f:
            a = f.read()
            print(a)
    
        # opening firefox
        print (colored("[+] opening firefox ... " ,'green'))
        driver = webdriver.Firefox(options=options)
        driver.get("https://www.instagram.com/")
        
        # pass and user name 
        print (colored("[+] Loging In ... ",'green'))
        time.sleep(3)
        pass_ = driver.find_element_by_name('password')
        pass_.clear()
        pass_.send_keys('09199721253mashali')
        usr = driver.find_element_by_name('username')
        usr.clear()
        usr.send_keys('mashalisha9')
        time.sleep(3)
        # loging in 
        btn = driver.find_elements_by_xpath("//*[contains(text(), 'Log In')]")
        btn[0].click()
        # search 
        time.sleep(10)
        buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Not Now')]")
        for btn in buttons:
            btn.click()
        ###
        time.sleep(10)
        search = driver.find_elements_by_xpath("//input[@placeholder='Search']")
        print (colored("[+] Start searching for hashtag "+name+" ... " , 'green'))
        for btn in search :
            btn.clear()
            btn.send_keys(hashtag_name)
            time.sleep(3)
            btn.send_keys(Keys.ARROW_DOWN)
            btn.send_keys(Keys.ENTER)
            
        time.sleep(10)
        c = 0
        url = []
        print (colored("[+] find and copy urls ..." , 'green'))
        
        # scrool thre page
        for i in range(scrool):
            c = c +1 
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            if c == 5 :
                for i in driver.find_elements_by_tag_name('img'):
                    html = driver.execute_script("return arguments[0].src;", i)
                    url.append(html)
                c  = 0 
                
        # save the data
        print (colored("[+] Save urls ...",'green'))
        try:
            with open(name+'_urls.txt','w') as f :
                for link in url :
                    f.write('%s\n' % link)
        except:
            print(colored("[-] cant save the urls [-] ",'red'))
    except :
        print(colored("[-] process failed [-]",'red'))
# main prog
if __name__ == "__main__":
    scrap('#'+name,int(num))  