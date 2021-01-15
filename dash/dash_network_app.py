import dash
import dash_cytoscape as cyto
import dash_html_components as html

app = dash.Dash(__name__)

data = [
            {'data': {'id': 'one', 'label': 'created'}, 'position': {'x': 75, 'y': 75}},
            {'data': {'id': 'two', 'label': 'assign'}, 'position': {'x': 200, 'y': 200}},
            {'data': {'id': 'three', 'label': 'pause'}, 'position': {'x': 200, 'y': 200}},
            {'data': {'id': 'four', 'label': 'assign'}, 'position': {'x': 200, 'y': 200}},
            {'data': {'source': 'one', 'target': 'two', 'label': 40}},
            {'data': {'source': 'two', 'target': 'three'}},
            {'data': {'source': 'three', 'target': 'four'}}
]

app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-two-nodes',
        layout={'name': 'grid'},
        style={'width': '100%', 'height': '400px'},
        elements=data,
            stylesheet=[
        {
            'selector': '[label = "assign"]',
            'style': {
                'background-color': '#FF4136',
                'label': 'data(label)'
                }
        },
           {
            'selector': 'edge',
            'style': {
                'label': 'data(label)',
                'position': {'y': 10}
                }
        },

        ]

    )
])

if __name__ == '__main__':
    app.run_server(debug=True)