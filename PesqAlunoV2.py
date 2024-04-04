#Gera informações sobre os alunos
import streamlit as st
import pandas as pd
import plotly.express as px

#c:\Users\prcral\AppData\Local\Programs\Python\Python312\python.exe -m streamlit run PesqAlunoV2.py

st.set_page_config(page_title="PPE – Pesquisa de Alunos", layout="wide")

# Carrega o DataFrame a partir do arquivo 'VisaoFull.xlsx'
@st.cache_data
def load_data():
    return pd.read_excel("VisaoFull.xlsx", sheet_name="VisaoFull")

df = load_data()

# Transformar valores numéricos em strings
df = df.map(lambda x: str(int(x)) if pd.api.types.is_numeric_dtype(x) else x)

# Preencher campos nulos, sem valor ou com valor zero com "Não informado"
df.fillna("Não informado", inplace=True)

# Criar dataframe df_pesquisa com colunas únicas
df_pesquisa = df.drop_duplicates(subset=["Cód.", "Aluno", "Nascimento", "Mãe"])

# Sidebar
st.sidebar.title("Pesquisar Aluno")
st.sidebar.write("")
st.sidebar.text("Última atualização: 04/04/2024")
st.sidebar.text("")
#st.sidebar.text("Digite o nome desejado e quando\nencontrado clique no mesmo")
aluno_filtro  = st.sidebar.selectbox("Digite o nome desejado e quando\nencontrado clique no mesmo", df["Aluno"].unique())
st.sidebar.text("Na tabela ao lado, encontrado\no aluno, digite aqui o código\ndo mesmo e pressione ENTER")
st.sidebar.text("Dados detalhados do aluno serão\napresentados nas outras abas")
idt_elegivel  = st.sidebar.number_input('Código do aluno no PPE', min_value=1, value=1)

# Filtrar df_pesquisa pelo aluno selecionado no sidebar
if aluno_filtro:
    df_pesquisa = df_pesquisa[df_pesquisa["Aluno"].str.contains(aluno_filtro, case=False)]

#Abas
tab1,tab2,tab3,tab4 = st.tabs(["Pesquisa","Dados Pessoais","Resultados","Benefícios" ])

with tab1:
    # Aba "Pesquisa"
    # Apresentar dataframe na aba Pesquisa
    st.dataframe(df_pesquisa[["Cód.", "Aluno", "Nascimento", "Mãe"]].reset_index(drop=True),
                height=200, use_container_width=True, hide_index=True,
                column_config={"Cód.": st.column_config.NumberColumn(format="%.0f")})

with tab2:
#Aba "Dados Pessoais"
    dados_pessoais = df[df["Cód."] == idt_elegivel].iloc[0]
    st.header(f"{idt_elegivel} - {dados_pessoais['Aluno']}")
    st.text("Nascimento : " + dados_pessoais["Nascimento"])
    st.text("Mãe: " + dados_pessoais["Mãe"])
    st.text("Pai: " + dados_pessoais["Pai"])
    st.text("Email informado: " + dados_pessoais["Email informado"])
    st.text("Email CadUNICO: " + dados_pessoais["Email CadUNICO"])


    col1, col2 = st.columns(2)
    with col1:
        st.text("Sexo: " + dados_pessoais["Sexo"])

        # Dividir a string pelo ponto
        partes = str(dados_pessoais["Tel.Informado1"])
        partes = partes.split(".")
        primeira_parte = partes[0]
        st.text("Tel.Informado1: " + primeira_parte)
        
        # Dividir a string pelo ponto
        partes = str(dados_pessoais["CPF informado"])
        partes = partes.split(".")
        primeira_parte = partes[0]
        st.text("CPF informado: " + primeira_parte)
        
        st.text("CEP: " + str(dados_pessoais["CEP"]))

    with col2:
        st.text("Raça: " + dados_pessoais["Raça"])
        st.text("TelCadunico 1: " + str(dados_pessoais["TelCadunico 1"]))
        st.text("CPF CadUNICO: " + str(dados_pessoais["CPF CadUNICO"]))
        st.text("Bairro: " + dados_pessoais["Bairro"])
 
with tab3:
    #Aba Resultados
    st.header(f"{idt_elegivel} - {dados_pessoais['Aluno']}")

    # Filtrar df para obter histórico do aluno
    df_historico = df[df["Cód."] == idt_elegivel][["Ano Letivo", "Série", 
                                                   "Andamento adesão", "Situacao", 
                                                   "Matrícula", "Escola"]]
    df_historico.sort_values(by="Ano Letivo", inplace=True)
    # Apresentar histórico na aba Histórico
    st.dataframe(df_historico, use_container_width=True, hide_index=True,
                 column_config={"Ano Letivo": st.column_config.NumberColumn(format="%.0f")})
                                
with tab4:
    #Aba Benefícios
    st.header(f"{idt_elegivel} - {dados_pessoais['Aluno']}")

    # Filtrar df para obter benefícios do aluno
    df_beneficio = df[df["Cód."] == idt_elegivel][["Ano Letivo", "Série", 
                                                   "Depositado", "Poupança","Num. PA", "CPF conta", 
                                                   "Banco", "Num.Agência", "Conta"]]
    df_beneficio.sort_values(by="Ano Letivo", inplace=True)
    # Apresentar benefícios na aba Benefícios
    st.dataframe(df_beneficio, use_container_width=True, hide_index=True,
                 column_config={"Ano Letivo": st.column_config.NumberColumn(format="%.0f"),
                                 "Num.Agência": st.column_config.NumberColumn(format="%.0f"),
                                 "CPF conta": st.column_config.NumberColumn(format="%.0f")})
    
    