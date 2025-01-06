import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import streamlit as st

sns.set()

def plota_pivot_table(df, value, index, func, ylabel, xlabel, opcao='nada'):
    plt.figure(figsize=[15, 5])
    if opcao == 'nada':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).plot()
    elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).unstack().plot()
    elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).sort_values(value).plot()
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(f'{ylabel} ao longo do tempo')
    st.pyplot(plt)
    return None

st.set_page_config(page_title='SINASC Rondônia',page_icon='https://upload.wikimedia.org/wikipedia/commons/e/ea/Flag_map_of_Rondonia.png', layout='wide')

st.write('# Análise SINASC RO 2019')

sinasc = pd.read_csv("C:/Users/Paulo Roberto/Downloads/Exercício 01 Módulo 15/input/SINASC_RO_2019.csv")

# Converter a coluna DTNASC para o formato datetime
sinasc['DTNASC'] = pd.to_datetime(sinasc['DTNASC'], format='%Y-%m-%d', errors='coerce')

# Obter a data mínima e máxima no formato brasileiro
min_data = sinasc['DTNASC'].min().strftime('%d/%m/%Y')
max_data = sinasc['DTNASC'].max().strftime('%d/%m/%Y')

# Exibir a data mínima e máxima
st.write('Data mínima: ', min_data)
st.write('Data máxima: ', max_data)

# Criar um DataFrame com as datas únicas e ordená-las
datas = pd.DataFrame(sinasc['DTNASC'].unique(), columns=['DTNASC'])
datas.sort_values(by='DTNASC', inplace=True, ignore_index=True)

# Converter as datas para o formato brasileiro no DataFrame
datas['DTNASC'] = datas['DTNASC'].dt.strftime('%d/%m/%Y')

# Exibir o DataFrame
st.write(datas)

# Filtrar os dados pela data selecionada
data_inicial = st.sidebar.date_input('Data inicial',
                value=sinasc['DTNASC'].min(),
                min_value=sinasc['DTNASC'].min(),
                max_value=sinasc['DTNASC'].max())
data_final = st.sidebar.date_input('Data final',
                value=sinasc['DTNASC'].max(),
                min_value=sinasc['DTNASC'].min(),
                max_value=sinasc['DTNASC'].max())
st.sidebar.write('Data inicial selecionada: ', data_inicial.strftime('%d/%m/%Y'))
st.sidebar.write('Data final selecionada: ', data_final.strftime('%d/%m/%Y'))

sinasc = sinasc[(sinasc['DTNASC'] <= pd.to_datetime(data_final)) & (sinasc['DTNASC'] >= pd.to_datetime(data_inicial))]


# Criar diretório para salvar os gráficos
os.makedirs(f'./output/figs/{max_data}', exist_ok=True)

# Gráficos
plota_pivot_table(sinasc, 'IDADEMAE', 'DTNASC', 'mean', 'Média idade mãe por data', 'Data nascimento')
plt.savefig(f'./output/figs/{max_data}/media_idade_mae_por_data.png')

plota_pivot_table(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean', 'Média idade mãe', 'Data de nascimento', 'unstack')
plt.savefig(f'./output/figs/{max_data}/media_idade_mae_por_sexo.png')

plota_pivot_table(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'Média peso bebê', 'Data de nascimento', 'unstack')
plt.savefig(f'./output/figs/{max_data}/media_peso_bebe_por_sexo.png')

plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median', 'Peso mediano', 'Escolaridade mãe', 'sort')
plt.savefig(f'./output/figs/{max_data}/peso_mediano_por_escolaridade_mae.png')

plota_pivot_table(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'Apgar1 médio', 'Gestação', 'sort')
plt.savefig(f'./output/figs/{max_data}/media_apgar1_por_gestacao.png')
