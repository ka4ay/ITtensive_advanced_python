'''Возьмите данные по вызовам пожарных служб в Москве за 2015-2019 годы:
https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv
Получите из них фрейм данных (таблицу значений). По этому фрейму вычислите среднее значение вызовов пожарных машин
в месяц в одном округе Москвы, округлив до целых'''

import pandas as pd
data = pd.read_csv('https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv', delimiter=';')
print('Среднее значение вызовов пожарных машин в месяц:', data['Calls'].mean().round())