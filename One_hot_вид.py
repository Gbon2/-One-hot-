import pandas as pd

# Создание исходного DataFrame
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

# Преобразование в one-hot
one_hot_encoded = pd.get_dummies(data['whoAmI']).groupby(level=0).max()

# Вывод результата
print(one_hot_encoded.head())
