import pandas as pd #imports Pandas
import matplotlib.pyplot as plt


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

#fig, ax = plt.subplots()
#ax.scatter(df['Duration'], df['Calories'], label = 'Duration', color = 'green')
#plt.show()

#print(df)

import numpy as np
from matplotlib.widgets import CheckButtons
 
x = np.arange(0.0, 3.0, 0.01)
y1 = np.sin(1 * np.pi * x)
y2 = np.sin(2 * np.pi * x)
y3 = np.sin(4 * np.pi * x)

#Opretter plot
fig, ax = plt.subplots()
#Vores plots
scatter1 = ax.scatter(df['Date'], df['Duration'], color='blue', label='Duration', visible = False)
scatter2 = ax.scatter(df['Date'], df['Calories'], color='green', label='Calories', visible = True)
#Justering af layoutet
lines = [scatter1, scatter2]
fig.subplots_adjust(left=0.25)
 
#Tilføjer vores checkboxes
rax = fig.add_axes([0.025, 0.4, 0.1, 0.15]) #Changed to 0.15
labels = [str(line.get_label()) for line in lines]
visible = [line.get_visible() for line in lines]
check = CheckButtons(rax, labels, visible)
 
#Click function
def handleClick(label):
    index = labels.index(label)
    lines[index].set_visible(not lines[index].get_visible())
    plt.draw()
 
check.on_clicked(handleClick)

#labels
ax.set_title("Fitness-data")
ax.set_xlabel('Dato')
ax.set_ylabel('Værdi')

plt.savefig('fitness_plot.pdf')

plt.show()

