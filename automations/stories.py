from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver import Remote
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from rich import print
from .modulosmb import traterror
from selenium.webdriver.common.actions import interaction
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from appium.webdriver.common.touch_action import TouchAction

# --base-path /wd/hub

def watchingStories(driver,quantEng):
    try:
        storys = driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value='reels_tray_container')
        story = storys.find_element(By.XPATH,'//androidx.recyclerview.widget.RecyclerView[@content-desc="reels_tray_container"]/android.widget.LinearLayout[2]')
    except:
        el1 = driver.find_element(by=MobileBy.ID, value="com.instagram.android:id/tab_avatar")
        el1.click()
        el2 = driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value="Opções")
        el2.click()
        el3 = driver.find_element(by=MobileBy.XPATH, value="//android.widget.Button[@content-desc=\"Distraction Free settings\"]/android.view.ViewGroup/android.widget.TextView")
        el3.click()
        el5 = driver.find_element(by=MobileBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.RelativeLayout/android.widget.TextView")
        el5.click()
        driver.back()
        driver.back()
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(825, 510)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(833, 920)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        driver.implicitly_wait(4)
        sleep(4)
        storys = driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value='reels_tray_container')

        
    for i in range(2, 5):
        story = storys.find_element(By.XPATH,'//androidx.recyclerview.widget.RecyclerView[@content-desc="reels_tray_container"]/android.widget.LinearLayout[' + str(i) + ']')
        try:
            live = story.find_element('id','com.instagram.android:id/live_badge_view')
        except:
            story.click()
            break
    try:
        el1 = driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value="Continue assistindo stories")
        el1.click()
    except:
        None

    quant = 0
    numbersto = quantEng
    driver.implicitly_wait(1)
    while quant <= numbersto:
        print(f'Current: {quant}')
        try:
            name =  driver.find_element('id','com.instagram.android:id/reel_viewer_title').text
        except:
            print('sem nome')
        print(f'user: {name}')
        for i in range(5):  
            try:
                
                driver.find_element(By.XPATH,'//android.widget.ImageView[@content-desc="Curtir"]').click()

                print(f'Curtiu {i+1}')
            except:
                break
            actions = ActionChains(driver)
            actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(1050, 1200)  ####(714, 670)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0)
            actions.w3c_actions.pointer_action.release()
            actions.perform()   
            try:
                sleep(2)
                nametwo = driver.find_element('id','com.instagram.android:id/reel_viewer_title').text
                print(f'user2: {nametwo}')
            except:
                continue
            if name != nametwo :
                continue
        try: 
            actions = ActionChains(driver)
            actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(1000, 1130)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(200, 1130)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
        except:
            print('erro ao passar') 
        quant += 1
    driver.back()
    driver.implicitly_wait(3)
    el1 = driver.find_element(by=MobileBy.ID, value="com.instagram.android:id/tab_avatar")
    el1.click()
    sleep(1)
    el2 = driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value="Opções")
    el2.click()
    sleep(1)
    el3 = driver.find_element(by=MobileBy.XPATH, value="//android.widget.Button[@content-desc=\"Distraction Free settings\"]/android.view.ViewGroup/android.widget.TextView")
    el3.click()
    sleep(1)
    driver.find_element(by=MobileBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.LinearLayout/android.widget.Switch").click()
    driver.back()
    driver.implicitly_wait(0)
 
   


