import pandas as pd

def deformat_genre(raw:str)->str:
    return raw[4:]

def get_all_genres(data:pd.DataFrame):
    genres = []
    for row in data.itertuples():
        if not( deformat_genre(row.genre) in genres):
            genres.append(deformat_genre(row.genre))
    return genres
