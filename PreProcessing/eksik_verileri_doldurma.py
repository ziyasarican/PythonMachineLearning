# Eksik olan sayısal veri içeren sütunlardaki verileri, kalan verilerin ortalaması ile doldurma.

import pandas as pd
import numpy as np
df = pd.read_csv("/Users/ziyasarican/Desktop/eksikveriler.csv")

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

Yas = df.iloc[:,1:4].values 
print(Yas)

# Fit öğrenme işlemini yapar. Öğrenilecek değeri veririz
imputer = imputer.fit(Yas[:,1:4])

# Fit ile öğrenip transform ile öğrendiğini uygular
Yas[:,1:4] = imputer.transform(Yas[:,1:4])

print(Yas)
