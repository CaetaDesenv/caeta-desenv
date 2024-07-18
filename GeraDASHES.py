## Geração das planilhas para pesquisa de alunos ativos na base do PPE
import pyodbc
import pandas as pd

# Configurações de conexão
server = '10.11.30.31'
database = 'PROGPOUPESCOLANIT2'
username = 'PROGPOUPESCOLANIT2_uud1'
password = 'Prohia290'
# Conectando ao banco de dados
conn = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}')
cursor = conn.cursor()

## ---  GERAÇÃO DOS DATAFRAMES DOS ALUNOS ATIVOS  ---

# DF_ALUNOS.csv
query_DF_ALUNOS = """
SELECT DISTINCT Aluno FROM V_VISAO_FULL_PPE
"""
conn.execute(query_DF_ALUNOS)

# Executa a consulta e coloca os resultados em um dataframe
df = pd.read_sql(query_DF_ALUNOS, conn)

# Grava o dataframe no arquivo CSV
arquivo_csv = 'C:/Users/prcral/Documents/PYTHON Modulos/DASHES/DF_ALUNOS.csv'
df.to_csv(arquivo_csv, index=False)
print("Fim Geração DF_ALUNOS.csv")

# DF_BENEFICIOS.csv
query_DF_BENEFICIOS = """
SELECT [Cód.],[Ano Letivo],Serie,Depositado,Poupanca,[Num. PA],
[CPF conta],Banco,[Num.Agência],Conta
FROM V_VISAO_FULL_PPE
"""
conn.execute(query_DF_BENEFICIOS)

# Executa a consulta e coloca os resultados em um dataframe
df = pd.read_sql(query_DF_BENEFICIOS, conn)

# Grava o dataframe no arquivo CSV
arquivo_csv = 'C:/Users/prcral/Documents/PYTHON Modulos/DASHES/DF_BENEFICIOS.csv'
df.to_csv(arquivo_csv, index=False)
print("Fim Geração DF_BENEFICIOS.csv")

# DF_DADOSBASICOS.csv
query_DF_DADOSBASICOS = """
SELECT DISTINCT [Cód.], Aluno, Nascimento,Mae,Pai,[Email informado],[Email CadUNICO],Sexo,
[Tel.Informado1],[CPF informado],CEP,Raca,[TelCadunico 1],[CPF CadUNICO],Bairro
FROM V_VISAO_FULL_PPE
"""
conn.execute(query_DF_DADOSBASICOS)

# Executa a consulta e coloca os resultados em um dataframe
df = pd.read_sql(query_DF_DADOSBASICOS, conn)

# Grava o dataframe no arquivo CSV
arquivo_csv = 'C:/Users/prcral/Documents/PYTHON Modulos/DASHES/DF_DADOSBASICOS.csv'
df.to_csv(arquivo_csv, index=False)
print("Fim Geração DF_DADOSBASICOS.csv")

# DF_FAMILIAS.csv
query_DF_FAMILIAS = """
SELECT DISTINCT [Cód.], Aluno, Nascimento,Mae
FROM V_VISAO_FULL_PPE
"""
conn.execute(query_DF_FAMILIAS)

# Executa a consulta e coloca os resultados em um dataframe
df = pd.read_sql(query_DF_FAMILIAS, conn)

# Grava o dataframe no arquivo CSV
arquivo_csv = 'C:/Users/prcral/Documents/PYTHON Modulos/DASHES/DF_FAMILIAS.csv'
df.to_csv(arquivo_csv, index=False)
print("Fim Geração DF_FAMILIAS.csv")

# DF_RESULTADOS.csv
query_DF_RESULTADOS = """
SELECT DISTINCT [Cód.],[Ano Letivo],Serie,[Andamento adesao],Situacao,Matricula,Escola
FROM V_VISAO_FULL_PPE
"""
conn.execute(query_DF_RESULTADOS)

# Executa a consulta e coloca os resultados em um dataframe
df = pd.read_sql(query_DF_RESULTADOS, conn)

