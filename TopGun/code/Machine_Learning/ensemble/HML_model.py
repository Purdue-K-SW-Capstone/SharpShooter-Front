import joblib
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import numpy as np

#Load csv files for each classes
input_l = pd.read_csv('./ensemble/split/test_i_l.csv')
input_m = pd.read_csv('./ensemble/split/test_i_m.csv')
input_h = pd.read_csv('./ensemble/split/test_i_h.csv')
target_l = pd.read_csv('./ensemble/split/test_t_l.csv')
target_m = pd.read_csv('./ensemble/split/test_t_m.csv')
target_h = pd.read_csv('./ensemble/split/test_t_h.csv')

#convert pandas df to numpy array
test_input_l = input_l.to_numpy()
test_input_m = input_m.to_numpy()
test_input_h = input_h.to_numpy()
test_target_l = target_l.to_numpy()
test_target_m = target_m.to_numpy()
test_target_h = target_h.to_numpy()

#Apply a polynomial regression function
poly = PolynomialFeatures(degree=3)
poly.fit(test_input_l)
test_poly_l = poly.transform(test_input_l)
poly.fit(test_input_m)
test_poly_m = poly.transform(test_input_m)
poly.fit(test_input_h)
test_poly_h = poly.transform(test_input_h)

#Data Standardization
ss = StandardScaler()
ss.fit(test_poly_l)
test_scaled_l = ss.transform(test_poly_l)
ss.fit(test_poly_m)
test_scaled_m = ss.transform(test_poly_m)
ss.fit(test_poly_h)
test_scaled_h = ss.transform(test_poly_h)

# # Load the ML low model
# model_low = joblib.load('./Machine_Learning/Gala/ensemble/models/low.pkl')
# # Load the ML med model
# model_med = joblib.load('./Machine_Learning/Gala/ensemble/models/medium.pkl')
# # Load the ML high model
# model_high = joblib.load('./Machine_Learning/Gala/ensemble/models/high.pkl')

# Load the tuned ML low model
model_low = joblib.load('./ensemble/tuned_model/low.pkl')
# Load the tuned ML med model
model_med = joblib.load('./ensemble/tuned_model/medium.pkl')
# Load the tuned ML high model
model_high = joblib.load('./ensemble/tuned_model/high.pkl')

#Predict sugar level with each model
preds_l = model_low.predict(test_scaled_l)
preds_m = model_med.predict(test_scaled_m)
preds_h = model_high.predict(test_scaled_h)
#add predictions to the array to find the loss value of the entire model.
preds = []
for i in preds_l:
    preds.append(i)
for i in preds_m:
    preds.append(i)
for i in preds_h:
    preds.append(i)
test_target = []
for i in test_target_l:
    test_target.append(i)
for i in test_target_m:
    test_target.append(i)
for i in test_target_h:
    test_target.append(i)

#Find the loss value of the entire model and each model
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

rmse_l = np.sqrt(mean_squared_error(test_target_l, preds_l))
MAEsum_l = 0
count_l = 0
for i, j in zip(test_target_l, preds_l):
    count_l += 1
    MAEsum_l += abs(i - j)
MAE_l = MAEsum_l/count_l
print("MAE_l: " + str(MAE_l[0]))
print("MSE_l: %f" % (mean_squared_error(test_target_l, preds_l)))
print("RMSE_l: %f" % (rmse_l))

rmse_m = np.sqrt(mean_squared_error(test_target_m, preds_m))
MAEsum_m = 0
count_m = 0
for i, j in zip(test_target_m, preds_m):
    count_m += 1
    MAEsum_m += abs(i - j)
MAE_m = MAEsum_m/count_m
print("MAE_m: " + str(MAE_m[0]))
print("MSE_m: %f" % (mean_squared_error(test_target_m, preds_m)))
print("RMSE_m: %f" % (rmse_m))

rmse_h = np.sqrt(mean_squared_error(test_target_h, preds_h))
MAEsum_h = 0
count_h = 0
for i, j in zip(test_target_h, preds_h):
    count_h += 1
    MAEsum_h += abs(i - j)
MAE_h = MAEsum_h/count_h
print("MAE_h: " + str(MAE_h[0]))
print("MSE_h: %f" % (mean_squared_error(test_target_h, preds_h)))
print("RMSE_h: %f" % (rmse_h))

#Determine the accuracy by setting the range of correct answers.
right = 0
for i, j in zip(preds, test_target):
    if abs(i - j) <1:
        right += 1
print(right/count)