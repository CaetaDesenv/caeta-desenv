#Gera informações sobre os alunos com inconsistencia na progressao
import streamlit as st
import pandas as pd
import plotly.express as px

#c:\Users\prcral\AppData\Local\Programs\Python\Python312\python.exe -m streamlit run AndamentoPPE.py

st.set_page_config(page_title="PPE – Visualização do andamento", layout="wide")
st.title('Andamento PPE por Ano Letivo')
# Carrega os DataFrames
@st.cache_data
def load_data():
    df_esfera = pd.read_csv('DF_ALUNOSESF.csv')
    df_conclu1 = pd.read_csv('DF_CONCLU1.csv')
    df_conclu2 = pd.read_csv('DF_CONCLU2.csv')
    df_benefanolet = pd.read_csv('DF_BENEFANOLET.csv')
    df_benefpa = pd.read_csv('DF_BENEFPA.csv')
    df_unicos = pd.read_excel('DF_UNICOS.xlsx')
    
    return df_esfera, df_conclu1, df_conclu2, df_benefanolet, df_benefpa, df_unicos

df_esfera, df_conclu1, df_conclu2, df_benefanolet, df_benefpa, df_unicos = load_data()

#Abas
tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["Elegíveis p/ Esfera","Novos Elegíveis",
          "Concluintes","Premiação por Resultado","Benefícios pagos", "Beneficiários Ano PA",])

with tab1:
        # 1 - Alunos por esfera para gráfico de barras segmentadas
        # Número de elegíveis por ano letivo segmentados pelas esferas

        # Agrupamento e soma dos alunos por ano letivo e esfera
    df_grouped = df_esfera.groupby(['Ano Letivo', 'Esfera'])['NumAlunos'].sum().reset_index()

        # Criação do gráfico de barras
    fig = px.bar(df_grouped, x='Ano Letivo', y='NumAlunos', color='Esfera',
                        labels={'NumAlunos': 'Nº Alunos'}, title='Segmentação por Esfera')

    # Adicionar texto com o valor total em cada barra
    for i in range(len(df_grouped)):
        total_value = df_grouped.loc[df_grouped['Ano Letivo'] == df_grouped.loc[i, 'Ano Letivo']]['NumAlunos'].sum()
        fig.add_annotation(x=df_grouped['Ano Letivo'][i], y=total_value,
                       text=str(total_value),
                       showarrow=True)

        # Configurações adicionais (opcional)
    fig.update_layout(
                            xaxis_title='Ano Letivo',
                            yaxis_title='Nº Alunos',
                            legend_title='Esfera',
                            yaxis=dict(tickformat='d')
                        )

        # Exibição do gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    # 2 - Entrada de novos alunos por ano

    # Criar o gráfico de linha
    fig = px.line(df_unicos, x='Ano Letivo', y='Num Alunos', markers=True)

    # Adicionar texto com o valor de cada ponto no gráfico
    for i in range(len(df_unicos)):
        fig.add_annotation(x=df_unicos['Ano Letivo'][i], y=df_unicos['Num Alunos'][i],
                       text=str(df_unicos['Num Alunos'][i]),
                       showarrow=True)
     
    # Personalizar o gráfico (opcional)
    fig.update_layout(
        title='Alunos novos no PPE',
        xaxis_title='Ano Letivo',
        yaxis_title='Novos Alunos',
        xaxis=dict(tickmode='linear', tick0=0, dtick=1),  # Exibir valores inteiros no eixo X
        #yaxis=dict(tickmode='linear', tick0=0, dtick=1),  # Exibir valores inteiros no eixo Y
        )

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

with tab3:  
    # 3 - Análise concluintes

    #Alterar em df_conclu1 o nome de NumConcluintes para NºConcluintes
    df_conclu1 = df_conclu1.rename(columns={'NumConcluintes': 'NºConcluintes'})

    # Crie o gráfico de linha com cores diferentes
    fig = px.line(df_conclu1, x="Ano Letivo", y="NºConcluintes", title="Concluintes & Concluintes Beneficiados",
                line_shape="linear", color_discrete_sequence=["red"])
    fig.add_trace(px.line(df_conclu2, x="Ano Letivo", y="NumConcBenef", 
                title="Análise Concluintes", line_shape="linear", color_discrete_sequence=["white"]).data[0])

    # Personalize o gráfico
    fig.update_traces(mode="markers+lines", marker=dict(size=10, 
        line=dict(width=2, color="DarkSlateGrey")), selector=dict(type="scatter"))
    fig.update_layout(showlegend=True, legend_title_text="Dados")

    # Adicione setas para os pontos
    for i in range(len(df_conclu1)):
        fig.add_annotation(x=df_conclu1["Ano Letivo"][i], 
                        y=df_conclu1["NºConcluintes"][i], text=str(df_conclu1["NºConcluintes"][i]),
                        showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor="gray")

    for i in range(len(df_conclu2)):
        fig.add_annotation(x=df_conclu2["Ano Letivo"][i], 
                        y=df_conclu2["NumConcBenef"][i], text=str(df_conclu2["NumConcBenef"][i]),
                        showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor="gray")

    # Adicione rótulos identificando cada linha
    fig.add_annotation(x=2020, y=700, text="Concluintes", showarrow=False, font=dict(size=16, color="red"))
    fig.add_annotation(x=2020, y=500, text="Beneficiados", showarrow=False, font=dict(size=16, color="white"))

    # Ajuste os rótulos do eixo X para exibir apenas os anos letivos
    fig.update_xaxes(tickvals=df_conclu1["Ano Letivo"].tolist() + df_conclu2["Ano Letivo"].tolist(),
                    ticktext=df_conclu1["Ano Letivo"].tolist() + df_conclu2["Ano Letivo"].tolist())

    st.plotly_chart(fig, use_container_width=True)


