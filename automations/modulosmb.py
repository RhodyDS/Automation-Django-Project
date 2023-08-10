from time import sleep
from selenium.webdriver.common.by import By
from random import  randint
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time
from rich import print
from appium.webdriver.common.mobileby import MobileBy
import datetime


def ocutec(driver):
    try:
        driver.hide_keyboard()
    except:
        driver.hide_keyboard()


def sair(driver):
    try:
        driver.find_element(By.CSS_SELECTOR,'[content-desc="Perfil"]').click()
    except:
        sleep(1)
        driver.find_element(By.CSS_SELECTOR,'[content-desc="Perfil"]').click()
    sleep(1)
    try:
        driver.find_element(By.CSS_SELECTOR,'[content-desc="Opções"]').click()
        sleep(1)
        driver.find_element(By.CSS_SELECTOR,'[text="Configurações"]').click()
    except:
        sleep(1)
        driver.find_element(By.CSS_SELECTOR,'[content-desc="Opções"]').click()
        sleep(1)
        driver.find_element(By.CSS_SELECTOR,'[content-desc="Configurações"]').click()

        
        
    sleep(2)
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(140, 554) 
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(140, 272) 
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    sleep(1)
    try:
        driver.find_element(By.CSS_SELECTOR,'[text^="Desconectar"]').click()
    except:
        driver.find_element(By.CSS_SELECTOR,'[text^="Sair"]').click()
    sleep(1)
    try:
        driver.find_element(By.CSS_SELECTOR,'[text="Sair"]').click()
    except:
        driver.find_element(by=MobileBy.ID, value="com.instagram.android:id/primary_button").click()


def entrar(nom, sen,driver):
    print(f'o nome:{nom} a senha {sen}')
    try:
        driver.find_element(By.CSS_SELECTOR,'[text*="NENHUMA DAS"]').click()
    except:
        sleep(1)
        try:
            driver.find_element(By.CSS_SELECTOR,'[text*="NENHUMA DAS"]').click()
        except:
            print('não apareceu o smart lock')
    try:
        
        try:
            sleep(1)
            driver.find_element(By.CSS_SELECTOR,f'[text="{nom}"]').click()

            #ocutec(driver)

            senha = driver.find_element(By.CSS_SELECTOR,'[text="Senha"]')


            senha.send_keys(sen)


            ###################botao entrar##################
            driver.find_element(By.CSS_SELECTOR,'[text="Entrar"]').click()


        except:
            driver.find_element(By.CSS_SELECTOR,'[text="Trocar de conta"]').click()
            sleep(1)
            driver.find_element(By.CSS_SELECTOR,'[text*="Número"]').click()
            sleep(1)
            #ocutec(driver)
            driver.find_element(By.CSS_SELECTOR,'[text*="Número"]').send_keys(nom)
            sleep(randint(1, 3))
            #################################################senha###############################################
            try:
                senha = driver.find_element('id','com.instagram.android:id/password').click()
                sleep(1)
                #ocutec(driver)
                driver.find_element('id','com.instagram.android:id/password').send_keys(sen)
            except:
                senha = driver.find_element('id','com.instagram.android:id/password')
                sleep(1)
                senha.send_keys(sen)
            
            sleep(randint(1, 3))
            ###################botao entrar##################
            driver.find_element(By.CSS_SELECTOR,'[text="Entrar"]').click()

    except:
        print('entrou direto')



def pesquisar(user,driver):
        try:
            driver.find_element('id','com.instagram.android:id/search_tab').click()
            driver.find_element('id','com.instagram.android:id/action_bar_search_edit_text').click()
            driver.find_element('id','com.instagram.android:id/action_bar_search_edit_text').clear()
            driver.find_element('id','com.instagram.android:id/action_bar_search_edit_text').send_keys(
                user)
        except:
            print('erro ao tentar pesquisar')
            try:
                driver.back()
                sleep(randint(1, 2))
            except:
                print('não deu de voltar a page')
            try:
                driver.find_element(By.CSS_SELECTOR,'[text="OK"]').click()
                sleep(randint(1, 2))
            except:
                print('o insta não parou')
            try:
                driver.find_element(By.CSS_SELECTOR,'[text="Instagram"]').click()
                sleep(randint(1, 2))
            except:
                print('parece que já estamos no instagram..')

        sleep(randint(2, 3))
            
        try:
            perf = driver.find_elements(By.CSS_SELECTOR,'[text= '+ user + ' ]')[1]
            print(perf)
            if perf.text == user:
                perf.click()
            else:
                print(f'usuario {user} não encontrado. pulando para o proximo')
        except:
            print('sem usuario para essa busca....proximo..')


def traterror(driver,problem,user,sen):
    driver.back()
    try:
        try:
            driver.find_element(By.CSS_SELECTOR,'[text="Instagram"]').click()
        except: 
            driver.find_element(By.XPATH,'//android.view.View[6]').click()
    except:
        print('parece que já estamos no instagram..')
    entrar(user,sen,driver)
    if problem == 'unf':
        try:
            driver.find_element(By.CSS_SELECTOR,'[content-desc="Perfil"]').click()
            sleep(randint(3, 5))
            driver.find_element(By.CSS_SELECTOR,'[text="Seguindo"]').click()
            sleep(randint(3, 5))
            driver.find_element(By.CSS_SELECTOR,'[text^="Classificado"]').click()
            sleep(randint(2, 3))
            driver.find_element(By.CSS_SELECTOR,'[text="Data em que começou a seguir: mais antigas"]').click()
            sleep(randint(3, 5))
        except:
            print('não foi possivel ir para area de seguidores,tentando de novo')
            
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
    elif problem == 'fol':
        try:
            driver.find_element(By.XPATH,'//android.widget.FrameLayout[@content-desc="Página inicial"]/android.view.ViewGroup').click()
            driver.find_element(by=MobileBy.ACCESSIBILITY_ID, value='Pesquisar e explorar').click()

        except:
            print('não conseguimos ir para barra de pesquisa')
            driver.back()


