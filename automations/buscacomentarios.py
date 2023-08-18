from time import sleep
from selenium.webdriver.common.by import By
from random import choices, randint
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from rich import print
from .modulosmb import  pesquisar
from pymongo import MongoClient
import datetime
import random

def commentEngaging(driver, quantComment , cliente , pessoasalvas):
    print(pessoasalvas)
    data = datetime.date.today()
    client = MongoClient()
    db = client["Rengage"]
    dbwork_diario = db["workday"]

    errolist = []
    quant = 0
    repetiu = 0
    ultimo = []
    tente = 0
    jafoi = 0

    coluna = 1
    travado = 0
    tentativa = True



    packcoment = [
        "Você é uma pessoa incrível!",
        "Seu talento é inspirador.",
        "Sua generosidade não tem limites.",
        "Que Post incrível! É realmente inspirador.",
        "Simplesmente maravilhoso! Adoro como capturou esse momento.",
        "esse post está um arraso! Você tem um olhar artístico incrível.",
        "Uau! Que beleza radiante você capturou nessa imagem.",
        "Estou impressionad com esse post. Você possui um talento extraordinário.",
        "Essa imagem é espetacular! Você realmente sabe como enxergar a beleza ao seu redor.",
        "Que Post encantador! Ela transmite muita serenidade.",
        "Você está arrasando nesse post! Seu olhar é único.",
        "Que composição elegante! Você tem um olhar impecável.",
        "esse post está simplesmente deslumbrante! Você é um verdadeiro artista.",
        "Você está incrível nesse post! Adoro sua visão de mundo.",
        "Que imagem magnífica! Você capturou a essência desse momento de forma incrível.",
        "Adorei esse post! Você possui um talento único e cativante.",
        "esse post transmite uma energia positiva contagiante. Parabéns!",
        "Seu Post é pura elegância! Você tem uma percepção visual invejável.",
        "Essa imagem mostra toda a sua autenticidade. É maravilhoso ver sua criatividade.",
        "Estou sem palavras! esse post é simplesmente deslumbrante.",
        "Você tem um olhar magnético! O mundo merece ver toda a sua visão artística.",
        "esse post é simplesmente incrível! Adoro como você capturou a emoção do momento.",
        "Que imagem poderosa! Ela transmite uma história inteira.",
        "Você possui um talento extraordinário para capturar a beleza ao seu redor.",
        "esse post é tão envolvente! Ela me transporta para outro lugar.",
        "Uau! Essa imagem é impressionante. Você tem realmente mt talento.",
        "Que Post magnífico! Ela transmite uma sensação de paz e tranquilidade.",
        "Estou apaixonad por esse Post! Ela mostra uma perspectiva única.",
        "Você tem um olhar artístico incrível. Esse post é simplesmente deslumbrante.",
        "Essa imagem transmite uma energia tão positiva! Parabéns pela captura.",
        "Que Post maravilhoso! Ele desperta a minha imaginação.",
        "Você tem um talento único para encontrar beleza nas pequenas coisas. Esse Post é prova disso.",
        "esse post é simplesmente mágico! Você tem um dom para capturar momentos especiais.",
        "Que post incrível! Ele me faz querer explorar o mundo ao seu redor.",
    ]

    emoji = [
        "😊",
        "😄",
        "🥰",
        "😍",
        "🤗",
        "🌺",
        "🌼",
        "🌻",
        "💖",
        "💕",
        "💝",
        "🌟",
        "🌞",
        "🎉",
        "🎈",
        "🎁",
        "🎶",
        "🔥",
        "🙌",
        "🎊",
        "🎀",
        "💌",
        "💯",
        "✨",
        "💫",
        "🎵",
        "🌸",
        "🍀",
        "🌹",
        "😃",
        "😊",
        "😍",
        "🤩",
        "😆",
        "😁",
        "😄",
        "🥰",
        "🥳",
        "🤗",
        "🌟",
        "💖",
        "💕",
        "💝",
        "🌞",
        "🎉",
        "🎈",
        "🎶",
        "🔥",
        "🙌",
        "🎊",
        "🎀",
        "💌",
        "💯",
        "✨",
        "💫",
        "🎵",
        "🌸",
        "🍀",
        "🌹",
        "🌻",
        "🌼",
        "🌺",
        "🌷",
        "🎵",
        "🎶",
        "🎀",
        "🎊",
        "🎉",
        "💖",
        "💝",
        "💕",
        "🔥",
        "🌞",
        "🌻",
        "🌼",
        "🌸",
        "🥰",
        "😊",
        "😄",
        "😍",
    ]



    perfis = [
        "_absintra",
        "wendersonsq",
        "jeff_rodrigues.jr",
        "matheuscavalliini",
        "wellington_wallker",
        "wessthug",
        "byelsilveira",
        "dori.souz",
        "alekix_",
    ]  # perfil que será visitado



    if pessoasalvas == "n":
        dbwork_diario.update_one({"data": str(data)}, {"$set": {"pessoas_comentadas": []}})
    while tentativa:
        perfil = random.choice(perfis)

        driver.find_element("id", "com.instagram.android:id/search_tab").click()
        driver.find_element(
            "id", "com.instagram.android:id/action_bar_search_edit_text"
        ).click()
        driver.find_element(
            "id", "com.instagram.android:id/action_bar_search_edit_text"
        ).clear()
        driver.find_element(
            "id", "com.instagram.android:id/action_bar_search_edit_text"
        ).send_keys(perfil)

        try:
            sleep(2)
            perf = driver.find_elements(By.CSS_SELECTOR, "[text= " + perfil + " ]")[1]
            print(perf.text)
            if perf.text == perfil:
                perf.click()
            else:
                print(f"usuario {perfil} não encontrado. pulando para o proximo")
                errolist.append(perfil)
                print(f"[on red]usuarios que com erro ao achar {errolist}[/]")
                continue
        except:
            print("sem usuario para essa busca....proximo..")
            errolist.append(perfil)
            print(f"[on red]usuarios que com erro ao achar {errolist}[/]")
            continue
        # entrar nos perfil que comentaram sem repetir
        try:
            sleep(2)
            driver.find_element(
                By.CSS_SELECTOR,
                '[content-desc *= "linha 1, coluna ' + str(coluna) + '"]',
            ).click()
        except:
            print("não conseguimos entrar na primeira Post")
            sleep(randint(2, 3))
            try:
                driver.find_element(
                    By.CSS_SELECTOR, '[content-desc *= "linha 1, coluna 2"]'
                ).click()
            except:
                print("realmente n conseguimos")
                continue

        # entrando no post
        sleep(2)
        try:
            driver.find_element(By.CSS_SELECTOR, '[content-desc *= "Comentar"]').click()
            sleep(randint(1, 3))

        except:
            print("erro ao entrar nos comentarios")
            continue

        while quant < quantComment:
            if tente == 5:
                break
            for n in range(1, 11):
                try:
                    a = driver.find_elements(
                        "id", "com.instagram.android:id/row_comment_textview_comment"
                    )[n]
                    b = a.find_element(
                        By.CLASS_NAME, "android.widget.Button"
                    ).get_attribute("content-desc")
                    print(b)

                    if (
                        b in ultimo
                        or b
                        in dbwork_diario.find_one({"data": str(data)})[
                            "pessoas_comentadas"
                        ]
                    ):
                        print("usuario já comentado antes")
                        print(f"repetiu {repetiu} vezes")
                        repetiu += 1
                        if repetiu >= 9:
                            try:
                                a = driver.find_element(
                                    "id",
                                    "com.instagram.android:id/row_load_more_button",
                                ).click()
                            except:
                                print("não tem botão de +")

                            actions = ActionChains(driver)
                            actions.w3c_actions = ActionBuilder(
                                driver,
                                mouse=PointerInput(interaction.POINTER_TOUCH, "touch"),
                            )
                            actions.w3c_actions.pointer_action.move_to_location(
                                308, 1090
                            )
                            actions.w3c_actions.pointer_action.pointer_down()
                            actions.w3c_actions.pointer_action.move_to_location(
                                308, 611
                            )
                            actions.w3c_actions.pointer_action.release()
                            actions.perform()
                            tente += 1
                            print(f"{tente} tentativas")
                            if tente >= 20:
                                driver.back()
                                pesquisar(random.choice(perfis), driver)
                                sleep(randint(2, 3))
                                driver.find_element(
                                    By.CSS_SELECTOR,
                                    '[content-desc *= "linha 1, coluna"'
                                    + str(coluna + 1)
                                    + "]",
                                ).click()
                                sleep(0.5)
                                driver.find_element(
                                    By.CSS_SELECTOR, '[content-desc *= "Comentar"]'
                                ).click()
                                tente = 0
                                continue
                        continue
                    elif b == perfil:
                        print("usuario é o dono do post")
                        ultimo.append(b)
                        continue
                    elif b == cliente:
                        print("usuario é o cliente")
                        ultimo.append(b)
                        continue

                    ultimo.append(b)
                    # driver.find_elements('id','com.instagram.android:id/row_comment_textview_comment')[n].click()
                    a.find_element(By.CLASS_NAME, "android.widget.Button").click()
                    repetiu = 0
                    tente = 0
                    travado = 0
                except:
                    print("erro em tentar achar quem comentou")
                    try:
                        a = driver.find_element(
                            "id", "com.instagram.android:id/row_load_more_button"
                        )
                        a.find_element_by_xpath("//android.widget.ImageView").click()
                    except:
                        print("não tem botão de +")
                        travado += 1
                        if travado >= 5:
                            driver.back()
                            driver.back()
                            if jafoi == 1:
                                driver.find_element(
                                    "id", "com.instagram.android:id/search_tab"
                                ).click()
                                driver.find_element(
                                    "id",
                                    "com.instagram.android:id/action_bar_search_edit_text",
                                ).click()
                                # ocutec(driver)
                                driver.find_element(
                                    "id",
                                    "com.instagram.android:id/action_bar_search_edit_text",
                                ).clear()
                                driver.find_element(
                                    "id",
                                    "com.instagram.android:id/action_bar_search_edit_text",
                                ).send_keys(perfil)
                                sleep(2)
                                perf = driver.find_elements(
                                    By.CSS_SELECTOR, "[text= " + perfil + " ]"
                                )[1]
                                perf.click()
                                perfil = random.choice(perfis)
                            driver.find_element(
                                By.CSS_SELECTOR, '[content-desc *= "linha 1, coluna 3"]'
                            ).click()
                            sleep(0.5)
                            driver.find_element(
                                By.CSS_SELECTOR, '[content-desc *= "Comentar"]'
                            ).click()
                            travado = 0
                            jafoi = 1
                            continue
                    actions = ActionChains(driver)
                    actions.w3c_actions = ActionBuilder(
                        driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch")
                    )
                    actions.w3c_actions.pointer_action.move_to_location(308, 1090)
                    actions.w3c_actions.pointer_action.pointer_down()
                    actions.w3c_actions.pointer_action.move_to_location(308, 611)
                    actions.w3c_actions.pointer_action.release()
                    actions.perform()
                    n = 1
                    continue
                sleep(randint(1, 3))
                try:
                    try:
                        driver.find_element(
                            By.CSS_SELECTOR, '[content-desc *= "linha 1, coluna 1"]'
                        ).click()
                    except:
                        driver.back()
                        sleep(1)
                        continue

                    sleep(randint(1, 3))
                    try:
                        driver.find_element(
                            By.CSS_SELECTOR, '[content-desc *= "Comentar"]'
                        ).click()
                    except:
                        try:
                            actions = ActionChains(driver)
                            actions.w3c_actions = ActionBuilder(
                                driver,
                                mouse=PointerInput(interaction.POINTER_TOUCH, "touch"),
                            )
                            actions.w3c_actions.pointer_action.move_to_location(
                                308, 900
                            )
                            actions.w3c_actions.pointer_action.pointer_down()
                            actions.w3c_actions.pointer_action.move_to_location(
                                308, 611
                            )
                            actions.w3c_actions.pointer_action.release()
                            actions.perform()
                            driver.find_element(
                                By.CSS_SELECTOR, '[content-desc *= "Comentar"]'
                            ).click()
                        except:
                            print("erro ao achar botão comentar")
                            for s in range(2):
                                driver.back()
                                sleep(1)
                            continue

                    sleep(randint(1, 3))
                    addcom = driver.find_element(
                        "id", "com.instagram.android:id/layout_comment_thread_edittext"
                    )
                    addcom.click()
                    sleep(randint(1, 3))
         
                    for j in range(3):
                        """if j == 2:
                            numemoji = randint(1, 2)
                            if numemoji == 1:
                                addcom.send_keys('retribui por gentileza', choices(emoji))
                            else:
                                addcom.send_keys('retribui por gentileza', choices(emoji), choices(emoji))
                        else:"""
                        numemoji = randint(1, 2)
                        if numemoji == 1:
                            addcom.send_keys(choices(packcoment), choices(emoji))
                        else:
                            addcom.send_keys(
                                choices(packcoment), choices(emoji), choices(emoji)
                            )
                        sleep(randint(3, 5))
                        driver.find_element(
                            "id",
                            "com.instagram.android:id/layout_comment_thread_post_button",
                        ).click()
                        repetiu = 0
                        tente = 0
                    quant += 1
                    print(f"{quant} pessoas comentadas")
                    dbwork_diario.update_one(
                        {"data": str(data)}, {"$push": {"pessoas_comentadas": b}}
                    )

                except:
                    print("erro ao comentar na Post de usuario")
                for s in range(3):
                    driver.back()
 
        jafoi = 0
        tentativa = False
        driver.back()

