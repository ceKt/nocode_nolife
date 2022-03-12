from re import search
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def main(keyword):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #5ちゃんねるにアクセスして検索
    driver.get("https://find.5ch.net/search")
    search_form = driver.find_element_by_name("q")
    search_form.send_keys(keyword)
    search_form.submit()
    #検索結果のスレッドを取得
    result_list = driver.find_elements_by_class_name("list_line")
    result=[]
    for i in result_list:
        a = i.find_element_by_class_name("list_line_link")
        link = a.get_attribute("href")
        title = a.find_element_by_class_name("list_line_link_title").text
        result.append({"link":link,"title":title})
        print(result[-1])
    
    return result

if __name__=="__main__":
    main("じゃんたま")
