import pymysql
import pandas as pd
import matplotlib.pyplot as plt
sensor_db = pymysql.connect(
    user="user",
    passwd="12345",
    host="13.124.240.211",
    db="SmartInside",
    port=51642,
    charset='utf8'
)
cursor = sensor_db.cursor(pymysql.cursors.DictCursor)

mflsql = "select * from `MFL`;"
areasql = "select * from `AREA`;"
# sql = "load data local infile 'td50_reshape.lvm' into table sensor columns terminated by '\t' ignore 1 lines;"
# cursor.execute(selectsql)
cursor.execute(mflsql)
mflresult = cursor.fetchall()

cursor.execute(areasql)
arearesult = cursor.fetchall()


MFLaf = pd.DataFrame(mflresult)
MFLdf = MFLaf.astype(float)
AREAdf = pd.DataFrame(arearesult)
