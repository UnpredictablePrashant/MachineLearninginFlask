from trainingset import *
from sklearn.linear_model import LinearRegression
import pickle

predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)
pickle.dump(predictor, open('model.pkl','wb'))

X_TEST = [[10, 20, 30]]
outcome = predictor.predict(X=X_TEST)

# coefficients = predictor.coef_

print('Outcome : {}'.format(outcome))