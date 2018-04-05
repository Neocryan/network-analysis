import numpy as np
import pandas as pd
with open('result/grouped100.txt','r',encoding='utf8') as grou:
    a = (grou.read().replace('v','').split('\n'))
    b = np.array(list(map(lambda x:x.split(','),a))).astype('int')

group2stop = {}
for i in set(b[:,1]):
    group2stop[i] = (b[b[:,1] == i][:,0])

stop2group = {}
for i in range(b.shape[0]):
    stop2group[b[i,0]] = b[i,1]


name2stop = pd.read_csv('gtfs/stops.txt')[['stop_id','stop_name']]
name2id = {}
id2name = {}
edge_tuple = []
with open('gtfs/transfers.txt','r',encoding='utf8') as tran:
    next(tran)
    xx = tran.read()
    xxx = list(map(lambda x: x.split(',')[:2], xx.split('\n')))
    for x in xxx:
        try:
            edge_tuple.append((int(x[0]),int(x[1])))
        except:
            print(1)

for i in np.array(name2stop):
    name2id[i[1].lower()] = name2id.get(i[1].lower(),[]) + [i[0]]
    id2name[i[0]] = i[1]

def check_node_and_edge(name):
    id = name2id[name.lower()][0]
    group_id = stop2group[id]
    nodes = group2stop[group_id]
    edge = 0
    for i in nodes:
        for j in nodes:
            if (i,j) in edge_tuple:
                edge +=1

    return len(nodes), edge

def out_edge():
    with open('edgelist.txt','w') as ww:
        for i in edge_tuple:
            ww.write('{}\t{}\n'.format(i[0],i[1]))

