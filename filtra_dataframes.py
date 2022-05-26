import dataframes
import graficos
from dataframes import separa_em_topicos
from dataframes import geradf
from graficos import *
import time

def separa_dataframes(df):
    df = df
    df_int= int(df.__len__())

    posicoes = []
    for i in df['id']:
        posicoes.append(i)

    if df_int <= 1:

        print('dados insuficientes')

    elif df_int == 2:

        df1= df[df['id']==posicoes[0]]
        df2 = df[df['id'] == posicoes[1]]
        df1 = df1.drop(columns=['id','paciente_id'])
        df2 = df2.drop(columns=['id', 'paciente_id'])
        frames = [df1,df2]
        return frames

    elif df_int == 3:

        df1 = df[df['id'] == posicoes[0]]
        df2 = df[df['id'] == posicoes[1]]
        df3 = df[df['id'] == posicoes[2]]
        df1 = df1.drop(columns=['id', 'paciente_id'])
        df2 = df2.drop(columns=['id', 'paciente_id'])
        df3 = df3.drop(columns=['id', 'paciente_id'])
        frames = [df1, df2, df3]
        return frames

    elif df_int == 4:

        df1 = df[df['id'] == posicoes[0]]
        df2 = df[df['id'] == posicoes[1]]
        df3 = df[df['id'] == posicoes[2]]
        df4 = df[df['id'] == posicoes[3]]
        df1 = df1.drop(columns=['id', 'paciente_id'])
        df2 = df2.drop(columns=['id', 'paciente_id'])
        df3 = df3.drop(columns=['id', 'paciente_id'])
        df4 = df4.drop(columns=['id', 'paciente_id'])
        frames = [df1, df2, df3, df4]
        return frames


id= 5

#---------------Dataframes para Radares-----------------
relatorio1 = separa_dataframes(separa_em_topicos().conceitos_filogeneticos(geradf(), id))
relatorio2 = separa_dataframes(separa_em_topicos().coordenacao_oculopedal_oculomanual(geradf(), id))
relatorio3 = separa_dataframes(separa_em_topicos().extensibilidade_dos_membros(geradf(), id))
relatorio4 = separa_dataframes(separa_em_topicos().equilibrio_postural(geradf(), id))

#-------------Dataframes para Barras--------------------


os.remove('templates/graficos.html')
f = open('templates/Graficos_arquivo_descartavel.html', 'w')
graficos = """<html>
    <head>
    <title>Graficos</title>
    </head>
    <body>
    <h2>Bem vindo aos Graficos Opentech</h2>

    <p>Default code has been loaded into the Editor.</p>

    </body>
    </html>
    """
f.write(f'templates/{graficos}')
f.close()




gerar_radar(relatorio1, 'Conceitos Filogenéticos')
gerar_radar(relatorio2, 'Coordenacão Óculopedal/Óculomanual')

gerar_radar(relatorio3, 'Extensibilidade dos Membros')
gerar_radar(relatorio4, 'Equilíbrio Postural')
