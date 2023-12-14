import yfinance as yf
import pandas as pd




def download_data(symbols, start_date, end_date):
    path = '/home/eraylson/aula_mlops/data/raw/'
    for symbol in symbols:
        path_full = path+symbol+'.parquet.gzip'
        
        df = yf.download(symbol, start=start_date, end=end_date)
        if df.shape[0] == 0:
            print(f"A base {symbol} não está disponivel ")
        else:
            df['Name'] = symbol
            df.to_parquet(path_full, compression='gzip')
        

symbols = ['BTC-USD', 'ETH-USD', 'USDT-USD', 'SOL-USD', 'DOGE-USD']
start_date = '2018-01-01'
end_date = '2023-11-29'

download_data(symbols, start_date, end_date)
