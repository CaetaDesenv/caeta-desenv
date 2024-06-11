#Gera informações sobre os alunos
import streamlit as st
import pandas as pd
import plotly.express as px

#c:\Users\prcral\AppData\Local\Programs\Python\Python312\python.exe -m streamlit run dashppe.py

st.set_page_config(page_title="PPE - Informações", layout="wide", initial_sidebar_state="collapsed")

# Carrega o DataFrame a partir do arquivo 'VisaoFull.xlsx'
@st.cache_data
def load_data():
    df_listaalunos = pd.read_csv('DF_LISTAALUNOS.csv')
   
    return df_listaalunos

def emissao(ano_base, df_listaalunos, notas):
       
       #Grupo 1
       # Criando três colunas
        col1, col2, col3 = st.columns(3)
    
        # Cria um filtro para os alunos de 2019
        filtro_dfalunos = df_listaalunos[df_listaalunos['Ano Letivo'] == ano_base]
        # Garantir que a série seja tratada como string
        filtro_dfalunos['Serie'] = filtro_dfalunos['Serie'].astype(str)  
        grade_counts = filtro_dfalunos['Serie'].value_counts().reindex(['6', '7', '8', '9', '1', '2', '3'])
            
        with col1:
            st.subheader('PPE - Visão do andamento')
           
            # Filtrar o dataframe para o Ano letivo igual ao ano_base
            df_ano_base = df_listaalunos[df_listaalunos['Ano Letivo'] == ano_base]

            # Contar o número de alunos 'Aluno' e o número de escolas 'Escola'
            num_alunos = len(df_ano_base)
            num_escolas = df_ano_base['Escola'].nunique()

            # Apresentar os valores
            st.write(f"Ano letivo: {ano_base}")
            st.write(f"Número de Alunos: {num_alunos}")
            st.write(f"Número de Escolas: {num_escolas}")
            st.write(f"NOTAS: {notas}")
###################################################################################            
            st.write("FONTE: Base de dados do PPE referência 10jun2024")
####################################################################################

        with col2:
            # Código para o gráfico tipo torta da distribuição de gênero
            gender_counts = filtro_dfalunos['Sexo'].value_counts()
            # Criar o gráfico de pizza (torta) com Plotly
            figTS = px.pie(values=gender_counts, names=gender_counts.index, #labels=gender_counts.index, 
                         title='Distribuição por gênero em: '+ str(ano_base))
            # Definir cores para os gêneros
            colors = {'Feminino': 'pink', 'Masculino': 'blue'}
            # Mapear as cores de acordo com o gênero
            figTS.update_traces(marker=dict(colors=[colors.get(gender, 'grey') for gender in gender_counts.index]))

            st.plotly_chart(figTS, use_container_width=True)

        with col3:
            # Código para o gráfico tipo torta da distribuição por raça
            race_counts = filtro_dfalunos['Raca'].value_counts()
            # Criar o gráfico de pizza (torta) com Plotly
            figTR = px.pie(values=race_counts, names=race_counts.index, labels=race_counts.index, 
                         title='Distribuição por raça em: '+ str(ano_base))
            
            # Definir cores para raças
            colors = {'Parda': 'brown', 'Branca': 'white','Preta': 'black', 'Amarela': 'yellow',
                      'Indigena': 'red'}
            # Mapear as cores de acordo com o gênero
            figTR.update_traces(marker=dict(colors=[colors.get(race, 'grey') for race in race_counts.index]))

            st.plotly_chart(figTR, use_container_width=True)

