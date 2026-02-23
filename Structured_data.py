import pandas as pd
import json

with open('data/new_raw_jobs.json','r') as f:
    data = json.load(f)

jobs_list = data.get('results', [])
df_flattened = pd.json_normalize(jobs_list)
df_flattened['average_salary'] = df_flattened[['salary_min','salary_max']].mean(axis=1)

column_mapping = {
    'title': 'Job Title',
    'location.display_name': 'Location',
    'salary_min': 'Min Salary',
    'salary_max': 'Max Salary',
    'average_salary': 'Avg_Salary',
    'company.display_name': 'Company',
    'created': 'Date Posted'
}

df = df_flattened[list(column_mapping.keys())].rename(columns=column_mapping)
df['Date Posted'] = pd.to_datetime(df['Date Posted']).dt.date

pd.set_option('display.max_columns',None)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', None)


print(df)