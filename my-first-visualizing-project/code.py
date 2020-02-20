# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data= pd.read_csv(path)
#Code starts here 

data['Gender'].replace('-','Agender',inplace=True)
gender_count= data['Gender'].value_counts()
plt.bar('gender_count',len('gender_count'))
plt.show()




# --------------
#Code starts here
alignment=data['Alignment'].value_counts()
plt.pie(alignment)
plt.xlabel('Character Alignment')
plt.show()


# --------------
#Code starts here
sc_df=data[['Strength','Combat']]
#strenth_mean= data.Strength.mean()
#combat_mean=data.Combat.mean()
#diff_strenth=
sc_covariance= sc_df['Strength'].cov(sc_df['Combat'])
sc_strength= data['Strength'].std()
sc_combat= data['Combat'].std()
sc_pearson= sc_covariance/(sc_strength * sc_combat)
ic_df= data[['Intelligence','Combat']]
ic_covariance=ic_df['Intelligence'].cov(ic_df['Combat'])
ic_intelligence= data['Intelligence'].std()
ic_combat= data['Combat'].std()
ic_pearson=ic_covariance/(ic_intelligence * ic_combat)


# --------------
#Code starts here
total_high=data['Total'].quantile(q=0.99)
super_best=data[data['Total']> total_high]
super_best_names=list(super_best['Name'])



# --------------
#Code starts here
import matplotlib.pyplot 
ax_1=plt.subplot()
ax_1.boxplot(super_best['Intelligence'])
ax_2=plt.subplot()
ax_2.boxplot(super_best['Speed'])
ax_3=plt.subplot()
ax_3.boxplot(super_best['Power'])
plt.show()


