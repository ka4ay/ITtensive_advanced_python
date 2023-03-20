'''Получите данные по безработице в Москве:
https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv
Найдите, с какого года процент людей с ограниченными возможностями (UnemployedDisabled) среди всех безработных
(UnemployedTotal) стал меньше 2%.'''

import pandas as pd

data = pd.read_csv("https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv", delimiter=";")
data["Sum"] = data.apply(lambda x: 100 * x[6] / x[7], axis=1)
data = data[data["Sum"] < 2]
data = data.set_index("Year")
data = data.sort_index()
print(data.index[0:1].values)
