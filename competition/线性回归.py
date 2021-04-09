from sklearn.model_selection import train_test_split
from yellowbrick.regressor import PredictionError, ResidualsPlot
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import skew
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import Imputer
import xlwt

plt.rcParams['font.sans-serif']=['SimHei']
#用来正常显示负号
plt.rcParams['axes.unicode_minus']=False
plt.style.use("ggplot")
plt.rcParams['figure.figsize'] = (16, 16)
def fillNaN(dataSet):
    data = np.array(dataSet)
    imp_mean = Imputer(missing_values="NaN", strategy="mean", axis=0)
    data = imp_mean.fit_transform(data)
    return pd.DataFrame(data)

def dataWrite(lis):
    f = xlwt.Workbook()
    sheet = f.add_sheet(u'sheet',cell_overwrite_ok=True)
    sheet.write(0, 0, '成本预测值')
    for i in range(len(lis)):
        sheet.write(i + 1, 0, round(lis[i]))
    f.save('成本预测值.xlsx')

advert = pd.read_excel("灰度表1.xlsx")
columns =['交易成功时长','总里程', '业务类型',
           '需求类型2', '是否续签', '车辆长度',
           '打包类型','运输等级','标的展示策略',
            ]
# columns = ['线路价格（不含税）','总里程',
#            '需求类型2','车辆吨位', '需求紧急程度',
#            '线路总成本']
advert.drop(advert[advert.交易成功时长 > 2000].index, inplace=True)
advert = advert[columns]
advert = fillNaN(advert)
advert.columns = columns
print(columns)
# advert.head()
# advert.info()
col = columns[1:]
# sns.pairplot(advert, x_vars=col, y_vars='线路价格（不含税）', height=14, aspect=0.7)
X = advert[col]
y = advert['交易成功时长']
lm1 = LinearRegression()
lm1.fit(X, y)
lm1_predict = lm1.predict(X[col])
print(lm1.intercept_)
print(lm1.coef_)
xtrain,xtest,ytrain,ytest = train_test_split(X,y,random_state=1)
print("R^2:",r2_score(y,lm1_predict))
# 高因素影响 R^2: 0.9797304791768885
# lm2 = LinearRegression().fit(xtrain,ytrain)
# lm2_predict = lm2.predict(xtest)
# print("RMSE:",np.sqrt(mean_squared_error(ytest, lm2_predict)))
# print("R^2:",r2_score(y,lm1_predict))
# R^2: 0.9797304791768885
# RMSE: 535.8592414949177
visualizer = PredictionError(lm1).fit(xtrain,ytrain)
visualizer.score(xtest,ytest)
visualizer.poof()
# sns.heatmap(advert.corr(),cmap="YlGnBu",annot=True)
# plt.show()

# plt.show()
