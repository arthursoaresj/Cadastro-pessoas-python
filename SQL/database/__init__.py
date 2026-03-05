import pyodbc
from time import sleep
from datetime import datetime


def conectar():
    try:
        dados_conexao = (
            'Driver={MySQL ODBC 9.6 Unicode Driver};'
            'Server=127.0.0.1; '
            'Database=pysql;'
            'UID=root;'
            'PWD=;'
            'port=3306;'
        )

        return pyodbc.connect(dados_conexao)
    except pyodbc.Error:
        print('Erro ao conectar')
        exit()


def cadastrar(cursor,conexao):
    nome = str(input('Digite o nome da pessoa: ')).capitalize()
    while True:
        nascimento = input('Digite o ano de nascimento [AAAA-MM-DD]: ')
        try:
            data_convertida = datetime.strptime(nascimento, '%Y-%m-%d')
            break
        except ValueError:
            print('Data invalida')
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
    while sexo not in ['F','M']:
        sexo = str(input('Digite o sexo [M/F]: ')).upper()

    nacionalidade = str(input('Digite o nacionalidade: ')).capitalize()
    comando = "INSERT INTO pessoas(nome,nascimento,sexo,nacionalidade) values (?,?,?,?)"
    cursor.execute(comando,(nome,nascimento,sexo,nacionalidade))
    conexao.commit()

    sleep(0.5)
    print(f'{nome} Cadastrado com sucesso')
    sleep(1)



def visualizar(cursor):
    cursor.execute("SELECT * FROM pessoas")

    for id, nome, nascimento, sexo, nacionalidade in cursor.fetchall():
        data_formatada = nascimento.strftime('%d/%m/%Y')
        print(f'{id} | {nome} | {data_formatada} | {sexo} | {nacionalidade}')
    sleep(1)
    print('-=' * 20)




