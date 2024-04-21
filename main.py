# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:44:38 2023

@author: Labtop
"""
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy
from plotly.subplots import make_subplots
from PIL import Image
import os
import numpy as np
st.set_page_config(layout="wide", page_title='Emission Inventory of Khon Kean Province', page_icon=":mortar_board:")
st.sidebar.markdown("Home Page")


# =============================================================================
# Template
# =============================================================================
css_file = r'styles/main.css'
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


st.header('Emission Inventory of Khon Kean Province')

st.caption('For more information and details contact: Ekbordinw@ait.asia or pongsakon@ait.asia')



df = pd.read_excel(r'./csv_for_WEDAPP/_emissioninventory_static_khonkean.xlsx')
left_column, right_column = st.columns(2)
choice_left = df.columns[1:]
choice_selected_left = left_column.selectbox("Select the pollutant types", choice_left)

choice_right = ['All']
for i in df['Sectors'].to_list():
    choice_right.append(i)
choice_selected_right = right_column.multiselect("Select the sector types", choice_right, default=['All'])

df_selected = pd.DataFrame()
if 'All' in choice_selected_right:
    df_selected = df.copy()
    df.replace(0, np.nan, inplace=True)
else:
    for se in choice_selected_right:
        da = df[df['Sectors'] == se]
        df_selected = pd.concat([df_selected,da])

st.subheader(f"{choice_selected_left} Emissions (by Sector)")      
fig = go.Figure(
    go.Pie(labels=df_selected.iloc[:,0], values=df_selected[choice_selected_left])
)
fig.update_layout(
    paper_bgcolor="black",
    width=400,
    height=800,
)
fig.update_traces(textfont_size=14)  # Adjust font size as desired
fig.update_layout(margin={"r": 0, "t": 150, "l": 0, "b": 0})

st.plotly_chart(fig, use_container_width=True)