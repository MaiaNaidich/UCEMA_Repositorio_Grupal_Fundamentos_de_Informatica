import pandas as pd
def unirDF(df1,df2):
    return pd.concat([df1, df2], ignore_index=True, sort=False)
