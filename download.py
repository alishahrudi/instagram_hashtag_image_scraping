# import libs
import wget 
import threading
import concurrent.futures
import argparse
import os 
from termcolor import colored
# argument parsing for command line 
ap = argparse.ArgumentParser()
ap.add_argument('--file', help='the url file path')
arg = vars(ap.parse_args())

# show the download ascii pic
with open('dpic.txt','r')as f :
    a = f.read()
    print(a)
    
# reading the url's file
with open(arg['file'],'r')as f :
    file = f.read()

# make list of url's
urls = []
for i in range(len(file.split("https"))):
    urls.append('https'+file.split("https")[i])
    
# make repo for downloaded image 
os.makedirs('./download')
os.chdir("./download/")
print(colored('Start Dowload' , 'green'))

# start downloading using multi thread
with concurrent.futures.ThreadPoolExecutor() as executer:
    executer.map(wget.download, urls)
print(colored('Finish' , 'pink'))