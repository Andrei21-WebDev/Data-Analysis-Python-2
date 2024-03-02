import pandas as pd
from cluster import *
from functions import *

citireTabel = pd.read_csv("Date/someri.csv", index_col=1)
#print(citireTabel)
capTabel = list(citireTabel)[1:]
#print(capTabel)

model_cluster = cluster(citireTabel, capTabel)
p_opt = model_cluster.calcul_partitie()

ierarhie(model_cluster.h, citireTabel.index, model_cluster.threshold)
partitii = pd.DataFrame(data={
    "P_Opt": p_opt
}, index=citireTabel.index)

p4 = model_cluster.calcul_partitie(4)
ierarhie(model_cluster.h, citireTabel.index, model_cluster.threshold)
partitii["P4"] = p4

for v in capTabel:
    histograme(citireTabel[v].values,p4,v)

print(partitii)
show()