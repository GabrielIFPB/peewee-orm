
from models import Pessoa, db, Grupo, Nota

# Pessoa.create_table()

db.create_tables([Pessoa, Grupo, Nota])

p1 = Pessoa(
	nome='João',
	email="joao@gmail.com",
	senha="123456",
	idade=18
)

p2 = Pessoa(
	nome='Maria',
	email="maria@gmail.com",
	senha="654321",
	idade=20
)
