import pandas as pd
import matplotlib.pyplot as plt

dir = '/Users/yurisafonov/Desktop/my_git_project/'
organisations = pd.read_csv(dir + 'organisations.csv')

data = organisations.drop(columns=['org_id', 'city', 'rating', 'rubrics_id', 'features_id'], axis=1)
grouped_data = data.groupby('average_bill').size()
grouped_data = grouped_data.reset_index(name='count')
plt.figure(figsize=(10,6))
print(plt.hist(grouped_data['average_bill'].dropna(), bins=20, edgecolor='k', alpha=0.7))
