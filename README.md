
# EX 09 Smarthis

## Funcionalidades

- Carregar um template de e-mail em HTML a partir de um arquivo.
- Enviar relatórios sobre notas fiscais, incluindo:
  - Total de notas processadas.
  - Notas acima de R$ 5.000.
  - Quantidade de notas com valor zerado.
- Incluir notas fiscais em um banco de dados (simulação).

## Requisitos

Antes de executar o script, você precisará instalar as seguintes bibliotecas:

- `smtplib`: biblioteca padrão do Python para enviar e-mails.
- `email`: biblioteca padrão do Python para construir e-mails.
- `sqlite3`: biblioteca padrão do Python para interagir com bancos de dados SQLite.

Não é necessário instalar essas bibliotecas com pip, pois elas já vêm com a instalação do Python. No entanto, você deve garantir que sua versão do Python é compatível.

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/JoseGuilhermeLima/rpa_smarthis_ex09/
   cd rpa_smarthis_ex09
   ```
## Como Usar

1. Abra o arquivo Python principal.
2. Execute o script:

   ```bash
   python main.py
   ```

3. Siga as instruções na tela para inserir seu e-mail, senha, servidor SMTP e porta.

## Estrutura do Código

### Classes

- **Email**: Classe responsável por gerenciar a configuração e o envio de e-mails.
- **BancoDeDados**: Classe responsável pelo Banco de Dados do nosso RPA.

### Métodos

- **Email**:
  - `__init__`: Inicializa a classe com as configurações de e-mail.
  - `carregar_html_de_arquivo`: Carrega um template HTML a partir de um arquivo.
  - `enviar_email`: Envia um e-mail com o corpo e assunto especificados.

- **BancoDeDados**:
  - `__init__`: Inicializa a classe BancoDeDados.
    - **Parâmetros**:
      - `arg_strDBName` (str): Nome do arquivo do banco de dados SQLite.
  - `conectar`: Função responsável por conectar com o banco de dados.
  - `incluir_nota`: Função responsável por inserir uma nota fiscal no banco de dados.
    - **Parâmetros**:
      - `arg_dictNota` (dict): Dicionário da classe NotaFiscal.


