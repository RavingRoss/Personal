from ast import main
import pandas as pd
import matplotlib.pyplot as plt

def main ():
    def firstLED():
        var = pd.read_excel('400nm UV LED spectra (high res).xlsx')

        y = list(var['Y-data'])
        x = list(var['X-data'])

        plt.figure(figsize=(10,10))
        plt.style.use('seaborn')
        plt.scatter(x,y,marker="o",s=50,edgecolors="black",c="red")
        plt.title("Example Graph for Labs")
        plt.show()
    firstLED()
main()
