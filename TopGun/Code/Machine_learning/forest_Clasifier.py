import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

at = pd.read_csv('C:/python/apple_sweet/Apple_attribute.csv')
apple_attribute = at.to_numpy()
sw = pd.read_csv('C:/python/apple_sweet/Apple_sweetness_c.csv')
apple_sweetness = sw.to_numpy()
train_input, test_input, train_target, test_target = train_test_split(apple_attribute, apple_sweetness, test_size = 0.2)

poly = PolynomialFeatures()
poly.fit(train_input)
train_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)

ss = StandardScaler()
ss.fit(train_poly)
train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)

forest = RandomForestClassifier(n_estimators=100, max_features=100, max_depth= 100)
forest.fit(train_scaled, train_target.ravel())
print(round(forest.score(train_scaled, train_target), 4))
print(round(forest.score(test_scaled, test_target), 4))
# print(list(forest.feature_importances_))