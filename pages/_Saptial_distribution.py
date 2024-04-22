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
# Data Downloading
# =============================================================================

json1 = r"csv_for_WEDAPP/base.json"
with open(json1) as response:
    geo = json.load(response)

left_column, right_column = st.columns(2)
list_file = {'All sectors':'all',
             'Air Traffic' : 'air',
             'Construction' : 'cst', 
             'Gasoline Station' : 'gsl',
             'Insdustry' : 'ind',
             'Live Stock' : 'lis',
             'Power Plant' : 'pwp',
             'Railway' : 'rai',
             'Residentail' : 'rds',
             'Waste Open Burning' : 'wob'}

choice_left = list_file.keys()
choice_selected_left = left_column.selectbox("Select the sector", choice_left)

df = pd.read_csv(rf'csv_for_WEDAPP/{list_file.get(choice_selected_left)}.csv')
choice_right = df.columns[1:]
choice_selected_right = right_column.selectbox("Select the pollutant types", choice_right)

fig = go.Figure(
go.Choroplethmapbox(
    geojson= geo,
    locations=df['Id'],
    featureidkey="properties.Id",
    z=df[choice_selected_right],
    colorscale="sunsetdark",
    # zmin=0,
    # zmax=500000,
    marker_opacity=0.5,
    marker_line_width=0,
)
)
fig.update_layout(
paper_bgcolor="Black",
mapbox_style="carto-positron",
mapbox_zoom=8,
mapbox_center={"lat": 16.382, "lon": 102.7},
width=800,
height=600,
)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
st.plotly_chart(fig, use_container_width=True)