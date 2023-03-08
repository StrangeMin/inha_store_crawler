from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
driver = webdriver.Chrome(executable_path = r"C:\Users\이상민\Desktop/chromedriver.exe")

def check_exists_by_class(className):
    try:
        driver.find_element(by = By.CLASS_NAME, value = className)
    except NoSuchElementException:
        return False
    return True

def menu(data): # 메뉴 크롤링
    driver.get("https://map.naver.com/v5/search/"+data) # 검색창에 가게이름 입력
    driver.implicitly_wait(20)

    iframe = driver.find_element(By.ID, "searchIframe")
    
    driver.switch_to.frame(iframe)

    if check_exists_by_class('place_bluelink.TYaxT'):
        driver.find_element(by= By.CLASS_NAME, value = 'place_bluelink.TYaxT').click()
    else:
        driver.find_element(by= By.CLASS_NAME, value = 'place_bluelink.YwYLL').click()
        
    #driver.find_element(by= By.CLASS_NAME, value = 'place_bluelink.YwYLL').click()
    #driver.find_element(by = By.XPATH, value = '//*[@id="_pcmap_list_scroll_container"]/ul/li[1]/div[1]/a/div/div/span[1]').click()
                                                        
            
    #driver.implicitly_wait(20)
    driver.switch_to.default_content()

    driver.implicitly_wait(20)
    #iframe = 
    driver.implicitly_wait(20)
    driver.switch_to.frame(driver.find_element(By.ID, "entryIframe")) # 메뉴정보가 entryIframe에 있기 때문에 frame 변경함
    driver.implicitly_wait(20)

    print("가게이름 : " + driver.find_element(by=By.CLASS_NAME, value = 'Fc1rA').text)
    print("카테고리 : " + driver.find_element(by=By.CLASS_NAME, value = 'DJJvD').text)
    
    
    #driver.find_element(By.XPATH,'//*[@id="app-root"]/div/div/div/div[5]/div/div/div/div/a[2]').click()

    driver.find_element(by = By.XPATH, value = "//*[contains(text(), '메뉴')]").click()
    #driver.find_element(by= By.XPATH, value = '//*[@id="app-root"]/div/div/div/div[5]/div/div/div/div/a[3]').click()
    driver.implicitly_wait(20)
    
    
    #driver.implicitly_wait(5)

    if check_exists_by_class('_3ak_I'):
        print("배민")
    elif check_exists_by_class('order_list_inner'):
        middleCategory = driver.find_elements(By.CLASS_NAME, value = 'order_list_wrap.store_delivery')
        for category in middleCategory:
            print(category.find_element(by = By.CLASS_NAME, value = 'title').text)# 중분류
            c = category.find_elements(by = By.CLASS_NAME, value = 'order_list_item')
            for m in c:
                #print(m.find_element(by = By.CLASS_NAME, value = 'title').text) 
                #print(m.find_element(by = By.CLASS_NAME, 'K0PDV').style) # 사진
                print(m.find_element(by = By.CLASS_NAME, value = 'tit').text) # 메뉴 
                print(m.find_element(by = By.CLASS_NAME, value ='detail_txt').text) # 설명
                print(m.find_element(by = By.CLASS_NAME, value ='price').text) # 가격
            print("\n")
    else:
        menuList = driver.find_elements(By.CLASS_NAME, value = 'P_Yxm')
        for m in menuList:
            #print(m.find_element(by = By.CLASS_NAME, 'K0PDV').style) # 사진
            print(m.find_element(by = By.CLASS_NAME, value = 'Sqg65').text) # 메뉴 
            print(m.find_element(by = By.CLASS_NAME, value ='eCaG_').text) # 설명
            print(m.find_element(by = By.CLASS_NAME, value ='SSaNE').text) # 가격
            
        """
    try:
        start = driver.find_element(by= By.CLASS_NAME, value = '_3ak_I') # 배달의 민족에서 제공하는 메뉴가 랜더링 되어 있는 경우
        if len(start) == 0: # 가게에서 직접 제공하는 메뉴가 랜더링 되어 있는 경우
            start = driver.find_elements_by_class_name('V1UmJ')
        if len(start) == 0: # 메뉴가 없는 경우
            print('메뉴가 없습니다')
            return -1
        
    except:
        menuList = driver.find_elements(By.CLASS_NAME, value = 'P_Yxm')
        for m in menuList:
            #print(m.find_element(by = By.CLASS_NAME, 'K0PDV').style) # 사진
            print(m.find_element(by = By.CLASS_NAME, value = 'Sqg65').text) # 메뉴 
            print(m.find_element(by = By.CLASS_NAME, value ='eCaG_').text) # 설명
            print(m.find_element(by = By.CLASS_NAME, value ='SSaNE').text) # 가격
            print("\n")
            
        
    #return start[0].text"""
        return 2
    

menu("인하대 식당")



