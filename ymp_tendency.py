import segment
import membership

import pandas as pd

db = pd.read_excel("./data/2025/EIF 2025 Transaction Data for EFI Hackathon.xls",usecols="C,F,I:K",skiprows=5,names=["genre","ticket_count","segment","subsegment","membership"])

def exclude_list_values(source_list, exclude_list):
    # 使用列表推导式过滤
    return [item for item in source_list if item not in exclude_list]

s_s = segment.get_segment_to_subsegment()

YMPtendency = {}
for i in exclude_list_values(segment.subsegments,s_s["Music"]):
    YMPtendency[i] = 0


for row in db.itertuples():
    if membership.isYMP(row.membership) and row.segment!="Music" and not ("Music" in row.genre) :
        s = row.segment if (row.segment == row.segment) else "Non"
        ss = row.subsegment if (row.subsegment == row.subsegment) else "Non"
        YMPtendency[ss] += row.ticket_count

data_sheet = {
    "Segment":[],
    "Subsegment":[],
    "Size":[]
}



for i in s_s:
    if i == "Music":
        continue
    data_sheet["Segment"].append(i)
    data_sheet["Subsegment"].append("")
    size = 0
    for j in s_s[i]:
        size += YMPtendency[j]
    data_sheet["Size"].append(size)
    for j in s_s[i]:
        size = YMPtendency[j]
        data_sheet["Segment"].append("")
        data_sheet["Subsegment"].append(j)
        data_sheet["Size"].append(size)

df = pd.DataFrame(data_sheet)
df.to_excel("./output/ymp_tendency.xlsx",index=False,sheet_name="ymp_segment_exclude_music")