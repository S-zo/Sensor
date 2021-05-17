import pandas as pd

origin_df = pd.read_table('td50.lvm', sep ='\t',   engine="python" ,header=None)
new_col = ["space","sensor1","sensor2","sensor3","sensor4","sensor5","sensor6","sensor7","sensor8","sensor9","sensor10"]
origin_df.columns = new_col
reshape_df=origin_df.drop(columns=["space"])
reshape_df.to_csv('td50_reshape.lvm', index=False,sep="\t")
