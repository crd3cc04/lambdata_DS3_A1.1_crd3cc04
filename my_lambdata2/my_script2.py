import pandas as pd 

df = pd.DataFrame({'wk_birthday': pd.date_range('2020-09-20', periods=7)})
print(df)

from my_lambdata2.my_mod2 import wk_birthday

df = wk_birthday(df)
print(df)