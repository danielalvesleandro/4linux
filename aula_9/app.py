import threading

import modules.banco as banco

if __name__ '__main__':             # 
    usuario = input('Digite seu nick: ')
    try:
        f = threading.Thread(target=banco.select)
        f.start()
    except Exception as err:
        print('Falha ao criar thread: {}'.format(err))
    
    while f.isAlive:
        mensagem = input()
        banco.cadastrar(usuario, mensagem)