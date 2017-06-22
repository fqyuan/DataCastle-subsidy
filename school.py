import pandas as pd
import warnings
warnings.filterwarnings("ignore")
names_card=['学生id','消费类别','消费地点','消费方式','消费时间','消费金额','剩余金额']

#导入学生饭卡数据
card_train=pd.read_csv("../input/card_train.txt",header=None,encoding='utf-8',names=names_card,index_col=False)
#pd.read_csv():read csv file, save dataframe as an csv in the working directory.
card_test=pd.read_csv("../input/card_final_test.txt",header=None,encoding='utf-8',names=names_card,index_col=False)
#pd.concat(): 默认将[data1,data2,...]按列排列，连成同一个dataframe.
card_data =pd.concat([card_train, card_test]);

#Added by fqyuan: store processed file into data_processed directory.
card_data.to_csv('../data_processed/card_data.csv')

#导入学生成绩数据
namse_score=['学生id','学院编号','成绩排名']
score_train=pd.read_csv("../input/score_train.txt",header=None,encoding='utf-8',names=namse_score,index_col=False)
score_test=pd.read_csv("../input/score_final_test.txt",header=None,encoding='utf-8',names=namse_score,index_col=False)
score_data=pd.concat([score_train,score_test])
score_data.to_csv("/data_processed/score_data.csv")

#数据展示
print(card_data.shape)
print(score_data.shape)
len(card_data.学生id.unique())

#处理消费方式变量
card_data['消费方式']=card_data['消费方式'].astype('category')
card_data['消费方式'].describe()
print(card_data['消费方式'].unique())

#缺失值处理
card_data.isnull().sum()
#由于消费方式中食堂消费最多，使用食堂代替缺失的消费类别
card_data['消费方式'].fillna('食堂',inplace=True)

#每个学生的总消费
#DataFrame.groupby(arg):某种映射集合或某些列的组合
card_sum_by_ID=card_data.groupby('学生id')['消费金额'].sum()
card_sum_by_ID.head(20)

#每个学生各个类别消费
card_sum_by_ID_type=card_data.groupby(['学生id','消费方式'])['消费金额'].sum().unstack('消费方式')
card_sum_by_ID_type.head()

#缺失值
card_sum_by_ID_type.fillna(0,inplace=True)

#结合数据
#axis=1, default 0,means the axis to concatenate along
card=pd.concat([card_sum_by_ID,card_sum_by_ID_type],axis=1)
#显示数据
card.head()
#删除数据
del card_sum_by_ID,card_sum_by_ID_type,card_data

#成绩数据标准化
score_data.成绩排名=score_data.groupby('学院编号').成绩排名.transform(lambda x: (x-x.mean())/x.std())
score_data.set_index('学生id')

#保存数据
score_data.to_csv('../input/cleaned_score.csv')
card.to_csv('../input/cleaned_card.csv')

