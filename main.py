
from models import Pessoa, db, Grupo, Nota

# Pessoa.create_table()

db.create_tables([Pessoa, Grupo, Nota])

joao = Pessoa(
	nome='João',
	email="joao@gmail.com",
	senha="123456",
	idade=18
)

Pessoa.create(
	nome='Maria',
	email="maria@gmail.com",
	senha="654321",
	idade=20
)

joao.save()

pessoas = [
	{'nome': 'augusto', 'email': 'augusto@email', 'idade': 1, 'senha': '123'},
	{'nome': 'flavio', 'email': 'flavio@email', 'idade': 1, 'senha': '123'},
	{'nome': 'dora', 'email': 'dora@email', 'idade': 1, 'senha': '123'},
]
Pessoa.insert_many(pessoas).execute()

Grupo.create(
	nome='Azul',
	pessoa=Pessoa.select().where(Pessoa.nome == 'flavio')
)
grupo = Grupo.select().get()
print(grupo.nome)
print(grupo.pessoa)
print(grupo.pessoa.nome)

Nota.create(
	titulo='titulo da note',
	texto='texto da note bla ble bli blo blu',
	pessoa=Pessoa.select().where(Pessoa.nome == 'flavio')
)
nota = Nota.select().get()
print(nota.titulo)

nota = Nota.select().where(Nota.titulo == 'titulo da note').get()
grupo = Grupo.select().where(Grupo.nome == 'Azul').get()

# update
nota.grupo = grupo

nota.save()

notas_azuis = (
	Nota.select()
	.join(Grupo)
	.where(Grupo.nome == 'Azul')
	.get()
)

print(notas_azuis.titulo)
