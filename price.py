from est_price import check_node_and_edge
a = ['La Courneuve 8 Mai 1945','Bobigny-Pablo Picasso','Fort d\'Aubervilliers','Créteil-Pointe du Lac','Saint-Denis-Porte de Paris','Aubervilliers - Front Populaire','Basilique de Saint-Denis','Créteil-Préfecture (Hôtel de Ville)','Aubervilliers-Pantin']

for i in a:
    try:
        print(i,check_node_and_edge(i))
    except:
        print(i,'error')