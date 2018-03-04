//#Statistical Averages
import pandas as pd
df=pd.read_csv('MU_REPORT.csv')
#summary statistics
stat=df.EHR_Product_Name.value_counts()
print('Min:')
print(stat.min())
print('Max:')
print(stat.max())
print('Mean:')
print(stat.mean())
print('Standard Deviation:')
print(stat.std())
print(stat.describe())

//#Visualization 1
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("file_clean.csv")
vendors=df.groupby('Vendor_Name').Provider_Stage_Number.value_counts().unstack()
new_vendor=vendors.sort_values(by='Stage 1', ascending=False)[:10]
print(new_vendor)
new_vendor.plot(kind='barh', stacked=True, figsize=[16,10], colormap='winter',
title='Number of providers by stage of meaningful use')
plt.show()

//#Visualization 2
import pandas as pd
import matplotlib.pyplot as plt
#Pandas Data Frame has been used here
df=pd.read_csv("file_clean.csv")
#User defined function has been used
def prog_year(df):
df1=df.groupby('Program_Year').Program_Type.value_counts().unstack()
pg. 17
df1.plot(kind='area', figsize=[16,10], stacked=True, title='Yearly analysis of number of providers registered in incentive program')
plt.ylabel('Number of Providers Registered')
plt.xlabel('Program Year')
prog_year (df)

//#Visualization 3
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("file_clean.csv")
plot1=df.Specialty.value_counts()
new_plot1=plot1.sort_values(ascending=False)[:10]
#Using tuple to store values in explode
explode = (0.1, 0, 0, 0,0,0,0,0,0,0)
new_plot1.plot.pie(figsize=(10, 10), explode=explode, title='Top 10 clinical specialities of providers')
plt.ylabel(' ')