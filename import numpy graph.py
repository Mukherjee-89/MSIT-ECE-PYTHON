import numpy
import matplotlib.pyplot as plt
class Graph:
       def RandomArrayGraph():
            x_axis=np.randomarray.ranint(10,90,12)
            y_axis=np.random.randint(50,120,12)
            x_axis=array_split(x_axis,2)
            y_axis=array_split(y_axis,2)
            print(x_axis),len(x_axis)
            print(y_axis),len(y_axis)
            plt.plot(x_axis,y_axis,marker="o",mfc="red",mec="red",colour="blue")
            plt.plot(x_axis,marker="o",mfc="red",mec="red",colour="blue")
            plt.plot(y_axis,marker="o",mfc="red",mec="red",colour="yellow")
            plt.grid(colour="green")
            plt.xlabel("")
            plt.show() 
Graph.RandomArrayGraph()