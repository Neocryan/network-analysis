import json, pickle
try:
    from est_price import *
    from gtfs_recursive import *
except:
    print('load it')
def save():


    f = open('save/data.dat','wb')

    pickle.dump(id2geo,f)
    pickle.dump(group2stop,f)
    pickle.dump(stop2group,f)
    pickle.dump(name2id,f)
    pickle.dump(id2name,f)
    pickle.dump(edge_tuple,f)

    f.close()

def load():
    '''
    id2geo,group2stop,stop2group,name2id,id2name,edge_tuple = load()
    :return:
    '''
    f = open('save/data.dat','rb')
    # n = pickle.load(f)
    id2geo = pickle.load(f)
    group2stop = pickle.load(f)
    stop2group = pickle.load(f)
    name2id = pickle.load(f)
    id2name = pickle.load(f)
    edge_tuple = pickle.load(f)
    f.close()
    return id2geo,group2stop,stop2group,name2id,id2name,edge_tuple