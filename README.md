# Peewee ORM
--
Peewee é um ORM simples e pequeno. Possui poucos (mas expressivos) conceitos, tornando-o fácil de aprender e intuitivo de usar.

> Mapeamento Objeto Relacional (ORM) é uma técnica de acessar um banco de dados relacional a partir de uma linguagem orientada a objetos. É uma abstração da API do banco de dados Python.

## O que torna o Peewee um ORM útil?
--
Peewee pode ser uma biblioteca mais fácil de entender do que SQLAlchemy e outros ORMs. Ele foi projetado para ser mais fácil de hackear e entender, semelhante a como o Bottle é uma estrutura da web menor e de um arquivo em comparação com a estrutura abrangente do Django . Se você está apenas começando com o desenvolvimento web, pode valer a pena usar o Peewee para seu mapeamento e operações de banco de dados, especialmente se você usar um microframework como Flask ou Bottle.

O Peewee pode ser usado com praticamente qualquer framework web (embora usá-lo com Django seja atualmente complicado devido ao seu acoplamento ORM embutido) ou sem um framework web. No último caso, o Peewee é bom para extrair dados de um banco de dados relacional em um script ou bloco de notas Jupyter.

Qualquer um dos back-ends de banco de dados relacionais comuns, como PostgreSQL , MySQL ou SQLite, são suportados, embora um driver de banco de dados ainda seja necessário. O gráfico abaixo mostra alguns exemplos de configurações que poderiam usar o Peewee como um ORM.
