import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



url = input('请输入文档地址：')
f = open('path.txt', "r")
driver = Chrome(f.read())
driver.get(url)
driver.maximize_window()
banji = int(input("班上有多少人？："))
Line = input('你要写哪一列？（大写）：')
hangshu = 1;
time.sleep(3)


def denglu():  # 登录模块
    time.sleep(2)
    driver.find_element_by_id('header-login-btn').click()
    time.sleep(2)
    driver.switch_to.frame('login_frame')
    time.sleep(2)
    driver.find_element_by_id('img_out_29633886').click()
    return True

denglu()

# driver.minimize_window()
for i in range(1,banji):



    def fuzhizhantie():
        if hangshu == 2:
            pass
        else:
            ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
            ActionChains(driver).key_down(Keys.TAB).perform()
            ActionChains(driver).key_down(Keys.TAB).perform()
            ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
            time.sleep(2)
            ActionChains(driver).key_down(Keys.LEFT).perform()
            ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
            ActionChains(driver).key_down(Keys.TAB).perform()
            ActionChains(driver).key_down(Keys.TAB).perform()
            ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
            ActionChains(driver).key_down(Keys.TAB).perform()
            ActionChains(driver).key_down(Keys.ENTER).perform()


    def dingwei():
        ActionChains(driver).key_down(Keys.CONTROL).send_keys(Keys.HOME).key_up(Keys.CONTROL).perform()


    def lieshu():
        if hangshu == 2:
            pass
        else:
            for j in range(0, hanghao(Line) - 3):
                ActionChains(driver).key_down(Keys.TAB).perform()

    def hanghao(string):
        li = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
        n = m =0
        hanghao = string
        while True:
            if li[n] == hanghao:
                return (n+1)
                break
            else:
                li.append(li[m] + li[n])
                n += 1
                if n >= 26:
                    m +=1
                    n = 0
                else:
                    if li[(int(str(len(li)))) - 1] == hanghao:
                        return ((int(str(len(li)))))
                        break
                    else:
                        pass

    for i in range(0, hangshu):
        ActionChains(driver).key_down(Keys.ENTER).perform()
    hangshu += 1

    time.sleep(2)
    lieshu()
    time.sleep(2)
    fuzhizhantie()
    time.sleep(2)
    dingwei()
    time.sleep(2)
input('填写完毕')
driver.quit()
