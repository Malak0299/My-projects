import pandas as pd #imports Pandas

df = pd.read_csv('fitness_fejl.csv') #reads the file

#print(df.head(10))
#print(df.tail(10))

#------------------
#.....METODES......
#------------------

df = df.drop([18,26]) #removes the line

df.at[20, "Date"] = "'2020/12/20'" #creates the valible
df['Date'] = pd.to_datetime(df['Date'], format = 'mixed') #formats everything

df.loc[7, "Duration"] = 45 #changes the valible (specific)
df.loc[21, "Pulse"] = 101 #changes line 21 "Pulse" to 101
df.loc[21, "Maxpulse"] = 130 #changes line 21 "Maxpulse" to 130

#print(df.duplicated()) #shows duplicates

df.drop_duplicates(inplace=True) #removes duplicates
print(df)

