import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Load Csv
data=pd.read_csv("ToyotaCorolla.csv")
print(data.head())

#Scatter Plot
plt.scatter(data["Age"],data["Price"],c="blue")
plt.xlabel("Age")
plt.ylabel("Price")
plt.title("Scatter plot of Age(x) vs Price(y)")
plt.show()

#Box Plot for Price,Age,KM
plt.boxplot([data["Price"],data["Age"],data["KM"]])
plt.xticks([1,2,3],["Price","Age","KM"],rotation=10)
plt.show()

#Heatmap
fig,ax=plt.subplots()
sns.heatmap(data.corr(),center=0, cmap='Blues')
plt.show()


#3d Surface plots
plt.figure(figsize=(10,8))
ax=plt.axes(projection="3d")
x=data['Price']
y=data['KM']
xx,yy=np.meshgrid(x,y)
z=xx*yy
ax.plot_surface(xx,yy,z) # type: ignore
plt.show()
