from trainingset import *
from sklearn.linear_model import LinearRegression

predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)

X_TEST = [[1, 2, 3, 5, 3]]
outcome = predictor.predict(X=X_TEST)

# coefficients = predictor.coef_

print('Outcome : {}'.format(outcome))