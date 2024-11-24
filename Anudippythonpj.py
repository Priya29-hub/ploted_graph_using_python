import matplotlib.pyplot as plt
import pandas as pd

# PRINT DATA

df=pd.read_excel("D:\\PRIYANKA\\ANUDIP Labs\\TrainDelay1.xlsx")
print(df)


#FOR MISSING DATA

df.isnull()
print(df)


#ISNULL AND ANY

df.isnull().sum()
print (df)


# ONE column value displayed :

a=df["DistanceBetweenStationskm"]
print(a)

#MEAN VALUE of the Column DistanceBetweenStationskm is Displayed

b=df['DistanceBetweenStationskm'].mean()
print(b)

# first 05 Rows are displayed

c=df.head(5)
print(c)


# BAR CHART

import matplotlib.pyplot as plt
import pandas as pd

x=df["DayoftheWeek"]
y=df["DistanceBetweenStationskm"]

plt.xlabel("DayoftheWeek",fontsize=15)
plt.ylabel("DistanceBetweenStationskm",fontsize=15)
plt.title("Train Delay Graph",fontsize=15)
plt.bar(x,y, width=0.5, color='skyblue', align="center")

plt.show()



# BAR GRAPH by considering 2 values on y axis

import matplotlib.pyplot as plt
import numpy as np

x=df["DayoftheWeek"]
y=df["DistanceBetweenStationskm"]
s=df["HistoricalDelaymin "]

width=0.5
p=np.arange(len(x))
p1=[j+width for j in p]

plt.xlabel("DayoftheWeek",fontsize=15)
plt.ylabel("DistanceBetweenStationskm",fontsize=15)
plt.title("Train Delay Graph",fontsize=15)

plt.bar(x,y, width, color='skyblue', align="center", label="DistanceBetweenStationskm")
plt.bar(p1,s, width, color='red', align="center", label="HistoricalDelaymin")

plt.legend()
plt.show()



# Scattered Graph

import matplotlib.pyplot as plt



x=df["DayoftheWeek"]
y=df["DistanceBetweenStationskm"]

plt.title("Scatter plot", fontsize=20)
plt.xlabel("DayoftheWeek",fontsize=15)
plt.ylabel("DistanceBetweenStationskm",fontsize=15)

c=["10","20","30","40","50","60","70","80","90","11","55","66","44","77","88","99","22","33","36","82"]

plt.scatter(x,y ,color="c")
plt.show()


#Pie chart


import matplotlib.pyplot as plt

y=["Morning","Afternoon","Evening", "Night"]
x=[179,190,181,138]


c=["lightblue","lightpink","orange","lightgrey"]
explode =[0.01,0.01,0.01,0.01]
plt.title("PIE CHART")


plt.pie(x, labels=y , explode=explode ,colors=c ,autopct='%0.1f%%', shadow=True )

plt.show()

# Ring Pie Chart


import matplotlib.pyplot as plt

y=["Morning","Afternoon","Evening", "Night"]
x=[179,190,181,138]

explode =[0.01,0.01,0.01,0.01]
plt.title("PIE CHART")

plt.pie(x, labels=y , explode=explode, radius=1.0)
plt.pie([1], radius=0.5 , colors="w")

plt.show()

















