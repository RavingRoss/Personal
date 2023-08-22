import pandas as pd
import matplotlib.pyplot as plt

var = pd.read_excel('Possible_roAp.xlsx')

y = list(var['GMAG0'])
x = list(var['BP-RP0'])

plt.figure(figsize=(10,10))
plt.style.use('seaborn')
plt.scatter(x,y,marker="*",s=100,edgecolors="black",c="red")
plt.title("HRD of Possible roAp's")
plt.gca().invert_yaxis()
plt.show()