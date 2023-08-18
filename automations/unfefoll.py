from time import sleep
from appium.webdriver import Remote
from .buscacomentarios import commentEngaging
from .stories import watchingStories
from .seguirmb import seguir
from .deixardeseguir2 import desseguir
import time
import datetime
from .modulosmb import sair, entrar
from pymongo import MongoClient
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from rich import print
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from celery import shared_task
channel_layer = get_channel_layer()

@shared_task
def unfandfol(
    dispositivo, fila, pacote, rodadas, timebreak, quantseguir, func="fol", cont="n"
):
    ################# mongodb ######################################################
    client = MongoClient()
    db = client["Rengage"]
    dbcliente = db["clientes"]
    dbwork_diario = db["workday"]


    data = datetime.date.today()

    # appium data
    caps = {"platformName": "android", "automationName": "UiAutomator2"}

    if dispositivo == "1":
        # caps["deviceName"] = "fb8a4f98"  # v
        # caps["udid"] = "127.0.0.1:5655"
        driver = Remote("http://localhost:4723/wd/hub", caps)
    elif dispositivo == "2":
        caps = {}
        caps["platformName"] = "android"
        # caps["deviceName"] = "emulator-5554"  #emulator-5556
        # caps["udid"] = "127.0.0.1:5555"

        driver = Remote("http://localhost:4728/wd/hub", caps)

    quant = len(fila)

    if dbwork_diario.find_one({"data": str(data)}):
        print("trabalho diario já iniciado.")

        
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {"type": "send_notification", "message": "trabalho diario já iniciado."},
        )

    else:
        dbwork_diario.insert_one({"data": str(data), "clientes": {}})
        print("primeira vez no dia")
        print(dbwork_diario.find_one({"data": str(data)}, {"_id": 0}))
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "send_notification",
                "message": f"primeira vez no dia. {dbwork_diario.find_one({'data': str(data)}, {'_id': 0})}",
            },
        )

    inicio = time.time()
    wait = WebDriverWait(driver, 2)

    if cont == "s" and func != "comment":
        save = dbwork_diario.find_one({"data": str(data)})[dispositivo]
        cont = "n"
    else:
        save = {"rodada": 0, "vez": 0, "qAtual": 0}
        dbwork_diario.update_one({"data": str(data)}, {"$set": {dispositivo: save}})
    for j in range(save["rodada"], rodadas):
        print(f"[on orange]{j + 1}° rodada[/]")
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {"type": "send_notification", "message": f" {j + 1}° rodada "},
        )

        for i in range(save["vez"], quant):
            dbwork_diario.update_one(
                {"data": str(data)}, {"$set": {dispositivo + ".rodada": j}}
            )
            dbwork_diario.update_one(
                {"data": str(data)}, {"$set": {dispositivo + ".vez": i}}
            )
            try:
                if dbwork_diario.find_one({"data": str(data)})["clientes"][fila[i]]:
                    print(
                        dbwork_diario.find_one({"data": str(data)})["clientes"][fila[i]]
                    )
                    async_to_sync(channel_layer.group_send)(
                        "notifications",
                        {"type": "send_notification", "message": f" {dbwork_diario.find_one({'data': str(data)})['clientes'][fila[i]]}"},
                    )
            except:
                day = {"unf": 0, "fol": 0}
                dbwork_diario.update_one(
                    {"data": str(data)}, {"$set": {"clientes." + fila[i] + "": day}}
                )
                print(dbwork_diario.find_one({"data": str(data)})["clientes"][fila[i]])
                async_to_sync(channel_layer.group_send)(
                        "notifications",
                        {"type": "send_notification", "message": f" {dbwork_diario.find_one({'data': str(data)})['clientes'][fila[i]]}"},
                    )
            ############ primeira etapa , entrando na conta ################################
            if i == 0:
                try:
                    entrar(
                        fila[i], dbcliente.find_one({"user": fila[i]})["senha"], driver
                    )
                except:
                    print("conta já logada")
                    async_to_sync(channel_layer.group_send)(
                        "notifications",
                        {"type": "send_notification", "message": "conta já logada"},
                    )
            ############ segunda etapa, definindo caminho da automação #####################
            if func == "fol":
                seguir(
                    fila[i],
                    quantseguir / rodadas,
                    pacote[i],
                    driver,
                    j + 1,
                    i + 1,
                    dispositivo,
                )
            elif func == "unf":
                desseguir(
                    fila[i], quantseguir / rodadas, driver, j + 1, i + 1, dispositivo
                )
            elif func == "str":
                watchingStories(driver, quantseguir / rodadas)

            elif func == "comment":
                commentEngaging(driver, quantseguir / rodadas, fila[i], cont)
            fim = time.time()
            print(f"o tempo de execução foi de: {(fim - inicio) / 60}")
            async_to_sync(channel_layer.group_send)(
                        "notifications",
                        {"type": "send_notification", "message": f"o tempo de execução foi de: {(fim - inicio) / 60}"},
                    )
            a = i + 1
            dbwork_diario.update_one(
                {"data": str(data)}, {"$set": {dispositivo + ".qAtual": 0}}
            )
            if a == quant:
                a = 0
                print("aqui")
                dbwork_diario.update_one(
                    {"data": str(data)}, {"$set": {dispositivo + ".vez": 0}}
                )

            sleep(1)
            ############ terceira etapa , sair da conta ##################################
            try:
                sair(driver)
            except:
                print("erro ao sair")
                async_to_sync(channel_layer.group_send)(
                        "notifications",
                        {"type": "send_notification", "message": "erro ao sair"},
                    )
            sleep(1)
            driver.back()

            try:
                insta = driver.find_element(
                    by=MobileBy.ACCESSIBILITY_ID, value="Instagram"
                )
            except:
                driver.back()
                sleep(1)
                insta = driver.find_element(
                    by=MobileBy.ACCESSIBILITY_ID, value="Instagram"
                )
            actions = TouchAction(driver)
            actions.press(insta)
            actions.perform()
            sleep(1)
            driver.find_element(
                by=MobileBy.ACCESSIBILITY_ID, value="Informações do app"
            ).click()

            el = driver.find_element(
                by=MobileBy.XPATH,
                value="//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.RelativeLayout/android.widget.TextView[1]",
            )
            el.click()
            sleep(1)
            wait.until(
                EC.element_to_be_clickable(
                    (MobileBy.ID, "com.android.settings:id/button2")
                )
            ).click()

            """el3 = driver.find_element(by=MobileBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.ListView/android.widget.TextView[2]")
            el3.click()

            el4 = driver.find_element(by=MobileBy.ID, value="android:id/button1")
            el4.click()"""
            driver.back()
            driver.back()

            driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value="Instagram").click()

            try:
                entrar(fila[a], dbcliente.find_one({"user": fila[a]})["senha"], driver)

            except:
                print("n foi possivel logar,tentando de novo")
                async_to_sync(channel_layer.group_send)(
                        "notifications",
                        {"type": "send_notification", "message": "n foi possivel logar,tentando de novo"},
                    )
                try:
                    entrar(
                        fila[a], dbcliente.find_one({"user": fila[a]})["senha"], driver
                    )

                except:
                    print("n foi possivel logar")
                    async_to_sync(channel_layer.group_send)(
                        "notifications",
                        {"type": "send_notification", "message": "n foi possivel logar"},
                    )

        sleep(timebreak)
    fim = time.time()
    print(f"o tempo de execução foi de: {(fim - inicio) / 60}")
    async_to_sync(channel_layer.group_send)(
        "notifications",
        {"type": "send_notification", "message": f"o tempo de execução foi de: {(fim - inicio) / 60}"},
    )
