# Peewee ORM

Peewee é um ORM simples e pequeno. Possui poucos (mas expressivos) conceitos, tornando-o fácil de aprender
e intuitivo de usar.

> Mapeamento Objeto Relacional (ORM) é uma técnica de acessar um banco de dados relacional a partir
> de uma linguagem orientada a objetos. É uma abstração da API do banco de dados Python.

## O que torna o Peewee um ORM útil?

Peewee pode ser uma biblioteca mais fácil de entender do que SQLAlchemy e outros ORMs. Ele foi projetado para ser mais 
fácil de hackear e entender, semelhante ao Bottle, que é uma estrutura da ‘web’ menor em comparação
com a estrutura abrangente do Django. Se você está apenas começando com o desenvolvimento ‘web’, pode valer a pena 
usar o Peewee para seu mapeamento e operações de banco de dados, especialmente se você usar um microframework
como Flask, Bottle, FastApi entre outros.

O Peewee pode ser usado com praticamente qualquer framework ‘web’ (Embora usá-lo com Django seja atualmente 
complicado devido ao seu acoplamento ORM embutido) ou sem um framework ‘web’. No último caso, o Peewee é bom para
extrair dados de um banco de dados relacional em um script ou bloco de notas Jupyter.

Qualquer um dos back-ends de banco de dados relacionais comuns, como PostgreSQL, MySQL ou SQLite, são suportados, 
embora um ‘driver’ de banco de dados ainda seja necessário.

## Peewee field types

Field type      | SQLite   | PostgreSQl | MySQL
----------------|----------|------------|---------
CharField       | varchar  | varchar    | varchar
TextField       | text     | text       | longtext
DateTimeField   | datetime | timestamp  | datetime
IntegerField    | integer  | integer    | integer
BooleanField    | smallint | boolean    | bool
FloatField      | real     | real       | real
DoubleField     | real     | double     | double
BigIntegerField | integer  | bigint     | bigint
DecimalField    | decimal  | numeric    | numeric
PrimaryKeyField | integer  | serial     | integer
ForeignKeyField | integer  | integer    | integer
DateField       | date     | date       | date
TimeField       | time     | time       | time

## Executando projeto usando virtualenv
### Requisitos
___
- Download [https://pypi.org/project/virtualenv/](https://pypi.org/project/virtualenv/).
- Instalação usando pip ```pipx install virtualenv```.
- Verificar a versão ```virtualenv --help```.
- Criar um ambiente virtual ```python3 -m virtualenv venv```, antes de executar o comado escolha um local para criar a pasta do virtualenv.

### Executando o virtualenv
___

- Ativando o virtualenv
```
dell@dell:~$ source venv/bin/activate
(venv) dell@dell:~$
```

### Instalando dependência
___
No repositório tem um arquivo chamado **_requirements.txt_** com todas as dependências do projeto. Para instalar execute o comando abaixo.

```
$ pip install -r requirements.txt
```
