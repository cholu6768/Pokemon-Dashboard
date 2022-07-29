#import libraries
import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.express as px 
from plotly.subplots import make_subplots
import plotly.graph_objects as go

#page setting
st.set_page_config(layout="wide")

#add a title 
st.markdown("<h1 style='text-align: center; color: gray;'>Pokemon Stats Dashboard</h1>", unsafe_allow_html=True)

#import data
pokemon = pd.read_csv('data/pokedex.csv')

#group by generation and then count pokemon per each generation
generations = pokemon.groupby(['generation'])['name'].count().reset_index()
generations = generations.rename(columns = {'name':'pokemon'})

#row 1
a1, a2 = st.columns(2)

#plot the bar graph
gen=['<b>Gen 1', '<b>Gen 2', '<b>Gen 3', '<b>Gen 4', '<b>Gen 5', '<b>Gen 6', '<b>Gen 7', '<b>Gen 8']

bar_chart = px.bar(generations, x=gen, y='pokemon', text='pokemon', title='<b>Pokemon by Generation',
            labels={'x':'<b>Generation', 'pokemon':'<b>Number of Pokemon'})

bar_chart.update_traces(
    textposition='outside', 
    marker_color='#7f9ebf', 
    width=0.7, 
    marker=dict(
        color='#7f9ebf',
        line=dict(
            color='#141414',
            width=1.5
        )
    ))

bar_chart.update_layout(width=600, height=500)

bar_chart.update_xaxes(showline=True, linewidth=0.8, linecolor='#dcdcdc', mirror=True, ticks='outside')
bar_chart.update_yaxes(showline=True, linewidth=0.8, linecolor='#dcdcdc', mirror=True, ticks='outside')

bar_chart.update_layout(
    font_family="Benton Sans Low-DPI",
    font_color="#141414",
    title_font_family="Trebuchet MS",
    title_font_color="black",
    plot_bgcolor='rgba(0,0,0,0)') 

a1.plotly_chart(bar_chart)


#group by generation and average of each stat per generation
average_stats = pokemon.groupby(['generation'])[['attack','defense', 'hp' ,'sp_attack', 'sp_defense', 'speed']].mean().reset_index()

#rename columns
average_stats = average_stats.rename(columns = {'attack':'Avg. Attack', 
                                                'defense':'Avg. Defense', 
                                                'hp':'Avg. HP', 
                                                'sp_attack':'Avg. Sp Atk',
                                                'sp_defense':'Avg. Sp Def',
                                                'speed':'Avg. Speed'})

#round avg values to 2 decimals                                               
cols = ['Avg. Attack', 'Avg. Defense', 'Avg. HP', 'Avg. Sp Atk',
       'Avg. Sp Def', 'Avg. Speed']
average_stats[cols] = average_stats[cols].round(2)


#subplot line charts
gen=['<b>Gen 1', '<b>Gen 2', '<b>Gen 3', '<b>Gen 4', '<b>Gen 5', '<b>Gen 6', '<b>Gen 7', '<b>Gen 8']

line_chart = make_subplots(
                rows=1, cols=6, 
                shared_yaxes=True,
                subplot_titles=('<b>Avg. Attack', '<b>Avg. Defense', '<b>Avg. HP', '<b>Avg. Sp Atk', '<b>Avg. Sp Def', '<b>Avg. Speed'))

line_chart.add_trace(go.Scatter(x=gen, y=average_stats['Avg. Attack'], line=dict(color='#e15a5c', width=3)),
              row=1, col=1)

line_chart.add_trace(go.Scatter(x=gen, y=average_stats['Avg. Defense'], line=dict(color='#e15a5c', width=3)),
              row=1, col=2)

line_chart.add_trace(go.Scatter(x=gen, y=average_stats['Avg. HP'], line=dict(color='#e15a5c', width=3)),
              row=1, col=3)

line_chart.add_trace(go.Scatter(x=gen, y=average_stats['Avg. Sp Atk'], line=dict(color='#e15a5c', width=3)),
              row=1, col=4)

