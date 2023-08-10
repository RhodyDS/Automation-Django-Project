import modulos















while True:
    # menu RENGAGE
    modulos.tit('RENGAGE SISTEM')
    menup = input('''
    01 - interação
    02 - ferramentas
    03 - relatorios
    ''')
    if menup == '1':
        while True:
            modulos.tit('INTERAÇÃO')
            menus1 = input('''
            01 - impussionar postagem
            02 - seguir
            03 - deixar de seguir
            04 - voltar
            ''')
            if menus1 == '1':
                modulos.impuspost()
            elif menus1 == '2':
                modulos.seguir()
            elif menus1 == '3':
                modulos.deseguir()
            else:
                break

    elif menup == '2':
        while True:
            modulos.tit('FERRAMENTAS')
            menus2 = input('''
            01 - clientes
            02 - rhodybots
            03 - pack de comentarios
            04 - pack de seguidores
            05 - pack seguindo
            06 - pack de seguidores por like
            07 - lista branca
            [outro valor] - voltar
            ''')
            if menus2 == '1':            
                modulos.clientes()
            elif menus2 =='2':
                modulos.rhodybots()
            elif menus2 =='3':
                modulos.packcoment()
            elif menus2 == '4':
                modulos.packsegui()
            elif menus2 == '5':
                modulos.packseguindo()
            elif menus2 == '6':
                modulos.packporlike()
            elif menus2 == '7':
                modulos.listbranca()
            else:
                break
    elif menup == '3':
        while True:
            modulos.tit('RELATORIOS')
            menus3 = input('''
            01 - ver relatorio
            02 - deletar relatorio
            03 - voltar
            ''')
    else:
        break