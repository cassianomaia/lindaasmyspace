# Projeto 1 - Sistemas Distribuidos
Esse projeto tem o objetivo de implementar um espaço persistente de dados compartilhado, nos moldes do Linda Tuplespace, com as seguintes funcionalidades:
- Operação in: Utilizada para remover uma postagem de determinado tópico
- Operação rd: Utilizada para ler as postagens de determinado usuário sobre um tópico
- Operação out: Utilizada para realizar as postagens no blog

O projeto conta também com uma api rest, permitindo assim que as mensagens sejam enviadas para o blog através de JSON.

### Utilização
Para executar o projeto você deve clonar o repositório e executar os seguintes comandos:
```sh
$ cd lindaasmyspace
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python startServer.py
```
Após esses passos você terá o servidor rodando em sua máquina local, caso queira modificar o caminho de acesso, basta alterar o arquivo ConstCS.py. Para testar o funcionamento do servidor, basta executar o comando:
```sh
$ python example.py
```

### Testando a API
Para testar a API recomendamos que você utilize algum software de teste, iremos utilizar o [Insomnia REST Client](https://insomnia.rest/).
- Em um terminal execute o seguinte comando para iniciar o servidor:
```sh
$ python startServer.py
```
- Em outro terminal execute o seguinte comando para iniciar a API:
```sh
$ python app.py
```

Agora, dentro do Insomnia os testes são feitos da seguinte forma:
- GET

- POST

- DELETE

### Organização dos arquivos
- ``/linda``: Pasta contendo os arquivos necessários para implementar o espaço de dados compartilhado, sendo eles:
        - ``init.py``:
        - ``server.py``:
        - ``utils.py``:
- ``app.py``:Arquivo contendo a especificação da API em Flask
- ``example.py``: Exemplo de publicação e leitura do espaço de dados compartilhado 
- ``startServer.py``: Arquivo de inicialização do servidor
- ``constCS.py``: Arquivo para especificar o endereço e porta do nosso servidor
----------------------------------------------------------------------
**Projeto realizado pelos alunos:**
**Cassiano Maia - 726507**
**Rodrigo Pesse de Abreu - 726588**
