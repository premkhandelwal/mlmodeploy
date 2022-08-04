import json
from django.http import HttpResponse
from django.shortcuts import render
from joblib import load
from rest_framework.viewsets import ModelViewSet
from django.views.decorators.csrf import csrf_exempt
from irisApp.models import Predict
from rest_framework.decorators import api_view
from irisApp.serializers import PredictSerializer
import rest_framework  


def predictor(req):
    return render(req, 'index.html')

@csrf_exempt
def predict(request): 
    model =  load('./savedModels/model.joblib')      
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)
    sepal_len = int(data['sepal_length'])
    petal_len = int(data['petal_length'])
    sepal_wid = int(data['sepal_width'])
    petal_wid = int(data['petal_width'])
    print(sepal_wid)
    y_pred = model.predict([[sepal_len, sepal_wid, petal_len, petal_wid]])
    return HttpResponse(json.dumps({'result': y_pred[0]}), content_type='application/json')    



class PredictionView(ModelViewSet):
    serializer_class = PredictSerializer
    queryset = Predict.objects.all()

        