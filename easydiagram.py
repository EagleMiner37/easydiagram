import matplotlib.pyplot as plt
import numpy as np
b=[]
d=[]
f=[]
user_sizes=[]
def bardiagram():
    print(".................................")
    print(".................................")
    print("Created by EagleMiner37")
    print(".................................")
    print(".................................")
    count=int(input("Enter number of entries "))
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    for i in range(count):
        a=int(input("Enter value "))
        b.append(a)
        c=input("Enter label ")
        d.append(c)
        print("-----------------------------------------------------------------------------------------")
    values=np.array(b)
    labels=np.array(d)
    user_color=str(input("Enter color "))
    user_width=float(input("Enter width of the lines of diagram "))
    plt.bar(labels , values,color=user_color,width=user_width)
    plt.show()
def piediagram():
    print(".................................")
    print(".................................")
    print("Created by EagleMiner37")
    print(".................................")
    print(".................................")
    count=int(input("Enter number of entries "))
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    for i in range(count):
        a=int(input("Enter percent "))
        b.append(a)
        c=input("Enter label ")
        d.append(c)
        e=float(input("Enter explode "))
        f.append(e)
        print("-----------------------------------------------------------------------------------------")
    values=np.array(b)
    user_labels=np.array(d)
    user_shadow=bool(input("Have shadow?(Enter True or False) "))
    plt.pie(values,labels=user_labels, colors=["gold","blue","green","red","black","white","yellow","cyan","light-green","brown","purple","gray","orange","dark-blue","crimson"],explode=f,shadow=user_shadow)
    user_legend=bool(input("Have legend?(Enter True or False) "))
    if user_legend==True:
        user_title_legend=str(input("Enter the title of legend "))
        plt.legend(title=user_title_legend)
    plt.show()
def plotdiagram():
    print(".................................")
    print(".................................")
    print("Created by EagleMiner37")
    print(".................................")
    print(".................................")
    count=int(input("Enter number of entries "))
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    for i in range(count):
        a=int(input("Enter position`s x "))
        c=int(input("Enter position`s y "))
        b.append(a)
        d.append(c)
        print("-----------------------------------------------------------------------------------------")
    user_linewidth=float(input("Enter linewidth of lines of the diagram "))
    user_title=input("Enter title of diagram ")
    user_xlabel=input("Enter xlabel ")
    user_ylabel=input("Enter ylabel ")
    plt.title(user_title)
    plt.xlabel(user_xlabel)
    plt.ylabel(user_ylabel)
    y_values=np.array(d)
    x_values=np.array(b)
    user_grid=bool(input("Have grid?(Enter True or False) "))
    if user_grid==True:
        plt.grid()
    user_color=str(input("Enter color "))
    plt.plot(x_values,y_values,color=user_color,linewidth=user_linewidth)
    plt.show()
def scatterdiagram():
    print(".................................")
    print(".................................")
    print("Created by EagleMiner37")
    print(".................................")
    print(".................................")
    count=int(input("Enter number of entries "))
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    user_color=str(input("Enter color "))
    for i in range(count):
        a=int(input("Enter position`s x "))
        b.append(a)
        c=int(input("Enter position`s y "))
        d.append(c)
        user_size=float(input("Enter size of dot "))
        user_sizes.append(user_size)
        x_values=np.array(b)
        y_values=np.array(d)
    plt.scatter(x_values,y_values,color=user_color,s=user_sizes)
    plt.show()
def histogram():
    print(".................................")
    print(".................................")
    print("Created by EagleMiner37")
    print(".................................")
    print(".................................")
    count=int(input("Enter number of entries "))
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    for i in range(count):
        a=float(input("Enter value "))
        b.append(a)
        print("-----------------------------------------------------------------------------------------")
    user_color=str(input("Enter color "))
    plt.hist(b,color=user_color)
    plt.show()
