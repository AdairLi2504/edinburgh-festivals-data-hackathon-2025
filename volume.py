import pandas as pd
import segment
import membership

def get_subsegment_number(data:pd.DataFrame):
    subsegment_number = {}
    for i in segment.subsegments:
        subsegment_number[i] = 0
    for row in data.itertuples():
        subsegment_number[(row.subsegment if row.subsegment == row.subsegment else 'Non' )] += row.ticket_count
    return subsegment_number

def get_segment_number(data:pd.DataFrame):
    segment_number = {}
    for i in segment.segments:
        segment_number[i] = 0
    for row in data.itertuples():
        segment_number[(row.segment if row.segment == row.segment else 'Non' )] += row.ticket_count
    return segment_number

def get_member_number(data:pd.DataFrame):
    membership_number = {}
    for i in membership.memberships:
        membership_number[i] = 0
    for row in data.itertuples():
        membership_number[membership.deformat_membership(row.membership)] += row.ticket_count
    return membership_number