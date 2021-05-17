import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import os
# 데이터 프레임 맞춰준다
# 6
# 964
# test = pd.DataFrame(np.arange(0, 5784).reshape(964, 6))
# test = test.drop([0])
# test = test.drop([0], axis=1)
outp = []
path_dir = '/media/sf_.VirtualBox/em_Data/'
file_list = os.listdir(path_dir)

for k in file_list:
    os.mkdir('/media/sf_.VirtualBox/em/{}'.format(k))
    for i in range(1, 6):
        for j in range(1, len(file_list)):
            area_df = pd.read_table('/media/sf_.VirtualBox/em_Data/{}/area_s_{}_{}'.format(
                k, i, j), sep='\n', engine="python", header=None)
            da = area_df.drop([0], axis=0)
            x = np.mean(da)
            test[i][j] = x
    area = DataFrame(test)
    area.to_table('/media/sf_VirtualBox/em/{}'.format(k))
