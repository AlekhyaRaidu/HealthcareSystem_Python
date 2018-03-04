
// data cleaning1
import pandas as pd
new_lables=['National_Provider_Identifier','CMS_Certified_Number', 'Provider_Type', 
'Business_State_Territory', 'ZIP', 'Specialty', 'Hospital_Type', 'Program_Type', 
'Program_Year', 'Provider_Stage_Number', 'Payment_Year', 'Attestation_Month', 
'Attestation_Year', 'MU_Definition_2014', 'Stage_2_Scheduled_2014', 
'EHR_Certification_Number', 'EHR_Product_CHP_Id', 'Vendor_Name', 'EHR_Product_Name', 
'EHR_Product_Version', 'Product_Classification', 'Product_Setting', 'Product_Certification_Edition_Yr']
df=pd.read_csv('MU_REPORT.csv', header=0,names= new_lables)
print(df.head())

// data cleaning2
import pandas as pd
df=pd.read_csv("MU_REPORT.csv")
#Using 'String' inbuilt split function to split 'EHR_Product_CHP_Id'
df[['EHR_Product_Chip', 'EHR_Product_ID']] = df['EHR_Product_CHP_Id'].str.split('-', expand=True)
print(df.head())

// data cleaning 3
import pandas as pd
df=pd.read_csv("MU_REPORT.csv")
new_df=df.dropna(subset=['Specialty'], how='any')
#Using 'file' attribute to save the dataset in new CSV file 
new_df.to_csv("file_clean.csv",index=False) // index is set true- return row names
