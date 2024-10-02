import sqlite3
from datetime import datetime

class BancoDeDados:
    """
    Classe responsável pelo Banco de Dados do nosso RPA.
    """
    
    def __init__(self, arg_strDBName="notas_fiscais.db"):
        """
        Inicializa a classe BancoDeDados

        Parâmetros:
            arg_strDBName (str): Nome do arquivo do banco de dados SQLite.
        """
        self.var_strDBName = arg_strDBName

    def conectar(self):
        """
        Função responsável por conectar com o banco de dados 
        """
        return sqlite3.connect(self.var_strDBName)

    def incluir_nota(self, arg_dictNota:dict):
        """ 
        Função responsável por inserir uma NF no banco de dados
        
        Parâmetros:
        - arg_dictNota (dict) : Dicionario da classe NotaFiscal
        """
        
        var_connNFdb = self.conectar()
        cursor = var_connNFdb.cursor()
        var_strData = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        cursor.execute('''
            INSERT INTO notas_fiscais (id_nota, valor, data_hora_insercao)
            VALUES (?, ?, ?)
        ''', (arg_dictNota['id'], arg_dictNota['valor'], var_strData))
        var_connNFdb.commit()
        var_connNFdb.close()
        print(f"Incluindo nota {arg_dictNota['id']} no banco de dados com valor de R$ {arg_dictNota['valor']}")