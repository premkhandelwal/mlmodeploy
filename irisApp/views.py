from django.shortcuts import render
from joblib import load

# Create your views here.
def predictor(req):
    model = load('./savedModels/model.joblib')      
    if(req.method == 'POST'):
        sepal_len = int(req.POST['sepal_length'])
        petal_len = int(req.POST['petal_length'])
        sepal_wid = int(req.POST['sepal_width'])
        petal_wid = int(req.POST['petal_width'])
        y_pred = model.predict([[sepal_len, sepal_wid, petal_len, petal_wid]])
        
        # print(y_pred)
        # return render(req, 'main.html', {'result': y_pred})
        return render(req, 'index.html', {'result': y_pred})
    return render(req, 'index.html')