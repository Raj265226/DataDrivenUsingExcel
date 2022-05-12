import XLUtils
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="E:\Work Files\Webdrives_for_Automation\chromedriver.exe")
driver.get("https://demo.guru99.com/test/newtours/")
driver.maximize_window()

path="C:\\Users\Rohit\OneDrive\Desktop\Login.xlsx"

rows=XLUtils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    username=XLUtils.readData(path,"Sheet1",r,1)
    password = XLUtils.readData(path,"Sheet1",r,2)

    driver.find_element(By.NAME,"userName").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "submit").click()

    if driver.title=="Login: Mercury Tours":
        print("Test Passed")
        XLUtils.WriteData(path,"Sheet1",r,3,"Passed")
    else:
        print("Test Failed")
        XLUtils.WriteData(path, "Sheet1", r, 3, "Failed")

    driver.find_element(By.XPATH,"//a[contains(text(),'SIGN-OFF')]").click()

