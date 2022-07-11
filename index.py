import dash_core_components as dcc
import dash_html_components as html
import os
from dash.dependencies import Input, Output

from app import app
from app import server

from layouts import regions, keyapps, themes, legacy, sla, compare
import callbacks    
menulinks = {'/ServiceNowDashboard/' : regions, 
             '/ServiceNowDashboard/regions' : regions,
              '/ServiceNowDashboard/keyapps' : keyapps,
              '/ServiceNowDashboard/legacy' : legacy,
              '/ServiceNowDashboard/sla' : sla,
              '/ServiceNowDashboard/compare' : compare,
              '/ServiceNowDashboard/themes' : themes,}

#Application Layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
    ])
                
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    try:
        path = menulinks[pathname]
        return path
    except KeyError:
            return "404 Page Error! Please choose a link"

port = int(os.getenv('PORT', 8000))

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=port, debug=False)
    # app.run_server(debug=False, host=('0.0.0.0'))
