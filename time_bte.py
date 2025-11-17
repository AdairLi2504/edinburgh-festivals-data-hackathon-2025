import pandas as pd
from dateutil import parser
from datetime import date
import segment
import membership

def get_tbte_ap(data:pd.DataFrame):
    tbte_ap = []
    for row in data.itertuples():
        if membership.isAP(row.membership):
            tbte_ap.append(row.event_d_t-row.transaction_d_t)
    return tbte_ap

def get_tbte_nonap(data:pd.DataFrame):
    tbte_ap = []
    for row in data.itertuples():
        if not(membership.isAP(row.membership)):
            tbte_ap.append(row.event_d_t-row.transaction_d_t)
    return tbte_ap

def get_tbte_membership(data:pd.DataFrame):
    tbte_membership = {}
    for i in membership.memberships:
        tbte_membership[i] = []
    for row in data.itertuples():
        tbte_membership[membership.deformat_membership(row.membership)].append(row.event_d_t-row.transaction_d_t)
    return tbte_membership