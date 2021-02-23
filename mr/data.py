import pandas as pd


def get_data():
    '''
    Gets notebook movie dataframe
    '''
    mdf = pd.read_csv('./notebooks/mdf.csv')
    final_dataset = pd.read_csv('./notebooks/final_dataset.csv')
    poster_data = pd.read_csv('./notebooks/links_copy.csv')
    
    return mdf, final_dataset, poster_data
