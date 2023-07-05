import numpy
import matplotlib.pyplot as plt
import random
class Plot:
       def GraphPlot():
            x_axis=np.random.ranint(10,40,10)
            y_axis=np.random.randint(20,50,10)
            print("X axis values ",x_axis)
            print("Y axis values ",y_axis)
            plt.plot(x_axis,marker="o",mfc="violet",mec="yellow",colour="red",lifestyle="-.",label="first line")
            plt.plot(y_axis,marker="o",mfc="black",mec="black",colour="green",lifestyle="dashed",label="second line")
            plt.grid(colour="green")
            plt.xlabel('Market cap')
            plt.ylabel('share prices')
            plt.legend()
            plt.legend()
            plt.show() 
Plot.GraphPlot()
