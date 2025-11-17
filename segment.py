import pandas as pd

subsegments = ['Drama New Writing', 'Scratch Night/Rehearsal', 'UK & Ireland Folk Music', 'Chamber & Recitals', 'Classical Choral', 'Youth Music', 'Baroque', 'Orchestral', 'World Music', 'Jazz & Blues', 'Opera', 'Electronic Music', 'Modern Classical Music', 'Contemporary Dance' , 'Family Workshops - Performance Skills', 'C&F Concert', 'Other Talks', 'Not Applicable','Non']

segments = ['Plays/Drama', 'Music', 'Dance', 'Workshops', 'Children/Family', 'Other Artforms', 'Not Applicable', 'Non']

def get_segment_to_subsegment():
    data = pd.read_excel("./data/2025/EIF 2025 Transaction Data for EFI Hackathon.xls",usecols="I:J",skiprows=5,names=["segment","subsegment"])
    segment = {}
    for row in data.itertuples():
        s = row.segment if (row.segment == row.segment) else "Non"
        ss = row.subsegment if (row.subsegment == row.subsegment) else "Non"
        if not (s in segment):
            segment[s]=[]
        if not (ss in segment[s]):
            segment[s].append(ss)
    return segment


