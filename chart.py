import plotly.express as px
import pandas as pd

def Jogador(atributo1:int,atributo2:int,atributo3:int,atributo4:int,nome:str,sobrenome:str):
    Titulo = "Jogador "+nome+" "+sobrenome
    df = pd.DataFrame(dict(
        r=[atributo1, atributo2, atributo3, atributo4],
        theta=['atributo1','atributo2','atributo3',
            'atributo4']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True,title = Titulo)
    fig.write_image("yourfile.png") 