# Grava o dataframe no arquivo CSV
arquivo_csv = 'C:/Users/prcral/Documents/PYTHON Modulos/DASHES/DF_RESULTADOS.csv'
df.to_csv(arquivo_csv, index=False)
print("Fim Geração DF_RESULTADOS.csv")



## ---  GERAÇÃO DOS DATAFRAMES DOS ALUNOS COM PROGRESSÃO INCONSISTENTE  ---

# DF_ALUNOSI.csv
query_DF_ALUNOSI = """
SELECT DISTINCT Aluno FROM V_INCON
"""
conn.execute(query_DF_ALUNOSI)

# Executa a consulta e coloca os resultados em um dataframe
df = pd.read_sql(query_DF_ALUNOSI, conn)

# Grava o dataframe no arquivo CSV
arquivo_csv = 'C:/Users/prcral/Documents/PYTHON Modulos/DASHES/DF_ALUNOSI.csv'
df.to_csv(arquivo_csv, index=False)
print("Fim Geração DF_ALUNOSI.csv")

# DF_BENEFICIOSI.csv
query_DF_BENEFICIOSI = """
SELECT [Cód.],[Ano Letivo],Serie,Depositado,Poupanca,[Num. PA],
[CPF conta],Banco,[Num.Agência],Conta
FROM V_INCON
"""
conn.execute(query_DF_BENEFICIOSI)

# Executa a consulta e coloca os resultados em um dataframe
df = pd.read_sql(query_DF_BENEFICIOSI, conn)

# Grava o dataframe no arquivo CSV
arquivo_csv = 'C:/Users/prcral/Documents/PYTHON Modulos/DASHES/DF_BENEFICIOSI.csv'
df.to_csv(arquivo_csv, index=False)
print("Fim Geração DF_BENEFICIOSI.csv")

# DF_DADOSBASICOSI.csv
query_DF_DADOSBASICOSI = """
SELECT DISTINCT [Cód.], Aluno, Nascimento,Mae,Pai,[Email informado],[Email CadUNICO],Sexo,
[Tel.Informado1],[CPF informado],CEP,Raca,[TelCadunico 1],[CPF CadUNICO],Bairro
FROM V_INCON
"""
conn.execute(query_DF_DADOSBASICOSI)

# Executa a consulta e coloca os resultados em um dataframe
df = pd.read_sql(query_DF_DADOSBASICOSI, conn)

# Grava o dataframe no arquivo CSV
arquivo_csv = 'C:/Users/prcral/Documents/PYTHON Modulos/DASHES/DF_DADOSBASICOSI.csv'
df.to_csv(arquivo_csv, index=False)
print("Fim Geração DF_DADOSBASICOSI.csv")

# DF_FAMILIASI.csv
query_DF_FAMILIASI = """
SELECT DISTINCT [Cód.], Aluno, Nascimento,Mae
FROM V_INCON
"""
conn.execute(query_DF_FAMILIASI)

# Executa a consulta e coloca os resultados em um dataframe
df = pd.read_sql(query_DF_FAMILIASI, conn)

# Grava o dataframe no arquivo CSV
arquivo_csv = 'C:/Users/prcral/Documents/PYTHON Modulos/DASHES/DF_FAMILIASI.csv'
df.to_csv(arquivo_csv, index=False)
print("Fim Geração DF_FAMILIASI.csv")

# DF_RESULTADOSI.csv
query_DF_RESULTADOSI = """
SELECT DISTINCT [Cód.],[Ano Letivo],Serie,[Andamento adesao],Situacao,Matricula,Escola
FROM V_INCON
"""
conn.execute(query_DF_RESULTADOSI)

# Executa a consulta e coloca os resultados em um dataframe
df = pd.read_sql(query_DF_RESULTADOSI, conn)

# Grava o dataframe no arquivo CSV
arquivo_csv = 'C:/Users/prcral/Documents/PYTHON Modulos/DASHES/DF_RESULTADOSI.csv'
df.to_csv(arquivo_csv, index=False)
print("Fim Geração DF_RESULTADOSI.csv")


