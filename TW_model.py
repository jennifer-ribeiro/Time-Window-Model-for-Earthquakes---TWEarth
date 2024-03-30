#%%

import pandas as pd

df_original = pd.read_csv('/media/jennifer/HD_Externo_JENNIFER/DOC_COMP_LAB/Documents/DOUTORADO/R_codes/Redes_Terremotos/TW/Dados_Mundo_2000_2019_Mag55_SHALLOW.csv')

df_original['Event'] = range(1, len(df_original) + 1)


# %%

win = 3800

results = []

for index in range(( len(df_original) - 1 )):
    row_original = df_original.iloc[index]
    id_bairro_original = row_original['Site_Numb']
    tempo_min_original = row_original['Time']
    id_event_original = row_original['Event']
    
    index2 = index + 1
    row_next = df_original.iloc[index2]
    id_bairro_next = row_next['Site_Numb']
    tempo_min_next = row_next['Time']
    id_event_next = row_next['Event']

    while ( (tempo_min_next - tempo_min_original) <= win )  or index2 == len(df_original):
        #print(tempo_min_next - tempo_min_original)
        results.append(
            {
            'Site_Numb1': id_bairro_original,
            'Time1': tempo_min_original,
            'Site_Numb2': id_bairro_next,
            'Time2': tempo_min_next,
            'Tempo_diff': (tempo_min_next - tempo_min_original),
            'Event1': id_event_original,
            'Event2': id_event_next,
            }
        )

        index2 += 1

        #print(index2)

        if (index2 >= len(df_original)):
            break
        else:
            row_next = df_original.iloc[index2]
            id_bairro_next = row_next['Site_Numb']
            tempo_min_next = row_next['Time']
            id_event_next = row_next['Event']


df_results = pd.DataFrame(results)

arestas = df_results.loc[:, ~df_results.columns.isin(['Time1', 'Time2', 'Tempo_diff', 'Event1', 'Event2'])]
arestas = arestas.rename(columns={'Site_Numb1': 'source', 'Site_Numb2': 'target'}, inplace=False)

arestas_event = df_results.loc[:, ~df_results.columns.isin(['Time1', 'Time2', 'Tempo_diff', 'Site_Numb1', 'Site_Numb2'])]
arestas_event = arestas_event.rename(columns={'Event1': 'source', 'Event2': 'target'}, inplace=False)

arestas.to_csv('arestas_win_'+str(win)+'s_Shallow_Mag55_2000_2019_Python.csv',index=False)

arestas_event.to_csv('arestas_EVENT_win_'+str(win)+'s_Shallow_Mag55_2000_2019_Python.csv',index=False)

# %%

############# VARIOUS WINDOWS ################

for win in range(4700,8100,100):

    results = []

    for index in range(( len(df_original) - 1 )):
        row_original = df_original.iloc[index]
        id_bairro_original = row_original['Site_Numb']
        tempo_min_original = row_original['Time']
        id_event_original = row_original['Event']
        
        index2 = index + 1
        row_next = df_original.iloc[index2]
        id_bairro_next = row_next['Site_Numb']
        tempo_min_next = row_next['Time']
        id_event_next = row_next['Event']

        while ( (tempo_min_next - tempo_min_original) <= win )  or index2 == len(df_original):
            #print(tempo_min_next - tempo_min_original)
            results.append(
                {
                'Site_Numb1': id_bairro_original,
                'Time1': tempo_min_original,
                'Site_Numb2': id_bairro_next,
                'Time2': tempo_min_next,
                'Tempo_diff': (tempo_min_next - tempo_min_original),
                'Event1': id_event_original,
                'Event2': id_event_next,
                }
            )

            index2 += 1

            #print(index2)

            if (index2 >= len(df_original)):
                break
            else:
                row_next = df_original.iloc[index2]
                id_bairro_next = row_next['Site_Numb']
                tempo_min_next = row_next['Time']
                id_event_next = row_next['Event']


    df_results = pd.DataFrame(results)

    arestas = df_results.loc[:, ~df_results.columns.isin(['Time1', 'Time2', 'Tempo_diff', 'Event1', 'Event2'])]
    arestas = arestas.rename(columns={'Site_Numb1': 'source', 'Site_Numb2': 'target'}, inplace=False)

    arestas_event = df_results.loc[:, ~df_results.columns.isin(['Time1', 'Time2', 'Tempo_diff', 'Site_Numb1', 'Site_Numb2'])]
    arestas_event = arestas_event.rename(columns={'Event1': 'source', 'Event2': 'target'}, inplace=False)

    arestas.to_csv('arestas_win_'+str(win)+'s_Shallow_Mag5_2000_2019_Python.csv',index=False)

    arestas_event.to_csv('arestas_EVENT_win_'+str(win)+'s_Shallow_Mag5_2000_2019_Python.csv',index=False)
# %%
