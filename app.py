from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import mysql
import mysql_utils

app = Dash()
user = 'root'
password = 'root_user'
port = '127.0.0.1'

app.layout = [
    html.Div(children = 'Title')
]

if __name__ == '__main__':
    mysql_utils.initialize_database(user, password, port)
    app.run(debug=True)