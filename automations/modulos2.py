from pymongo import MongoClient






client =  MongoClient()
db = client['Rengage']
dbplano = db['planos']
dbcliente = db['clientes']
dbbot =db['rhobots']

#classes
class Rhobots:
    def __init__(self, user, senha, sexo,numero,email, idade):
        self.user = user
        self.senha = senha
        self.sexo = sexo
        self.idade = idade
        self.numero = numero
        self.email = email

class Planos:
    def __init__(self,nome,buscarpessoas,gerarcomentarios,gerarsave,buscarcomentarios):
        self.nome = nome
        self.buscar_pessoas = buscarpessoas
        self.gerar_comentarios = gerarcomentarios
        self.gerar_save = gerarsave
        self.buscar_comentarios = buscarcomentarios
    '''
    def cad():
        
        plan.insert_one(
            {'nome': plano.nome,
            'buscar pessoas': plano.buscar_pessoas,
            'gerar save': plano.gerar_save,
            'buscar comentarios': plano.gerar_comentarios
            }
        )
        '''

class Cliente:
    def __init__(self, nome, user, senha, email, numero, sexo, plano):
        self.nome = nome
        self.user = user
        self.senha = senha
        self.email = email
        self.numero = numero
        self.sexo = sexo
        lista_planos = ['moon', 'saturn', 'mercury', 'venus', 'jupiter']
        if plano in lista_planos:
            self.plano = plano



def cadastro_cliente():
    nome = input('insira o nome:\n')
    user = input('insira o user:\n')
    senha = input('insira a senha:\n')
    email = input('insira o email:\n')
    numero = input('insira o numero:\n')
    sexo = input('insira o sexo:\n')
    plano = input('insira o plano:\n')

    cliente = Cliente(nome,user,senha,email,numero,sexo,plano)
    dbcliente.insert_one(
    {'nome': cliente.nome,
     'user': cliente.user,
     'senha': cliente.senha,
     'numero': cliente.numero,
     'email': cliente.email,
     'sexo': cliente.sexo,
     'plano': dbplano.find_one({'nome': cliente.plano}, {'nome': 0,'buscar pessoas': 0,'gerar save': 0, 'buscar comentarios': 0})['_id']
         }
)


def editar_cliente():
    while True:
        cliente = input('qual o user do cliente você deseja editar:\n')
        if dbcliente.find_one({'user': f'{cliente}'}):
            print(dbcliente.find_one({'user': f'{cliente}'},{'_id':0}))
            print('cliente encontrado')
            break
        else:
            print('cliente não encontrado digite novamentee')
    
    while True:
        edit = input('o que você deseja editar:\n')
        if dbcliente.find_one({'user': f'{cliente}'},{'_id':0, f'{edit}':1}):
            print('dado encontrado')
            print(dbcliente.find_one({'user': f'{cliente}'},{'_id':0, f'{edit}':1}))
            break
        else:
            print('dado não encontrado digite novamentee')
    new = input(f'insira a nova informação em {edit}:\n')
    dbcliente.update_one( {'user': f'{cliente}'},{ "$set": {f"{edit}": new } } )
    print(dbcliente.find_one({'user': f'{cliente}'},{'_id':0, f'{edit}':1}))
    

def excluir_cliente():
    while True:
        cliente = input('qual o user do cliente você deseja excluir:\n')
        if dbcliente.find_one({'user': f'{cliente}'}):
            print(dbcliente.find_one({'user': f'{cliente}'},{'_id':0}))
            print('cliente encontrado')
            break
        else:
            print('cliente não encontrado digite novamentee')
    confir = input('tem certeza que deseja excluir?\ns-[sim]\nn-[não]')
    if confir == 's':
        dbcliente.delete_one({'user': f'{cliente}'})
        print('deletado.')
    else:
        print('cliente não deletado')



def cadastro_rhobot():
    user = input('insira o user:\n')
    senha = input('insira a senha:\n')
    email = input('insira o email:\n')
    numero = input('insira o numero:\n')
    sexo = input('insira o sexo:\n')
    idade = input('insira a idade:\n')

    bot = Rhobots(user,senha,sexo,numero,email,idade)
    dbbot.insert_one(
        {
     'user': bot.user,
     'senha':bot.senha,
     'numero':bot.numero,
     'email':bot.email,
     'sexo': bot.sexo,
     'idade': bot.idade
         }
    )
    

