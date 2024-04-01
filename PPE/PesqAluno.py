import streamlit as st
import pandas as pd
import plotly.express as px

#c:\Users\prcral\AppData\Local\Programs\Python\Python312\python.exe -m streamlit run PesqAluno.py

st.set_page_config(page_title="Pesquisa Aluno", layout="wide")
st.title("Pesquisa Aluno")

df = pd.read_excel('VisaoFull.xlsx', sheet_name='VisaoFull')
#df.info()

#df['Ano letivo'] = pd.to_numeric(df['Ano letivo'], errors='coerce')
#df = df.dropna(subset=['Ano letivo'])
#df['Ano letivo'] = df['Ano letivo'].astype(int)

df=df.sort_values(by="Aluno", ascending=True)
df=df.sort_values(by="Ano Letivo", ascending=True)

Aluno = st.sidebar.selectbox("Aluno", df["Aluno"].unique())
df_filtered = df[df["Aluno"] == Aluno]

st.dataframe(df_filtered, column_config={"Ano Letivo": st.column_config.NumberColumn(format="%.0f"),
                                         "Cod.INEP": st.column_config.NumberColumn(format="%.0f"), 
                                         "Cód.": st.column_config.NumberColumn(format="%.0f"),
                                         "CPF informado": st.column_config.NumberColumn(format="%.0f"),
                                         "CPF conta": st.column_config.NumberColumn(format="%.0f"),
                                         "CEP": st.column_config.NumberColumn(format="%.0f"),
                                         "Tel.Informado1": st.column_config.NumberColumn(format="%.0f"),
                                         "Tel.Informado2": st.column_config.NumberColumn(format="%.0f")})	

