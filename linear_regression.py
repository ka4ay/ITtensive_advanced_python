'''Возьмите данные по безработице в городе Москва:
video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv
Сгруппируйте данные по годам, и, если в году меньше 6 значений, отбросьте эти годы.
Постройте модель линейной регрессии по годам среднего значения отношения UnemployedDisabled к UnemployedTotal
(процента людей с ограниченными возможностями) за месяц и ответьте, какое ожидается значение процента безработных
инвалидов в 2020 году при сохранении текущей политики города Москвы?

Ответ округлите до сотых.'''

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv", delimiter=";")
data["UDP"] = data["UnemployedDisabled"] / data["UnemployedTotal"] * 100
data_group = data.groupby("Year").filter(lambda x: x["UDP"].count() > 5)
data_group = data_group.groupby("Year").mean()
dl = len(data_group.index)
x = np.array(data_group.index).reshape(dl, 1)
y = np.array(data_group["UDP"]).reshape(dl, 1)
model = LinearRegression().fit(x, y)
predict = np.round(model.predict(np.array(2020).reshape(1, 1)), 2)
print("Ожидаемое значение процента безработных инвалидов в 2020 году - ", predict[0, 0], "%")
