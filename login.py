from selenium import webdriver
from selenium.webdriver.support.ui import Select
import datetime
import time

print(datetime.datetime.now())
driver=webdriver.Chrome(executable_path="C:\\Users\mkottak\git\intermix\IMX\GAP_Intermix\\target\classes\webdriver\\chromedriver.exe")
driver.get("https://www.bankofamerica.com/")

driver.find_element_by_name("onlineId1").send_keys("12345")
driver.find_element_by_name("passcode1").send_keys("Pass@123")

driver.find_element_by_id("saveOnlineId").click()
driver.save_screenshot("LoginPage "+str(datetime.datetime.now())[:10]+".png")
#driver.save_screenshot("LoginPage.png")

driver.maximize_window()
p="//div[@class='products-container']//span[@class='show-for-large-up']"
#print(driver.find_element_by_xpath(p).text)

driver.find_element_by_class_name("open-account").click()
no_of_products=driver.find_elements_by_xpath("//div[contains(text(),'started')]")
print("No of services available are " + str(len(no_of_products)))

driver.find_element_by_xpath("//div[contains(text(),'started')]").click()
driver.implicitly_wait(4)
driver.find_element_by_xpath("//a[@class='open-cta']").click()
driver.switch_to.window((driver.window_handles[1]))
driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("00831")
driver.find_element_by_id("go-button-zip-modal").click()


savings_account=input("Do you want to add a savings account(Y/N):")
if savings_account.upper()=='Y':
    #driver.find_element_by_id("rb-rewards-savings-account").click()
    driver.find_element_by_xpath("//input[@type='radio']").click()
else:
    driver.find_element_by_xpath("//input[@type='rb-savings-account-none']").click()

driver.find_element_by_id("isBoaClient").click()

driver.find_element_by_id("go-to-application-mediumup").click()
driver.implicitly_wait(3)
time.sleep(4)
driver.find_element_by_name("Link_continue_guest").click()

driver.find_element_by_id("zz_name_tb_fnm_v_1").send_keys("Vandhana")
driver.find_element_by_id("zz_name_tb_lnm_v_1").send_keys("Shetty")
driver.find_element_by_id("zz_addr_tb_line1_v_1").send_keys("2000 Marcus Avenue")
driver.find_element_by_id("zz_addr_tb_city_v_1").send_keys("North Hyde")
sel=Select(driver.find_element_by_id("zz_addr_lb_state_v_1"))
sel.select_by_visible_text("Maine")
time.sleep(3)
driver.implicitly_wait(3)
driver.find_element_by_id("zz_addr_tb_zip_v_1").send_keys("04005")

driver.find_element_by_id("zz_phn_tb_ppno_v_1").send_keys("9885679707")
driver.find_element_by_id("zz_email_tb_addr_v_1").send_keys("vandhana@gmail.com")

driver.find_element_by_id("zz_email_tb_readdr_v_1").send_keys("vandhana@gmail.com")
driver.find_element_by_xpath("//label[@for='zz_citz_lb_uscit_no_v_1-real']/input").click()
driver.save_screenshot("new account"+str(datetime.datetime.now())[:10]+".png")

sel1=Select(driver.find_element_by_id("zz_citz_lb_citzcntry_v_1"))
sel1.select_by_visible_text("India")
