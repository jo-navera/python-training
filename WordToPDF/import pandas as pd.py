import pandas as pd
import databricks.koalas as ks

d = {'col1': [1], 'col2': [2]}
df = pd.DataFrame(data=d)
ks_df = ks.DataFrame(df)

df['Masked_Verbatim'] = ["hello"]
