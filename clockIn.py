# -*- codeing = utf-8 -*-
# @Time : 2021/3/15 22:13
# @Author : 海苔
# @File : clockIn.py
# @Sotfware : PyCharm

from selenium import webdriver
import time
import datetime

#填入学号
username = ['']
#填入密码(默认身份证后六位)
password = ['']

def signIn(i):
    #1.进入事务中心
    driver = webdriver.Chrome()
    driver.get('https://my.jluzh.edu.cn')
    driver.find_element_by_id("username").send_keys(username[i])
    driver.find_element_by_id("password").send_keys(password[i])
    driver.find_element_by_name("submit").click()
    time.sleep(1)

    #2.进入健康卡填报
    driver.get('https://work.jluzh.edu.cn/default/work/jlzh/jkxxtb/jkxxcj.jsp')
    time.sleep(1)

    nextButton = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button')
    js = 'document.getElementsByClassName("btn btn-default prompt_box_nextBtn")[0].removeAttribute("disabled")'
    driver.execute_script(js)
    nextButton.click()

    #3.提交健康卡
    cn = driver.find_element_by_xpath('//*[@id="cn"]')
    driver.execute_script("arguments[0].removeAttribute('sui')",cn)

    submit = "document.getElementById('post').click()"
    driver.execute_script(submit)

    time.sleep(1)
    driver.quit()
    print("提交成功......")

def main():
    for i in range(len(username)):
        signIn(i)

if __name__ == '__main__':
    main()