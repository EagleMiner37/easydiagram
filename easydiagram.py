import matplotlib.pyplot as plt
import numpy as np
b=[]
d=[]
print("Welcome")
print("This is a tiny library with Matplotlib")
print("Created by EagleMiner37")
def bardiagram():
    count=int(input("Enter number of entries "))
    for i in range(count):
        a=int(input("Enter value "))
        b.append(a)
        c=input("Enter label ")
        d.append(c)
    values=np.array(b)
    labels=np.array(d)
    plt.bar(labels , values)
    plt.show()
def piediagram():
    count=int(input("Enter number of entries "))
    for i in range(count):
        a=int(input("Enter percent "))
        b.append(a)
        c=input("Enter label ")
        d.append(c)
    values=np.array(b)
    user_labels=np.array(d)
    plt.pie(values,labels=user_labels, colors=["gold","blue","green","red","black","white","yellow","cyan","light-green","brown","purple","gray","orange","dark-blue"])
    plt.legend()
    plt.show()
def plotdiagram():
    count=int(input("Enter number of entries "))
    for i in range(count):
        a=int(input("Enter position`s x "))
        c=int(input("Enter position`s y "))
        b.append(a)
        d.append(c)
    y_values=np.array(d)
    x_values=np.array(b)
    plt.plot(x_values,y_values)
    plt.show()
def scatterdiagram():
    count=int(input("Enter number of entries "))
    for i in range(count):
        a=int(input("Enter position`s x "))
        c=int(input("Enter position`s y "))
        b.append(a)
        d.append(c)
    y_values=np.array(d)
    x_values=np.array(b)
    plt.scatter(x_values,y_values)
    plt.show()
def histogram():
    count=int(input("Enter number of entries "))
    for i in range(count):
        a=int(input("Enter value "))
        b.append(a)
    plt.hist(b)
    plt.show()