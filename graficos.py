import plotly.graph_objects as go
import plotly.express as px

def gerar_radar(dataframe, nome):
    categorias = dataframe[0].columns.values
    fig = go.Figure()

    conta = 0
    for i in dataframe:

        valores = None
        for itens in i.values:
            valores = itens

        fig.add_trace(go.Scatterpolar(
            r=valores,
            theta=categorias,
            opacity= 1,
            fill='none',
            name= f'{conta+1}ª passagem'
        ))
        conta += 1

    fig.update_layout(
        template= 'xgridoff',
        polar=dict(
            radialaxis_showline= True,
            angularaxis_tickfont=dict(size=16),
            radialaxis_showticklabels= True,
            radialaxis_angle= -45,
            radialaxis_categoryarray= None,
            radialaxis_dtick= 1,
            radialaxis=dict(visible=True,
                            range=[0, 4])),
        showlegend=True,
    )

    with open('p_graph.html', 'a') as f:
        f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))





