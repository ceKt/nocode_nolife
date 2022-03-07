from unittest.util import _MAX_LENGTH
import requests
from bs4 import BeautifulSoup

#対象の文字数制限
MAX_LENGTH = 50
#thread数
THREAD_NUM = 5

def main(targetword):
    url = "https://find.5ch.net/search?q="+targetword
    response = requests.get(url)
    index = BeautifulSoup(response.content, 'lxml')
    wordlist = []
    f = open('chats.txt', 'w',encoding="utf-8",errors="ignore")
    for i in (index.find_all(class_="list_line"))[:THREAD_NUM]:
        link = i.find(class_="list_line_link").get("href")
        res = requests.get(link)
        chats = BeautifulSoup(res.text, 'lxml')
        threadlist = chats.find_all(class_="escaped")
        wordlist.append([a.get_text(strip=True) for a in threadlist])
        print(link)
    for i in wordlist:
        #print(i)
        c = [x for x in i]
        for i in c:
            if(len(i)<MAX_LENGTH):
                f.write((i.encode('utf-8')).decode("utf-8")+ "\n")
        f.write("\n")
        
    f.close()
    
if __name__=="__main__":
    print("探索ワードを入力：")
    t = input()
    main(t)


