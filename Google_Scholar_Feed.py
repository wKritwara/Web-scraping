from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import codecs
import time

# initialize an instance of the chrome driver (browser)
driver = webdriver.Chrome()
driver_01 = webdriver.Chrome()

# visit your target site
Keyword_Search = ''
Start_year = '2019'
Stop_year = '2023'
Page_file = codecs.open("page.html", "w", "utf-8")
Data_file = codecs.open(Start_year+"_"+Stop_year+"_"+Keyword_Search.replace(" ","_")+".text", "w", "utf-8")
driver.get('https://scholar.google.com/')
search_box = driver.find_element("name", "q")
search_box.send_keys(Keyword_Search)
search_box.submit()
time.sleep(3)
date_box = driver.find_element(By.XPATH, "//a[@id='gs_res_sb_yyc']")
date_box.click()
actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.send_keys(Start_year)
actions.send_keys(Keys.TAB)
actions.send_keys(Stop_year)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.RETURN)
actions.perform()
#date_box = driver.find_element(By.XPATH, "//a[@id='gs_res_sb_yyc']")
#date_box.click()
time.sleep(3)
#wait = WebDriverWait(date_box, 3)
#wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@nmae='as_ylo']")))
#driver.find_element(By.NAME, "as_ylo").send_keys("2000")
Page_file.write(driver.page_source)
#driver.find_element(By.XPATH,"//input[@name='as_ylo']").send_keys('2000')
#ylo = driver.find_element(By.NAME, "as_ylo").send_keys("2000")
#yhi = driver.find_element(By.NAME, "as_yhi").send_keys("2008")
#search_btn = driver.find_element(By.XPATH, "//button[@class='gs_btn_lsb']").click()

time.sleep(3)

Load_nav = driver.find_element(By.XPATH,"//div[@role='navigation' and @id='gs_n']")
Page_L = Load_nav.find_elements(By.TAG_NAME,"a")
PageNext = ["1"]
for PP in Page_L:
      if(PP.text != "ถัดไป"):
            PageNext.append(PP.text)
            print(PP.text)
      else:
            break 

for P in PageNext:
      if P != "1":
            search_box = driver.find_element(By.LINK_TEXT, P).click()
            driver.implicitly_wait(10) # seconds      

      Link01 = driver.find_elements(By.XPATH,"//div[@class='gs_r gs_or gs_scl']")
      for L in Link01:
            try:
                  Sub_L = []
                  D01_L = L.find_element(By.XPATH,".//div[@class='gs_ri']")
                  Sub_L = D01_L.find_elements(By.TAG_NAME,'a')
                  print(len(Sub_L))
                  Data_file.write(Sub_L[0].text+"\n")                  
                  Data_file.write(D01_L.text+"\n")                  
                  for Sub in Sub_L:
                        Sub_text = Sub.get_attribute('href')
                        if Sub_text.find("http")> -1 and Sub_text.find("scholar.google.com") == -1:
                              Data_file.write(Sub_text+"\n")
                  Link_01 = Sub_L[0].get_attribute('href')      
                  print("*"+Sub_L[0].text+"*")
                  #Author_L = D01_L.find_element(By.XPATH,"//div[@class='gs_a']")
                  #Author_L_data = Author_L.text.replace("-","\t")
                  #Detail_L = D01_L.find_element(By.XPATH,"//div[@class='gs_rs']")
                  #Data_file.write(L.text+"\t"+Link_01+"\t"+Author_L_data+"\t"+Detail_L.text+"\t")
                  if(Link_01.find("www.sciencedirect.com") > -1):
                        driver_01.get(Link_01)
                        Paper_01 = driver_01.find_element(By.XPATH,"//div[@id='preview-section-abstract']") 
                        Abstract_01 = Paper_01.find_element(By.TAG_NAME,'p')
                        Data_file.write(Abstract_01.text)
                        #print(Abstract_01.text)  
                  Sub_L = []
                  try:
                        D02_L = L.find_element(By.XPATH,".//div[@class='gs_ggs gs_fl']")
                        Sub_L = D02_L.find_elements(By.TAG_NAME,'a')
                        for Sub in Sub_L:
                              Sub_text = Sub.get_attribute('href')
                              if Sub_text.find("http")> -1 :
                                    Data_file.write(Sub.text+"("+Sub_text+")\n")                  
                  except:
                        print("An exception occurred")                  
                  Data_file.write("\n") 
            except:
                  print("An exception occurred")

  
driver_01.quit()  
driver.quit()
