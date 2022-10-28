import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import lightgbm as lgb

at = pd.read_csv('C:/python/apple_sweet/Apple_attribute.csv')
apple_attribute = at.to_numpy()
sw = pd.read_csv('C:/python/apple_sweet/Apple_sweetness.csv')
apple_sweetness = sw.to_numpy()
train_input, test_input, train_target, test_target = train_test_split(apple_attribute, apple_sweetness, test_size=0.2)

poly = PolynomialFeatures()
poly.fit(train_input)
train_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)

ss = StandardScaler()
ss.fit(train_poly)
train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)

lgbm = lgb.LGBMRegressor()
lgbm.fit(train_scaled, train_target)
y_pred = lgbm.predict(train_scaled)

accuracy = accuracy_score(train_pred, test_target)
print('LightGBM Model accuracy score: {0:0.4f}'.format(accuracy_score(test_target, y_pred)))