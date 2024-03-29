import pandas as pd
import os
import re
from dash import html, dash_table, dcc, callback, Output, Input
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash

PATH_REGRESSION = "C:\\git\\Trex\\hackthon\\Hackathon_PB04\\PROJECT1\\REGR_STATUS_RTL\\"
PATH_REGRESSION_OUT = "C:\git\Trex\hackthon\out\REGR_STATUS_RTL\\"

# def extract_date(log):
#     if isinstance(log, str):
#         match = re.search(r'(\d{2}_\d{2}_\d{2})', log)
#     #print(match)
#         if match:
#             date = match.group()
#             formatted_date = date.replace('_', '-')
#             return formatted_date
#         else:
#             return None
#     else:
#         return None

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Incorporate data

# Initialize the app
app = DjangoDash('regression', external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Regression Graph'),
    dcc.Graph(id='graph1', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
    dcc.Graph(id='graph2', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
    dcc.Graph(id='graph3', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
    dcc.Graph(id='graph4', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),

    dcc.Slider(
        id='slider-updatemode',
        marks={i: '{}'.format(i) for i in range(20)},
        max=20,
        value=2,
        step=1,
        updatemode='drag',
    ),
])


@app.callback(
    [Output('graph1', 'figure'),
     Output('graph2', 'figure'),
     Output('graph3', 'figure'),
     Output('graph4', 'figure'),
    ],
    [Input('slider-updatemode', 'value')]
    )
def display_value(value):
    # sam_path = PATH_REGRESSION
    result_df = pd.DataFrame()
    # for filename in os.listdir(sam_path):
    #     file_path = os.path.join(sam_path, filename)
    #     if os.path.isfile(file_path) and os.path.getsize(file_path) > 0:
    #         df = pd.read_csv(sam_path + "\\" + filename, on_bad_lines='skip')
    #         df['DateTime'] = extract_date(df.iloc[0]['Log'])
    #         #print(df.iloc[0]['DateTime'])
    #         df['Status'] = df['Status'].replace(['make_error', 'timeout', 'tool_failure', 'expected_failure'], 'failed')
    #         short = df.groupby('Category')['Status'].value_counts().unstack(fill_value=0).reset_index()
    #         owners = df.groupby('Category')['Owner'].first().reset_index(name='Owner')
    #         short = pd.merge(short, owners, on='Category')
    #         short["DateTime"] = df.iloc[0]['DateTime']
    #         result_df = pd.concat([result_df, short], ignore_index=True)
    #         #result_df.reset_index(drop=True)
    #     else:
    #         print(f"File '{filename}' is empty or doesn't exist.")
            
    # out_sam_path = "C:\\git\\Trex\\hackthon\\out\\COV_STATUS_TOGGLE"
    # if not os.path.exists(out_sam_path):
    #     os.makedirs(out_sam_path)
    #     result_df.to_csv(os.path.join(out_sam_path, 'result_df.csv'), index=False)
    #     result_df.to_csv("C:\\git\\Trex\\hackthon\\out\\COV_STATUS_TOGGLE\\",sep=',')
    out_sam_path = PATH_REGRESSION_OUT
    filename_cat_vs_status = "CategoryVsStatus.csv"
    cat_vs_status_df = pd.read_csv(out_sam_path + "\\" + filename_cat_vs_status, on_bad_lines='skip')
    x1 = cat_vs_status_df['Category']
    y1_passed = cat_vs_status_df['passed']
    y1_failed = cat_vs_status_df['failed']
    
    graph11 = go.Bar(x=x1, y=y1_passed, name='Passed')#, marker=dict(color='green')
    graph12 = go.Bar(x=x1, y=y1_failed, name='Failed')#, marker=dict(color='red')
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
    
    graph21 = go.Bar(x=x2, y=y2_passed, name='Passed')#, marker=dict(color='green')
    graph22 = go.Bar(x=x2, y=y2_failed, name='Failed')#, marker=dict(color='red')
    layout2 = go.Layout(
        title='Owner Vs Status',
        xaxis_title='Owner',
        yaxis_title='Status : Passed/Failed',
        font=dict(color='black'),
        barmode='stack'
    )
    
    filename_week_vs_status = "WeekVsStatus.csv"
    week_vs_status_df = pd.read_csv(out_sam_path + "\\" + filename_week_vs_status, on_bad_lines='skip')
    x3 = week_vs_status_df['Week_Number']
    y3_passed = week_vs_status_df['passed']
    y3_failed = week_vs_status_df['failed']
    
    graph31 = go.Bar(x=x3, y=y3_passed, name='Passed')#, marker=dict(color='green')
    graph32 = go.Bar(x=x3, y=y3_failed, name='Failed')#, marker=dict(color='red')

    layout3 = go.Layout(
        title='Owner Vs Status',
        xaxis_title='Owner',
        yaxis_title='Status : Passed/Failed',
        font=dict(color='black'),
        barmode='stack'
    )
    
    filename_month_vs_status = "MonthVsStatus.csv"
    month_vs_status_df = pd.read_csv(out_sam_path + "\\" + filename_month_vs_status, on_bad_lines='skip')
    x4 = month_vs_status_df['Month_Number']
    y4_passed = month_vs_status_df['passed']
    y4_failed = month_vs_status_df['failed']
    
    graph41 = go.Bar(x=x4, y=y4_passed, name='Passed')#, marker=dict(color='green')
    graph42 = go.Bar(x=x4, y=y4_failed, name='Failed')#, marker=dict(color='red')
    layout4 = go.Layout(
        title='Owner Vs Status',
        xaxis_title='Owner',
        yaxis_title='Status : Passed/Failed',
        font=dict(color='black'),
        barmode='stack'
    )

    return [{'data': [graph11,graph12], 'layout': layout1},
            {'data': [graph21,graph22], 'layout': layout2},
            {'data': [graph31,graph32], 'layout': layout3},
            {'data': [graph41,graph42], 'layout': layout4}]