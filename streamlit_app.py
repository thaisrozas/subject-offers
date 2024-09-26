import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("Projeção da oferta dos cursos EaD: Com ou Sem Carrosel")

# Sem carrossel
st.header("Sem Carrossel")
st.write("Isso significa que a oferta seria de todos os semestres dos cursos das matrizes antigas e até o terceiro semestre dos cursos nas matrizes novas")

all20251 = './tables/all2025-1.csv'
dataall = pd.read_csv(all20251)

# Filtrar as disciplinas por matriz
matriz_nova = dataall[dataall['Matriz'].str.contains('Nova', case=False, na=False)]
matriz_antiga = dataall[dataall['Matriz'].str.contains('Antiga', case=False, na=False)]

# Contar as ocorrências de disciplinas para cada curso na matriz nova
cursos_nova = matriz_nova['Curso'].unique()
ocorrencias_cursos_nova = {curso: matriz_nova['Curso'].str.contains(curso, case=False, na=False).sum() for curso in cursos_nova}
ocorrencias_cursos_nova_dataall = pd.DataFrame(list(ocorrencias_cursos_nova.items()), columns=['Curso', 'Quantidade de Disciplinas'])

# Contar as ocorrências de disciplinas para cada curso na matriz antiga
cursos_antiga = matriz_antiga['Curso'].unique()
ocorrencias_cursos_antiga = {curso: matriz_antiga['Curso'].str.contains(curso, case=False, na=False).sum() for curso in cursos_antiga}
ocorrencias_cursos_antiga_data = pd.DataFrame(list(ocorrencias_cursos_antiga.items()), columns=['Curso', 'Quantidade de Disciplinas'])

# # Outros gráficos sobre a base
# # Exibir os títulos e os gráficos de barras no Streamlit
# st.subheader("Quantidade de Disciplinas por Curso")

# st.subheader(f"**Matriz Nova**")
# st.bar_chart(ocorrencias_cursos_nova_dataall.set_index('Curso'))

# st.subheader(f"**Matriz Antiga**")
# st.bar_chart(ocorrencias_cursos_antiga_data.set_index('Curso'))

countall20251 = './tables/count-all2025-1.csv'
data_countall = pd.read_csv(countall20251)

data_countall_cleaned = data_countall.drop(columns=['Quantidade'])

# Mostrar a tabela apenas quando o usuário clicar no botão
if st.button("Listar disciplinas sem oferta carrossel"):
    st.dataframe(data_countall_cleaned)

# Com carrossel
st.header("Com Carrossel")
st.write("Isso significa que a oferta seria de de acordo com o carrossel projetado.")

count_carousel20251 = './tables/count-carousel2025-1.csv'
data_countcarousel = pd.read_csv(count_carousel20251)

# Mostrar a tabela apenas quando o usuário clicar no botão
if st.button("Listar disciplinas com oferta carrossel"):
    st.dataframe(data_countcarousel)

# Contar o número total de ocorrências (linhas) em cada DataFrame
total_countall = data_countall.shape[0]  # Total de linhas no primeiro DataFrame
total_countcarousel = data_countcarousel.shape[0]  # Total de linhas no segundo DataFrame

# Criando um DataFrame com os totais
total_data = pd.DataFrame({
    'Tipos': ['Sem Carrossel', 'Com Carrossel'],
    'Total': [total_countall, total_countcarousel]
})

# Gerando o gráfico de barras usando Matplotlib
fig, ax = plt.subplots(figsize=(8, 7))
bars = ax.bar(total_data['Tipos'], total_data['Total'], color=['lightblue', 'blue'])

# Adicionando o número total em cima de cada barra
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}', 
                xy=(bar.get_x() + bar.get_width() / 2, height),  # Coordenadas do texto
                xytext=(0, 3),  # Deslocamento do texto
                textcoords="offset points", 
                ha='center', va='bottom')

# Configurando os rótulos e o título do gráfico
ax.set_xlabel('Tipo de Oferta')
ax.set_ylabel('Quantidade de Disciplinas')
ax.set_title('Quantidade de Disciplinas por Tipo de Oferta')

# Exibindo o gráfico no Streamlit
st.pyplot(fig)