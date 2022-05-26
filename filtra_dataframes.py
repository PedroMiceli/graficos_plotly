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


relatorio1 = separa_dataframes(separa_em_topicos().coordenacao_oculopedal_oculomanual(geradf(), id))
relatorio2 = separa_dataframes(separa_em_topicos().conceitos_filogeneticos(geradf(), id))
gerar_radar(relatorio1, 'Coordenacao')
gerar_radar(relatorio2, 'filo')
