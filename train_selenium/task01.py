from selenium import webdriver
import chromedriver_binary
import time

driver = webdriver.Chrome()

driver.get("http://www.a-force.biz/")

elem_serch_chatbot = driver.find_element_by_id("button-area")
elem_serch_chatbot.click()


#iframeに切替
iframe = driver.find_element_by_id("effect")
driver.switch_to.frame(iframe) 

elem_input_chatbot = driver.find_element_by_id("tweet")
elem_input_chatbot.send_keys("こんにちは")
elem_comment_chatbot = driver.find_element_by_id("send_btn")
elem_comment_chatbot.click()

#待機時間10秒：読み込み時間の確保
time.sleep(10)

elem_input_chatbot.send_keys("昇給について教えて")
elem_comment_chatbot.click()

elemText1 = driver.find_elements_by_class_name("row")
print(str(elemText1))

time.sleep(10)
driver.close()