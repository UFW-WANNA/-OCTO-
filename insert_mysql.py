import pandas as pd
from sqlalchemy import create_engine
import sys

input_file = sys.argv[1]
engine = create_engine('mysql+pymsql://root:123456789@127.0.0.1:3306/tb')



#pandas从数据库中读取数据表
sql = '''select * from sal_day;'''
df = pd.read_sql(sql,engine)
print(df)


#pandas读取csv文件并存入数据库中
data = pd.read_csv(input_file)
data.to_sql('mydata',engine,index=False)
print("阿童木已经完成任务")
