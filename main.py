from SQL.database import conectar
from SQL.database import cadastrar
from SQL.database import visualizar
from time import sleep


conexao = conectar()
cursor = conexao.cursor()

print('-=' * 20)
print('CADASTRO DE PESSOAS'.center(40))
print('-=' * 20)

while True:
    print('[1] Cadastrar alguem\n[2] Visualizar pessoas cadastradas\n[3] Sair')
    sleep(0.5)
    op = str(input('O que você deseja fazer? '))
    sleep(0.5)
    print('-=' * 20)

    if op == '1':
        cadastrar(cursor,conexao)


    elif op == '2':
        visualizar(cursor)


    elif op == '3':

        break

    else:
        print('Digite uma opção válida')
        sleep(0.5)
print('PROGRAMA FINALIZADO')
print('-=' * 20)