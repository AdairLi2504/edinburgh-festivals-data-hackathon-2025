import pandas as pd
import membership

import genre


def get_relations_membership_genre(data:pd.DataFrame):
    membership_genre = []
    for row in data.itertuples():
        membership_genre.append((genre.deformat_genre(row.genre),membership.deformat_membership(row.membership),row.ticket_count))
    return membership_genre

def get_number_membership_genre(membership:str,genre:str,data:pd.DataFrame):
    n = 0
    for i in get_relations_membership_genre(data):
        if (genre,membership) == (i[0],i[1]):
            n += i[2]
    return n
