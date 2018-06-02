from selenium import webdriver
import os
import time

chromedriver = "D:/tool/Python36/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

url = "http://182.131.21.139/gspt/ccm-action/domesticgame/searchGame"
browser.get(url)

for x in range(501, 2216):
    doc_list = browser.find_element_by_class_name("content-top").find_elements_by_tag_name("li")

    xh, bawh, yymc, pwrq = "", "", "", ""
    for doc in doc_list:
        id = doc.get_attribute("id")
        if id == 'xh':
            xh, bawh, yymc, pwrq = "", "", "", ""
            xh = doc.text
        elif id == 'bawh':
            bawh = doc.text
        elif id == 'yymc':
            yymc = doc.text
        elif id == 'pwrq':
            pwrq = doc.text
		
        """
        游戏名称 神魔录
        公司名称 北京灵动时空科技有限责任公司
        公示类型 国产游戏
        备案文号 文网游备字〔2017〕Ｍ-RPG 0956 号
        批文发布日期 2017-07-25
        """
        if "RPG 0956" in bawh:
            print(x, xh, bawh, yymc, pwrq)
            browser.quit()
            break
			
    print(x, xh, bawh, yymc, pwrq)
		
    # 自动翻到下一页
    # time.sleep(1)
    # browser.find_element_by_class_name("content-fy").find_element_by_link_text("下一页").click()
    page = browser.find_element_by_id("page")
    browser.execute_script("arguments[0].value='" + str(x) + "';", page)
    browser.find_element_by_id("queryform").submit()

# 关闭浏览器
# browser.quit()
