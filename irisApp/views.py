from django.shortcuts import render
from joblib import load

model = load('./savedModels/model.joblib')

def predictor(req):
    return render(req, 'main.html')

def formInfo(req):
    sepal_len = req.GET['sepal_length']
    petal_len = req.GET['petal_length']
    sepal_wid = req.GET['sepal_width']
    petal_wid = req.GET['petal_width']
    y_pred = model.predict([[sepal_len, sepal_wid, petal_len, petal_wid]])
    print(y_pred)
    return render(req, 'result.html', {'result': y_pred[0]})    