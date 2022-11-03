import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

path = '/Users/tangchencheng/Desktop/Data/rData/Objects_1.txt'
data = pd.read_csv(path, sep='\t',header=None)

sns.set_style('white')
sns.set(font_scale=1.2)  # 字号是原来的1.2倍
# sns.despine(offset=10,trim=True) #两坐标轴相隔距离
sns.histplot(data.iloc[:, -2], bins=800, kde=False, 
stat='probability', color='black', edgecolor='white')
print(data.head())
# data.iloc[:, -2].plot.hist(bins=100)
# plt.xticks(range(0, max(data.iloc[:,-2]), 500), fontsize=8, rotation=90)

plt.xlabel("Nuclei - Intencity Nucleus")
plt.ylabel("Fraction Of Cells")
# plt.xlim(0, 12000)
plt.tight_layout()
plt.show()