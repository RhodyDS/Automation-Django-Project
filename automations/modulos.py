from selenium.webdriver import Firefox
from time import sleep
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
import modulos2
from pymongo import MongoClient
from modulosmb import pesquisar
client = MongoClient()
db = client['Rengage']
dbbot = db['rhobots']
dbcliente = db['clientes']
dbxerox = db['packfollowers']

emoji = ['😮','😍','💅','🙏','🤝','🙌','🤙','✌','🙀','😻','😺','🥴','😎','😌','😬','😜','🤗','😚','😗','🤩','😇','😊','😉','🙃','🙂','😀','😃','😄','😁','😆','😊','😘','🥰','❤','💯','🔥','👏']
def ocutec(driver):
    try:
        driver.hide_keyboard()
    except:
        driver.hide_keyboard()


def sairdeconta(browser):
    sleep(1)
    try:
        perfilbotao = browser.find_element(By.XPATH,
                                           '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/span/img')
        perfilbotao.click()
    except:

        perfilbotao = browser.find_element(By.CSS_SELECTOR,'.qNELH')
        perfilbotao.click()
        print('achei o  botao do perfil')
    sleep(randint(1, 2))
    try:
        sairbotao = browser.find_element(By.XPATH,
                                         '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div')
    except:

        sairbotao = browser.find_element(By.CSS_SELECTOR,
            '#f2b10fbcc5b80b4 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
        print('achei o botao sair')
    sairbotao.click()

    sleep(1)
    browser.close()



def entrardenovo(browser, url, user, sen, retu=False):
    while tent < 5:
        browser.close()
        sleep(1)
        browser = webdriver.Firefox()
        browser.get(url)
        sleep(randint(3, 4))
        try:

            nick = browser.find_element(By.CSS_SELECTOR,
                'div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
            nick.click()
            nick.clear()
            nick.send_keys(user)
            sleep(randint(1, 3))
            senha = browser.find_element(By.CSS_SELECTOR,
                'div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
            senha.click()
            senha.clear()
            senha.send_keys(sen)
            sleep(randint(1, 3))
            botao = browser.find_element(By.CSS_SELECTOR, '.L3NKy')
            botao.click()
            sleep(4)

        except:
            print('ocorreu um erro em entra de novo')
            tent += 1
        try:
            une = browser.find_element(By.CSS_SELECTOR,'.eiCW-')
            print(une)
            print('usuario existe ou senha incorreta')
            print('tentando logar novamente')
        except:
            break
    if retu == True:
        return browser


def tit(txt):
    print('-=' * 40)
    print('-=' * 40)
    print(f'{txt:^70}')
    print('-=' * 40)
    print('-=' * 40)


############################################interação
# 01 impulsionar
# submenus do impuspost
def ultpost():
    arq = open('dados/rhodybots.pkl', 'rb')
    dic = pickle.load(arq)
    arq.close()
    arqqpack = open('dados/packcoment.pkl', 'rb')
    dicpack = pickle.load(arqqpack)
    arqqpack.close()
    errocont = []

    url = 'https://www.instagram.com/'

    # dadoscontadores
    contadorconta = 0
    numcoment = 0
    contacs = 0
    contass = 0
    repetido = []
    # buscar links
    quanti = int(input(
        'digite a quantidade de fotos a ser curtida:(pega as ultimas fotos postadas) '))  # variavel contadora de fotos
    while True:
        linkdafoto = input('insira o user do perfil: ')
        tc = input(f'o nome de usuario que vc quer trabalhar é {linkdafoto},tem certeza?\n[s]-sim\n[outro valor]-não')
        if tc in 's':
            break

    # selecionar pack de comentarios
    while True:
        print(dicpack.keys())
        pack = input('qual o pack de comentarios deseja usar: ')
        if pack in dicpack.keys():
            print('tudo certo.')
            comentarios = dicpack[pack]
            break
        else:
            print('nada certo. tente de novo.')

    # entrar no perfil
    print(dic.items())
    for user, sen in dic.items():
        browser = webdriver.Firefox()
        try:

            browser.get(url)
            sleep(randint(3, 4))
            try:
                nick = browser.find_element(By.CSS_SELECTOR,
                    'div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
                nick.click()
                nick.clear()
                nick.send_keys(user)
                sleep(randint(1, 4))
                senha = browser.find_element(By.CSS_SELECTOR,
                    'div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
                senha.click()
                senha.clear()
                senha.send_keys(sen)
                sleep(randint(1, 4))
                botao = browser.find_element(By.CSS_SELECTOR, '.L3NKy')
                botao.click()
                sleep(2)
            except:
                tit('houve algum erro ao tentar logar. reiniciando a pagina.')
                browser = entrardenovo(browser, url, user, sen, True)

            # teste de senha ou login incorreto
            tent = 0
            while tent <= 5:
                sleep(3)
                try:
                    une = browser.find_element(By.CSS_SELECTOR,'.eiCW-')
                    print(une)
                    print('usuario n existe ou senha incorreta ou algum erro.')
                    browser = entrardenovo(browser, url, user, sen, True)
                    tent += 1
                    print(f'foram {tent} tentativas de entrar na conta')


                except:
                    print('aguarde...')
                    break

            # teste se conta realmente entrou
            try:
                sleep(3)
                nick = browser.find_element(By.CSS_SELECTOR,
                    'div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
                nick.click()
                nick.clear()
                nick.send_keys(user)
                sleep(randint(1, 4))
                senha = browser.find_element(By.CSS_SELECTOR,
                    'div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
                senha.click()
                senha.clear()
                senha.send_keys(sen)
                sleep(randint(1, 4))
                botao = browser.find_element(By.CSS_SELECTOR,'.L3NKy > div:nth-child(1)')
                botao.click()

            except:
                print('perfil já logado')

            # entrar na da primeira foto
            tent = 0
            while tent <= 5:
                try:
                    browser.get('https://www.instagram.com/' + linkdafoto + '/')
                    sleep(randint(3, 4))
                    botaoentrarnafot = browser.find_element(By.CSS_SELECTOR,
                        'div.Nnq7C:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(2)')
                    botaoentrarnafot.click()
                    break
                except:
                    tit('houve algum erro ao carregar a primeira foto foto.tentando de novo..')
                    browser = entrardenovo(browser, url, user, sen, True)
                    tent += 1
                    print(f'ao todo foram {tent} tentativas')

            # curtir e comentar
            for i in range(0, quanti):
                sleep(randint(3, 4))
                try:
                    try:
                        curtir = browser.find_element(By.CSS_SELECTOR,
                            '.fr66n > button:nth-child(1) > div:nth-child(1) > svg:nth-child(1)')
                        curtir = browser.find_element(By.CSS_SELECTOR,'.fr66n > button:nth-child(1)')
                        curtir.click()
                    except:
                        print('foto já foi curtida')
                except:
                    tit('houve algum erro ao tentar curtir a foto. tentando de novo...')
                    try:
                        curtir = browser.find_element(By.CSS_SELECTOR,
                            '.fr66n > button:nth-child(1) > div:nth-child(1) > svg:nth-child(1)')
                        curtir = browser.find_element(By.CSS_SELECTOR,'.fr66n > button:nth-child(1)')
                        curtir.click()
                    except:
                        print('foto já foi curtida')
                sleep(randint(1, 3))
                try:
                    salvar = browser.find_element(By.CSS_SELECTOR,
                        '.wmtNn > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > div:nth-child(1) > svg:nth-child(1)').get_attribute(
                        'aria-label')
                    if salvar == 'Salvar':
                        salvar = browser.find_element(By.CSS_SELECTOR,
                            '.wmtNn > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)')
                        salvar.click()
                    else:
                        print('foto já foi salva')
                except:
                    tit('houve algum erro ao salvar a foto. tentando de novo')
                    salvar = browser.find_element(By.CSS_SELECTOR,
                        '.wmtNn > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > div:nth-child(1) > svg:nth-child(1)').get_attribute(
                        'aria-label')
                    if salvar == 'Salvar':
                        salvar = browser.find_element(By.CSS_SELECTOR,
                            '.wmtNn > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)')
                        salvar.click()
                    else:
                        print('foto já foi salvar')
                sleep(randint(1, 3))
                botaocoment = browser.find_element(By.CSS_SELECTOR,'._15y0l > button:nth-child(1)')
                botaocoment.click()
                addcom = browser.find_element(By.CSS_SELECTOR,'.Ypffh')
                confirma = browser.find_element(By.XPATH,
                                                '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button')
                coment = 1
                while coment <= 3:  # comentarios
                    while True:
                        comentario = choices(comentarios)
                        if comentario not in repetido:
                            repetido.append(comentario)
                            break
                    addcom.send_keys(comentario)
                    numemoji = randint(1,2)
                    if numemoji == 1:
                        addcom.send_keys(choices(emoji))
                    else:
                        addcom.send_keys(choices(emoji),choices(emoji))
                    sleep(randint(4, 5))
                    confirma.click()
                    sleep(3)

                    try:  # tentativa caso de erro ao bloquear

                        confirmabotao = browser.find_element(By.XPATH,
                                                             '/html/body/div[7]/div/div/div/div[2]/button[2]')
                        confirmabotao.click()
                        print('houve algum erro ao comentar a foto.')

                    except:
                        print('comentado com sucesso')
                        numcoment += 1
                        print(f'{numcoment} comentarios gerados!!')

                    coment += 1
                repetido.clear()
                if quanti > 1:
                    try:
                        sleep(randint(3, 5))
                        try:
                            passarbotao = browser.find_element(By.CSS_SELECTOR,'[aria-label="Avançar"]')

                        except:
                            passarbotao = browser.find_element(By.CSS_SELECTOR,
                                '.l8mY4 > button:nth-child(1) > div:nth-child(1) > span:nth-child(1) > svg:nth-child(1)')
                        passarbotao.click()
                        sleep(randint(3, 5))
                    except:
                        print('houve algum erro ao passar de foto.')
                        confirmabotao = browser.find_element(By.CSS_SELECTOR,'button.aOOlW:nth-child(2)')
                        confirmabotao.click()
                        try:
                            passarbotao = browser.find_element(By.CSS_SELECTOR,'._65Bje')
                        except:
                            passarbotao = browser.find_element(By.CSS_SELECTOR,
                                '.l8mY4 > button:nth-child(1) > div:nth-child(1) > span:nth-child(1) > svg:nth-child(1)')
                        passarbotao.click()
                        sleep(randint(3, 5))
                else:
                    try:
                        sleep(1)
                        xis = browser.find_element(By.XPATH, '/html/body/div[6]/div[1]/button')
                        xis.click()
                        print('foto fechada.')
                    except:
                        sleep(1)
                        xis = browser.find_element(By.CSS_SELECTOR, '.NOTWr > button:nth-child(1)')
                        xis.click()
                        print('foto fechada.')
            try:
                # sair da conta         
                sairdeconta(browser)
                contacs += 1
                contadorconta += 1

            except:
                try:
                    sleep(1)
                    xis = browser.find_element(By.XPATH, '/html/body/div[6]/div[1]/button')
                    xis.click()
                    print('foto fechada.')
                except:
                    sleep(1)
                    xis = browser.find_element(By.CSS_SELECTOR, '.NOTWr > button:nth-child(1)')
                    xis.click()
                    print('foto fechada.')
                sairdeconta(browser)
                contacs += 1
                contadorconta += 1




        except:
            tit('houve algum erro ao processar nesta conta.')
            errocont.append(user)
            contadorconta += 1
            contass += 1
            browser.close()

        # resultados gerados da ultima conta usada:
        print(f'já foram acessadas total de {contadorconta} contas de {len(dic)}')
        print(f'contas com sucesso: {contacs}')
        print(f'contas sem sucesso: {contass}')
        print(f'contas que precisam ser analisadas:{errocont}')


def esppost():
    dbcoment = db['packcomentarios']
    errocont = []
    repetido = []
    url = 'https://www.instagram.com/'
    quantbot = dbbot.estimated_document_count()
    # dadoscontadores
    contadorconta = 0
    numcoment = 0
    contacs = 0
    contass = 0
    rep = 0
    # buscar links

    while True:
        linkdafoto = input('insira o link da foto ')
        tc = input(f'o link que vc quer trabalhar é {linkdafoto},tem certeza?\n[s]-sim\n[outro valor]-não')
        if tc in 's':
            break

    # selecionar pack de comentarios
    while True:
        for i in dbcoment.find():
            print(i['nome'])
        pack = input('qual o pack de comentarios deseja usar: ')
        if dbcoment.find_one({'nome':pack}):
            print('tudo certo.')
            comentarios = dbcoment.find_one({'nome':pack})['pack']
            break
        else:
            print('nada certo. tente de novo.')

    # entrar no perfil
    for user in dbbot.find():
        browser = webdriver.Firefox()
        try:

            browser.get(url)
            sleep(randint(3, 4))
            try:
                nick = browser.find_element(By.CSS_SELECTOR,
                    'div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
                nick.click()
                nick.clear()
                nick.send_keys(user['user'])
                sleep(randint(2, 4))
                senha = browser.find_element(By.CSS_SELECTOR,
                    'div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
                senha.click()
                senha.clear()
                senha.send_keys(user['senha'])
                sleep(randint(2, 4))
                botao = browser.find_element(By.CSS_SELECTOR, '.L3NKy')
                botao.click()
                sleep(2)
            except:
                tit('houve algum erro ao tentar logar. reiniciando a pagina.')
                browser = entrardenovo(browser, url, user['user'], user['senha'], True)

            # teste de senha ou login incorreto
            tent = 0
            while tent <= 5:
                sleep(3)
                try:
                    une = browser.find_element(By.CSS_SELECTOR,'.eiCW-')
                    print(une)
                    print('usuario existe ou senha incorreta ou algum erro.')
                    browser = entrardenovo(browser, url, user['user'], user['senha'], True)
                    tent += 1
                    print(f'foram {tent} tentativas de entrar na conta')


                except:
                    print('aguarde...')
                    break

            # teste se conta realmente entrou
            try:
                sleep(3)
                nick = browser.find_element(By.CSS_SELECTOR,
                    'div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
                nick.click()
                nick.clear()
                nick.send_keys(user['user'])
                sleep(randint(1, 4))
                senha = browser.find_element(By.CSS_SELECTOR,
                    'div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
                senha.click()
                senha.clear()
                senha.send_keys(user['senha'])
                sleep(randint(1, 4))
                botao = browser.find_element(By.CSS_SELECTOR,'.L3NKy > div:nth-child(1)')
                botao.click()

            except:
                print('perfil já logado')

            # entrar na da primeira foto
            tent = 0
            while tent <= 5:
                try:
                    browser.get(linkdafoto)
                    sleep(randint(2, 3))
                    try:
                        curtir = browser.find_element(By.XPATH,'//section[1]/span[1]/button')
                        break
                    except:
                        print('like não encontrado,talvez a foto n tem sido carregada...')
                        tent += 1
                        print(f'ao todo foram {tent} tentativas')
                except:
                    tit('houve algum erro ao carregar a foto foto.tentando de novo..')
                    browser = entrardenovo(browser, url, user['user'], user['senha'], True)
                    tent += 1
                    print(f'ao todo foram {tent} tentativas')

            # curtir e comentar

            sleep(randint(1, 2))
            try:
                curtir = browser.find_element(By.XPATH,'//section[1]/span[1]/button')
                curtir.click()
            except:
                tit('houve algum erro ao tentar curtir a foto. tentando de novo...')
                curtir = browser.find_element(By.XPATH,'//section[1]/span[1]/button')
            sleep(randint(1, 2))
            try:
                salvar = browser.find_element(By.XPATH,'//span[4]/div/div/button')
                salvar.click()
            except:
                tit('houve algum erro ao salvar a foto. tentando de novo')
                salvar = browser.find_element(By.XPATH,'//span[4]/div/div/button')
                salvar.click()
            sleep(randint(1, 2))
            # variaveis de comentarios
            try:
                botaocoment = browser.find_element(By.XPATH,'//section[1]/span[2]/button')
                botaocoment.click()
                addcom = browser.find_element(By.XPATH,'//section[3]/div[1]/form/textarea')
                confirma = browser.find_element(By.XPATH,'//section[3]/div/form/button')
                coment = 1
            except:
                print('não foi possivel encontrar variaveis de comentario')
            while coment <= 3:  # comentarios
                while True:
                    comentario = choices(comentarios)
                    if comentario not in repetido:
                        repetido.append(comentario)
                        break
                addcom.send_keys(comentario)
                numemoji = randint(1, 3)
                if numemoji == 1:
                    addcom.send_keys(choices(emoji))
                elif numemoji == 2:
                    addcom.send_keys(choices(emoji), choices(emoji))
                sleep(randint(4, 5))
                confirma.click()
                sleep(3)

                try:  # tentativa caso de erro ao bloquear

                    confirmabotao = browser.find_element(By.XPATH,
                                                         '/html/body/div[7]/div/div/div/div[2]/button[2]')
                    confirmabotao.click()
                    print('houve algum erro ao comentar a foto.')

                except:
                    print('comentado com sucesso')
                    numcoment += 1
                    print(f'{numcoment} comentarios gerados!!')
                coment += 1
            if rep >= 5:
                repetido.clear()
                rep = 0
            rep +=1
            try:
                # sair da conta
                sleep(1)
                try:
                    perfilbotao = browser.find_element(By.XPATH,'//div/div[6]/div[1]/span')
                    perfilbotao.click()
                except:
                    print('erro ao achar botao sair')
                    perfilbotao = browser.find_element(By.XPATH,'//div/div[6]/div[1]/span')
                sleep(randint(1, 2))
                try:
                    sairbotao = browser.find_element(By.XPATH,'//div[6]/div[2]/div[2]/div[2]/div[2]')
                except:
                    sairbotao = browser.find_element(By.XPATH,'//section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div/div[2]/div[5]/div/div/div/div')
                sairbotao.click()
                contadorconta += 1
                contacs += 1
                sleep(1)
                browser.close()
            except:
                print("erro ao sair de conta!")


        except:
            tit('houve algum erro ao processar nesta conta.')
            contadorconta += 1
            contass += 1
            errocont.append(user['user'])
            browser.close()
        
        # resultados gerados da ultima conta usada:
        print(f'já foram acessadas total de {contadorconta} contas de {quantbot}')
        print(f'contas com sucesso: {contacs}')
        print(f'contas sem sucesso: {contass}')
        print(f'contas que precisam ser analisadas:{errocont}')


################################menu principal interação##############################################
def impuspost():  # sub menu impussionar post
    while True:
        tit('IMPUSSIONAR POSTAGEM')
        menut1 = input('''
                01 - ultimas postagens
                02 - postagem especifica
                03 - voltar\n
                                    ''')
        if menut1 == '1':
            ultpost()
        elif menut1 == '2':
            esppost()
        else:
            break


##########################02 seguir#######################################
def seguir():
    dicarq = open('dados/clientesrengage.pkl', 'rb')  # abrir dados de clientes
    cliente = pickle.load(dicarq)
    dicarq.close()
    arq = open("dados/listadexerox.pkl", "rb")  # abrir pack de seguidores
    xerox = pickle.load(arq)
    arq.close()
    list = []

    def ocutec(driver):
        try:
            driver.hide_keyboard()
        except:
            driver.hide_keyboard()
    jatem = 0
    x = []
    w = []
    sen = []
    ###################################### cliente que vai ser trabalhado###############################################
    quanti = int(input('quantos clientes vamos trabalhar?'))
    for i in range(0, quanti):
        while True:
            x.append(input(f'digite o nome do cliente {i+1} que vamos trabalhar: '))
            if x[i] in cliente.keys():
                print('cliente encontrado')
                sen.append(cliente[x[i]])
                break
            else:
                print('cliente não encontrado...digite novamente.')
        ############################## pack de seguidores##################################################
        while True:
            w.append(input('digite o nome do pack de seguidores que vamos trabalhar nessa conta: '))
            if w[i] in xerox.keys():
                print('pack encontrado')
                break
            else:
                print('pack não encontrado digite novamente.')
    try:
        arq = open("dados/listjaseguidos.pkl", "rb")  # abre lista de pessoas já seguidas anteriormente.
        contas = pickle.load(arq)
        print('leu')
        arq.close()
    except:
        arq = open("dados/listjaseguidos.pkl", "wb")  # alternativa!! abre lista de pessoas já seguidas anteriormente.
        contas = {}
        print('nao leu')
        arq.close()
        list = []



    ####################################quantidade de fotos que deseja curtir##############################################
    # while True:
    # z = int(input('digite o numero de fotos a curtir '))
    # tc = input(f'tem certeza que quer curtir {z} fotos?\n[1] - sim\n[outro valor] - não\n')
    # if tc in '1':
    #    break

    ##################### quantidade que vamos seguir:##################################################
    while True:
        y = int(input('digite o numero de pessoas a seguir '))
        tc = input(f'tem certeza que quer seguir {y} pessoas?\n[1] - sim\n[outro valor] - não\n')
        if tc in '1':
            break
    #########################verificanddo se já tem lista de já seguidos para usuario################################
    for i in range(0, quanti):
        try:
            print(f'o usuario {x[i]} já seguiu um total de {len(contas[x[i]])} pessoas!!')
        except:
            print(f'o usuario {x} ainda não seguiu ninguem.')
            contas[x[i]] = list[:]
    ############################################# logarinsta###########################################
    driver = Remote('http://localhost:4723/wd/hub',
                    {'platformName': 'android'})
    
    saber = input('fazer login de forma automatica?\n[1]-sim\n[outro valor]-não\n')
    if saber == '1':
        jatem = 1
    
    for i in range(0,quanti):
        if jatem == 0:
            try:
                driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Instagram"]').click()
            except:
                print('já estamos no app')
            ##########fazer login###################

            sleep(5)
            try:
                driver.find_element_by_xpath(
                    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[3]').click()
            except:
                print('já estamos na area de login')
            sleep(1)
            try:
                ##########################usuario#######################################
                driver.find_element('id','com.instagram.androie:id/login_username').click()
                sleep(1)
                #ocutec(driver)
                driver.find_element('id','com.instagram.androie:id/login_username').send_keys(x[i])
                sleep(randint(1, 3))
                #################################################senha###############################################
                driver.find_element('id','com.instagram.androie:id/login_password').click()
                sleep(1)
                #ocutec(driver)
                driver.find_element('id','com.instagram.androie:id/login_password').send_keys(sen[i])
                sleep(randint(1, 3))
                ###################botao entrar##################
                driver.find_element('id','com.instagram.androie:id/next_button').click()
            except:
                print('conta já logada')




        ##################################seguirconta#################################################
        cont = 0
        seguiu = 0
        tentativa = 0
        errolist = []
        while seguiu < y:          
            if xerox[w[i]][cont] not in contas[x[i]]:
                print(f'usuario {cont + 1} da lista')
                try:
                    driver.find_element_by_xpath(
                        '//android.widget.FrameLayout[@content-desc="Pesquisar e explorar"]/android.widget.ImageView').click()
                    driver.find_element('id','com.instagram.android:id/action_bar_search_edit_text').click()
                    #ocutec(driver)
                    driver.find_element('id','com.instagram.android:id/action_bar_search_edit_text').clear()
                    driver.find_element('id','com.instagram.android:id/action_bar_search_edit_text').send_keys(
                        xerox[w[i]][cont])
                except:
                    print('erro ao tentar pesquisar')
                sleep(randint(2, 3))

                try:
                    perf = driver.find_element('id','com.instagram.android:id/row_search_user_username')
                    if xerox[w[i]][cont] == perf.text:
                        perf.click()
                    else:
                        print(f'usuario {xerox[w[i]][cont]} não encontrado. pulando para o proximo')
                        errolist.append(xerox[w[i]][cont])
                        print(f'usuarios que com erro ao achar {errolist}')
                        cont += 1
                        continue
                except:
                    print('sem usuario para essa busca....proximo..')
                    errolist.append(xerox[w[i]][cont])
                    print(f'usuarios que com erro ao achar {errolist}')
                    cont += 1
                    continue
                # botão de seguir
                sleep(randint(2, 3))
                try:
                    a = driver.find_elements_by_xpath(
                        '//android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button')

                    for j in a:
                        print(j.text)
                        if j.text == 'Seguir':
                            btseguir = j
                            break
                        else:
                            btseguir = j

                    if btseguir.text == 'Seguir':
                        btseguir.click()
                        print('clicado em seguir')

                        try:  # tentativa caso de erro ao bloquear
                            try:
                                confirmabotao = driver.find_element(By.XPATH,
                                                                        '/html/body/div[7]/div/div/div/div[2]/button[2]')
                                confirmabotao.click()
                            except:
                                confirmabotao = driver.find_element(By.CSS_SELECTOR, 'button.aOOlW:nth-child(2)')
                            print('houve algum erro ao seguir o usuario.')
                            if tentativa < 5:
                                print('vamos tentar seguir a proxima conta, se o erro persistir tente mais tarde.')
                                tentativa += 1
                                cont += 1
                                continue
                            else:
                                break
                        except:
                            print('seguido com sucesso')
                            a = driver.find_elements_by_xpath(
                                '//android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button')
                            for j in a:
                                print(f'resultado:{j.text}')
                                if j.text == 'Seguindo':
                                    seguiu += 1
                                    break
                            print(f'{seguiu} pessoas seguidas!!')
                            contas[x[i]].append(
                                xerox[w[i]][cont])  ######aarmazena a conta seguida na lista de já seguidos#############
                            with open("dados/listjaseguidos.pkl", "wb") as arq:
                                pickle.dump(contas, arq)
                            #################### etapa de dar like###################
                            try:
                                sleep(randint(1, 2))
                                fotos = driver.find_elements_by_xpath(
                                    '//android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.Button')
                                quant = len(fotos)
                                try:
                                    for i in range(0, quant):
                                        fotos = driver.find_elements_by_xpath(
                                            '//android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.Button')
                                        print(f'foto numero {i + 1}')
                                        try:
                                            fotos[i].click()
                                            while True:
                                                try:
                                                    sleep(randint(1, 2))
                                                    like = driver.find_elements('id',
                                                        'com.instagram.android:id/row_feed_button_like')
                                                    for k in like:
                                                        if len(like) == 1:
                                                            k.click()
                                                        else:
                                                            if like.index(k) == 1:
                                                                k.click()

                                                    print('ganhou like hehe')
                                                    break
                                                except:
                                                    ActionChains(driver) \
                                                        .key_down(Keys.DOWN) \
                                                        .perform()
                                            sleep(1)
                                            driver.back()
                                        except:
                                            print(f'não encontramos a foto 0{fotos.index(i + 1)}')
                                        sleep(randint(1, 2))
                                except:
                                    print('ocorreu algum erro')
                            except:
                                print('usuario n possui fotos')
                            ###############################hora de sair##########################
                        driver.find_element_by_xpath(
                            '//android.widget.FrameLayout[@content-desc="Pesquisar e explorar"]/android.widget.ImageView').click()

                    else:
                        contas[x[i]].append(xerox[w][cont])  ##########caso esteja seguindo mas não esteja na lista##############################
                        with open("dados/listjaseguidos.pkl", "wb") as arq:
                            pickle.dump(contas, arq)
                        print('conta já foi seguida anteriormente.')
                        sleep(randint(1, 3))
                    sleep(randint(2, 3))
                    cont += 1
                except:
                    print('ocorreu algum erro no processo de seguir')
            else:
                cont += 1
            #print(f'cliente {x[i]} usando pack {xerox[w[i]]}')
            try:
                print(cont)
                print(len(xerox[w[i]]))
                print(xerox[w[i]][cont+1])                
                if cont > len(xerox[w[i]]):
                    print(xerox[w[i]])
                    print(len(xerox[w[i]]))
                    print(
                        f'esta lista de seguidores tem {len(xerox[w[i]])} pessoas e você já chegou no fim da lista!!\ntente seguir por outra lista.')
                    break
                else:
                    print(f'já percorreu {cont} de {len(xerox[w[i]])} nessa lista!')
            except:
                print('não foi possibvel ver se já seguiu todo mundo.')
        print(f'fim do trabalho\n{seguiu} pessoas seguidas e percorreu {cont} pessoas na lista')
        print(f'contas que ocorreram erro:\n{errolist}')
        saber = input('deseja remover usuarios com erro do pack?\n[s]-sim\n[outro valor]-não')
        if saber == 's':
            for i in errolist:
                try:
                    xerox[w[i]].remove(i)
                except:
                    print('erro ao remover usuario')
            with open("dados/listadexerox.pkl", "wb") as arq:
                pickle.dump(xerox, arq)
            print('contas removidas.')
        #######troca conta############################
        driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="Perfil"]/android.view.ViewGroup').click()
        driver.find_element('id','com.instagram.android:id/action_bar_title_chevron').click()
        sleep(1)
        usuarios = driver.find_elements('id','com.instagram.android:id/action_bar_title_chevron')
        for j in usuarios:
            if x[i+1] == i:
                j.click
                jatem = 1
                break
        if jatem == 0:
            driver.find_element('id','//android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.LinearLayout/android.widget.TextView').click()

        




###########################################ferramentas

# 01-clientes
def clientes():
    try:
        arq = open("dados/clientesrengage.pkl", "rb")
        contas = pickle.load(arq)
        print('leu')
        arq.close()
    except:
        arq = open("dados/clientesrengage.pkl", "wb")
        contas = {}
        print('nao leu')
        arq.close()

    # menu
    while True:
        tit('CLIENTES')
        menu = input('''
        01 - cadastrar cliente
        02 - clientes cadastrados
        03 - alterar dados
        04 - deletar cliente 
        [outro valor] - sair   
        ''')
        if menu == '1':
            while True:
                tit('CADASTRO DE CLIENTE')
                contas[input('insira o nome de usuario:\n')] = input('insira a senha:\n')
                cont = input('deseja continuar? S-[SIM],[qualquer tecla para cancelar]')
                if cont not in 'Ss':
                    print('cadastro feito com sucesso')
                    with open("dados/clientesrengage.pkl", "wb") as arq:
                        pickle.dump(contas, arq)
                        break
        elif menu == '2':
            tit('CLIENTES CADASTRADOS:')
            print('-' * 30)
            for user in contas.keys():
                print(f'nome de usuario: {user}\nsenha: {contas[user]}')
                print('-' * 30)

        elif menu == '3':
            tit('ALTERAR DADOS')
            menu2 = input('ALTERAÇÃO DE DADOS\n'
                          '01-alterar senha\n'
                          '02-alterar nome de usuario\n'
                          '[outro valor]-sair\n')
            if menu2 == '1':
                ususealt = input('informe o usuario que deseja alterar a senha:').lower().strip()
                if ususealt in contas.keys():
                    print(f'usuario encontrado\n'
                          f'usuario: {ususealt}\n'
                          f'senha: {contas[ususealt]}\n')
                    senhanova = input('digite a nova senha:\n')
                    temcert = input(f'senha antiga: {contas[ususealt]}\n'
                                    f'senha nova:{senhanova}\n'
                                    'deseja mesmo alterar?\n'
                                    '1 - sim\n'
                                    '[outro valor] - não\n')
                    if temcert == '1':
                        contas[ususealt] = senhanova

                        print('senha alterada com sucesso!!\n')
                        with open("dados/clientesrengage.pkl", "wb") as arq:
                            pickle.dump(contas, arq)

                    else:
                        print('senha não alterada\n')
                else:
                    print('conta não encontrada.\n')
            elif menu2 == '2':
                usualt = input('informe o usuario que deseja alterar o nick:\n').lower().strip()
                if usualt in contas.keys():
                    print(f'usuario encontrado\n'
                          f'usuario: {usualt}\n'
                          f'senha: {contas[usualt]}\n')
                    usunovo = input('digite o novo nick:\n')
                    temcert = input(f'nick antigo: {usualt}\n'
                                    f'nick novo:{usunovo}\n'
                                    'deseja mesmo alterar?\n'
                                    '1 - sim\n'
                                    '[outro valor] - não\n')
                    if temcert == '1':
                        contas[usunovo] = contas[usualt]
                        del contas[usualt]
                        print('conta alterada com sucesso!!\n')
                        with open("dados/clientesrengage.pkl", "wb") as arq:
                            pickle.dump(contas, arq)

                    else:
                        print('conta não alterada\n')
                else:
                    print('conta não encontrada.\n')
        elif menu == '4':
            tit('DELETAR CLIENTE')
            delcont = input('insira a conta que deseja apagar: \n')
            if delcont in contas.keys():
                print(f'conta encontrada!!\n'
                      f'usuario: {delcont}\n'
                      f'senha: {contas[delcont]}\n')

                temcert2 = input('deseja mesmo deletar?\n'
                                 '1 - sim\n'
                                 '[outro valor] - não\n')
                if temcert2 == '1':
                    del contas[delcont]
                    print('conta deletada com sucesso!!\n')
                    with open("dados/clientesrengage.pkl", "wb") as arq:
                        pickle.dump(contas, arq)

                else:
                    print('conta não alterada\n')
            else:
                print('conta não encontrada')
        else:
            break


# 02-rhodybots
def rhodybots():
    try:
        arq = open("dados/rhodybots.pkl", "rb")
        contas = pickle.load(arq)
        print('leu')
        arq.close()
    except:
        arq = open("dados/rhodybots.pkl", "wb")
        contas = {}
        print('nao leu')
        arq.close()
    # menu
    while True:
        tit('RHODYBOTS')
        menu = input('''
        01 - cadastrar conta
        02 - contas cadastradas
        03 - alterar dados
        04 - deletar conta 
        [outro valor] - sair   
        ''')
        if menu == '1':
            while True:
                tit('CADASTRO DE CONTA')
                modulos2.cadastro_rhobot()
        elif menu == '2':
            tit('CONTAS CADASTRADAS:')
            print(f'{len(contas)} pessoas cadastradas')
            print('-' * 30)
            for user in contas.keys():
                print(f'nome de usuario: {user}\nsenha: {contas[user]}')
                print('-' * 30)

        elif menu == '3':
            menu2 = input('ALTERAÇÃO DE DADOS\n'
                          '01-alterar senha\n'
                          '02-alterar nome de usuario\n'
                          '[outro valor]-sair\n')
            if menu2 == '1':
                ususealt = input('informe o usuario que deseja alterar a senha:').lower().strip()
                if ususealt in contas.keys():
                    print(f'usuario encontrado\n'
                          f'usuario: {ususealt}\n'
                          f'senha: {contas[ususealt]}\n')
                    senhanova = input('digite a nova senha:\n')
                    temcert = input(f'senha antiga: {contas[ususealt]}\n'
                                    f'senha nova:{senhanova}\n'
                                    'deseja mesmo alterar?\n'
                                    '1 - sim\n'
                                    '[outro valor] - não\n')
                    if temcert == '1':
                        contas[ususealt] = senhanova

                        print('senha alterada com sucesso!!\n')
                        with open("dados/rhodybots.pkl", "wb") as arq:
                            pickle.dump(contas, arq)

                    else:
                        print('senha não alterada\n')
                else:
                    print('conta não encontrada.\n')
            elif menu2 == '2':
                usualt = input('informe o usuario que deseja alterar o nick:\n').lower().strip()
                if usualt in contas.keys():
                    print(f'usuario encontrado\n'
                          f'usuario: {usualt}\n'
                          f'senha: {contas[usualt]}\n')
                    usunovo = input('digite o novo nick:\n')
                    temcert = input(f'nick antigo: {usualt}\n'
                                    f'nick novo:{usunovo}\n'
                                    'deseja mesmo alterar?\n'
                                    '1 - sim\n'
                                    '[outro valor] - não\n')
                    if temcert == '1':
                        contas[usunovo] = contas[usualt]
                        del contas[usualt]
                        print('conta alterada com sucesso!!\n')
                        with open("dados/rhodybots.pkl", "wb") as arq:
                            pickle.dump(contas, arq)

                    else:
                        print('conta não alterada\n')
                else:
                    print('conta não encontrada.\n')
        elif menu == '4':
            delcont = input('insira a conta que deseja apagar: \n')
            if delcont in contas.keys():
                print(f'conta encontrada!!\n'
                      f'usuario: {delcont}\n'
                      f'senha: {contas[delcont]}\n')

                temcert2 = input('deseja mesmo deletar?\n'
                                 '1 - sim\n'
                                 '[outro valor] - não\n')
                if temcert2 == '1':
                    del contas[delcont]
                    print('conta deletada com sucesso!!\n')
                    with open("dados/rhodybots.pkl", "wb") as arq:
                        pickle.dump(contas, arq)

                else:
                    print('conta não alterada\n')
            else:
                print('conta não encontrada')
        else:
            break


# 03-pack de comentarios
def packcoment():
    lis = []
    try:
        arq = open("dados/packcoment.pkl", "rb")
        contas = pickle.load(arq)
        print('leu')
        arq.close()
    except:
        arq = open("dados/packcoment.pkl", "wb")
        contas = {}
        arq.close()

        print('nao leu')
    # menu
    while True:
        tit('PACKS DE COMENTARIOS')
        menu = input('''
        01 - cadastrar pack
        02 - pack cadastrados
        03 - alterar pack
        04 - deletar pack
        [outro valor] - sair   
        ''')
        if menu == '1':
            while True:
                print('CADASTRO DE PACK')
                r = input('insira o nome do pack:\n')
                contas[r] = lis[:]
                while True:
                    contas[r].append(input('insira um cometario:\n'))
                    cont1 = input('deseja continuar a cadastrar comentarios? S-[SIM],[qualquer tecla para cancelar]')
                    if cont1 not in 'Ss':
                        print('cadastro de comentario com sucesso')
                        with open("dados/packcoment.pkl", "wb") as arq:
                            pickle.dump(contas, arq)

                            break

                cont2 = input('deseja continuar a criar packs? S-[SIM],[qualquer tecla para cancelar]')
                if cont2 not in 'Ss':
                    print('cadastro de pack com sucesso')
                    with open("dados/packcoment.pkl", "wb") as arq:
                        pickle.dump(contas, arq)
                        break

        elif menu == '2':
            print('PACKS CADASTRADOS:')
            print('-' * 30)
            for user in contas.keys():
                print(f'\033[7;30;41mnome de usuario: {user}\033[m\ncomentarios: {contas[user]}')
                print('-' * 30)

        elif menu == '3':
            menu2 = input('ALTERAÇÃO DE PACK\n'
                          '01-alterar comentario\n'
                          '02-alterar nome do pack\n'
                          '03-inserir novo comentario'
                          '[outro valor]-sair\n')
            if menu2 == '1':
                ususealt = input('informe o pack que deseja alterar o comentario:').lower().strip()
                if ususealt in contas.keys():
                    print(f'pack encontrado\n'
                          f'pack: {ususealt}\n'
                          f'comentarios: {contas[ususealt]}\n')
                    senhanova = input('digite o nome do novo comentario:\n')
                    comentant = input('digite o nome do antigo comentario:\n')
                    if comentant in contas[ususealt]:
                        z = contas[ususealt].index(comentant)
                        temcert = input(f'comentario antigo: {contas[ususealt][z]}\n'
                                        f'comentario novo:{senhanova}\n'
                                        'deseja mesmo alterar?\n'
                                        '1 - sim\n'
                                        '[outro valor] - não\n')
                        if temcert == '1':
                            contas[ususealt][z] = senhanova
                            print('comentario alterado com sucesso!!\n')
                            with open("dados/packcoment.pkl", "wb") as arq:
                                pickle.dump(contas, arq)
                        else:
                            print('comentario não alterado\n')
                else:
                    print('pack não encontrado.\n')
            elif menu2 == '2':
                usualt = input('informe o pack que deseja alterar o nome:\n').lower().strip()
                if usualt in contas.keys():
                    print(f'usuario encontrado\n'
                          f'usuario: {usualt}\n'
                          f'senha: {contas[usualt]}\n')
                    usunovo = input('digite o novo nome:\n')
                    temcert = input(f'nome antigo: {usualt}\n'
                                    f'nome novo:{usunovo}\n'
                                    'deseja mesmo alterar?\n'
                                    '1 - sim\n'
                                    '[outro valor] - não\n')
                    if temcert == '1':
                        contas[usunovo] = contas[usualt]
                        del contas[usualt]
                        print('conta alterada com sucesso!!\n')
                        with open("dados/packcoment.pkl", "wb") as arq:
                            pickle.dump(contas, arq)

                    else:
                        print('nome do pack não alterado\n')
                else:
                    print('conta não encontrada.\n')
            elif menu2 == '3':
                while True:
                    packnc = input('insira o pack que deseja inserir:\n')
                    if packnc in contas.keys():
                        print('pack encontrado')
                        while True:
                            newcmt = input('digite o novo comentario que deseja inserir:\n')
                            contas[packnc].append(newcmt)
                            desc = input('deseja continuar? s -sim [outro valor] - não').lower()
                            if desc not in 's':
                                break

                    else:
                        print('pack não encontrado.')
                    tf = input('deseja continuar a inserir comentarios ?\n').lower()
                    if tf not in 's':
                        break
            elif menu2 == '4':

                packcmt = input('insira o pack que deseja apagar comentario')
                if packcmt in contas.keys():
                    print('pack encontrado.')
                    while True:

                        print(contas[packcmt])
                        apagcmt = input('insira o comentario q deseja apagar:')
                        if apagcmt in contas[packcmt]:
                            del (contas[packcmt][contas[packcmt].index(apagcmt)])
                            print('comentario apagado.')

                        else:
                            print('comentario n encontrado')
                        descs = input('deseja continuar apagando? s -sim [outro valor] - não').lower()
                        if descs not in 's':
                            with open("dados/packcoment.pkl", "wb") as arq:
                                pickle.dump(contas, arq)
                            break
                else:
                    print('pack não encontrado.')

        elif menu == '4':
            delcont = input('insira o pack que deseja apagar: \n')
            if delcont in contas.keys():
                print(f'conta encontrada!!\n'
                      f'pack: {delcont}\n'
                      f'comentarios: {contas[delcont]}\n')

                temcert2 = input('deseja mesmo deletar?\n'
                                 '1 - sim\n'
                                 '[outro valor] - não\n')
                if temcert2 == '1':
                    del contas[delcont]
                    print('pack deletada com sucesso!!\n')
                    with open("dados/packcoment.pkl", "wb") as arq:
                        pickle.dump(contas, arq)

                else:
                    print('pack não alterada\n')
            else:
                print('pack não encontrada')
        else:
            break


# 04-pack de seguidores
##01 -cadastrar seguidor
def cadseguidor(modo='criar', tipo='seguidores'):
    driver = Remote('http://localhost:4723/wd/hub',
                    {        "platformName": "android",
        "automationName": "UiAutomator2"})
    tit(f'função de xerocar no tipo {tipo} e modo {modo}')

    print(f'função de xerocar no tipo {tipo} e modo {modo}')
    ##########################arquivos#############################################
    if tipo == 'seguidores':
        perfilxerox = input('nome da conta que deseja copiar seguidores:')
    elif tipo == 'seguindo':
        perfilxerox = input('nome da conta que deseja copiar seguidores:')
    if tipo == 'like':
        perfilxerox = input('nome da conta que deseja copiar seguidores dos likes:')
        post = input('digite o link do post em que vamos copiar os seguidores')


    if dbxerox.find_one({'user': perfilxerox}):
        try:
            if dbxerox.find_one({'user': perfilxerox})[tipo]:
                print('leu')
        except:
            dbxerox.update_one({'user': perfilxerox},{'$set':{tipo:[]}}) 
            print('not read')
    else:
        dbxerox.insert_one({'user': perfilxerox,tipo:[] })


    listsegui = []

    
    

    # perfil que sera gerado lista

    


    saber = input('deseja fazer scroll automatico ou manual?\n[1]-sim\n[outro valor]-não\n')
    if saber in '1':
        # z = int(input('digite a quantidade de usuarios que a conta que vamos copiar possui(vamos tentar copiar a quantia que digitar): '))
        # entrar no insta
        if tipo == 'like':
            pesquisar(perfilxerox,driver)
        else:
            pesquisar(perfilxerox,driver)
        sleep(2)
        if tipo == 'Seguidores':
            botaoseguir = driver.find_element(By.ID,
                                               'com.instagram.android:id/row_profile_header_textview_followers_count')

        elif tipo == 'Seguindo':
            botaoseguir = driver.find_element(By.ID,
                                               'com.instagram.android:id/row_profile_header_textview_following_count')

            # elif tipo == 'like':

        botaoseguir.click()
        sleep(randint(2, 3))
        while True:
            for i in range(0, 500):
                actions = ActionChains(driver)
                actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                actions.w3c_actions.pointer_action.move_to_location(140, 570) #(479, 250)
                actions.w3c_actions.pointer_action.pointer_down()
                actions.w3c_actions.pointer_action.move_to_location(140, 200) #(479, 1932)
                actions.w3c_actions.pointer_action.release()
                actions.perform()
            k = input('deseja continuar?[1-sim]')
            if k not in '1':
                break
    while True:
        for i in range(1, 1000):
            try:
                print(f'rodada {i}')
                a = driver.find_elements('id','com.instagram.android:id/follow_list_username')
                for j in a:
                    print(f'{a.index(j)}-{j.text}')
                    if j.text in dbxerox.find_one({'user': perfilxerox})[tipo]:
                        print('usuario repetido')
                    else:
                        dbxerox.update_one({'user': perfilxerox}, {'$push': {tipo: j.text}})
                try:
                    driver.find_element('id','com.instagram.android:id/row_load_more_button').click()

                except:
                    print('não tem botão de +')

                actions = ActionChains(driver)
                actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                actions.w3c_actions.pointer_action.move_to_location(536, 1400) #(308, 1005)
                actions.w3c_actions.pointer_action.pointer_down()
                actions.w3c_actions.pointer_action.move_to_location(501, 744) #(308, 481)
                actions.w3c_actions.pointer_action.release()
                actions.perform()
                #for i in range(0, 11):
                    #try:
                       # ActionChains(driver) \
                        #    .key_down(Keys.DOWN) \
                       #     .perform()
                   # except:
                   #     print('não foi possivel subir mais')
            except:
                print('não está sendo possivel ir para a proxima rodada.')
        k = input('deseja continuar?[1-sim]')
        if k not in '1':
            break

    print('processo finalizado com sucesso!!')
 


def packsegui():
    lis = []
    try:
        arq = open("dados/listadexerox.pkl", "rb")
        contas = pickle.load(arq)
        print('leu')
        arq.close()
    except:

        contas = {}

        print('nao leu')
    
    # menu
    while True:
        tit('PACKS DE SEGUIDORES')
        menu = input('''
            01 - cadastrar pack
            02 - pack cadastrados
            03 - alterar pack
            04 - deletar pack
            [outro valor] - sair   
            ''')
        if menu == '1':
            while True:
                print('CADASTRO DE PACK')
                cadseguidor()

                cont2 = input('deseja continuar a criar packs? S-[SIM],[qualquer tecla para cancelar]')
                if cont2 not in 'Ss':
                    print('cadastro de pack com sucesso')
                    break

        elif menu == '2':
            print('PACKS CADASTRADOS:')
            print('-' * 30)
            for user in contas.keys():
                print(f'nome de usuario: {user}\n')
                print(f'existem {len(contas[user])} pessoas cadastradas nessa lista')
                print('-' * 30)

        elif menu == '3':
            menu2 = input('ALTERAÇÃO DE PACK\n'
                          '01-alterar nick de seguidor\n'
                          '02-alterar nome do pack\n'
                          '03-inserir novo seguidor'
                          '[outro valor]-sair\n')
            if menu2 == '1':
                ususealt = input('informe o pack que deseja alterar o seguidor:').lower().strip()
                if ususealt in contas.keys():
                    print(f'pack encontrado\n'
                          f'pack: {ususealt}\n'
                          f'seguidores: {contas[ususealt]}\n')
                    senhanova = input('digite o nome do novo nick:\n')
                    comentant = input('digite o nome do antigo nick:\n')
                    if comentant in contas[ususealt]:
                        z = contas[ususealt].index(comentant)
                        temcert = input(f'nick antigo: {contas[ususealt][z]}\n'
                                        f'nick novo:{senhanova}\n'
                                        'deseja mesmo alterar?\n'
                                        '1 - sim\n'
                                        '[outro valor] - não\n')
                        if temcert == '1':
                            contas[ususealt][z] = senhanova
                            print('nick alterado com sucesso!!\n')
                            with open("dados/listadexerox.pkl", "wb") as arq:
                                pickle.dump(contas, arq)
                        else:
                            print('nick não alterado\n')
                else:
                    print('pack não encontrado.\n')
            elif menu2 == '2':
                usualt = input('informe o pack que deseja alterar o nome:\n').lower().strip()
                if usualt in contas.keys():
                    print(f'usuario encontrado\n'
                          f'usuario: {usualt}\n'
                          f'seguidores: {contas[usualt]}\n')
                    usunovo = input('digite o novo nome:\n')
                    temcert = input(f'nome antigo: {usualt}\n'
                                    f'nome novo:{usunovo}\n'
                                    'deseja mesmo alterar?\n'
                                    '1 - sim\n'
                                    '[outro valor] - não\n')
                    if temcert == '1':
                        contas[usunovo] = contas[usualt]
                        del contas[usualt]
                        print('pack alterado com sucesso!!\n')
                        with open("dados/listadexerox.pkl", "wb") as arq:
                            pickle.dump(contas, arq)

                    else:
                        print('nome do pack não alterado\n')
                else:
                    print('pack não encontrado.\n')
            elif menu2 == '3':
                while True:
                    packnc = input('insira o pack que deseja inserir:\n')
                    if packnc in contas.keys():
                        print('pack encontrado')
                        cadseguidor('inserir')


                    else:
                        print('pack não encontrado.')
                    tf = input('deseja continuar a inserir seguidores ?\n').lower()
                    if tf not in 's':
                        break
            elif menu2 == '4':

                packcmt = input('insira o pack que deseja apagar seguidor')
                if packcmt in contas.keys():
                    print('pack encontrado.')
                    while True:

                        print(contas[packcmt])
                        apagcmt = input('insira o nick do seguidor q deseja apagar:')
                        if apagcmt in contas[packcmt]:
                            del (contas[packcmt][contas[packcmt].index(apagcmt)])
                            print('seguidor apagado.')

                        else:
                            print('seguidor n encontrado')
                        descs = input('deseja continuar apagando? s -sim [outro valor] - não').lower()
                        if descs not in 's':
                            with open("dados/listadexerox.pkl", "wb") as arq:
                                pickle.dump(contas, arq)
                            break
                else:
                    print('pack não encontrado.')

        elif menu == '4':
            delcont = input('insira o pack que deseja apagar: \n')
            if delcont in contas.keys():
                print(f'conta encontrada!!\n'
                      f'pack: {delcont}\n'
                      f'seguidores: {contas[delcont]}\n')

                temcert2 = input('deseja mesmo deletar?\n'
                                 '1 - sim\n'
                                 '[outro valor] - não\n')
                if temcert2 == '1':
                    del contas[delcont]
                    print('pack deletada com sucesso!!\n')
                    with open("dados/listadexerox.pkl", "wb") as arq:
                        pickle.dump(contas, arq)

                else:
                    print('pack não alterada\n')
            else:
                print('pack não encontrada')
        else:
            break


def listbranca():
    lis = []
    try:
        arq = open("dados/listbranca.pkl", "rb")
        contas = pickle.load(arq)
        print('leu')
        arq.close()
    except:
        arq = open("dados/listbranca.pkl", "wb")
        contas = {}
        arq.close()

        print('nao leu')
    # menu
    while True:
        tit('LISTA BRANCA')
        menu = input('''
        01 - cadastrar lista
        02 - lista cadastrados
        03 - alterar lista
        04 - deletar lista
        [outro valor] - sair   
        ''')
        if menu == '1':
            while True:
                print('CADASTRO DE LISTA')
                r = input('insira o nome da lista:\n')
                contas[r] = lis[:]
                while True:
                    contas[r].append(input('insira um user:\n'))
                    cont1 = input('deseja continuar a cadastrar users? S-[SIM],[qualquer tecla para cancelar]')
                    if cont1 not in 'Ss':
                        print('cadastro de user com sucesso')
                        with open("dados/listbranca.pkl", "wb") as arq:
                            pickle.dump(contas, arq)

                            break

                cont2 = input('deseja continuar a criar listas? S-[SIM],[qualquer tecla para cancelar]')
                if cont2 not in 'Ss':
                    print('cadastro de lista com sucesso')
                    with open("dados/listbranca.pkl", "wb") as arq:
                        pickle.dump(contas, arq)
                        break

        elif menu == '2':
            print('LISTAS CADASTRADAS:')
            print('-' * 30)
            for user in contas.keys():
                print(f'nome da lista: {user}\nusuarios: {contas[user]}')
                print('-' * 30)

        elif menu == '3':
            menu2 = input('ALTERAÇÃO DE LISTA\n'
                          '01-alterar usuario\n'
                          '02-alterar nome da lista\n'
                          '03-inserir novo user\n'
                          '[outro valor]-sair\n')
            if menu2 == '1':
                ususealt = input('informe a lista que deseja alterar o user:').lower().strip()
                if ususealt in contas.keys():
                    print(f'lista encontrada\n'
                          f'lista: {ususealt}\n'
                          f'users: {contas[ususealt]}\n')
                    senhanova = input('digite o nome do novo user:\n')
                    comentant = input('digite o nome do antigo user:\n')
                    if comentant in contas[ususealt]:
                        z = contas[ususealt].index(comentant)
                        temcert = input(f'user antigo: {contas[ususealt][z]}\n'
                                        f'user novo:{senhanova}\n'
                                        'deseja mesmo alterar?\n'
                                        '1 - sim\n'
                                        '[outro valor] - não\n')
                        if temcert == '1':
                            contas[ususealt][z] = senhanova
                            print('user alterado com sucesso!!\n')
                            with open("dados/listbranca.pkl", "wb") as arq:
                                pickle.dump(contas, arq)
                        else:
                            print('user não alterado\n')
                else:
                    print('lista não encontrado.\n')
            elif menu2 == '2':
                usualt = input('informe a lista que deseja alterar o nome:\n').lower().strip()
                if usualt in contas.keys():
                    print(f'usuario encontrado\n'
                          f'lista: {usualt}\n'
                          f'users: {contas[usualt]}\n')
                    usunovo = input('digite o novo nome:\n')
                    temcert = input(f'nome antigo: {usualt}\n'
                                    f'nome novo:{usunovo}\n'
                                    'deseja mesmo alterar?\n'
                                    '1 - sim\n'
                                    '[outro valor] - não\n')
                    if temcert == '1':
                        contas[usunovo] = contas[usualt]
                        del contas[usualt]
                        print('conta alterada com sucesso!!\n')
                        with open("dados/listbranca.pkl", "wb") as arq:
                            pickle.dump(contas, arq)

                    else:
                        print('nome da lista não alterado\n')
                else:
                    print('lista não encontrada.\n')
            elif menu2 == '3':
                while True:
                    packnc = input('insira a lista que deseja inserir:\n')
                    if packnc in contas.keys():
                        print('lista encontrada')
                        while True:
                            newcmt = input('digite o novo user que deseja inserir:\n')
                            contas[packnc].append(newcmt)
                            desc = input('deseja continuar? s -sim [outro valor] - não').lower()
                            if desc not in 's':
                                break

                    else:
                        print('lista não encontrada.')
                    tf = input('deseja continuar a inserir users ?\n').lower()
                    if tf not in 's':
                        break
            elif menu2 == '4':

                packcmt = input('insira a lista que deseja apagar comentario')
                if packcmt in contas.keys():
                    print('lista encontrada.')
                    while True:

                        print(contas[packcmt])
                        apagcmt = input('insira o user q deseja apagar:')
                        if apagcmt in contas[packcmt]:
                            del (contas[packcmt][contas[packcmt].index(apagcmt)])
                            print('user apagado.')

                        else:
                            print('user n encontrado')
                        descs = input('deseja continuar apagando? s -sim [outro valor] - não').lower()
                        if descs not in 's':
                            with open("dados/listbranca.pkl", "wb") as arq:
                                pickle.dump(contas, arq)
                            break
                else:
                    print('lista não encontrada.')

        elif menu == '4':
            delcont = input('insira a lista que deseja apagar: \n')
            if delcont in contas.keys():
                print(f'conta encontrada!!\n'
                      f'lista: {delcont}\n'
                      f'usuarios: {contas[delcont]}\n')

                temcert2 = input('deseja mesmo deletar?\n'
                                 '1 - sim\n'
                                 '[outro valor] - não\n')
                if temcert2 == '1':
                    del contas[delcont]
                    print('lista deletada com sucesso!!\n')
                    with open("dados/listbranca.pkl", "wb") as arq:
                        pickle.dump(contas, arq)

                else:
                    print('lista não alterada\n')
            else:
                print('lista não encontrada')
        else:
            break


def packseguindo():
    lis = []
    try:
        arq = open("dados/following.pkl", "rb")
        contas = pickle.load(arq)
        print('leu')
        arq.close()
    except:
        arq = open("dados/following.pkl", "wb")
        contas = {}
        arq.close()
        print('nao leu')
        xerox = {}
    # menu
    while True:
        tit('PACKS DE FOLLOWING')
        menu = input('''
            01 - cadastrar pack
            02 - pack cadastrados
            03 - alterar pack
            04 - deletar pack
            [outro valor] - sair   
            ''')
        if menu == '1':
            while True:
                print('CADASTRO DE PACK')
                cadseguidor('criar', 'seguindo')

                cont2 = input('deseja continuar a criar packs? S-[SIM],[qualquer tecla para cancelar]')
                if cont2 not in 'Ss':
                    print('cadastro de pack com sucesso')
                    break

        elif menu == '2':
            print('PACKS CADASTRADOS:')
            print('-' * 30)
            for user in contas.keys():
                print(f'ao todo são {len(contas[user])} pessoas cadastrados nesse pack')
                print(f'nome de usuario: {user}\nseguindo: {contas[user]}')
                print('-' * 30)

        elif menu == '3':
            menu2 = input('ALTERAÇÃO DE PACK\n'
                          '01-alterar nick de seguindo\n'
                          '02-alterar nome do pack\n'
                          '03-inserir novo user'
                          '[outro valor]-sair\n')
            if menu2 == '1':
                ususealt = input('informe o pack que deseja alterar o user que está seguindo:').lower().strip()
                if ususealt in contas.keys():
                    print(f'pack encontrado\n'
                          f'pack: {ususealt}\n'
                          f'seguindo: {contas[ususealt]}\n')
                    senhanova = input('digite o nome do novo nick:\n')
                    comentant = input('digite o nome do antigo nick:\n')
                    if comentant in contas[ususealt]:
                        z = contas[ususealt].index(comentant)
                        temcert = input(f'nick antigo: {contas[ususealt][z]}\n'
                                        f'nick novo:{senhanova}\n'
                                        'deseja mesmo alterar?\n'
                                        '1 - sim\n'
                                        '[outro valor] - não\n')
                        if temcert == '1':
                            contas[ususealt][z] = senhanova
                            print('nick alterado com sucesso!!\n')
                            with open("dados/following.pkl", "wb") as arq:
                                pickle.dump(contas, arq)
                        else:
                            print('nick não alterado\n')
                else:
                    print('pack não encontrado.\n')
            elif menu2 == '2':
                usualt = input('informe o pack que deseja alterar o nome:\n').lower().strip()
                if usualt in contas.keys():
                    print(f'usuario encontrado\n'
                          f'usuario: {usualt}\n'
                          f'seguindo: {contas[usualt]}\n')
                    usunovo = input('digite o novo nome:\n')
                    temcert = input(f'nome antigo: {usualt}\n'
                                    f'nome novo:{usunovo}\n'
                                    'deseja mesmo alterar?\n'
                                    '1 - sim\n'
                                    '[outro valor] - não\n')
                    if temcert == '1':
                        contas[usunovo] = contas[usualt]
                        del contas[usualt]
                        print('pack alterado com sucesso!!\n')
                        with open("dados/following.pkl", "wb") as arq:
                            pickle.dump(contas, arq)

                    else:
                        print('nome do pack não alterado\n')
                else:
                    print('pack não encontrado.\n')
            elif menu2 == '3':
                while True:
                    packnc = input('insira o pack que deseja inserir:\n')
                    if packnc in contas.keys():
                        print('pack encontrado')
                        while True:
                            cadseguidor('inserir', 'seguindo')

                            cont2 = input('deseja continuar a criar packs? S-[SIM],[qualquer tecla para cancelar]')
                            if cont2 not in 'Ss':
                                print('cadastro de pack com sucesso')
                                break



                    else:
                        print('pack não encontrado.')
                    tf = input('deseja continuar a inserir following ?\n').lower()
                    if tf not in 's':
                        break
            elif menu2 == '4':

                packcmt = input('insira o pack que deseja apagar following')
                if packcmt in contas.keys():
                    print('pack encontrado.')
                    while True:

                        print(contas[packcmt])
                        apagcmt = input('insira o nick do following q deseja apagar:')
                        if apagcmt in contas[packcmt]:
                            del (contas[packcmt][contas[packcmt].index(apagcmt)])
                            print('seguidor apagado.')

                        else:
                            print('seguidor n encontrado')
                        descs = input('deseja continuar apagando? s -sim [outro valor] - não').lower()
                        if descs not in 's':
                            with open("dados/following.pkl", "wb") as arq:
                                pickle.dump(contas, arq)
                            break
                else:
                    print('pack não encontrado.')

        elif menu == '4':
            delcont = input('insira o pack que deseja apagar: \n')
            if delcont in contas.keys():
                print(f'conta encontrada!!\n'
                      f'pack: {delcont}\n'
                      f'seguindo: {contas[delcont]}\n')

                temcert2 = input('deseja mesmo deletar?\n'
                                 '1 - sim\n'
                                 '[outro valor] - não\n')
                if temcert2 == '1':
                    del contas[delcont]
                    print('pack deletada com sucesso!!\n')
                    with open("dados/following.pkl", "wb") as arq:
                        pickle.dump(contas, arq)

                else:
                    print('pack não alterada\n')
            else:
                print('pack não encontrada')
        else:
            break


def deseguir():
    dicwhite = {}
    listabranca = ''
    dicwhite[listabranca] = 0
    dicarq = open('dados/clientesrengage.pkl', 'rb')
    cliente = pickle.load(dicarq)
    dicarq.close()

    pack = open('dados/following.pkl', 'rb')
    packs = pickle.load(pack)
    pack.close()

    url = 'https://www.instagram.com/'
    browser = Firefox()

    ############################################ cliente e pack que vai ser trabalhado #############################################
    while True:
        x = input('digite o nome do cliente que vamos trabalhar: ')
        if x in cliente.keys():
            print('cliente encontrado')

        else:
            print('cliente não encontrado digite novamente.')
            continue

        if x in packs.keys():
            print('encontramos tambem o pack que este cliente está seguindo!!')
            break
        else:
            print('não encontramos nenhum pack registrado nesse nome.')
    ##################################lista branca########################################################
    while True:
        s = int(input('conta possui lista branca?'
                      '\n01 - sim (outros valores) - não'))
        if s != 1:
            break
        else:
            listwhite = open('dados/listbranca.pkl', 'rb')
            dicwhite = pickle.load(listwhite)
            listwhite.close()
            listabranca = x
            if listabranca in dicwhite.keys():
                print(f'encontramos a lista branca com {len(dicwhite[listabranca])} pessoas cadastrada nelas')
                break
            else:
                print('lista não encontrada,tente de novo')

    try:
        arq = open("dados/listajadeixoudeseguir.pkl", "rb")
        contas = pickle.load(arq)
        print('leu')
        arq.close()
    except:
        arq = open("dados/listajadeixoudeseguir.pkl", "wb")
        contas = {}
        print('nao leu')
        arq.close()
        list = []
        contas[x] = list[:]

    ######################################### quantidade que vamos dar unfollow:######################################################################
    y = int(input('digite o numero de pessoas que vamos dar unfollow '))

    # logarinsta
    try:
        browser.get(url)
        sleep(randint(2, 4))
        nick = browser.find_element(By.CSS_SELECTOR,
            'div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
        nick.click()
        nick.clear()
        nick.send_keys(x)
        sleep(randint(1, 4))
        senha = browser.find_element(By.CSS_SELECTOR,
            'div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
        senha.click()
        senha.clear()
        senha.send_keys(cliente[x])
        sleep(randint(1, 4))
        botao = browser.find_element(By.CSS_SELECTOR, '.L3NKy')
        botao.click()
    except:
        print('houve algum erro ao tentar logar. reiniciando a pagina.')
        browser = entrardenovo(browser, url, x, cliente[x], True)

    # teste de senha ou login incorreto
    try:
        une = browser.find_element(By.CSS_SELECTOR,'.eiCW-')
        print(une)
        print('usuario existe ou senha incorreta')
        browser = entrardenovo(browser, url, x, cliente[x], True)


    except:
        print('aguarde...')

    # teste se conta realmente entrou
    try:
        sleep(3)
        nick = browser.find_element(By.CSS_SELECTOR,
            'div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
        nick.click()
        nick.clear()
        nick.send_keys(x)
        sleep(randint(1, 4))
        senha = browser.find_element(By.CSS_SELECTOR,
            'div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
        senha.click()
        senha.clear()
        senha.send_keys(cliente[x])
        sleep(randint(1, 4))
        botao = browser.find_element(By.CSS_SELECTOR,'.L3NKy > div:nth-child(1)')
        botao.click()

    except:
        print('perfil já logado')
    #######################parametro para saber se já deixou de seguir tudo################################################
    quantlist = len(packs[x])
    # seguirconta
    cont = 0
    unf = 0
    while unf <= y:
        try:
            if packs[x][cont] not in dicwhite[listabranca]:
                browser.get('https://www.instagram.com/' + packs[x][cont] + '/')
                sleep(randint(2, 3))
                try:
                    botaodseguir = browser.find_element(By.XPATH,
                                                        '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button/div/div/span')
                except:
                    try:
                        botaodseguir = browser.find_element(By.CSS_SELECTOR, '.glyphsSpriteFriend_Follow')
                    except:
                        botaodseguir = browser.find_element(By.XPATH,
                                                            '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button/div')

                if botaodseguir.text != 'Seguir':
                    botaodseguir.click()
                    sleep(2)
                    try:
                        confirmunf = browser.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[1]')
                        confirmunf.click()
                        print(f'usuario {packs[x][cont]} acabou de levar unfollow...')
                    except:
                        print(f'usuario {packs[x][cont]} , não foi possiveel confirmar o unfollow')

                    try:  # tentativa caso de erro ao bloquear

                        confirmabotao = browser.find_element(By.XPATH,
                                                             '/html/body/div[6]/div/div/div/div[2]/button[2]')
                        confirmabotao.click()
                        print('houve algum erro ao deixar de seguir usuario. tente mais tarde!!')
                        browser.close()
                        break


                    except:
                        print('unfollow com sucesso')  # seguidores
                        cont += 1
                        sleep(1)
                        botaodseguir = browser.find_element(By.XPATH,
                                                            '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button/div')
                        if botaodseguir.text == 'Seguir':
                            unf += 1
                        print(f'{unf} pessoas deixadas de seguir!!')
                        contas[x].append(packs[x][cont])
                        del (packs[x][cont])
                        with open("dados/following.pkl", "wb") as arq:
                            pickle.dump(packs, arq)
                        with open("dados/listajadeixoudeseguir.pkl", "wb") as arq:
                            pickle.dump(contas, arq)
                            sleep(2)


                else:
                    print('conta já levou unfollow')
                    contas[x].append(packs[x][cont])
                    with open("dados/listajadeixoudeseguir.pkl", "wb") as arq:
                        pickle.dump(contas, arq)
                    del (packs[x][cont])
                    with open("dados/following.pkl", "wb") as arq:
                        pickle.dump(packs, arq)

                    cont += 1



            else:
                cont += 1
        except:
            print('erro nessa conta,vamos para a proxima')
            cont += 1

        if cont >= quantlist:
            break


def packporlike():
    lis = []
    try:
        arq = open("dados/listseglike.pkl", "rb")
        contas = pickle.load(arq)
        print('leu')
        arq.close()
    except:
        arq = open("dados/listseglike.pkl", "wb")
        contas = {}
        arq.close()
        print('nao leu')
    # menu
    while True:
        tit('PACKS DE SEGUIDORES POR LIKES')
        menu = input('''
            01 - cadastrar pack
            02 - pack cadastrados
            03 - alterar pack
            04 - deletar pack
            [outro valor] - sair   
            ''')
        if menu == '1':
            while True:
                print('CADASTRO DE PACK')
                cadseguidor(modo='criar', tipo='like')

                cont2 = input('deseja continuar a criar packs? S-[SIM],[qualquer tecla para cancelar]')
                if cont2 not in 'Ss':
                    print('cadastro de pack com sucesso')
                    break

        elif menu == '2':
            print('PACKS CADASTRADOS:')
            print('-' * 30)
            for user in contas.keys():
                print(f'existem {len(contas[user])} pessoas cadastradas nessa lista')
                print(f'nome de usuario: {user}\nseguidores: {contas[user]}')
                print('-' * 30)

        elif menu == '3':
            menu2 = input('ALTERAÇÃO DE PACK\n'
                          '01-alterar nick de seguidor\n'
                          '02-alterar nome do pack\n'
                          '03-inserir novo seguidor'
                          '[outro valor]-sair\n')
            if menu2 == '1':
                ususealt = input('informe o pack que deseja alterar o seguidor:').lower().strip()
                if ususealt in contas.keys():
                    print(f'pack encontrado\n'
                          f'pack: {ususealt}\n'
                          f'seguidores: {contas[ususealt]}\n')
                    senhanova = input('digite o nome do novo nick:\n')
                    comentant = input('digite o nome do antigo nick:\n')
                    if comentant in contas[ususealt]:
                        z = contas[ususealt].index(comentant)
                        temcert = input(f'nick antigo: {contas[ususealt][z]}\n'
                                        f'nick novo:{senhanova}\n'
                                        'deseja mesmo alterar?\n'
                                        '1 - sim\n'
                                        '[outro valor] - não\n')
                        if temcert == '1':
                            contas[ususealt][z] = senhanova
                            print('nick alterado com sucesso!!\n')
                            with open("dados/listseglike.pkl", "wb") as arq:
                                pickle.dump(contas, arq)
                        else:
                            print('nick não alterado\n')
                else:
                    print('pack não encontrado.\n')
            elif menu2 == '2':
                usualt = input('informe o pack que deseja alterar o nome:\n').lower().strip()
                if usualt in contas.keys():
                    print(f'usuario encontrado\n'
                          f'usuario: {usualt}\n'
                          f'seguidores: {contas[usualt]}\n')
                    usunovo = input('digite o novo nome:\n')
                    temcert = input(f'nome antigo: {usualt}\n'
                                    f'nome novo:{usunovo}\n'
                                    'deseja mesmo alterar?\n'
                                    '1 - sim\n'
                                    '[outro valor] - não\n')
                    if temcert == '1':
                        contas[usunovo] = contas[usualt]
                        del contas[usualt]
                        print('pack alterado com sucesso!!\n')
                        with open("dados/listseglike.pkl", "wb") as arq:
                            pickle.dump(contas, arq)

                    else:
                        print('nome do pack não alterado\n')
                else:
                    print('pack não encontrado.\n')
            elif menu2 == '3':
                while True:
                    packnc = input('insira o pack que deseja inserir:\n')
                    if packnc in contas.keys():
                        print('pack encontrado')
                        cadseguidor(modo='inserir', tipo='like')


                    else:
                        print('pack não encontrado.')
                    tf = input('deseja continuar a inserir seguidores ?\n').lower()
                    if tf not in 's':
                        break
            elif menu2 == '4':

                packcmt = input('insira o pack que deseja apagar seguidor')
                if packcmt in contas.keys():
                    print('pack encontrado.')
                    while True:

                        print(contas[packcmt])
                        apagcmt = input('insira o nick do seguidor q deseja apagar:')
                        if apagcmt in contas[packcmt]:
                            del (contas[packcmt][contas[packcmt].index(apagcmt)])
                            print('seguidor apagado.')

                        else:
                            print('seguidor n encontrado')
                        descs = input('deseja continuar apagando? s -sim [outro valor] - não').lower()
                        if descs not in 's':
                            with open("dados/listseglike.pkl", "wb") as arq:
                                pickle.dump(contas, arq)
                            break
                else:
                    print('pack não encontrado.')

        elif menu == '4':
            delcont = input('insira o pack que deseja apagar: \n')
            if delcont in contas.keys():
                print(f'conta encontrada!!\n'
                      f'pack: {delcont}\n'
                      f'seguidores: {contas[delcont]}\n')

                temcert2 = input('deseja mesmo deletar?\n'
                                 '1 - sim\n'
                                 '[outro valor] - não\n')
                if temcert2 == '1':
                    del contas[delcont]
                    print('pack deletada com sucesso!!\n')
                    with open("dados/listseglike.pkl", "wb") as arq:
                        pickle.dump(contas, arq)

                else:
                    print('pack não alterada\n')
            else:
                print('pack não encontrada')
        else:
            break
