import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas 

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)


st.title('Análisis Denuncias Maltrato Animal')


left_column, right_column = st.columns(2)

@st.cache
def load_data():
    return pd.read_csv(r'C:\Users\samue\OneDrive\Documents\GitHub\captain_planet_sammy\captain-planet\analisis_maltrato_animal\data\clean\datos_corr_gral.csv',encoding='utf-8')

@st.cache
def load_social_data():
    return pd.read_csv(r'C:\Users\samue\OneDrive\Documents\GitHub\captain_planet_sammy\captain-planet\analisis_maltrato_animal\data\clean\datos_desarrollo',encoding='utf-8')

@st.cache
def load_map_data():
    return pd.read_csv(r'C:\Users\samue\OneDrive\Documents\GitHub\captain_planet_sammy\captain-planet\analisis_maltrato_animal\data\clean\mapas\para_los_mapas.csv',encoding='utf-8')

datos_corr = load_data()

datos_soc = load_social_data()

map_data = load_map_data()

columnas = ['colonia','alcaldia','num_denuncias','maltrato_fisico','intemperie_o_inmovilidad','subalimentacion']

left_column.subheader('Correlaciones')

option = left_column.selectbox(
     'Selecciona especificidad',
     ('Colonia', 'Alcaldia'))


if left_column.checkbox('Datos poblacionales'):
    columnas.extend(['poblacion_2010','superficie_metros_cuadrados','densidad'])
if left_column.checkbox('Unidades economicas'):
    columnas.extend(['unidades_economicas','industriales','comerciales','servicios'])
if left_column.checkbox('Carpetas de investigacion'):
    columnas.extend(['num_carpetas','num_carpetas_maltrato','num_carpetas_robo_animales'])

vista = datos_corr.loc[:,columnas]

if(option=='Alcaldia'):
    columnas.remove('colonia')
    vista = vista.groupby('alcaldia').sum()
    vista.reset_index(inplace=True)

    if('densidad' in vista.columns):
        vista['densidad']=vista['poblacion_2010'] / vista['superficie_metros_cuadrados']
    
    
    vista = pd.merge(vista, datos_soc, on='alcaldia')

    if left_column.checkbox('Desarrollo social telefonia', key='tel'):
        columnas.extend(['pctg_alto_tel', 'pctg_medio_tel', 'pctg_bajo_tel'])
    
    if left_column.checkbox('Desarrollo social vivienda', key='viv'):
        columnas.extend(['pctg_alto_viv', 'pctg_medio_viv', 'pctg_bajo_viv'])


vista = vista.loc[:,columnas]

fig = px.imshow(vista.corr(), text_auto=True, title='Heatmap Correlaciones')



right_column.plotly_chart(fig)


st.subheader('Mapas')

map_data.plot('densidad')
st.pyplot()

