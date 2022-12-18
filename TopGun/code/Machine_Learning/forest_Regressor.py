import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

at = pd.read_csv('./apple_attribute.csv') #open input file
apple_attribute = at.to_numpy()
sw = pd.read_csv('./apple_Sweetness.csv') #open target file
apple_sweetness = sw.to_numpy()
train_input, test_input, train_target, test_target = train_test_split(apple_attribute, apple_sweetness, test_size = 0.2, random_state=5)

#Apply a polynomial regression function
poly = PolynomialFeatures(degree=3)
poly.fit(train_input)
train_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)

#Data Standardization
ss = StandardScaler()
ss.fit(train_poly)
train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)

#train model
forest = RandomForestRegressor(n_estimators=200, max_features=35, max_depth= 17)
forest.fit(train_scaled, train_target.ravel())
print(round(forest.score(train_scaled, train_target), 4))
print(round(forest.score(test_scaled, test_target), 4))

#save prediction
preds = forest.predict(test_scaled)
#Find the loss value of the model
rmse = np.sqrt(mean_squared_error(test_target, preds))
MAEsum = 0
count = 0
for i, j in zip(test_target, preds):
    count += 1
    MAEsum += abs(i - j)
MAE = MAEsum/count
print("MAE: " + str(MAE[0]))
print("MSE: %f" % (mean_squared_error(test_target, preds)))
print("RMSE: %f" % (rmse))


#Determine the accuracy by setting the range of correct answers.
right = 0

for i, j in zip(preds, test_target):
    if abs(i - j) <1:
        right += 1
print(right/count)

# forest.fit(train_input, train_target.ravel())
# print(list(forest.feature_importances_))
