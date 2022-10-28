import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

at = pd.read_csv('C:/python/apple_sweet/Apple_attribute.csv')
apple_attribute = at.to_numpy()
sw = pd.read_csv('C:/python/apple_sweet/Apple_sweetness.csv')
apple_sweetness = sw.to_numpy()
train_input, test_input, train_target, test_target = train_test_split(apple_attribute, apple_sweetness, test_size = 0.2, random_state=5)

poly = PolynomialFeatures()
poly.fit(train_input)
train_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)

ss = StandardScaler()
ss.fit(train_poly)
train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)

forest = RandomForestRegressor(n_estimators=200, max_features=3, max_depth= 4)
forest.fit(train_scaled, train_target.ravel())
print(round(forest.score(train_scaled, train_target), 4))
print(round(forest.score(test_scaled, test_target), 4))

# param_grid = [{'n_estimators': range(5, 50, 10), 'max_features': range(1, 4), 'max_depth': range(3, 5)}]
# gs = GridSearchCV(estimator=forest, param_grid=param_grid, scoring='r2', cv=5, n_jobs=-1)
# gs.fit(train_scaled, train_target)

# # 그리드서치 학습 결과 출력
# print('best hyper parameter: {0}'.format(gs.best_params_))
# print('best r^2: {0:.2f}'.format(gs.best_score_))

# # 최적화 모델 추출
# model = gs.best_estimator_

# # 테스트세트 R^2 점수 출력
# r2_score = model.score(test_scaled, test_target)
# print('test r2: {0:.2f}'.format(r2_score))

# # 테스트세트 예측 결과 샘플 출력
# predicted_y = model.predict(test_scaled)
# for i in range(10):
#     print('true: {0:.2f}, pridict: {1:.2f}'.format(test_target[i], predicted_y[i]))

# print(list(forest.feature_importances_))