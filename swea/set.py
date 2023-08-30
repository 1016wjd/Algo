### SWEA 폴더 안에 selen.py와 swea_skeleton.py를 넣어주세요
### SWEA 폴더 안에 .env 파일에 ID, PW가 입력 되어 있어야 합니다.
### <.env> || ID : <your_id>\n PW : <your_pw>
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.chrome.options import Options
from dotenv import dotenv_values
import sys
from sys import argv
import os
import shutil
from pathlib import Path
import time

def main():
    global ID, pw
    prob_name = argv[1]
    ## 파일 경로 작성
    parent_path = Path(__file__).parent
    folder_path = parent_path / prob_name
    
    # 폴더/파일 생성
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.mkdir(folder_path)
    f1 = open(folder_path / 'sol.py','w')

    # sol.py 기본 템플릿
    template = '''import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    pass
'''
    # sol.py 작성
    f1.write(template)
    f1.close()

    # f2 = open('swea_skeleton.py','r')
    # data = f2.read()
    # f1.write(data)
    # f1.close()
    # f2.close()
    
    Q_name = prob_name.split('_')[0]


    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': str(folder_path)}
    chrome_options.add_experimental_option('prefs',prefs)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

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
        ## input 파일 다운받기        
        try:
            down = browser.find_element(by.XPATH, '/html/body/div[4]/div[2]/div/div[7]/div/div[3]/div[1]/div[1]/div/a[2]')
            down.click()
            ## 다운로드 대기 (만약 3초 안에 다운이 완료되지 않는 경우 3초보다 큰 값으로 늘리세요)
            time.sleep(3)
            ## input 파일명 input.txt로 변경 (ex. samle_input.txt)
            for file in os.listdir(folder_path):
                if file.endswith('input.txt'):
                    old_file_path = folder_path / file
                    new_file_path = folder_path / 'input.txt'
                    os.rename(old_file_path,new_file_path)
        except NoSuchElementException:
            print("input 파일이 없습니다.")

    except NoSuchElementException:
        print("해당 문제가 없습니다. LEARN으로 이동해 주세요")

    input("프로그램이 완료되었습니다. 용무가 끝나면 엔터키를 눌러 종료해주세요:")    

    
if __name__ == '__main__':
    main()
    