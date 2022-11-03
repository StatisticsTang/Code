import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

path = '/Users/tangchencheng/Desktop/Data/rData/Objects_2.txt'
df = pd.read_csv(path, sep='\t',header=0)
for i in range(1, 21):
    data = df[(df["Plane"] == i)]
    sns.set_style('white')
    sns.set(font_scale=1.2)  # 字号是原来的1.2倍
    # sns.despine(offset=10,trim=True) #两坐标轴相隔距离
    sns.histplot(data.iloc[:, -2], bins=800, kde=False, 
    stat='probability', color='black', edgecolor='white')
    print(data.head())

    plt.xlabel("Nuclei - Intencity Nucleus")
    plt.ylabel("Fraction Of Cells")
    plt.xlim(0, 20000)
    plt.tight_layout()
    plt.savefig('/Users/tangchencheng/Desktop/实验室/temp/temp-{}.png'.format(i))  # 输入地址，并利用format函数修改图片名称
    # plt.show()
    plt.clf()  # 需要重新更新画布，否则会出现同一张画布上绘制多张图片