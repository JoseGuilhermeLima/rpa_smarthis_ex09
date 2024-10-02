import random
import getpass
from classes_smarthis.BancoDeDados import BancoDeDados
from classes_smarthis.Email import Email


"""Coletar info"""
var_strUser = str(input("Digite seu e-mail: "))
var_strSenha = getpass.getpass("Digite sua senha: ")  
var_strServer = str(input("Digite o servidor SMTP: "))
var_intPorta = int(input("Digite a porta SMTP: "))
var_strDestinatario = str(input("Digite o e-mail do destinatário: "))

"""Obter as notas a serem processadas no dia e criar um array de objetos que representem essas notas fiscais."""

"""Criei uma lista de dicionários para simular. Dois exemplos de cada caso."""
var_lisNotas = [
    {"id": 1, "valor": random.randint(1000 , 5000)},
    {"id": 2, "valor": random.randint(5000 , 10000)},
    {"id": 3, "valor": 0},
    {"id": 4, "valor": random.randint(1000 , 5000)},
    {"id": 5, "valor": random.randint(5000 , 10000)},
    {"id": 6, "valor": 0}
]

"""Inicializando listas e variavel para cada tipo de notas."""

var_listAcima5000 = []
var_listAbaixo5000 =  []
var_intQtdNF0 = 0
var_intQtdNotas = len(var_lisNotas)

"""Percorrer o array de notas fiscais:"""
for var_dictNota in var_lisNotas:
    if var_dictNota["valor"] == 0:
        """Se o valor da nota for igual a zero. Incrementar a contagem de notas zeradas."""
        var_intQtdNF0 += 1
    elif var_dictNota["valor"] < 5000:
        """Se o valor da nota for menor que R$ 5.000. Adicionar a nota à lista de notas a serem incluídas no banco de dados"""
        var_listAbaixo5000.append(var_dictNota)
    else: 
        var_listAcima5000.append(var_dictNota)
        

"""Inicializando e-mail e corpo de e-mail para cada situação"""

var_clssEmail = Email(var_strServer, var_intPorta, var_strUser, var_strSenha)

#1º Corpo Qtd total de notas
var_strMsgTotal = f"""
            <h2>Relatório de Notas Fiscais</h2>
            <p>Total de notas processadas hoje: <strong>{var_intQtdNotas}</strong></p>
"""

#2º Corpo Notas > 5000
if var_listAcima5000:
    var_strNotasHtml = ""
    for var_dictNota in var_listAcima5000:
        var_strNotasHtml += f"<li>Nota ID: {var_dictNota["id"]}, Valor: R$ {var_dictNota["valor"]:,.2f}</li>"

    var_strMsgAcima = f"""
                <h2>Notas Fiscais Acima de R$ 5.000</h2>
                <ul>{var_strNotasHtml}</ul>
    """

# 3º Corpo Notas = 0
var_strMsgZeradas = f"""
            <h2>Notas com Valor Zerado</h2>
            <p>Quantidade de notas com valor igual a zero: <strong>{var_intQtdNF0}</strong></p>
"""

"""Enviar um e-mail para o centro de custo com a quantidade total de notas."""
var_clssEmail.enviar_email(var_strDestinatario, "Quantidadetotal de notas", var_strMsgTotal)

"""Enviar um e-mail para o centro de custo com as notas acima de R$ 5.000"""

var_clssEmail.enviar_email(var_strDestinatario, "Notas Acima de R$ 5.000", var_strMsgAcima)

"""Enviar um e-mail para o centro de custo com a quantidade de notas com valor igual a zero."""

var_clssEmail.enviar_email(var_strDestinatario, "Relatório de Notas Zeradas", var_strMsgZeradas)

"""Incluir no banco de dados notas menores que R$ 5.000."""

var_clssSql = BancoDeDados()
"""Loop para inclusão"""
for var_dictNota in var_listAbaixo5000:
    var_clssSql.incluir_nota(arg_dictNota=var_dictNota)