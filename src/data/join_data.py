import glob
import pandas as pd

def data_append():
    path = "/home/eraylson/aula_mlops/data/raw"
    path_pattern = path + "/*.parquet.gzip"

    lista_paths = glob.glob(path_pattern)
    lista_dfs = []
    for file in lista_paths:
        df = pd.read_parquet(file)
        lista_dfs.append(df)
    
    df_appended = pd.concat(lista_dfs, ignore_index=True)
    path_to_save = "/home/eraylson/aula_mlops/data/processed/"
    df_appended.to_parquet(path_to_save+"df_appended.parquet.gzip", compression='gzip')

data_append()