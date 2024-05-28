import pandas as pd

dir = '/Users/yurisafonov/Desktop/my_git_project/'
organisations = pd.read_csv(dir + 'organisations.csv')
features = pd.read_csv(dir  +  'features.csv')
rubrics  = pd.read_csv(dir  +  'rubrics.csv')

print(features.head())