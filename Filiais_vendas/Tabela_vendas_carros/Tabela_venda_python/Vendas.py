import pandas as pd
import random
from faker import Faker
import os

fake = Faker('pt_BR')

#Listas de valores possiveis
marcas_modelos = {
    "Toyota" : ["Corolla", "Hilux", "Yaris"],
    "Honda" : ["Civic", "HR-V", "Fit"],
    "Ford" : ["Ka", "EcoSport", "Ranger"],
    "Chevrolet" : ["Onix", "Tracker", "S10"],
    "Volkswagem" : ["Gol", "Polo", "T-Cross"]
}

formas_pagamento = ["A vista", "Financiomanto", "Consórcio", "Leasing"]
cores = ["Preto", "Branco", "Prata", "Vermelho", "Azul"]
sexo_opcoes = ["Masculino", "Feminino"]

#Gerando os dados ficticios
dados = []
for i in range(1, 1001):
  sexo = random.choice(sexo_opcoes)
  nome = fake.first_name_male() if sexo == "Masculino" else fake.first_name_female()
  sobrenome = fake.last_name()
  nome_completo = f"{nome} {sobrenome}"

  idade = random.randint(18, 70)
  cpf = fake.cpf()
  email = fake.email()
  telefone = fake.phone_number()
  cidade = fake.city()
  estado = fake.state_abbr()

  marca = random.choice(list(marcas_modelos.keys()))
  modelo = random.choice(list(marcas_modelos[marca]))
  ano_fabricacao = random.randint(2015, 2024)
  cor = random.choice(cores)
  valor_venda = round(random.uniform(30000, 250000), 2)
  data_venda = fake.date_between(start_date="-2y", end_date="today")
  forma_pagamento = random.choice(formas_pagamento)

  dados.append([i, nome_completo, idade, cpf, sexo, email, telefone, cidade, estado,
               marca, modelo, ano_fabricacao, cor, valor_venda, data_venda, forma_pagamento])

#Criando o DataFrame
colunas = ["ID_CLIENTE", "NOME", "IDADE", "CPF", "SEXO", "EMAIL", "TELEFONE", "CIDADE", "ESTADO",
           "MARCA_VEICULO", "MODELO_VEICULO", "ANO_FABRICACAO", "COR", "VALOR_VENDA", "DATA_VENDA", "FORMA_PAGAMENTO"]

df_vendas = pd.DataFrame(dados, columns=colunas)

#Criando a pasta caso não existir
pasta = "tabela_vendas"
os.makedirs(pasta, exist_ok=True)

#Converter tabela para CSV e salvando na pasta tabela_vendas
caminho_csv = os.path.join(pasta, "tabela_vendas.csv")
df_vendas.to_csv(caminho_csv, index=False, encoding="utf-8")
print(f"Arquivo CSV salvo em: {caminho_csv}")