line_chart.add_trace(go.Scatter(x=gen, y=average_stats['Avg. Sp Def'], line=dict(color='#e15a5c', width=3)),
              row=1, col=5)

line_chart.add_trace(go.Scatter(x=gen, y=average_stats['Avg. Speed'], line=dict(color='#e15a5c', width=3)),
              row=1, col=6)

#update xaxis properties
line_chart.update_xaxes(showline=True, linewidth=0.8, linecolor='#dcdcdc', mirror=True, ticks='outside', tickangle = 270, tickfont=dict(family="Benton Sans Low-DPI", size=13),row=1, col=1)
line_chart.update_xaxes(showline=True, linewidth=0.8, linecolor='#dcdcdc', mirror=True, ticks='outside', tickangle = 270, row=1, col=2)
line_chart.update_xaxes(showline=True, linewidth=0.8, linecolor='#dcdcdc', mirror=True, ticks='outside', tickangle = 270, row=1, col=3)
line_chart.update_xaxes(showline=True, linewidth=0.8, linecolor='#dcdcdc', mirror=True, ticks='outside', tickangle = 270, row=1, col=4)
line_chart.update_xaxes(showline=True, linewidth=0.8, linecolor='#dcdcdc', mirror=True, ticks='outside', tickangle = 270, row=1, col=5)
line_chart.update_xaxes(showline=True, linewidth=0.8, linecolor='#dcdcdc', mirror=True, ticks='outside', tickangle = 270, row=1, col=6)

#update yaxis properties
line_chart.update_yaxes(showline=True, linewidth=0.8, linecolor='#dcdcdc', mirror=True, ticks='outside', row=1, col=1)
line_chart.update_yaxes(showline=True, linewidth=0.8, linecolor='#dcdcdc', mirror=True, row=1, col=2)
line_chart.update_yaxes(showline=True, linewidth=0.8, linecolor='#dcdcdc', mirror=True, row=1, col=3)
line_chart.update_yaxes(showline=True, linewidth=0.8, linecolor='#dcdcdc', mirror=True, row=1, col=4)
line_chart.update_yaxes(showline=True, linewidth=0.8, linecolor='#dcdcdc', mirror=True, row=1, col=5)
line_chart.update_yaxes(showline=True, linewidth=0.8, linecolor='#dcdcdc', mirror=True, row=1, col=6)

#add average horizontal line 
line_chart.add_hline(y=80.52,annotation_text='<b>Average', annotation_position="top left", row=1, col=1)
line_chart.add_hline(y=75.31,annotation_text='<b>Average', annotation_position="top left", row=1, col=2)
line_chart.add_hline(y=70.62,annotation_text='<b>Average', annotation_position="top left", row=1, col=3)
line_chart.add_hline(y=73.37,annotation_text='<b>Average', annotation_position="top left", row=1, col=4)
line_chart.add_hline(y=73.07,annotation_text='<b>Average', annotation_position="top left", row=1, col=5)
line_chart.add_hline(y=68.51,annotation_text='<b>Average', annotation_position="top left", row=1, col=6)

#update plot layout
line_chart.update_layout(
                height=500, width=800,
                title_text='<b>Avg Stat Trends',
                yaxis_title='<b>Attributes',
                showlegend=False,
                font_family='Benton Sans Low-DPI',
                font_color='black',
                title_font_family='Trebuchet MS',
                title_font_color='black',
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgb(255,255,255)')


a2.plotly_chart(line_chart)

#row 2

#draw the table 
table_chart = go.Figure(data=[go.Table(
    header=dict(values=['<b>Number', '<b>Name', '<b>Attack', '<b>Defense', '<b>HP', '<b>Sp Atk', '<b>Sp Def'],
                fill_color='white',
                align='center'),
    cells=dict(values=[pokemon.pokedex_number, pokemon.name, pokemon.attack, pokemon.defense, pokemon.hp, pokemon.sp_attack, pokemon.sp_defense],
               fill_color='white',
               align='left'))
])

table_chart.update_layout(width=1500, height=600, title_text='<b>Pokemon by Stat')

st.plotly_chart(table_chart)
