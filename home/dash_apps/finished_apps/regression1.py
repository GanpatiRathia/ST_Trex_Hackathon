import pandas as pd
import os
import re
from dash import html, dash_table, dcc, callback, Output, Input
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash

PATH_REGRESSION = "C:\\git\\Trex\\hackthon\\Hackathon_PB04\\PROJECT1\\REGR_STATUS_RTL\\"
PATH_REGRESSION_OUT = "C:\git\Trex\hackthon\out\REGR_STATUS_RTL\\"

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Incorporate data
out_sam_path = PATH_REGRESSION_OUT
# Initialize the app
app = DjangoDash('regression1', external_stylesheets=external_stylesheets)

filename_cat_vs_status = "CategoryVsStatus.csv"
cat_vs_status_df = pd.read_csv(out_sam_path + "\\" + filename_cat_vs_status, on_bad_lines='skip')
x1 = cat_vs_status_df['Category']
y1_passed = cat_vs_status_df['passed']
y1_failed = cat_vs_status_df['failed']

graph11 = go.Bar(x=x1, y=y1_passed, name='Passed')
graph12 = go.Bar(x=x1, y=y1_failed, name='Failed')
layout1 = go.Layout(
    title='Category Vs Status',
    xaxis_title='Category',
    yaxis_title='Status : Passed/Failed',
    font=dict(color='black'),
    barmode='stack'
)

filename_owner_vs_status = "OwnerVsStatus.csv"
owner_vs_status_df = pd.read_csv(out_sam_path + "\\" + filename_owner_vs_status, on_bad_lines='skip')
x2 = owner_vs_status_df['Owner']
y2_passed = owner_vs_status_df['passed']
y2_failed = owner_vs_status_df['failed']

graph21 = go.Bar(x=x2, y=y2_passed, name='Passed')
graph22 = go.Bar(x=x2, y=y2_failed, name='Failed')
layout2 = go.Layout(
    title='Owner Vs Status',
    xaxis_title='Owner',
    yaxis_title='Status : Passed/Failed',
    font=dict(color='black'),
    barmode='stack'
)

app.layout = html.Div([
    html.Div([
        html.Div([
            html.H1('Category Vs Status'),
            dcc.Graph(id='graph1', figure={'data': [graph11, graph12], 'layout': layout1})
        ], className='row'),
    ], className='row'),
    html.Div([
        html.Div([
            html.H1('Owner Vs Status'),
            dcc.Graph(id='graph2', figure={'data': [graph21, graph22], 'layout': layout2})
        ], className='row')
    ], className='row'),
    html.H1('Owner Vs Status'),
    dcc.RadioItems(
        id='time-period',
        options=[
            {'label': 'Week', 'value': 'week'},
            {'label': 'Month', 'value': 'month'}
        ],
        value='week'
    ),
    dcc.Graph(id='graph')
])

@app.callback(Output('graph', 'figure'), [Input('time-period', 'value')])
def update_figure(selected_period):
    if selected_period == 'week':
        filename = "WeekVsStatus.csv"
    else:
        filename = "MonthVsStatus.csv"

    df = pd.read_csv(out_sam_path + "\\" + filename, on_bad_lines='skip')
    x = df['Week_Number' if selected_period == 'week' else 'Month_Number']
    y_passed = df['passed']
    y_failed = df['failed']

    graph1 = go.Bar(x=x, y=y_passed, name='Passed')
    graph2 = go.Bar(x=x, y=y_failed, name='Failed')

    layout = go.Layout(
        title='Owner Vs Status',
        xaxis_title='Owner',
        yaxis_title='Status : Passed/Failed',
        font=dict(color='black'),
        barmode='stack'
    )

    return {'data': [graph1, graph2], 'layout': layout}