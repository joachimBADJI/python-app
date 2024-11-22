import streamlit as st
import pandas as pd
import geopandas as gpd
import folium as fl
from streamlit_folium import st_folium
st.set_page_config(layout="wide")
tb=gpd.read_file("https://raw.githubusercontent.com/tommyscodebase/12_Days_Geospatial_Python_Bootcamp/refs/heads/main/13_final_project_data/world.geojson")
dt=pd.read_csv("https://raw.githubusercontent.com/tommyscodebase/12_Days_Geospatial_Python_Bootcamp/main/13_final_project_data/world_population.csv")
done=dt[dt['Country/Territory'].isin(tb['name'])]['Country/Territory'].unique()
sele = st.selectbox('# **Sélectionne un pays**', options=done)
col1, col2 = st.columns([1, 1])
with col1:    
    an=['2022 Population','2020 Population','2015 Population','2010 Population','2000 Population','1990 Population','1980 Population','1970 Population']
    p_pop = dt[dt['Country/Territory'] == sele][an]
    an_mul=st.multiselect(f"**Population du {sele}**",options=an,default=an)
    pop_mul=p_pop[an_mul]
    st.markdown(f"##### **Population de {sele} selon l' ou les années**")
    st.bar_chart(pop_mul.T)

with col2:
    pays = tb[tb['name'] == sele]
    pa_ar=dt[dt['Country/Territory'] == sele]['Area (km²)'].values[0]
    pa_de=dt[dt['Country/Territory'] == sele]['Density (per km²)'].values[0]
    pa_gr=dt[dt['Country/Territory'] == sele]['Growth Rate'].values[0]
    pa_wo=dt[dt['Country/Territory'] == sele]['World Population Percentage'].values[0]
    st.markdown('#### Statistiques du pays')
    st.text(f'La superficie du pays est de {pa_ar} km²')
    st.text(f'La densité est de {pa_de} par km²')
    st.text(f'Le taux de croissance est de {pa_gr}')
    st.text(f'Son pourcentage par rapport au monde est de {pa_wo} %')
    m = fl.Map(location=[pays.geometry.centroid.y.values[0], pays.geometry.centroid.x.values[0]], zoom_start=5)
    fl.GeoJson(pays).add_to(m)
    st_folium(m, width=700, height=500)