with tab4:  

	# Filtrando os valores de ano letivo sem quebras
	df_benefanolet['Ano Letivo'] = df_benefanolet['Ano Letivo'].astype(str)  # Convertendo para string
	df_benefanolet = df_benefanolet.groupby('Ano Letivo').sum().reset_index()

	# Criando o gráfico de barras
	fig = px.bar(df_benefanolet, x='Ano Letivo', y='Depositado', 
                title="Depósitos por resultados obtidos",
    			labels={'Ano Letivo': 'Ano Letivo', 'Depositado': 'Valor Depositado (R$)'})

	# Adicionando os valores nas barras com setas
	for i in range(len(df_benefanolet)):
		fig.add_annotation(
			x=df_benefanolet['Ano Letivo'][i],
			y=df_benefanolet['Depositado'][i],
			text=f"R$ {df_benefanolet['Depositado'][i]:,.2f}",
			showarrow=True,
			arrowhead=1,
			yshift=10
		)

	# Exibindo o gráfico no Streamlit
	st.plotly_chart(fig, use_container_width=True)

with tab5: 

    #   Filtrando os valores de ano letivo sem quebras
    df_esfera['Ano Letivo'] = df_esfera['Ano Letivo'].astype(str)
    # Agrupamento e soma dos alunos por ano letivo e esfera
    df_esfera = df_esfera.groupby('Ano Letivo').sum().reset_index()

    #Alterar em df_conclu1 o nome de NumConcluintes para NºConcluintes
    df_esfera = df_esfera.rename(columns={'NumAlunos': 'Elegíveis'})

    # Crie o gráfico de linha com cores diferentes
    fig = px.line(df_esfera, x="Ano Letivo", y="Elegíveis", title="Elegíveis & Beneficiados",
                line_shape="linear", color_discrete_sequence=["red"])
    fig.add_trace(px.line(df_benefanolet, x="Ano Letivo", y="Beneficiados", 
                title="Elegíveis & Beneficiados", line_shape="linear", color_discrete_sequence=["white"]).data[0])

    # Personalize o gráfico
    fig.update_traces(mode="markers+lines", marker=dict(size=10, 
        line=dict(width=2, color="DarkSlateGrey")), selector=dict(type="scatter"))
    fig.update_layout(showlegend=True, legend_title_text="Dados")

    # Adicione setas para os pontos
    for i in range(len(df_esfera)):
        fig.add_annotation(x=df_esfera["Ano Letivo"][i], 
                        y=df_esfera["Elegíveis"][i], text=str(df_esfera["Elegíveis"][i]),
                        showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor="gray")

    for i in range(len(df_benefanolet)):
        fig.add_annotation(x=df_benefanolet["Ano Letivo"][i], 
                        y=df_benefanolet["Beneficiados"][i], text=str(df_benefanolet["Beneficiados"][i]),
                        showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor="gray")

    # Adicione rótulos identificando cada linha
    fig.add_annotation(x=2020, y=8000, text="Elegíveis", showarrow=False, font=dict(size=16, color="red"))
    fig.add_annotation(x=2020, y=6000, text="Beneficiados", showarrow=False, font=dict(size=16, color="white"))

    # Ajuste os rótulos do eixo X para exibir apenas os anos letivos
    fig.update_xaxes(tickvals=df_conclu1["Ano Letivo"].tolist() + df_conclu2["Ano Letivo"].tolist(),
                    ticktext=df_conclu1["Ano Letivo"].tolist() + df_conclu2["Ano Letivo"].tolist())

    st.plotly_chart(fig, use_container_width=True)

with tab6:

    df_benefpa['Ano'] = df_benefpa['Ano'].astype(str)  # Convertendo para string
    df_benefpa_unique = df_benefpa.drop_duplicates(subset=['Ano'])

    fig = px.bar(df_benefpa_unique, x='Ano', y='Depositado', title='Depósitos realizados pelos PAs',
                 labels={'Ano': 'Ano', 'Depositado': 'Valor Depositado pelos PAs(R$)'})

    for i in range(len(df_benefpa_unique)):
	    fig.add_annotation(
			   x=df_benefpa_unique['Ano'][i],
			   y=df_benefpa_unique['Depositado'][i],
			   text=f"R$ {df_benefpa_unique['Depositado'][i]:,.2f}",
			   showarrow=True,
			   arrowhead=1,
			   yshift=10,
			   font=dict(color='gray')
		   )

    st.plotly_chart(fig, use_container_width=True)


       