
from datetime import datetime
from peewee import (
	SqliteDatabase, Model, CharField, ForeignKeyField,
	TextField, DateTimeField, IntegerField
)

db = SqliteDatabase('db.sqlite3')


class BaseModel(Model):
	class Meta:
		database = db


class Pessoa(BaseModel):

	nome = CharField(max_length=60)
	email = CharField(max_length=60)
	senha = CharField(max_length=60)
	idade = IntegerField()


class Grupo(BaseModel):

	nome = CharField(max_length=50)
	pessoa = ForeignKeyField(Pessoa, backref='grupos')


class Nota(BaseModel):

	titulo = CharField(max_length=60)
	texto = TextField()
	criado_em = DateTimeField(default=datetime.now)
	modificado_em = DateTimeField(default=datetime.now)
	grupo = ForeignKeyField(Grupo, backref='notas', null=True, default=None)
	pessoa = ForeignKeyField(Pessoa, backref='notas')
