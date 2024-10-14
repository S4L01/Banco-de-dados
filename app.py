
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados
BANCO_ALUNOS = create_engine("sqlite:///bancoalunos.db")

# Criando conexão com banco de dados.

Session = sessionmaker(bind=BANCO_ALUNOS)
session = Session()

# Criando Tabela.

Base = declarative_base()

class Aluno(Base):
    __tablename__ = "alunos"

    # Definindo campos da tabela 

    ra = Column("id", Integer,primary_key=True,autoincrement=True)
    nome = Column("nome", String)
    sobrenome = Column("sobrenome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    # Definindo atributos da classe.
    def __init__ (self,nome:str,sobrenome:str,email:str,senha:str):
        self.nome = nome 
        self.sobrenome = sobrenome 
        self.email = email
        self.senha = senha 
# Criando tabela no banco de dados
Base.metadata.create_all(bind=BANCO_ALUNOS)
def create():
    print("Solicitando dados para o usuario: ")
    insert_nome = input("Digite seu nome: ")
    insert_sobrenome = input("Digite seu Sobrenome: ")
    insert_email = input("Digite seu email: ")
    insert_senha = input("Digite sua senha: ")

    aluno = Aluno(nome=insert_nome,sobrenome=insert_sobrenome,email=insert_email,senha=insert_senha)
    session.add(aluno)
    session.commit()

    print("Úsuario Salva com sucesso")

def read ():
    
    print("\nExibindo dados de todos os clientes.")
    lista_alunos = session.query(Aluno).all()

    for aluno in lista_alunos:
        print(f"{aluno.ra} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha}")
    
read()

