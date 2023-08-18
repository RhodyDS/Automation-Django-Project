from selenium.webdriver.common.by import By
import datetime
from rich import print
from .modulosmb import traterror
from pymongo import MongoClient
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()


def seguir(clientes, quantidade, pack, driver, rodd, z, dispositivo):
    driver.implicitly_wait(4)
    client = MongoClient()
    db = client["Rengage"]
    dbcliente = db["clientes"]
    dbxerox = db["packfollowers"]
    dbwork_diario = db["workday"]

    data = datetime.date.today()

    ##################### quantidade que vamos seguir:##############################
    wait = WebDriverWait(driver, 2)
    y = quantidade

    ###################### cliente que vai ser trabalhado###########################
    x = clientes
    w = pack
    quantipack = len(dbxerox.find_one({"user": w})["seguidores"])

    ############# verificanddo se já tem lista de já seguidos para usuario #########

    try:
        quanti = len(dbcliente.find_one({"user": x})["seguiu"])
        print(f"o usuario {x} já seguiu um total de {quanti} pessoas!!")
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "send_notification",
                "message": f"o usuario {x} já seguiu um total de {quanti} pessoas!!",
            },
        )
    except:
        print(f"o usuario {x} ainda não seguiu ninguem.")
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "send_notification",
                "message": f"o usuario {x} ainda não seguiu ninguem.",
            },
        )
        dbcliente.update_one({"user": x}, {"$set": {"seguiu": []}})

    ##################################seguirconta#################################################
    cont = dbwork_diario.find_one({"data": str(data)})[dispositivo]["qAtual"]
    seguiu = dbwork_diario.find_one({"data": str(data)})[dispositivo]["qAtual"]
    errolist = []
    tent = 0

    while seguiu < y:
        try:
            """if dbwork_diario.find_one({'data': str(data)})['clientes'][clientes]['fol'] >= \
                    dbplan.find_one({'_id': idplano})['buscar_pessoas']:
                print('cliente atingiu o limite diario')
                break"""
            if (
                dbxerox.find_one({"user": w})["seguidores"][cont]
                not in dbcliente.find_one({"user": x})["seguiu"]
            ):
                print(f"[on blue] usuario {cont + 1} de {quantipack} da lista[/]")
                async_to_sync(channel_layer.group_send)(
                    "notifications",
                    {
                        "type": "send_notification",
                        "message": f"usuario {cont + 1} de {quantipack} da lista",
                    },
                )

                usuario = dbxerox.find_one({"user": w})["seguidores"][cont]
                try:
                    driver.find_element(
                        by=MobileBy.ACCESSIBILITY_ID, value="Pesquisar e explorar"
                    ).click()
                    driver.find_element(
                        "id",
                        "com.instagram.android:id/action_bar_search_hints_text_layout",
                    ).click()

                    # driver.find_element(
                    #     "id", "com.instagram.android:id/action_bar_search_edit_text"
                    # ).clear()

                    driver.find_element(
                        "id", "com.instagram.android:id/action_bar_search_edit_text"
                    ).send_keys(usuario)

                except:
                    print("erro ao tentar pesquisar")
                    async_to_sync(channel_layer.group_send)(
                        "notifications",
                        {
                            "type": "send_notification",
                            "message": "erro ao tentar pesquisar",
                        },
                    )
                    try:
                        driver.find_element(
                            By.XPATH,
                            '//android.widget.Button[@content-desc="Pesquisar e explorar"]',
                        ).click()
                        driver.find_element(
                            "id", "com.instagram.android:id/action_bar_search_edit_text"
                        ).click()
                        driver.find_element(
                            "id", "com.instagram.android:id/action_bar_search_edit_text"
                        ).clear()
                        driver.find_element(
                            "id", "com.instagram.android:id/action_bar_search_edit_text"
                        ).send_keys(usuario)
                    except:
                        traterror(
                            driver,
                            "fol",
                            clientes,
                            dbcliente.find_one({"user": clientes})["senha"],
                        )
                        continue

                try:
                    perf = driver.find_element(
                        "id", "com.instagram.android:id/row_search_user_username"
                    )

                    if usuario == perf.text:
                        perf.click()
                    else:
                        print(
                            f"usuario {usuario} não encontrado. pulando para o proximo"
                        )
                        errolist.append(usuario)
                        print(f"[on red]usuarios que com erro ao achar {errolist}[/]")
                        async_to_sync(channel_layer.group_send)(
                            "notifications",
                            {
                                "type": "send_notification",
                                "message": f"usuario {usuario} não encontrado. pulando para o proximo, usuarios que com erro ao achar {errolist}",
                            },
                        )
                        cont += 1
                        continue
                except:
                    print("sem usuario para essa busca....proximo..")
                    async_to_sync(channel_layer.group_send)(
                        "notifications",
                        {
                            "type": "send_notification",
                            "message": "sem usuario para essa busca....proximo..",
                        },
                    )
                    errolist.append(usuario)
                    print(f"[on red]usuarios que com erro ao achar {errolist}[/]")
                    async_to_sync(channel_layer.group_send)(
                        "notifications",
                        {
                            "type": "send_notification",
                            "message": f"usuarios que com erro ao achar {errolist}",
                        },
                    )
                    cont += 1
                    continue

                ################ etapa do botao de seguir ######################################
                try:
                    btseguir = driver.find_element(
                        "id",
                        "com.instagram.android:id/profile_header_user_action_follow_button",
                    )
                    print(f"status: {btseguir.text}")
                    if btseguir.text == "Seguir":
                        btseguir.click()
                        print("clicado em seguir,seguido com sucesso")
                        
                        async_to_sync(channel_layer.group_send)(
                            "notifications",
                            {
                                "type": "send_notification",
                                "message": f"status: {btseguir.text},clicado em seguir, seguido com sucesso ",
                            },
                        )

                        btseguir = driver.find_element(
                            By.ID,
                            "com.instagram.android:id/profile_header_user_action_follow_button",
                        )
                        print(f"resultado:{btseguir.text}")
                        async_to_sync(channel_layer.group_send)(
                            "notifications",
                            {
                                "type": "send_notification",
                                "message": f"resultado:{btseguir.text}",
                            },
                        )
                        if btseguir.text == "Seguindo":
                            seguiu += 1
                            dbwork_diario.update_one(
                                {"data": str(data)},
                                {"$set": {dispositivo + ".qAtual": seguiu}},
                            )
                            som = (
                                dbwork_diario.find_one({"data": str(data)})["clientes"][
                                    clientes
                                ]["fol"]
                                + 1
                            )
                            dbwork_diario.update_one(
                                {"data": str(data)},
                                {"$set": {"clientes." + clientes + ".fol": som}},
                            )
                            print(
                                dbwork_diario.find_one({"data": str(data)})["clientes"][
                                    clientes
                                ]
                            )
                            async_to_sync(channel_layer.group_send)(
                                "notifications",
                                {
                                    "type": "send_notification",
                                    "message": dbwork_diario.find_one(
                                        {"data": str(data)}
                                    )["clientes"][clientes],
                                },
                            )

                            ######### ^^^^^^^ armazena a conta seguida na lista de já seguidos ^^^^^^ ######

                            ############################ etapa de dar like##################################
                            try:
                                fotos = driver.find_elements(
                                    By.CSS_SELECTOR, '[content-desc *= "linha 1"]'
                                )

                                quant = len(fotos)
                                try:
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
                                except:
                                    print("ocorreu algum erro")
                                    try:
                                        erro = driver.find_element(
                                            By.CSS_SELECTOR,
                                            '[text = "Try Again Later"]',
                                        )
                                        print("conta restringida")
                                        driver.find_element(
                                            By.CSS_SELECTOR, '[text = "OK"]'
                                        ).click()
                                    except:
                                        print("nenhuma mensagem de erro")
                                        tent += 1
                                        # driver.find_element('id','com.instagram.android:id/search_tab').click()
                                        print(f"{tent} tentativas")
                                        if tent >= 6:
                                            errolist.append(usuario)
                                            cont += 1
                                            tent = 0

                                        continue

                            except:
                                print("usuario n possui fotos")
                                async_to_sync(channel_layer.group_send)(
                                    "notifications",
                                    {
                                        "type": "send_notification",
                                        "message": f"usuario n possui fotos",
                                    },
                                )

                        ################################### etapa de sair###############################
                        print(
                            f'[on green ]rodada {rodd}° {z}°cliente:{clientes}[/]\n[on purple]:white_check_mark: {seguiu} pessoas seguidas!!TOTAL:{dbwork_diario.find_one({"data": str(data)})["clientes"][x]["fol"]}[/]'
                        )
                        async_to_sync(channel_layer.group_send)(
                            "notifications",
                            {
                                "type": "send_notification",
                                "message": f'rodada {rodd}° {z}°cliente:{clientes}\n {seguiu} pessoas seguidas!!TOTAL:{dbwork_diario.find_one({"data": str(data)})["clientes"][x]["fol"]}',
                            },
                        )
                        dbcliente.update_one(
                            {"user": x}, {"$push": {"seguiu": usuario}}
                        )
                    else:
                        dbcliente.update_one(
                            {"user": x}, {"$push": {"seguiu": usuario}}
                        )
                        print("conta já foi seguida anteriormente.")
                        async_to_sync(channel_layer.group_send)(
                            "notifications",
                            {
                                "type": "send_notification",
                                "message": "conta já foi seguida anteriormente.",
                            },
                        )

                    cont += 1

                except:
                    print("ocorreu algum erro no processo de seguir")
                    async_to_sync(channel_layer.group_send)(
                        "notifications",
                        {
                            "type": "send_notification",
                            "message": "ocorreu algum erro no processo de seguir",
                        },
                    )
                    try:
                        erro = driver.find_elements(
                            By.CSS_SELECTOR, '[text = "Try Again Later"]'
                        )
                        print("conta restringida")
                        driver.find_elements(By.CSS_SELECTOR, '[text = "OK"]').click()
                    except:
                        print("nenhuma mensagem de erro")
                        tent += 1
                        print(f"{tent} tentativas")
                        if tent >= 6:
                            errolist.append(usuario)
                            cont += 1
                            tent = 0
                        continue

            else:
                cont += 1
                tent = 0
        except:
            print("provavelmente esse pack acabou...pulando para o proximo cliente")
            break
        tent = 0
        try:
            if cont >= quantipack:
                print(dbxerox.find_one({"user": w})["seguidores"])
                print(quantipack)
                print(
                    f"esta lista de seguidores tem {quantipack} pessoas e você já chegou no fim da lista!!\ntente seguir por outra lista."
                )
                break
        except:
            print("não foi possível ver se já seguiu todo mundo.")
    print(
        f"fim do trabalho\n{seguiu} pessoas seguidas e percorreu {cont} pessoas na lista"
    )
    print(f"contas que ocorreram erro:\n{errolist}")
    saber = "s"
    if saber == "s":
        for i in errolist:
            try:
                dbxerox.update_one({"user": w}, {"$pull": {"seguidores": i}})
            except:
                print("erro ao remover usuario")
        print("contas removidas.")
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {"type": "send_notification", "message": "contas removidas."},
        )
