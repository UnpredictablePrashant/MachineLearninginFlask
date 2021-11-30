# Simple Machine Learning code in Flask

We generated a training set which is based on simple mathematical equation which is `a + (5*b) + (10*c)`. The idea is to train this model using `LinearRegression` and then create flask end point to use it as web service.


## How to run the code?

Step 1: Install all the dependencies from `requirements.txt`
`pip install -r requirements.txt`

Step 1: Run and save the model in a `.pkl` file.
`python model.py`

Step 2: Run the flask server once the `model.pkl` file has been generated.
`python app.py`

