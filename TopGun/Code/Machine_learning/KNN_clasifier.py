import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

at = pd.read_csv('C:/python/apple_sweet/Apple_attribute.csv')
apple_attribute = at.to_numpy()
sw = pd.read_csv('C:/python/apple_sweet/Apple_sweetness_c.csv')
# bins = [9, 12.5, 14.5, 18]
# labels = ['low', 'normal', 'sweet']
# cuts = pd.cut(sw, bins, right = False, labels = labels)
# apple_sweetness = cuts.to_numpy()
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

knn = KNeighborsClassifier()
knn.fit(train_scaled, train_target)
print(round(knn.score(train_scaled, train_target), 4))
print(round(knn.score(test_scaled, test_target), 4))