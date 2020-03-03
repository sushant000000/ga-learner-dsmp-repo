# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df= pd.read_csv(path)
p_a = df[df['fico'].astype(float)>700].shape[0]/df.shape[0]
p_b = df[df['purpose'] == 'debt_consolidation'].shape[0]/df.shape[0]
print(p_b)
df1 = df[df['purpose']== 'debt_consolidation']
p_a_b =df1[df1['fico'].astype(float) >700].shape[0]/df1.shape[0]
print(p_a_b)
result = (p_a == p_a_b)
print(result)
# code ends here


# --------------
# code starts here
prob_lp=df[df['paid.back.loan'] == 'Yes'].shape[0] / df.shape[0]
prob_cs=df[df['credit.policy'] == 'Yes'].shape[0] / df.shape[0]
new_df=df[df['paid.back.loan'] == 'Yes']
prob_pd_cs= new_df[new_df['credit.policy'] == 'Yes'].shape[0] /new_df.shape[0]
bayes=(prob_pd_cs * prob_lp)/ prob_cs

# code ends here


# --------------
# code starts here
df1= df[df['paid.back.loan'] == 'No']


# code ends here


# --------------
# code starts here
inst_median= df['installment'].median()
inst_mean =  df['installment'].mean()
plt.hist(df['installment'] , normed = True , bins = 50)
#plt.hist(inst_median,inst_mean)

# code ends here


