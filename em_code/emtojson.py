# aftojson em 데이터 json 으로 변환
# 각 날짜별 폴더의 em 데이터를 json 으로 변환

import json
import os
import pandas as pd

path_dir = '/media/sf_.VirtualBox/em/'
file_list = os.listdir(path_dir)

for i in file_list:
    af = pd.read_table(path_dir+"{}/area_mean".format(i),sep=',',engine="python")
    bf=af.drop(['Unnamed: 0'],axis=1)
    bf.columns=['sensor1', 'sensor2', 'sensor3', 'sensor4', 'sensor5']
    
    result = bf.to_json(orient="index")
    json.dumps(result)
    em = json.loads(result)
    
    with open(path_dir+"{}/".format(i)+"em.json", 'w', encoding='utf-8') as make_file:
        json.dump(em, make_file)