import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
plt.style.use('seaborn')
def topPR(t = 10):
    top = []
    with open('/home/neoc/PR300c','r') as pr:
        for i in range(100):
            top.append(pr.readline().strip().split(','))

    from est_price import id2name

    top_array = np.array(top).astype('float')

    # pprint([id2name[x] for x in top_array[:,0].astype('int')][:t])
    pprint([z for z in zip([id2name[x] for x in top_array[:,0].astype('int')][:t],[x for x in top_array[:,1].astype('float')][:t])])

def plot_degree100():
    degree_list = []
    with open('result/degree100.txt','r') as de:
        while True:
            try:
                degree_list.append(int(de.readline().strip()))
            except:
                break
    plt.hist(np.log10(degree_list),bins=100)
    plt.show()

def plot_degree0():
    degree_list = []
    with open('result/degree0.txt','r') as de:
        while True:
            try:
                degree_list.append(int(de.readline().strip()))
            except:
                break
    plt.hist(np.log10(degree_list),bins=100)
    plt.show()

plot_degree0()
