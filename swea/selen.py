import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.chrome.options import Options
from dotenv import dotenv_values
import sys
from sys import argv



def main():
    global ID, pw
    Q_name = argv[1].split('_')[0]


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # download_path = 'C:/Users/dohyeong/Desktop/camp29/algorithm/swea'
    # prefs = {'download.default_directory': download_path}
    # chrome_options.add_experimental_option('prefs', prefs)
    # 크롬 드라이버 위치 설정 필요
    browser = webdriver.Chrome(options=chrome_options)
    
    browser.get("https://swexpertacademy.com/main/code/problem/problemList.do")
        
    account = browser.find_element(by.XPATH, '/html/body/nav/div[2]/div/div[2]/a[2]')
    account.click()    

    config = dotenv_values('.env')

    ID = config.get("ID")
    pw = config.get("PW")        
        
    if not ID:
        ID = input("ID를 입력하세요 : ")
    else:
        print("ID가 입력되었습니다.")
        
    if not pw:
        pw = input("비밀번호를 입력하세요 : ")
    else:
        print("비밀번호가 입력되었습니다.")
        
        
            
    login = browser.find_element(by.XPATH, '//*[@id="id"]')
    login.click()
    login.clear()
    login.send_keys(ID)
    password = browser.find_element(by.XPATH, '//*[@id="pwd"]')
    password.click()
    password.clear()
    password.send_keys(pw)
    confirm = browser.find_element(by.XPATH, '//*[@id="LoginForm"]/div/div/div[2]/div/div/fieldset/div/div[4]/button')
    confirm.click()  
            
    search = browser.find_element(by.XPATH, '//*[@id="searchinput"]')
    search.click()
    search.clear()
    search.send_keys(Q_name)
    search.send_keys(keys.ENTER)

    try:
        search = browser.find_element(by.XPATH, '//*[@id="searchForm"]/div[2]/div/div/div/div/div[2]/div/div[1]/div[1]/span[2]/a')
        search.click()
        

        # filename = 'input.txt'
        # down = browser.find_element(by.XPATH, '/html/body/div[4]/div[2]/div/div[7]/div/div[3]/div[1]/div[1]/div/a[2]')
        # down.click()
        
        
    except NoSuchElementException:
        print("해당 문제가 없습니다. LEARN으로 이동해 주세요")


    input("프로그램이 완료되었습니다. 용무가 끝나면 엔터키를 눌러 종료해주세요:")    

    
if __name__ == '__main__':
    main()
