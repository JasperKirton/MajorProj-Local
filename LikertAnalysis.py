import pandas as pd
from pandas.api.types import CategoricalDtype


# Pre-study Qs
df = pd.read_csv('Pre-study Survey (Responses) - study corresponding.csv', sep=',', header=None)

# define column names for dataframe
df.columns = ['time', 'noneed', 'name', 'gender', 'age', 'Musical experience', 'Musical importance', 'Actively Search Frequency',
              'Passive Discovery Frequency', 'Eclectic level', 'Musical taste change in past 2 years', 'Deep listening level']
'''



# Rate rec
df = pd.read_csv('Please rate this recommendation in the following; (Responses) - study corresponding.csv', sep=',', header=None)

df.columns = ['time', 'noneed', 'name', 'likelihood of revisiting rec', 'interest of rec', 'compare to sota', 'similarity to seed artist', '"anything else?"']




# Post-study Qs (to do
df = pd.read_csv('Post-study Survey (Responses) - 2nd iter.csv', sep=',', header=None)

df.columns = ['time', 'noneed', 'name', 'email', 'overall quality', 'how likely to re-use service', '"anything else?"']
'''



# not sure if i need this
# def similarity_score_compare(i, j):
# scores = []


del df['noneed']
#del df['email']


#print(df['age'].mean())
print(df.describe())