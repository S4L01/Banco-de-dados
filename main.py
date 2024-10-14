"""BANCO DE DADOS 
    -SQL (LINGUAGEM DE CONSULTA ESTRUTURADA)
    -EXEMPLO:
        - SELECT * FROM CLIENTE;
        - IRÁ CONSULTAR O BD NA TABELA CLIENTES.

        -SGBD:
            -GERENCIAR PERMISSOES DE ACESSO
            -ADMINISTRADOR DE BANCO DE DADOS (DBA)
            - CRIAR CONSULTAS PERSONALIZADAS 


        -ORM: MAPEAMENTO OBJETO RELACIONAÇ
                USAR A LINGUAGEM DE PROGRAMAÇÃO PARA MANIPULAR O BANCO DE DADOS.    
"""
import os 
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados.

Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# Criando Tabela.

Base = declarative_base()

class Cliente (Base):
    __tablename__ = "clientes"

    # Definindo campos da tabela 

    id = Column("id", Integer,primary_key=True,autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    # Definindo atributos da classe.
    def __init__ (self,nome:str,email:str,senha:str):
        self.nome = nome 
        self.email = email
        self.senha = senha 
# Criando tabela no banco de dados
Base.metadata.create_all(bind=MEU_BANCO)

# CRUD.
# Create - Insert - Salvar 
os.system("cls||clear")
print("Solicitando dados para o usuario: ")
insert_nome = input("Digite seu nome: ")
insert_email = input("Digite seu email: ")
insert_senha = input("Digite sua senha: ")

cliente = Cliente(nome=insert_nome,email=insert_email,senha=insert_senha)
session.add(cliente)
session.commit()

# Read - Select - Consulta

print("\nExibindo dados de todos os clientes.")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")
    


# U - Update - UPDATE - Atualizar 
print("\nAtualizando dados do cliente")
email_cliente = input("Digite o email do cliente que sera atualizado")

cliente = session.query(Cliente).filter_by(email = email_cliente).first()
if cliente:
    cliente_nome = input("Digite seu nome: ")
    cliente_email = input("Digite seu email: ")
    cliente_senha = input("Digite sua senha: ")
    session.commit()
else:
    print("Cliente não encotrado")


# Read - Select - Consulta

print("\nExibindo dados de todos os clientes.")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")
    

# D - Delete - DELETE - Excluir

print("\nExcluindo os dados ")
email_cliente = input("Digite o email que deseja deletar")

cliente = session.query(Cliente).filter_by(email = email_cliente).filter_by()

if cliente:
    session.delete(cliente)
    session.commit()
    print(f"Cliente {cliente.nome}excluido com sucesso")
else:
    print("Cliente não encontrado")    


# Read - Select - Consulta

print("\nExibindo dados de todos os clientes.")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

# Read - Select - Consulta

print("Consultando os dados de apenas um cliente.")
email_cliente = input("Digite o email que deseja consultar")

cliente = session.query(Cliente).filter_by(email = email_cliente).filter_by()

if cliente:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")
else:
    print("Cliente não encontrado")    

session.close()    