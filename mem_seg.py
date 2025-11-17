import pandas as pd

import membership


def get_relations_membership_subsegment(data:pd.DataFrame):
    membership_subsegment = []
    for row in data.itertuples():
        membership_subsegment.append((membership.deformat_membership(row.membership),row.subsegment if row.subsegment == row.subsegment else 'Non' ,row.ticket_count))
    return membership_subsegment

def get_number_membership_subsegment(membership:str,subsegment:str,data:pd.DataFrame):
    n = 0 
    for i in get_relations_membership_subsegment(data):
        if (membership,subsegment) == (i[0],i[1]):
            n += i[2]
    return n
