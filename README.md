# Peewee ORM

[Wiki](https://github.com/GabrielIFPB/peewee-orm/wiki)

Peewee é um ORM simples e pequeno. Possui poucos (mas expressivos) conceitos, tornando-o fácil de aprender
e intuitivo de usar.

* Licença MIT
* Versão atual: 3.14.4
* 11 anos de história (22/12/2010)
---
* a small, expressive ORM
* python 2.7+ and 3.4+ (developed with 3.6)
* supports sqlite, mysql, postgresql and cockroachdb

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

Qualquer um dos back-ends de banco de dados relacionais comuns, como PostgreSQL, MySQL, CockroachDB e SQLite, são suportados, 
embora um ‘driver’ de banco de dados ainda seja necessário.

## Peewee field types

Os tipos de campo em um modelo Peewee definem o tipo de armazenamento do modelo. Eles são convertidos para
os tipos de coluna do banco de dados correspondentes.

Esta tabela lista os tipos de campo Peewee e os tipos de coluna SQLite, PostgreSQL e MySQL correspondentes. 

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

### Quando dev optar pelo peewee

- MVCs
- Microsserviços
- Projetos pequenos
- Quando você precisar de simplicidade
- O SQLAlchemy é muito grande
- FAAS

### Peewee model definition

No exemplo abaixo criamos uma tabela de banco de dados simples.
```python
import peewee
import datetime

db = peewee.SqliteDatabase('db.sqlite3')

class Note(peewee.Model):

    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:

        database = db
        db_table = 'nota'


Note.create_table()

note1 = Note.create(text='Fui ao cinema')
note1.save()

note2 = Note.create(text='Me exercitei pela manhã',
        created=datetime.date(2021, 10, 20))
note2.save()

note3 = Note.create(text='Indo trabalhar no meu projeto',
        created=datetime.date(2021, 10, 22))
note3.save()

note4 = Note.create(text='Assistir um filme')
note4.save()
```

O exemplo cria uma tabela de banco de dados de notas em SQLite. 

```python
db = peewee.SqliteDatabase('db.sqlite3')
```

Iniciamos um banco de dados SQLite db.sqlite3. Isso cria um arquivo test.db no sistema de arquivos.

```python
class Note(peewee.Model):
...
```

Definimos um modelo de banco de dados denominado Note. Os modelos Peewee herdam de peewee.Model.

```python
text = peewee.CharField()
created = peewee.DateField(default=datetime.date.today)
```

Especificamos os campos do modelo. Temos um CharField e um DateField. CharField é uma classe de campo para
armazenar strings. DateField é uma classe de campo para armazenamento de datas. Leva um valor padrão se não for especificado.

```python
class Meta:
    database = db
    db_table = 'notes'
```

Na classe Meta, definimos a referência ao banco de dados e o nome da tabela do banco de dados. 

```python
Note.create_table()
```

A tabela é criada a partir de um modelo com create_table ().

```python
note1 = Note.create(text='Fui ao cinema')
note1.save()
```
Criamos e salvamos uma nova instância.

# Projeto

O projeto foi feito com Python 3.8.

O objetivo é criar um sistema de notas, cada pessoa vai poder criar um grupo de notas.

Vamos precisar criar 3 tabelas:
- Pessoa
- Grupo
- Notas

### Criando tabelas

Existem 3 formas de criar tabelas com Peewee.

- Tabela
    - tabela.create_table()
- db
    - db.create_tables([A, B, C])
- Migração
    - playhouse
    - form playhouse import migrate, SchemaMigrator

## Executando projeto usando virtualenv

### Requisitos
___
- download [https://www.python.org/](https://www.python.org/).
- Download [https://pypi.org/project/virtualenv/](https://pypi.org/project/virtualenv/).
- Instalação usando pip ```pipx install virtualenv```.
- Verificar a versão ```virtualenv --help```.
- Criar um ambiente virtual ```python3 -m virtualenv venv```, antes de executar o comado escolha um local para criar a pasta do virtualenv.

### Executando o virtualenv
___

- Ativando o virtualenv
```shell
dell@dell:~$ source venv/bin/activate
(venv) dell@dell:~$
```

### Instalando dependência
___
- Instalar o Peewee ```pip install peewee```
- Você também pode usar o arquivo **_requirements_**.
- Para instalar execute o comando abaixo.

```shell
$ pip install -r requirements.txt
```