#Grupo 2    
        col4, col5, col6 = st.columns(3)

        with col4:
        # Criar o gráfico de barras
            fig = px.bar(x=grade_counts.index, y=grade_counts.values, text=grade_counts.values,
                         labels={'x': 'Série', 'y': 'Nº de alunos'})
            #fig.update_traces( textposition='inside', hoverinfo="none", showlegend=False)
            fig.update_layout(title=('NºAlunos por Série em: '+ str(ano_base)), xaxis={'type': 'category'},
                              yaxis_title='Nº de alunos')
            fig.update_layout(bargap=0.25)  # Reduzir a largura da barra para 75% da largura atual
            st.plotly_chart(fig, use_container_width=True)
            
        with col5:
            # Código para o gráfico de barras da quantidade de alunos por situação
            situation_counts = filtro_dfalunos['Situacao'].value_counts()
            # Definir a ordem desejada para as categorias
            category_order = ['Aprovado', 'Dep.neste ano', 'Dep.outros anos', 'Dep.neste ano e outros', 
                              'Reprovado', 'Transferido', 'Abandonou', 'Faleceu']
            figR = px.bar(x=situation_counts.index, y=situation_counts.values,  text=situation_counts.values, 
                        labels={'x': 'Resultado', 'y': 'Nº de alunos'}, category_orders={'x': category_order})
            figR.update_traces( textposition='inside')
            figR.update_layout(title=('NºAlunos por Resultado em: '+ str(ano_base)), 
                                xaxis={'type': 'category'},yaxis_title='Nº de alunos')
            figR.update_layout(bargap=0.25)  # Reduzir a largura da barra para 75% da largura atual
            st.plotly_chart(figR, use_container_width=True)

        with col6:
            # Código para o gráfico de barras da quantidade de alunos por andamento
            progress_counts = filtro_dfalunos['Andamento'].value_counts()
            # Definir a ordem desejada para as categorias
            category_order = ['ELEGIVEL', 'INSCRICAO PARCIAL', 'EMAIL NAO CONFIRMADO', 'PRE-INSCRITO', 
                                'CONCLUIDA', 'AGUARDANDO DEPOSITO', 'VALOR DEPOSITADO', 
                                'CC aberta - SEM ADESÃO', 'RECUSA EM PARTICIPAR']
            figP = px.bar(x=progress_counts.index, y=progress_counts.values, text=progress_counts.values, 
                         labels={'x': 'Adesão', 'y': 'Nº de alunos'}, category_orders={'x': category_order})
            figP.update_traces(textposition='inside')
            figP.update_layout(title=('NºAlunos por Adesão em: '+ str(ano_base)),  
                                xaxis={'type': 'category'},yaxis_title='Nº de alunos')
            figP.update_layout(bargap=0.25)  # Reduzir a largura da barra para 75% da largura atual
            st.plotly_chart(figP, use_container_width=True)
            
#FIM DA EMISSÃO    

df_listaalunos = load_data()

#Abas
tab2019,tab2020,tab2021,tab2022,tab2023,tab2024 = st.tabs(["2019","2020","2021","2022","2023","2024"])

with tab2019: 
    ano_base = 2019
    notas = "Piloto do PPE, apenas escolas das esferas municipal e federal, alunos das séries 9, 1, 2 e 3"
    emissao(ano_base, df_listaalunos, notas)
  
with tab2020: 
    ano_base = 2020
    notas = "Escolas das esferas municipal, federal e estadual com alunos provenientes da rede municipal, alunos das séries 9, 1, 2 e 3"
    emissao(ano_base, df_listaalunos, notas)  
 
with tab2021: 
    ano_base = 2021
    notas = "Escolas das esferas municipal, federal e estadual, alunos das séries 9, 1, 2 e 3"
    emissao(ano_base, df_listaalunos, notas)

with tab2022: 
    ano_base = 2022
    notas = "Escolas das esferas municipal, federal, estadual e técnica, alunos das séries 6, 7, 8, 9, 1, 2 e 3"
    emissao(ano_base, df_listaalunos, notas)

with tab2023: 
    ano_base = 2023
    notas = "Escolas das esferas municipal, federal, estadual e técnica, alunos das séries 6, 7, 8, 9, 1, 2 e 3"
    emissao(ano_base, df_listaalunos, notas)

with tab2024: 
    ano_base = 2024
    notas = "Escolas das esferas municipal, federal, estadual e técnica, alunos das séries 6, 7, 8, 9, 1, 2 e 3"
    emissao(ano_base, df_listaalunos, notas)
   





