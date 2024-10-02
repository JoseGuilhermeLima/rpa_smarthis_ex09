import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email:
    
    def __init__(self, arg_strEmailServerSmtp:str, arg_intEmailPortaSmtp:int, arg_strUsuario:str, arg_strSenha:str=None) -> None:
        """
        Realiza as configuracoes de email que fica atrelada a classe
        
        Parâmetros:
            - arg_strEmailServerSmtp (str): endereço do servidor SMTP.
            - arg_intEmailPortaSmtp (int): porta do servidor SMTP.
            - arg_strUsuario (str): nome de usuário para autenticação.
            - arg_strSenha (str): senha para autenticação.
        """
        
        self.var_strEmailServerSmtp = arg_strEmailServerSmtp
        self.var_intEmailPortaSmtp = arg_intEmailPortaSmtp
        self.var_strUsuario = arg_strUsuario
        self.var_strSenha = arg_strSenha
        
    def carregar_html_de_arquivo(self, arg_strArquivo = 'template.txt') -> str:
            """
            Carrega o conteúdo HTML de um arquivo.

            Parâmetros:
            - arg_strArquivo(str): Caminho do arquivo que contém o HTML.

            Retorna:
            - str: Conteúdo HTML carregado do arquivo.
            """
            with open(arg_strArquivo, 'r', encoding='utf-8') as f:
                return f.read()
        
    def enviar_email(self, arg_strEnvioPara:str, arg_strAssunto:str, arg_strCorpo:str):
        """
        Envia o email inicial do robô, apenas precisando informar quem deve receber (separado por ;) e o nome do robô

        Parâmetros:
        - arg_strEnvioPara (str): destinatários separados por ';'.
        - arg_strAssunto (str): assunto do e-mail.
        - arg_strCorpo (str): corpo  do e-mail.

        Retorna:
        """
        
        #Configurando o e-mail
        var_dictMensagem =  MIMEMultipart()
        var_dictMensagem['From'] = self.var_strUsuario
        var_dictMensagem['To'] = arg_strEnvioPara
        var_dictMensagem['Subject'] = arg_strAssunto
        var_strTemplate = self.carregar_html_de_arquivo()
        var_strCorpo = var_strTemplate.replace("@texto", arg_strCorpo)
        var_dictMensagem.attach(MIMEText(var_strCorpo,'html'))
        
        # Enviando o e-mail
        try:
            var_objServer = smtplib.SMTP(self.var_strEmailServerSmtp, self.var_intEmailPortaSmtp)
            var_objServer.starttls()
            var_objServer.login(self.var_strUsuario, self.var_strSenha)
            var_objServer.sendmail(self.var_strUsuario, arg_strEnvioPara, var_dictMensagem.as_string())
            var_objServer.quit()
            print("E-mail enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar e-mail: {str(e)}")