import segment
import membership
import mem_seg
import volume
import genre
import mem_gen
import pandas as pd

db = pd.read_excel("./data/2025/EIF 2025 Transaction Data for EFI Hackathon.xls",usecols="I:K",skiprows=5,names=["segment","subsegment","membership"])

genres = genre.get_all_genres(db)

data_sheet = {
    "Genre":[],
    "Membership":[],
    "Size":[]
}

for i in genres:
    for j in membership.memberships:
        data_sheet["Genre"].append(i)
        data_sheet["Membership"].append(j)
        data_sheet["Size"].append(mem_gen.get_number_membership_genre(j,i,db))

df = pd.DataFrame(data_sheet)
df.to_excel("./output/g-m.xlsx",index=False,sheet_name="genre-member")