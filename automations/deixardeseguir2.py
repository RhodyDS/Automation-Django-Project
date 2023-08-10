from re import X
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pickle
from random import choices, randint
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver import Remote
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from .modulosmb import entrar , traterror
import datetime
from pymongo import MongoClient


def desseguir(clientes, quantidade, driver, rodd, i,dispositivo):
    client = MongoClient()
    db = client['Rengage']

    dbcliente = db['clientes']
    dbwork_diario = db['workday']
    dbplan = db['planos']

    def ocutec(driver):
        try:
            driver.hide_keyboard()
        except:
            driver.hide_keyboard()



    ###nome do cliente
    data = datetime.date.today()
    h = clientes



    sen = dbcliente.find_one({'user':h})['senha']
    # quantidade

    y = quantidade

    # verificar se está na lista branca e se está na lista de já deixou de seguir
    ######################### verificanddo se já tem lista de já seguidos para usuario ################################

    try:
        tamunf = len(dbcliente.find_one({'user': h})['desseguiu'])
        print(f'o usuario {h} já deixou de seguir um total de {tamunf} pessoas!!')
    except:
        print(f'o usuario {h} ainda não  deixou de seguir ninguem.')
        dbcliente.update_one({'user':h},{'$set':{'desseguiu':[]}})


    try:
        tamfol = len(dbcliente.find_one({'user': h})['seguiu'])
        print(f'o usuario {h} já seguiu um total de {tamfol} pessoas!!')
    except:
        print(f'o usuario {h} ainda não seguiu  ninguem.')
        dbcliente.update_one({'user':h},{'$set':{'seguiu':[]}})

    try:
        tamwhite = len(dbcliente.find_one({'user': h})['lista_branca'])
        print(f'o usuario {h} tem um total de {tamwhite} pessoas em sua lista branca!!')
    except:
        print(f'o usuario {h} ainda não  tem ninguem em sua lista branca.')
        dbcliente.update_one({'user':h},{'$set':{'lista_branca':[]}})

    #sleep(randint(1, 2))
    try:
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(1430,2450)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(1430,2455)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
    except:
        print('erro ao clicar em perfil')

    try:
        driver.implicitly_wait(2)
        driver.find_element(By.CSS_SELECTOR,'[content-desc="Perfil"]').click()
        driver.implicitly_wait(2)
        driver.find_element(By.CSS_SELECTOR,'[text="Seguindo"]').click()
        driver.implicitly_wait(2)
        driver.find_element(By.CSS_SELECTOR,'[text^="Classificado"]').click()
        driver.implicitly_wait(2)
        driver.find_element(By.CSS_SELECTOR,'[text="Data em que começou a seguir: mais antigas"]').click()
        sleep(randint(3, 5))
    except:
        print('não foi possivel ir para area de seguidores,tentando de novo')
        try:
            try:
                driver.find_element(By.CSS_SELECTOR,'[content-desc="Perfil"]').click()
            except:
                try:
                    driver.find_element('id','com.instagram.android:id/tab_avatar').click()
                except:
                    driver.find_element(By.XPATH,'//android.widget.FrameLayout[@content-desc="Perfil"]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ImageView').click()

            	
            sleep(randint(3, 5))
            driver.find_element(By.CSS_SELECTOR,'[text="Seguindo"]').click()
            sleep(randint(5, 7))
            driver.find_element(By.CSS_SELECTOR,'[text^="Classificado"]').click()
            sleep(randint(2, 3))
            driver.find_element(By.CSS_SELECTOR,'[text="Data em que começou a seguir: mais antigas"]').click()
            sleep(randint(5, 7))
        except:
            y = 0

    cont = dbwork_diario.find_one({'data': str(data)})[dispositivo]['qAtual']
    deseguiu = dbwork_diario.find_one({'data': str(data)})[dispositivo]['qAtual']
    tentativa = 0
    trat = 0
    sleep(2)
    #idplano = dbcliente.find_one({'user': clientes})['plano']
    while cont < y:
        """if dbwork_diario.find_one({'data': str(data)})['clientes'][clientes]['unf'] >= dbplan.find_one({'_id': idplano})['buscar_pessoas']:
            print('cliente atingiu o limite diario')
            break"""
        for k in range(0, 11):
            try:
                j = driver.find_elements('id','com.instagram.android:id/follow_list_username')[k]
            except:
                trat += 1
                if trat > 15:
                    traterror(driver,'unf',clientes,sen)
                    trat = 0
                continue
            nome = j.text
            if nome not in dbcliente.find_one({'user':h})['desseguiu'] and nome not in dbcliente.find_one({'user':h})['lista_branca']:
                j.click()
                sleep(randint(2, 3))
                try:
                    try:
                        btseguir = driver.find_elements(By.CSS_SELECTOR,'[text="Seguindo"]')[1]

                    except:
                        try:
                            btseguir = driver.find_element(By.CSS_SELECTOR,'[text="Solicitado"]')
                        except:
                            btseguir = driver.find_element(By.CSS_SELECTOR,'[text="Seguir"]')

                    if btseguir.text == 'Seguindo':
                        btseguir.click()
                        sleep(randint(2, 3))
                        driver.find_element(By.CSS_SELECTOR,'[text="Deixar de seguir"]').click()
                        sleep(1)
                        try:
                            driver.find_element(By.CSS_SELECTOR,'[text="Deixar de seguir"]').click()
                        except:
                            print('não tem confirmação')
                        print('clicado em deixar de seguir')

                        try:  # tentativa caso de erro ao bloquear
                            try:
                                confirmabotao = browser.find_element(By.XPATH,
                                                                     '/html/body/div[7]/div/div/div/div[2]/button[2]')
                                confirmabotao.click()
                            except:
                                confirmabotao = browser.find_element(By.CSS_SELECTOR, 'button.aOOlW:nth-child(2)')
                            print('houve algum erro ao seguir o usuario.')
                            if tentativa < 5:
                                print('vamos tentar seguir a proxima conta, se o erro persistir tente mais tarde.')
                                tentativa += 1
                                cont += 1
                                continue
                            else:
                                break
                        except:
                            print('unfollow com sucesso')
                            sleep(randint(2,3))
                            try:
                                btseguir = driver.find_element(By.CSS_SELECTOR,'[text="Seguir"]')

                            except:
                                try:
                                    btseguir = driver.find_element(By.CSS_SELECTOR,'[text="Solicitado"]')

                                except:
                                    btseguir = driver.find_element(By.CSS_SELECTOR,'[text="Seguir de volta"]')

                            print(f'resultado:{btseguir.text}')
                            if btseguir.text == 'Seguir' or 'Seguir de volta':
                                deseguiu += 1
                                dbwork_diario.update_one({'data':str(data)}, {'$set' :{dispositivo+'.qAtual': deseguiu}})

                                som = dbwork_diario.find_one({'data': str(data)})['clientes'][clientes]['unf'] + 1
                                dbwork_diario.update_one({'data': str(data)},
                                                         {'$set': {'clientes.' + clientes + '.unf': som}})
                                print(dbwork_diario.find_one({'data': str(data)})['clientes'][clientes])

                            print(
                                f'[on green]rodada {rodd}°[bold]{i}°cliente:{clientes}[/][/]\n[on red]:white_check_mark: {deseguiu} pessoas desseguidas!!TOTAL:{dbwork_diario.find_one({"data":str(data)})["clientes"][h]["unf"]}[/]')
                            dbcliente.update_one({'user': h}, {'$push': {'desseguiu': nome}})

                    else:
                        dbcliente.update_one({'user': h}, {'$push': {'desseguiu': nome}})
                         ##########caso esteja seguindo mas não esteja na lista##############################
                        print('conta já não é seguida.')
                    
                    cont += 1
                    
                    sleep(randint(2,3))
                except:
                    print('ocorreu algum erro no processo de umfollow')
                    traterror(driver,'unf',clientes,sen)
                    continue
                driver.back()
                if cont == y:
                    print('acabou')
                    break
            else:
                try:
                    print('usuario já levou unf antes ou tá em lista branca')
                    if driver.find_elements(By.CSS_SELECTOR,'[text="Seguindo"]')[k]:
                    #driver.find_elements('id','com.instagram.android:id/follow_list_row_large_follow_button')[k].text == 'Seguindo':
                        try:
                            if nome in dbcliente.find_one({'user': h})['lista_branca']:
                                print(f'usuario {nome} em lista branca')
                        except:
                            dbcliente.update_one({'user': h}, {"$pull": {'desseguiu': nome}})
                except:
                    print('erro ao verificar se está ou n na lista branca')

        #touch.press(x=702, y=2380).move_to(x=695, y=900).release().perform()
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(536, 1888)   #(308, 1105)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(536, 644)  #(308, 481)
        actions.w3c_actions.pointer_action.release()
        actions.perform()


