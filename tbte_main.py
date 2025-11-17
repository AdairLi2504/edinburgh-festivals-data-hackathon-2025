import segment
import membership
import mem_seg
import volume
import time_bte

import pandas as pd

db = pd.read_excel("./data/2025/EIF 2025 Transaction Data for EFI Hackathon.xls",usecols="B,H,K",skiprows=5,names=["event_d_t","transaction_d_t","membership"])

data_sheet = {
    "TimeInterval":[],
    "Size":[]
}
i = 0
tbte_m = time_bte.get_tbte_membership(db)




#df = pd.DataFrame(data_sheet)
#df.to_excel("./output/t.xlsx",index=False,sheet_name="time-between-transcation-event")