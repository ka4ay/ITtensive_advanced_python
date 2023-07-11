'''Загрузите данные по итогам марафона
https://video.ittensive.com/python-advanced/marathon-data.csv

Приведите время половины и полной дистанции к секундам.

Найдите, данные каких серии данных коррелируют (используя диаграмму pairplot в Seaborn).

Найдите коэффициент корреляции этих серий данных, используя scipy.stats.pearsonr.

Постройте график jointplot для коррелирующих данных.'''

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import seaborn as sns


def convert_time(a):
    return sum(x * int(t) for x, t in zip([3600, 60, 1], a.split(":")))


data = pd.read_csv("https://video.ittensive.com/python-advanced/marathon-data.csv")
data["split"] = data["split"].apply(convert_time)
data["final"] = data["final"].apply(convert_time)
sns.pairplot(data, hue="gender", height=4)
plt.show()
sns.jointplot(data, x="split", y="final", height=12, kind="kde")
plt.show()
print("Коэффициент корреляции максимально зависимых серий данных =", round(stats.pearsonr(data["split"], data["final"])[0], 2))
