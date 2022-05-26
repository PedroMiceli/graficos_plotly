import pandas as pd
from sqlalchemy import create_engine

def geradf():
    engine = create_engine('postgresql://psicomotricidade:psicomotricidade@172.16.4.190:5432/psicomotricidade_teste').connect()
    df = pd.read_sql_table('protocolos', engine)
    df = df.sort_values(by='id')
    return df

class separa_em_topicos:
    dataframe = geradf()

    def conceitos_filogeneticos(self, dataframe, id):
        df=self.dataframe[['id','paciente_id','rolar','engatinhar_quatro_apoios','rastejar','posicao_bipede','rolar']]
        df.columns = ['id', 'paciente_id', 'Rolar', 'Engatinhar em 4 apoios', 'Rastejar', 'Posicao bípede', 'Rolar']
        df=df[df['paciente_id']==id]
        return df.astype(int)

    def coordenacao_oculopedal_oculomanual(self, dataframe, id):
        df = self.dataframe[['id','paciente_id', 'apoio_unipodal_bracos_torax',
                             'saltar_dois_apoios', 'saltar_um_apoio','saltar_alternadamente',
                             'corrida_de_obstaculos','chutar_bola','atirar_bola',
                             'agilidade_movimentos_globais', 'apoio_unipodal_bracos_torax']]

        df.columns = ['id','paciente_id', 'Apoio unipodal c/ braços dobrados', 'Saltar com 2 apoios',
                      'Saltar com 1 apoio','Saltar alternadamente','Corrida de obstáculos','Chutar bola a cerca de 1m no alvo',
                      'Atirar bola a cerca de 1/5m no alvo','Agilidade nos movimentos globais', 'Apoio unipodal c/ braços dobrados']

        df = df[df['paciente_id'] == id]
        return df

    def extensibilidade_dos_membros(self, dataframe, id):
        df = self.dataframe[['id','paciente_id', 'balanco_passivo','acao_paratonia','relaxamento_passivo','sustentabilidade_bracos','sincinesias','persistencia_motora_global','freio_inibitorio','membros_inferiores','membros_superiores', 'balanco_passivo']]
        df.columns = ['id','paciente_id', 'Balanco passivo','Tônus de ação paratonia','Tônus de relaxamento passivo','Sustentabilidade dos braços','Sincinesias','Persistência motora global','Freio inibitório','Membros inferiores','Membros superiores', 'Balanco passivo']
        df = df[df['paciente_id'] == id]
        return df
    def intensidades_extensibilidade_dos_membros(self, dataframe, id):
        df = self.dataframe[['id', 'paciente_id', 'extensibilidade_membros_inferiores', 'extensibilidade_membros_superiores','extensibilidade_membros_inferiores']]
        df.columns = ['id', 'paciente_id', 'Extensibilidade dos membros inferiores','Extensibilidade dos membros superiores', 'Extensibilidade dos membros inferiores']
        df = df[df['paciente_id'] == id]
        return df
    def equilibrio_postural(self, dataframe, id):
        df = self.dataframe[['id','paciente_id', 'ponte_equilibrio_frente', 'ponte_equilibrio_tras', 'permanece_ponta_pes','ponte_equilibrio_frente']]
        df.columns = ['id','paciente_id', 'Ponte de equilíbrio frente', 'Ponte de equilíbrio trás', 'Permanece na ponta dos pés (10 seg)','Ponte de equilíbrio frente']
        df = df[df['paciente_id'] == id]
        return df



