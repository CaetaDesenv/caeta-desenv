-- Geração dos DFs para pesquisa de alunos

-- DF_ALUNOS.csv
SELECT DISTINCT Aluno FROM V_VISAO_FULL_PPE

-- DF_BENFICIOS.csv
SELECT [Cód.],[Ano Letivo],Serie,Depositado,Poupanca,[Num. PA],
[CPF conta],Banco,[Num.Agência],Conta
FROM V_VISAO_FULL_PPE
 
-- DF_DADOSBASICOS.csv
SELECT DISTINCT [Cód.], Aluno, Nascimento,Mae,Pai,[Email informado],[Email CadUNICO],Sexo,
[Tel.Informado1],[CPF informado],CEP,Raca,[TelCadunico 1],[CPF CadUNICO],Bairro
FROM V_VISAO_FULL_PPE

-- DF_FAMILIAS.csv
SELECT DISTINCT [Cód.], Aluno, Nascimento,Mae
FROM V_VISAO_FULL_PPE

-- DF_RESULTADOS.csv
SELECT DISTINCT [Cód.],[Ano Letivo],Serie,[Andamento adesao],Situacao,Matricula,Escola
FROM V_VISAO_FULL_PPE

-- Geração dos DFs para pesquisa de alunos com progressão inconsistente

-- DF_ALUNOSI.csv
SELECT DISTINCT Aluno FROM V_INCON

-- DF_BENFICIOSI.csv
SELECT [Cód.],[Ano Letivo],Serie,Depositado,Poupanca,[Num. PA],
[CPF conta],Banco,[Num.Agência],Conta
FROM V_INCON
 
-- DF_DADOSBASICOSI.csv
SELECT DISTINCT [Cód.], Aluno, Nascimento,Mae,Pai,[Email informado],[Email CadUNICO],Sexo,
[Tel.Informado1],[CPF informado],CEP,Raca,[TelCadunico 1],[CPF CadUNICO],Bairro
FROM V_INCON

-- DF_FAMILIASI.csv
SELECT DISTINCT [Cód.], Aluno, Nascimento,Mae
FROM V_INCON

-- DF_RESULTADOSI.csv
SELECT DISTINCT [Cód.],[Ano Letivo],Serie,[Andamento adesao],Situacao,Matricula,Escola
FROM V_INCON

