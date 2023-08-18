from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from appium.webdriver.appium_service import AppiumService

caps = {"platformName": "android", "automationName": "UiAutomator2"}


appium_service = AppiumService()
appium_service.start(
    args=["--base-path", "/wd/hub"],
    node_path="C:/Program Files/nodejs/node.exe",
    npm_path="C:/Program Files/nodejs/npm.cmd",
    main_script="C:/Users/Administrator/AppData/Roaming/npm/node_modules/appium/build/lib/main.js"
)
driver = Remote("http://localhost:4723/wd/hub", caps)


fotos = driver.find_elements(
    By.CSS_SELECTOR, '[content-desc *= "linha 1"]'
)

quant = len(fotos)

for i in range(0, quant):
    print(f"foto numero {i + 1}")                                        
    fotos[i].click()
    like = driver.find_elements(
        AppiumBy.ID,
        "com.instagram.android:id/row_feed_button_like",
    )
    for k in like:
        if len(like) == 1:
            k.click()
        else:
            if like.index(k) == 1:
                k.click()
    print("ganhou like hehe")
    driver.back()